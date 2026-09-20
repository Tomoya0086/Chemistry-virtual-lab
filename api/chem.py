"""
ChemSpace API — Vercel Python serverless function.

Deployed automatically at /api/chem. Pure standard library, no dependencies.

Endpoints (query string):
    /api/chem?op=config&z=29          -> electronic configuration (exceptions applied)
    /api/chem?op=zeff&z=11&orbital=3s -> Slater screening + Zeff, with the full step table
    /api/chem?op=huckel&kind=ring&n=6 -> Huckel pi molecular orbital energies
    /api/chem?op=pib&n=1&length=1.0   -> particle-in-a-box energy levels
    /api/chem?op=elements             -> symbol/Z index for all 118 elements

Run locally:  python3 api/chem.py     (serves http://localhost:8000/api/chem?op=zeff&z=11)
"""

import json
import math
from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

SYMBOLS = (
    "H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn "
    "Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce "
    "Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn "
    "Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl "
    "Mc Lv Ts Og"
).split()

# Madelung (n + l) filling order
ORDER = [(1, "s"), (2, "s"), (2, "p"), (3, "s"), (3, "p"), (4, "s"), (3, "d"), (4, "p"),
         (5, "s"), (4, "d"), (5, "p"), (6, "s"), (4, "f"), (5, "d"), (6, "p"), (7, "s"),
         (5, "f"), (6, "d"), (7, "p")]
CAP = {"s": 2, "p": 6, "d": 10, "f": 14}
LORD = {"s": 0, "p": 1, "d": 2, "f": 3}
NOBLE = [(2, "He"), (10, "Ne"), (18, "Ar"), (36, "Kr"), (54, "Xe"), (86, "Rn")]

# Ground-state configurations that break the Aufbau order
EXCEPTIONS = {
    24: "[Ar] 3d5 4s1", 29: "[Ar] 3d10 4s1", 41: "[Kr] 4d4 5s1", 42: "[Kr] 4d5 5s1",
    44: "[Kr] 4d7 5s1", 45: "[Kr] 4d8 5s1", 46: "[Kr] 4d10", 47: "[Kr] 4d10 5s1",
    57: "[Xe] 5d1 6s2", 58: "[Xe] 4f1 5d1 6s2", 64: "[Xe] 4f7 5d1 6s2",
    78: "[Xe] 4f14 5d9 6s1", 79: "[Xe] 4f14 5d10 6s1", 89: "[Rn] 6d1 7s2",
    90: "[Rn] 6d2 7s2", 91: "[Rn] 5f2 6d1 7s2", 92: "[Rn] 5f3 6d1 7s2",
    93: "[Rn] 5f4 6d1 7s2", 96: "[Rn] 5f7 6d1 7s2", 103: "[Rn] 5f14 7s2 7p1",
}


def aufbau(n_electrons):
    """Plain Aufbau filling, ignoring anomalies."""
    out, left = [], n_electrons
    for n, l in ORDER:
        if left <= 0:
            break
        c = min(CAP[l], left)
        out.append({"n": n, "l": l, "count": c})
        left -= c
    return out


def _parse(spec):
    out = []
    for token in spec.split():
        if token.startswith("["):
            core = token.strip("[]")
            z = next(z for z, s in NOBLE if s == core)
            out.extend(aufbau(z))
        else:
            out.append({"n": int(token[0]), "l": token[1], "count": int(token[2:])})
    return out


def configuration(z):
    """Ground-state configuration in filling order, with known exceptions applied."""
    anomalous = z in EXCEPTIONS
    sub = _parse(EXCEPTIONS[z]) if anomalous else aufbau(z)
    sub = [s for s in sub if s["count"] > 0]
    sub.sort(key=lambda s: ORDER.index((s["n"], s["l"])))
    return sub, anomalous


def config_string(sub):
    return " ".join("%d%s%d" % (s["n"], s["l"], s["count"]) for s in sub)


def condensed(z):
    sub, _ = configuration(z)
    core = None
    for cz, cs in NOBLE:
        if cz < z:
            core = (cz, cs)
    if core is None:
        return config_string(sub)
    core_sub = {(s["n"], s["l"]): s["count"] for s in aufbau(core[0])}
    rest = []
    for s in sub:
        used = core_sub.get((s["n"], s["l"]), 0)
        if s["count"] - used > 0:
            rest.append({"n": s["n"], "l": s["l"], "count": s["count"] - used})
    return "[%s] %s" % (core[1], config_string(rest))


def orbital_diagram(sub):
    """Hund's rule filling of each subshell: list of per-orbital occupancies."""
    rows = []
    for s in sub:
        boxes = 2 * LORD[s["l"]] + 1
        up = min(s["count"], boxes)
        down = max(0, s["count"] - boxes)
        rows.append({
            "subshell": "%d%s" % (s["n"], s["l"]),
            "orbitals": [(1 if i < up else 0) + (1 if i < down else 0) for i in range(boxes)],
            "unpaired": up - down,
        })
    return rows


def slater_groups(z):
    """(1s)(2s,2p)(3s,3p)(3d)(4s,4p)(4d)(4f)(5s,5p)... in Slater's order."""
    sub, _ = configuration(z)
    groups = {}
    for s in sub:
        kind = "sp" if s["l"] in "sp" else s["l"]
        key = (s["n"], kind)
        g = groups.setdefault(key, {"n": s["n"], "kind": kind, "count": 0, "labels": []})
        g["count"] += s["count"]
        g["labels"].append("%d%s" % (s["n"], s["l"]))
    return sorted(groups.values(), key=lambda g: (g["n"], {"sp": 0, "d": 1, "f": 2}[g["kind"]]))


def zeff(z, orbital):
    """Effective nuclear charge for one electron in `orbital` (e.g. '3s', '3d')."""
    n, l = int(orbital[0]), orbital[1]
    kind = "sp" if l in "sp" else l
    groups = slater_groups(z)
    index = next((i for i, g in enumerate(groups) if g["n"] == n and g["kind"] == kind), None)
    if index is None:
        raise ValueError("orbital %s is not occupied in element Z=%d" % (orbital, z))

    target, steps, s_total = groups[index], [], 0.0
    same = 0.30 if (n == 1 and kind == "sp") else 0.35
    count = target["count"] - 1
    steps.append({"group": "(%s)" % ",".join(target["labels"]), "position": "same group",
                  "electrons": count, "factor": same, "contribution": count * same})
    s_total += count * same

    for g in groups[:index]:
        factor = (0.85 if g["n"] == n - 1 else 1.00) if kind == "sp" else 1.00
        if kind == "sp":
            position = "shell n-1" if g["n"] == n - 1 else "shell n-2 or lower"
        else:
            position = "inner group (d/f electron screens fully)"
        steps.append({"group": "(%s)" % ",".join(g["labels"]), "position": position,
                      "electrons": g["count"], "factor": factor,
                      "contribution": g["count"] * factor})
        s_total += g["count"] * factor

    for g in groups[index + 1:]:
        steps.append({"group": "(%s)" % ",".join(g["labels"]), "position": "outer group",
                      "electrons": g["count"], "factor": 0.0, "contribution": 0.0})

    return {"z": z, "symbol": SYMBOLS[z - 1], "orbital": orbital,
            "configuration": config_string(configuration(z)[0]),
            "slater_groups": ["(%s)%d" % (",".join(g["labels"]), g["count"]) for g in groups],
            "steps": steps, "screening_constant": round(s_total, 4),
            "zeff": round(z - s_total, 4)}


def huckel(kind, n):
    """Huckel pi MO energies as coefficients x in E = alpha + x*beta."""
    if kind == "ring":
        xs = [2 * math.cos(2 * math.pi * k / n) for k in range(n)]
    else:
        xs = [2 * math.cos(k * math.pi / (n + 1)) for k in range(1, n + 1)]
    xs.sort(reverse=True)

    occupancy, remaining, i = [0] * n, n, 0
    while remaining > 0 and i < n:
        degeneracy = 1
        while i + degeneracy < n and abs(xs[i + degeneracy] - xs[i]) < 1e-9:
            degeneracy += 1
        electrons = min(2 * degeneracy, remaining)
        remaining -= electrons
        for j in range(degeneracy):
            occupancy[i + j] = (1 if j < electrons else 0) if electrons <= degeneracy \
                else (2 if j < electrons - degeneracy else 1)
        i += degeneracy

    total = sum(o * x for o, x in zip(occupancy, xs))
    return {"kind": kind, "atoms": n, "pi_electrons": n,
            "levels": [{"x": round(x, 6), "energy": "alpha + %.4f beta" % x, "electrons": o}
                       for x, o in zip(xs, occupancy)],
            "total_pi_energy": "%d alpha + %.4f beta" % (n, total),
            "delocalisation_energy": "%.4f beta" % (total - n),
            "unpaired_electrons": occupancy.count(1),
            "aromatic": kind == "ring" and n % 4 == 2}


def particle_in_box(n, length_nm):
    """E_n = n^2 h^2 / 8 m L^2 for an electron, returned in eV."""
    h, m, e = 6.62607015e-34, 9.1093837015e-31, 1.602176634e-19
    L = length_nm * 1e-9
    energy = lambda k: (k * k * h * h) / (8 * m * L * L) / e
    return {"n": n, "length_nm": length_nm,
            "energy_eV": round(energy(n), 6),
            "wavefunction": "sqrt(2/L) * sin(%d*pi*x/L)" % n,
            "interior_nodes": n - 1,
            "wavelength_nm": round(2 * length_nm / n, 6),
            "levels_eV": [round(energy(k), 6) for k in range(1, 7)],
            "transition_to_n_plus_1_eV": round(energy(n + 1) - energy(n), 6)}


def dispatch(params):
    get = lambda k, d=None: params.get(k, [d])[0]
    op = get("op", "elements")

    if op == "elements":
        return {"count": len(SYMBOLS),
                "elements": [{"z": i + 1, "symbol": s, "block": configuration(i + 1)[0][-1]["l"]}
                             for i, s in enumerate(SYMBOLS)]}

    if op == "config":
        z = int(get("z", "1"))
        if not 1 <= z <= 118:
            raise ValueError("z must be between 1 and 118")
        sub, anomalous = configuration(z)
        return {"z": z, "symbol": SYMBOLS[z - 1], "configuration": config_string(sub),
                "condensed": condensed(z), "anomalous": anomalous,
                "exception_rule": EXCEPTIONS.get(z),
                "orbital_diagram": orbital_diagram(sub),
                "valence_electrons": sum(s["count"] for s in sub
                                         if s["n"] == max(x["n"] for x in sub) and s["l"] in "sp")}

    if op == "zeff":
        z = int(get("z", "1"))
        sub, _ = configuration(z)
        outer = [s for s in sub if s["n"] == max(x["n"] for x in sub) and s["l"] in "sp"]
        default = "%d%s" % (outer[-1]["n"], outer[-1]["l"]) if outer \
            else "%d%s" % (sub[-1]["n"], sub[-1]["l"])
        return zeff(z, get("orbital", default))

    if op == "huckel":
        n = int(get("n", "6"))
        if not 2 <= n <= 30:
            raise ValueError("n must be between 2 and 30")
        return huckel(get("kind", "chain"), n)

    if op == "pib":
        return particle_in_box(int(get("n", "1")), float(get("length", "1.0")))

    raise ValueError("unknown op: %s" % op)


class handler(BaseHTTPRequestHandler):  # noqa: N801 — Vercel expects this name
    def do_GET(self):
        params = parse_qs(urlparse(self.path).query)
        try:
            body, status = dispatch(params), 200
        except Exception as exc:  # noqa: BLE001
            body, status = {"error": str(exc)}, 400
        payload = json.dumps(body, indent=2).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Cache-Control", "public, max-age=3600")
        self.send_header("Content-Length", str(len(payload)))
        self.end_headers()
        self.wfile.write(payload)

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    from http.server import HTTPServer
    print("ChemSpace API on http://localhost:8000/api/chem?op=zeff&z=11")
    HTTPServer(("0.0.0.0", 8000), handler).serve_forever()

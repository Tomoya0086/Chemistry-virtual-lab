#!/usr/bin/env python3
"""
Cheminformatics Virtual Laboratory
Institutional Deployment: SRM Institute of Science and Technology, Tiruchirappalli
In collaboration with Tomoya Okazaki

Run locally:
    python3 app.py
Open:
    http://localhost:3000
"""

import os
import sys
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from urllib.parse import urlparse
from api.index import calculate_molecular_properties, EXAMPLE_MOLECULES, handler as APIHandler

PORT = int(os.environ.get("PORT", 3000))
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class CheminformaticsHandler(APIHandler, SimpleHTTPRequestHandler):
    """Handles both static file serving and dynamic Python cheminformatics API."""

    def __init__(self, *args, **kwargs):
        SimpleHTTPRequestHandler.__init__(self, *args, directory=BASE_DIR, **kwargs)

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/"):
            APIHandler.do_GET(self)
        else:
            SimpleHTTPRequestHandler.do_GET(self)

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/"):
            APIHandler.do_POST(self)
        else:
            self.send_error(405, "Method Not Allowed")

    def do_OPTIONS(self):
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/"):
            APIHandler.do_OPTIONS(self)
        else:
            SimpleHTTPRequestHandler.do_OPTIONS(self)

def main():
    print("=" * 68)
    print("🧪 CHEMINFORMATICS VIRTUAL LABORATORY (PYTHON ENGINE)")
    print("🏛️  SRM Institute of Science and Technology, Tiruchirappalli")
    print("👨‍🏫 Dr. R. Subramanian | Division of Chemistry, School of Sciences")
    print("⚡ Technical Collaboration: Tomoya Okazaki (Purple Team Systems)")
    print(f"🚀 Serving high-performance laboratory workstation on http://localhost:{PORT}")
    print("=" * 68)
    
    server = ThreadingHTTPServer(("", PORT), CheminformaticsHandler)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nLaboratory server halted.")
        server.server_close()
        sys.exit(0)

if __name__ == "__main__":
    main()

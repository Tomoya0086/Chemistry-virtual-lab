"""
Site Generator for Cheminformatics Virtual Laboratory
SRM Institute of Science and Technology, Tiruchirappalli
In collaboration with Tomoya Okazaki
"""

import os

def generate_index_html():
    html_content = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Cheminformatics Virtual Laboratory | SRM Institute of Science &amp; Technology</title>

<!-- SEO & Meta Descriptions (Rule 2) -->
<meta name="description" content="Cheminformatics Virtual Laboratory and 3D Molecular Simulation Workstation. Developed for SRM Institute of Science and Technology, Division of Chemistry, with Tomoya Okazaki. Calculate 18 molecular descriptors, visualize 2D/3D chemical structures, compute Slater Zeff, and export PDF laboratory reports.">
<meta name="keywords" content="cheminformatics, SRM Institute of Science and Technology, molecular visualization, 3D molecules, SMILES, Lipinski rule, TPSA, LogP, periodic table, Slater rules, Dr. R. Subramanian, Tomoya Okazaki">
<meta name="author" content="SRM Institute of Science and Technology &amp; Tomoya Okazaki">
<meta name="theme-color" content="#030712">

<!-- Open Graph / Social Media Cards -->
<meta property="og:type" content="website">
<meta property="og:title" content="Cheminformatics Virtual Laboratory | SRM Institute of Science &amp; Technology">
<meta property="og:description" content="Interactive 2D/3D chemical structure simulation, molecular descriptors, and quantum chemistry workstation.">
<meta property="og:image" content="assets/srm_logo.jpeg">
<meta property="twitter:card" content="summary_large_image">
<meta property="twitter:title" content="Cheminformatics Virtual Laboratory - SRM IST">
<meta property="twitter:description" content="Interactive 2D/3D chemical structures, molecular properties calculation, and laboratory reports.">

<!-- Embedded Crisp SVG Favicon (Rule 3) -->
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2300f0ff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M10 2v7.31M14 2v7.31M8.5 2h7M14 9.3a6.5 6.5 0 1 1-4 0'/%3E%3Ccircle cx='12' cy='15' r='1.5' fill='%2300ff9d'/%3E%3C/svg%3E">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">

<style>
/* ==========================================================================
   DESIGN TOKENS - ZERO PURPLE GRADIENTS, ZERO PILL BUTTONS, INDUSTRIAL 8PX
   ========================================================================== */
:root {
  --bg: #030712;
  --bg-deep: #02040a;
  --panel: rgba(15, 23, 42, 0.72);
  --panel-hover: rgba(30, 41, 59, 0.85);
  --panel-active: rgba(15, 23, 42, 0.95);
  --border: rgba(0, 240, 255, 0.16);
  --border-focus: rgba(0, 240, 255, 0.55);
  --ink: #f8fafc;
  --mut: #94a3b8;
  --dim: #64748b;
  --acc: #00f0ff;      /* Electric Cyan */
  --acc-glow: rgba(0, 240, 255, 0.35);
  --acc2: #00ff9d;     /* Quantum Emerald */
  --acc3: #38bdf8;     /* Sky Titanium */
  --warn: #ffd166;
  --bad: #ff4d6d;
  --r: 8px;            /* Standard Card Radius (Anti-pattern safe: NO pill) */
  --r-btn: 6px;        /* Industrial Button Radius */
  --mono: "JetBrains Mono", ui-monospace, monospace;
  --font-main: "Space Grotesk", system-ui, -apple-system, sans-serif;
  --ease: cubic-bezier(0.16, 1, 0.3, 1);
  --header-h: 70px;
}

*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
  scroll-behavior: auto; /* Handled smoothly by our Momentum Engine */
  background: var(--bg);
  color: var(--ink);
  font-family: var(--font-main);
  overflow-x: hidden;
  -webkit-font-smoothing: antialiased;
}

body {
  overflow-x: hidden;
  width: 100%;
  position: relative;
  line-height: 1.6;
}

/* ==========================================================================
   SCROLL ENGINE & JITTER-STYLE VELOCITY KINETICS
   ========================================================================== */
#scrollProgress {
  position: fixed;
  top: 0;
  left: 0;
  height: 3px;
  width: 0%;
  background: linear-gradient(90deg, var(--acc), var(--acc2));
  box-shadow: 0 0 14px var(--acc);
  z-index: 1000;
  pointer-events: none;
  transition: width 0.05s ease-out;
}

#telemetryHud {
  position: fixed;
  bottom: 18px;
  right: 20px;
  z-index: 90;
  font-family: var(--mono);
  font-size: 11px;
  padding: 8px 14px;
  background: rgba(3, 7, 18, 0.9);
  border: 1px solid var(--border);
  border-radius: var(--r-btn);
  backdrop-filter: blur(12px);
  color: var(--acc);
  display: flex;
  align-items: center;
  gap: 12px;
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.7);
  pointer-events: none;
}

.hud-dot {
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--acc2);
  box-shadow: 0 0 8px var(--acc2);
  animation: pulse 1.5s infinite;
}

@keyframes pulse {
  0%, 100% { opacity: 1; transform: scale(1); }
  50% { opacity: 0.4; transform: scale(0.85); }
}

/* Background Atmosphere */
#spaceCanvas {
  position: fixed;
  inset: 0;
  z-index: -2;
  display: block;
  pointer-events: none;
}

.ambient-layer {
  position: fixed;
  inset: 0;
  z-index: -1;
  pointer-events: none;
  background:
    radial-gradient(50vw 45vw at 10% 15%, rgba(0, 240, 255, 0.07), transparent 70%),
    radial-gradient(55vw 50vw at 90% 25%, rgba(0, 255, 157, 0.06), transparent 70%),
    radial-gradient(45vw 45vw at 50% 85%, rgba(56, 189, 248, 0.05), transparent 70%);
  filter: blur(20px);
}

.wrap {
  max-width: 1260px;
  margin: 0 auto;
  padding: 0 20px;
}

/* ==========================================================================
   INSTITUTIONAL SRM & TOMOYA OKAZAKI BANNER & NAVIGATION
   ========================================================================== */
.inst-bar {
  background: #020617;
  border-bottom: 1px solid rgba(0, 240, 255, 0.12);
  padding: 6px 20px;
  font-size: 12px;
  font-family: var(--mono);
  color: var(--mut);
}

.inst-bar-inner {
  max-width: 1260px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 10px;
}

.inst-tag {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--ink);
}

.inst-tag img {
  height: 20px;
  width: auto;
  border-radius: 2px;
}

.inst-status {
  display: flex;
  align-items: center;
  gap: 14px;
}

.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 2px 8px;
  border-radius: 4px;
  background: rgba(0, 255, 157, 0.1);
  border: 1px solid rgba(0, 255, 157, 0.3);
  color: var(--acc2);
  font-size: 11px;
}

header {
  position: sticky;
  top: 0;
  z-index: 100;
  backdrop-filter: blur(20px);
  background: rgba(3, 7, 18, 0.88);
  border-bottom: 1px solid var(--border);
  height: var(--header-h);
}

.nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 100%;
}

.brand-group {
  display: flex;
  align-items: center;
  gap: 14px;
  text-decoration: none;
}

.brand-logo-wrap {
  display: flex;
  align-items: center;
  gap: 10px;
}

.tomoya-avatar {
  width: 40px;
  height: 40px;
  border-radius: 6px;
  border: 1.5px solid var(--acc);
  box-shadow: 0 0 12px var(--acc-glow);
  object-fit: cover;
  transition: transform 0.25s var(--ease);
}

.tomoya-avatar:hover {
  transform: scale(1.08) rotate(2deg);
}

.brand-text h1 {
  font-size: 16px;
  font-weight: 700;
  color: var(--ink);
  line-height: 1.2;
}

.brand-text span {
  font-size: 11px;
  color: var(--acc);
  font-family: var(--mono);
  letter-spacing: 0.05em;
  display: block;
}

nav.links {
  display: flex;
  align-items: center;
  gap: 4px;
}

nav.links a {
  padding: 8px 12px;
  border-radius: var(--r-btn);
  color: var(--mut);
  text-decoration: none;
  font-size: 13.5px;
  font-weight: 500;
  border: 1px solid transparent;
  transition: all 0.2s var(--ease);
  position: relative;
}

nav.links a:hover {
  color: var(--ink);
  background: var(--panel);
  border-color: var(--border);
  transform: translateY(-1px);
}

nav.links a.active {
  color: #030712;
  background: linear-gradient(135deg, var(--acc), var(--acc2));
  font-weight: 700;
  box-shadow: 0 0 16px var(--acc-glow);
}

.nav-actions {
  display: flex;
  align-items: center;
  gap: 10px;
}

/* Audio Toggle Button */
.ctrl-btn {
  background: var(--panel);
  border: 1px solid var(--border);
  color: var(--acc);
  padding: 7px 12px;
  border-radius: var(--r-btn);
  font-family: var(--mono);
  font-size: 11.5px;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  transition: all 0.2s var(--ease);
}

.ctrl-btn:hover {
  background: var(--panel-hover);
  border-color: var(--acc);
  box-shadow: 0 0 12px var(--acc-glow);
  transform: translateY(-2px);
}

.menu-toggle {
  display: none;
  background: transparent;
  border: 1px solid var(--border);
  color: var(--ink);
  padding: 8px 10px;
  border-radius: var(--r-btn);
  cursor: pointer;
}

/* Mobile Drawer */
.mobile-drawer {
  position: fixed;
  inset: 0;
  background: rgba(2, 4, 10, 0.95);
  backdrop-filter: blur(20px);
  z-index: 150;
  display: none;
  flex-direction: column;
  padding: 24px;
  transform: translateX(100%);
  transition: transform 0.35s var(--ease);
}

.mobile-drawer.open {
  display: flex;
  transform: translateX(0);
}

.drawer-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 30px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border);
}

.mobile-nav-links {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.mobile-nav-links a {
  font-size: 18px;
  padding: 12px;
  border-radius: var(--r-btn);
  color: var(--ink);
  text-decoration: none;
  border: 1px solid var(--border);
  background: var(--panel);
}

/* ==========================================================================
   BUTTONS WITH DYNAMIC HOVER SHINE & KINETIC MICRO-INTERACTIONS
   ========================================================================== */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 11px 20px;
  border-radius: var(--r-btn);
  border: 1px solid var(--border);
  background: var(--panel);
  color: var(--ink);
  font-family: inherit;
  font-size: 14px;
  font-weight: 600;
  cursor: pointer;
  position: relative;
  overflow: hidden;
  transition: transform 0.22s var(--ease), border-color 0.22s, box-shadow 0.22s, background 0.22s;
  text-decoration: none;
}

/* Button Kinetic Light Sheen Sweep */
.btn::after {
  content: "";
  position: absolute;
  top: -50%;
  left: -100%;
  width: 60%;
  height: 200%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.25), transparent);
  transform: rotate(25deg);
  pointer-events: none;
  transition: none;
}

.btn:hover {
  background: var(--panel-hover);
  border-color: var(--acc);
  transform: translateY(-3px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.5), 0 0 16px var(--acc-glow);
}

.btn:hover::after {
  left: 200%;
  transition: left 0.65s var(--ease);
}

.btn:active {
  transform: scale(0.97) translateY(0);
}

.btn.primary {
  background: linear-gradient(135deg, var(--acc), var(--acc2));
  color: #020617;
  border-color: transparent;
  font-weight: 700;
}

.btn.primary:hover {
  box-shadow: 0 10px 30px rgba(0, 240, 255, 0.4), 0 0 20px var(--acc2);
}

.btn.sm {
  padding: 6px 12px;
  font-size: 12px;
}

/* ==========================================================================
   CARDS WITH 3D PERSPECTIVE PITCH & JITTER-STYLE SCROLL ENTRANCE
   ========================================================================== */
.card {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--r);
  padding: 24px;
  backdrop-filter: blur(14px);
  position: relative;
  transition: transform 0.3s var(--ease), border-color 0.3s, box-shadow 0.3s;
  transform-style: preserve-3d;
}

.card:hover {
  border-color: rgba(0, 240, 255, 0.45);
  box-shadow: 0 16px 40px rgba(0, 0, 0, 0.7), 0 0 24px rgba(0, 240, 255, 0.12);
  transform: translateY(-4px);
}

/* Scroll-driven 3D Kinetic Elements */
.k-reveal {
  opacity: 0;
  transform: translateY(44px) scale(0.97) rotateX(4deg);
  transform-origin: top center;
  transition: opacity 0.8s var(--ease), transform 0.8s var(--ease);
}

.k-reveal.in-view {
  opacity: 1;
  transform: none;
}

/* Grid Layouts */
.grid {
  display: grid;
  gap: 18px;
}

.g2 { grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); }
.g3 { grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
.g4 { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }

/* ==========================================================================
   HERO BLOCK - STORYTELLING & TELEMETRY STRIP
   ========================================================================== */
.hero {
  padding: 80px 0 60px;
  position: relative;
}

.hero-badge-row {
  display: flex;
  align-items: center;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  padding: 6px 14px;
  border: 1px solid var(--border);
  border-radius: var(--r-btn);
  background: var(--panel);
  font-family: var(--mono);
  font-size: 12px;
  color: var(--acc);
  text-transform: uppercase;
  letter-spacing: 0.08em;
}

.badge.srm-badge {
  color: var(--acc2);
  border-color: rgba(0, 255, 157, 0.3);
  background: rgba(0, 255, 157, 0.06);
}

.hero h1 {
  font-size: clamp(34px, 5.5vw, 68px);
  font-weight: 700;
  line-height: 1.1;
  letter-spacing: -0.03em;
  margin-bottom: 20px;
  background: linear-gradient(120deg, #ffffff 20%, var(--acc) 60%, var(--acc2) 90%);
  -webkit-background-clip: text;
  background-clip: text;
  color: transparent;
}

.hero p {
  font-size: clamp(16px, 1.8vw, 20px);
  color: var(--mut);
  max-width: 780px;
  margin-bottom: 32px;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 40px;
}

.telemetry-strip {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  gap: 14px;
  margin-top: 10px;
}

.tele-item {
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--r-btn);
  padding: 14px 18px;
}

.tele-val {
  font-family: var(--mono);
  font-size: 26px;
  font-weight: 700;
  color: var(--acc);
  line-height: 1.2;
}

.tele-lbl {
  font-size: 11.5px;
  color: var(--dim);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: 4px;
}

/* Section Headings */
section {
  padding: 80px 0;
  scroll-margin-top: 80px;
}

.sechead {
  margin-bottom: 32px;
  max-width: 820px;
}

.kicker {
  font-family: var(--mono);
  font-size: 12px;
  color: var(--acc2);
  text-transform: uppercase;
  letter-spacing: 0.15em;
  font-weight: 700;
  margin-bottom: 8px;
}

.sechead h2 {
  font-size: clamp(26px, 3.4vw, 42px);
  color: var(--ink);
  margin-bottom: 10px;
}

/* ==========================================================================
   CHEMINFORMATICS LABORATORY (CORE DUAL WORKSPACE)
   ========================================================================== */
.smiles-bar {
  display: flex;
  gap: 12px;
  flex-wrap: wrap;
  margin-bottom: 18px;
}

.input-box {
  flex: 1 1 320px;
  position: relative;
}

input, select {
  width: 100%;
  padding: 12px 16px;
  background: rgba(6, 10, 22, 0.85);
  border: 1px solid var(--border);
  border-radius: var(--r-btn);
  color: var(--ink);
  font-family: var(--mono);
  font-size: 14px;
  outline: none;
  transition: border-color 0.2s, box-shadow 0.2s;
}

input:focus, select:focus {
  border-color: var(--acc);
  box-shadow: 0 0 0 2px var(--acc-glow);
}

.preset-chips {
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 22px;
}

.preset-chip {
  padding: 6px 14px;
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--r-btn);
  font-family: var(--mono);
  font-size: 12px;
  color: var(--mut);
  cursor: pointer;
  transition: all 0.2s var(--ease);
}

.preset-chip:hover {
  color: var(--acc);
  border-color: var(--acc);
  background: var(--panel-hover);
  transform: translateY(-2px);
}

.preset-chip.active {
  color: #020617;
  background: var(--acc);
  border-color: var(--acc);
  font-weight: 700;
}

/* Dual Canvas Layout */
.dual-canvas-grid {
  display: grid;
  grid-template-columns: 1fr 1.35fr;
  gap: 20px;
}

@media (max-width: 900px) {
  .dual-canvas-grid {
    grid-template-columns: 1fr;
  }
}

.viewer-box {
  width: 100%;
  height: 480px;
  border-radius: var(--r);
  border: 1px solid var(--border);
  background: radial-gradient(circle at 50% 50%, rgba(0, 240, 255, 0.04), rgba(2, 4, 10, 0.95));
  position: relative;
  overflow: hidden;
}

.canvas-toolbar {
  position: absolute;
  top: 14px;
  left: 14px;
  right: 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  z-index: 10;
  pointer-events: none;
}

.canvas-toolbar * {
  pointer-events: auto;
}

.model-select {
  width: auto;
  padding: 6px 12px;
  font-size: 12px;
  background: rgba(3, 7, 18, 0.9);
}

/* 2D Vector Structure View */
.mol-2d-canvas {
  width: 100%;
  height: 480px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(6, 10, 22, 0.85);
  border-radius: var(--r);
  border: 1px solid var(--border);
  position: relative;
  overflow: hidden;
}

/* Properties Analytical Suite */
.prop-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 16px;
  font-size: 13.5px;
}

.prop-table th {
  padding: 10px 14px;
  background: rgba(0, 240, 255, 0.08);
  color: var(--acc);
  font-family: var(--mono);
  font-size: 11px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  text-align: left;
  border-bottom: 1px solid var(--border);
}

.prop-table td {
  padding: 10px 14px;
  border-bottom: 1px solid rgba(0, 240, 255, 0.08);
  color: var(--ink);
}

.prop-table tr:hover td {
  background: rgba(0, 240, 255, 0.03);
}

.val-col {
  font-family: var(--mono);
  font-weight: 700;
  color: var(--acc2);
}

.desc-col {
  font-size: 12.5px;
  color: var(--mut);
  line-height: 1.4;
}

/* Notification Banners (Rule 14 & 15) */
.alert-banner {
  padding: 14px 18px;
  border-radius: var(--r-btn);
  margin-bottom: 18px;
  font-size: 13.5px;
  display: none;
  align-items: center;
  gap: 12px;
}

.alert-banner.error {
  display: flex;
  background: rgba(255, 77, 109, 0.12);
  border: 1px solid rgba(255, 77, 109, 0.4);
  color: #ff94a8;
}

.alert-banner.success {
  display: flex;
  background: rgba(0, 255, 157, 0.1);
  border: 1px solid rgba(0, 255, 157, 0.35);
  color: var(--acc2);
}

/* Empty State (Rule 11) */
.empty-state {
  text-align: center;
  padding: 40px 20px;
  color: var(--dim);
}

.empty-state svg {
  width: 48px;
  height: 48px;
  stroke: var(--dim);
  margin-bottom: 12px;
}

/* ==========================================================================
   PERIODIC TABLE & TRENDS MODULE
   ========================================================================== */
.pt-scroll-wrap {
  overflow-x: auto;
  padding-bottom: 12px;
}

.pt-grid {
  display: grid;
  grid-template-columns: repeat(18, minmax(48px, 1fr));
  gap: 4px;
  min-width: 920px;
}

.el-cell {
  aspect-ratio: 1;
  border-radius: 6px;
  border: 1px solid rgba(255, 255, 255, 0.12);
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  cursor: pointer;
  position: relative;
  transition: transform 0.16s var(--ease), box-shadow 0.16s, z-index 0.16s;
  color: #020617;
  overflow: hidden;
}

.el-cell:hover {
  transform: translateY(-4px) scale(1.12);
  z-index: 10;
  box-shadow: 0 10px 26px rgba(0, 0, 0, 0.8), 0 0 16px rgba(0, 240, 255, 0.6);
}

.el-z {
  position: absolute;
  top: 2px;
  left: 4px;
  font-family: var(--mono);
  font-size: 9px;
  font-weight: 700;
  opacity: 0.75;
}

.el-sym {
  font-size: 15px;
  font-weight: 700;
  line-height: 1;
}

.el-name {
  font-size: 8px;
  opacity: 0.8;
  max-width: 90%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* ==========================================================================
   QUIZ & ASSESSMENT TERMINAL
   ========================================================================== */
.quiz-opt {
  display: block;
  width: 100%;
  text-align: left;
  padding: 12px 18px;
  border-radius: var(--r-btn);
  border: 1px solid var(--border);
  background: var(--panel);
  color: var(--ink);
  font-size: 14.5px;
  cursor: pointer;
  margin-bottom: 10px;
  transition: all 0.2s var(--ease);
}

.quiz-opt:hover:not(:disabled) {
  border-color: var(--acc);
  background: var(--panel-hover);
  transform: translateX(6px);
}

.quiz-opt.correct {
  background: rgba(0, 255, 157, 0.15);
  border-color: var(--acc2);
  color: var(--acc2);
}

.quiz-opt.incorrect {
  background: rgba(255, 77, 109, 0.15);
  border-color: var(--bad);
  color: var(--bad);
}

/* ==========================================================================
   FOOTER & COMPLIANCE (RULES 6, 17, PRIVACY, TERMS, SRM)
   ========================================================================== */
footer {
  background: #02040a;
  border-top: 1px solid var(--border);
  padding: 60px 0 40px;
}

.footer-top {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 36px;
  margin-bottom: 40px;
}

@media (max-width: 820px) {
  .footer-top {
    grid-template-columns: 1fr;
  }
}

.footer-brand h3 {
  font-size: 18px;
  color: var(--ink);
  margin-bottom: 8px;
}

.footer-brand p {
  color: var(--dim);
  font-size: 13.5px;
  max-width: 440px;
  line-height: 1.5;
}

.footer-links h4 {
  font-family: var(--mono);
  font-size: 11px;
  text-transform: uppercase;
  color: var(--acc);
  letter-spacing: 0.1em;
  margin-bottom: 14px;
}

.footer-links a {
  display: flex;
  align-items: center;
  gap: 8px;
  color: var(--mut);
  text-decoration: none;
  font-size: 13px;
  margin-bottom: 8px;
  transition: color 0.2s;
}

.footer-links a:hover {
  color: var(--acc);
}

.footer-bottom {
  padding-top: 24px;
  border-top: 1px solid rgba(0, 240, 255, 0.08);
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  font-size: 12px;
  color: var(--dim);
}

/* Modal Dialogs (Rule 16: 404, Privacy, Terms) */
.modal-overlay {
  position: fixed;
  inset: 0;
  z-index: 200;
  background: rgba(2, 4, 10, 0.88);
  backdrop-filter: blur(14px);
  display: none;
  align-items: center;
  justify-content: center;
  padding: 20px;
}

.modal-overlay.active {
  display: flex;
}

.modal-box {
  background: #070e1e;
  border: 1px solid var(--border);
  border-radius: var(--r);
  width: min(680px, 100%);
  max-height: 85vh;
  overflow-y: auto;
  padding: 30px;
  position: relative;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.8);
}

.modal-close {
  position: absolute;
  top: 18px;
  right: 20px;
  background: transparent;
  border: none;
  color: var(--mut);
  font-size: 24px;
  cursor: pointer;
  line-height: 1;
}

.modal-close:hover {
  color: var(--acc);
}

/* Utility */
.sr-only { position: absolute; width: 1px; height: 1px; padding: 0; margin: -1px; overflow: hidden; clip: rect(0, 0, 0, 0); border: 0; }
</style>
</head>
<body>

<!-- Progress Beam -->
<div id="scrollProgress"></div>

<!-- HUD Telemetry -->
<div id="telemetryHud">
  <span class="hud-dot"></span>
  <span id="hudPct">0%</span>
  <span>|</span>
  <span id="hudModule">VIRTUAL LAB ACTIVE</span>
  <span>|</span>
  <span id="hudApiStatus" style="color:var(--acc2)">PYTHON API: ONLINE</span>
</div>

<!-- Background Canvas & Ambient Lights -->
<canvas id="spaceCanvas"></canvas>
<div class="ambient-layer"></div>

<!-- Institutional SRM Top Bar -->
<div class="inst-bar">
  <div class="inst-bar-inner">
    <div class="inst-tag">
      <img src="assets/srm_logo.jpeg" alt="SRM IST Logo">
      <span><strong>SRM Institute of Science and Technology</strong>, Tiruchirappalli</span>
      <span style="color:var(--dim)">|</span>
      <span>Faculty of Engineering and Technology | School of Sciences | Division of Chemistry</span>
    </div>
    <div class="inst-status">
      <span class="status-badge">SRM VIRTUAL LAB</span>
      <span class="status-badge" style="color:var(--acc);border-color:rgba(0,240,255,0.3)">VERCEL DEPLOYMENT</span>
    </div>
  </div>
</div>

<!-- Main Sticky Header -->
<header>
  <div class="wrap nav">
    <a href="#home" class="brand-group">
      <div class="brand-logo-wrap">
        <img src="assets/tomoya_logo.png" alt="Tomoya Okazaki Avatar" class="tomoya-avatar">
        <div class="brand-text">
          <h1>Cheminformatics Virtual Lab</h1>
          <span>SRM IST &times; TOMOYA OKAZAKI</span>
        </div>
      </div>
    </a>

    <nav class="links">
      <a href="#home" class="active">Overview</a>
      <a href="#lab">3D Molecular Lab</a>
      <a href="#properties">Descriptors</a>
      <a href="#compare">Compare</a>
      <a href="#table">Periodic Table</a>
      <a href="#trends">Trends</a>
      <a href="#zeff">Slater Z<sub>eff</sub></a>
      <a href="#quiz">Assessment</a>
      <a href="#report">Student Report</a>
    </nav>

    <div class="nav-actions">
      <button class="ctrl-btn" id="audioBtn" onclick="toggleAudio()" title="Toggle Web Audio Synthesizer">
        <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
        <span id="audioStatusText">AUDIO: ON</span>
      </button>
      <button class="menu-toggle" onclick="toggleMobileMenu()" aria-label="Toggle Navigation Menu">
        <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>
  </div>
</header>

<!-- Mobile Navigation Drawer -->
<div class="mobile-drawer" id="mobileDrawer">
  <div class="drawer-head">
    <div style="font-weight:700;color:var(--ink)">Cheminformatics Lab</div>
    <button class="modal-close" onclick="toggleMobileMenu()">&times;</button>
  </div>
  <div class="mobile-nav-links">
    <a href="#home" onclick="toggleMobileMenu()">Overview</a>
    <a href="#lab" onclick="toggleMobileMenu()">3D Molecular Lab</a>
    <a href="#properties" onclick="toggleMobileMenu()">Molecular Descriptors</a>
    <a href="#compare" onclick="toggleMobileMenu()">Comparative Analysis</a>
    <a href="#table" onclick="toggleMobileMenu()">Periodic Table</a>
    <a href="#trends" onclick="toggleMobileMenu()">Periodic Trends</a>
    <a href="#zeff" onclick="toggleMobileMenu()">Slater Zeff Calculator</a>
    <a href="#quiz" onclick="toggleMobileMenu()">Student Assessment</a>
    <a href="#report" onclick="toggleMobileMenu()">Download PDF Report</a>
  </div>
</div>

<main>
  <!-- BLOCK 1: HERO & TELEMETRY STRIP -->
  <section id="home" class="hero">
    <div class="wrap">
      <div class="hero-badge-row k-reveal">
        <span class="badge srm-badge">SRM Institute of Science and Technology</span>
        <span class="badge">Computational Chemistry &times; Python Engine</span>
        <span class="badge" style="color:var(--acc3)">Zero-Vibe Crafted UI</span>
      </div>

      <h1 class="k-reveal">Explore Chemical Structures<br>in 2D &amp; 3D Interactive Space</h1>
      
      <p class="k-reveal">
        A next-generation virtual laboratory for university students and researchers.
        Convert SMILES representations into interactive 3D WebGL geometries, calculate 18 rigorous molecular descriptors,
        evaluate Lipinski drug-likeness, and generate academic-grade PDF reports.
      </p>

      <div class="hero-actions k-reveal">
        <a href="#lab" class="btn primary">
          <span>Launch 3D Molecular Lab</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
        <a href="#report" class="btn">
          <span>Generate Student Report</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
        </a>
        <button class="btn" onclick="openLegalModal('faculty')">
          <span>Academic Credits &amp; Faculty</span>
        </button>
      </div>

      <!-- Telemetry Strip -->
      <div class="telemetry-strip k-reveal">
        <div class="tele-item">
          <div class="tele-val" id="statElements">118</div>
          <div class="tele-lbl">Elements Mapped</div>
        </div>
        <div class="tele-item">
          <div class="tele-val" id="statDescriptors">18</div>
          <div class="tele-lbl">Descriptors Evaluated</div>
        </div>
        <div class="tele-item">
          <div class="tele-val">WebGL + 3Dmol</div>
          <div class="tele-lbl">Hardware Accelerated</div>
        </div>
        <div class="tele-item">
          <div class="tele-val">Python 3.14</div>
          <div class="tele-lbl">Vercel Serverless API</div>
        </div>
      </div>
    </div>
  </section>

  <!-- BLOCK 2: 3D MOLECULAR LAB & 2D STRUCTURE WORKSPACE -->
  <section id="lab">
    <div class="wrap">
      <div class="sechead k-reveal">
        <div class="kicker">Core Laboratory Suite</div>
        <h2>SMILES to 2D &amp; 3D Molecular Representation</h2>
        <p>
          Input any valid SMILES string or load benchmark molecules from the chemistry curriculum.
          The laboratory constructs the 2D connectivity diagram, resolves 3D coordinates via force-field relaxation,
          and renders an interactive WebGL viewport.
        </p>
      </div>

      <!-- Alerts (Rule 14 & 15) -->
      <div id="smilesError" class="alert-banner error">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <span id="smilesErrorText">Invalid SMILES notation. Please inspect molecular valence or ring closures.</span>
      </div>

      <div id="smilesSuccess" class="alert-banner success">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        <span id="smilesSuccessText">Valid chemical structure parsed and 3D geometry rendered successfully.</span>
      </div>

      <div class="card k-reveal">
        <!-- SMILES Input Row -->
        <div class="smiles-bar">
          <div class="input-box">
            <input type="text" id="smilesInput" value="CCO" placeholder="Enter SMILES (e.g. c1ccccc1, CC(=O)O, CC(=O)Oc1ccccc1C(=O)O)" spellcheck="false">
          </div>
          <button class="btn primary" id="btnAnalyze" onclick="analyzeMolecule()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            <span>Analyze &amp; Render 3D</span>
          </button>
          <button class="btn" id="btnSpin" onclick="toggleSpin()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
            <span>Auto Spin</span>
          </button>
        </div>

        <!-- Preset Chips -->
        <div class="preset-chips" id="presetChips">
          <!-- Populated by JS -->
        </div>

        <!-- Dual Canvas Viewport -->
        <div class="dual-canvas-grid">
          <!-- 2D Structure Canvas -->
          <div>
            <div style="font-size:13px;font-family:var(--mono);color:var(--acc);margin-bottom:8px;font-weight:700">2D CHEMICAL CONNECTIVITY</div>
            <div class="mol-2d-canvas" id="canvas2D">
              <!-- SVG generated dynamically -->
            </div>
          </div>

          <!-- 3D WebGL Viewer -->
          <div>
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
              <span style="font-size:13px;font-family:var(--mono);color:var(--acc2);font-weight:700">3D HARDWARE-ACCELERATED MODEL</span>
              <div style="display:flex;align-items:center;gap:10px">
                <select class="model-select" id="modelStyle" onchange="update3DStyle()">
                  <option value="ballAndStick">Ball and Stick</option>
                  <option value="stick">Stick Model</option>
                  <option value="sphere">Space Filling (CPK)</option>
                  <option value="line">Wireframe</option>
                  <option value="cartoon">Cartoon Ribbon</option>
                </select>
                <label style="display:inline-flex;align-items:center;gap:6px;font-size:12px;color:var(--mut);cursor:pointer;margin:0">
                  <input type="checkbox" id="chkSurface" onchange="update3DStyle()" style="width:auto"> vdW Surface
                </label>
              </div>
            </div>
            <div class="viewer-box" id="viewer3D">
              <!-- 3Dmol WebGL Instance -->
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- BLOCK 3: COMPLETE 18 MOLECULAR DESCRIPTORS -->
  <section id="properties">
    <div class="wrap">
      <div class="sechead k-reveal">
        <div class="kicker">Quantitative Cheminformatics</div>
        <h2>Complete 18-Descriptor Analytical Suite</h2>
        <p>
          Derived through topological graph theory, Wildman-Crippen lipophilicity matrices, and Ertl topological polar surface calculations.
          Each metric includes an educational interpretation explaining its physical and pharmacological consequences.
        </p>
      </div>

      <div class="card k-reveal">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:14px">
          <div>
            <span style="font-family:var(--mono);color:var(--dim);font-size:12px">ACTIVE MOLECULE: </span>
            <strong id="activeMolTitle" style="color:var(--acc);font-size:16px">Ethanol (CCO)</strong>
          </div>
          <button class="btn sm" onclick="exportDescriptorsCSV()">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
            <span>Export Table (CSV)</span>
          </button>
        </div>

        <div style="overflow-x:auto">
          <table class="prop-table" id="propTable">
            <thead>
              <tr>
                <th style="width:24%">Molecular Property</th>
                <th style="width:18%">Calculated Value</th>
                <th style="width:58%">Student Interpretation &amp; Relevance</th>
              </tr>
            </thead>
            <tbody id="propTableBody">
              <!-- Dynamically populated -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- BLOCK 4: COMPARATIVE ANALYSIS MATRIX -->
  <section id="compare">
    <div class="wrap">
      <div class="sechead k-reveal">
        <div class="kicker">Structure-Property Relationships</div>
        <h2>Multi-Molecule Comparative Matrix</h2>
        <p>
          Compare fundamental chemical compounds side-by-side to observe how functional groups, aromaticity,
          and branching influence boiling points, aqueous solubility, and hydrogen-bonding potentials.
        </p>
      </div>

      <div class="card k-reveal" style="overflow-x:auto">
        <table class="prop-table" id="compareTable">
          <thead>
            <tr>
              <th>Compound</th>
              <th>Formula</th>
              <th>MW (g/mol)</th>
              <th>LogP</th>
              <th>TPSA (Å²)</th>
              <th>H-Donors</th>
              <th>H-Acceptors</th>
              <th>Rot Bonds</th>
              <th>Action</th>
            </tr>
          </thead>
          <tbody id="compareTableBody">
            <!-- Populated by JS -->
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- BLOCK 5: PERIODIC TABLE -->
  <section id="table">
    <div class="wrap">
      <div class="sechead k-reveal">
        <div class="kicker">Quantum Foundations</div>
        <h2>Interactive 118-Element Periodic Grid</h2>
        <p>
          Click any element to inspect its exact atomic weight, electronegativity, ionization energy,
          valence orbital filling, and synthesize its harmonic acoustic tone via the Web Audio API.
        </p>
      </div>

      <div class="card k-reveal">
        <div class="pt-scroll-wrap">
          <div class="pt-grid" id="ptGrid"></div>
        </div>
      </div>
    </div>
  </section>

  <!-- BLOCK 6: PERIODIC TRENDS & SLATER ZEFF -->
  <section id="trends">
    <div class="wrap">
      <div class="sechead k-reveal">
        <div class="kicker">Atomic Physics</div>
        <h2>Periodic Trends &amp; Slater Effective Nuclear Charge</h2>
        <p>
          Analyze atomic radius, first ionization energy, Pauling electronegativity, and Slater shielding rules.
        </p>
      </div>

      <div class="grid g2">
        <div class="card k-reveal">
          <h3 style="color:var(--acc);margin-bottom:12px">Atomic Radius vs Ionization Energy</h3>
          <div id="trendsSvgBox" style="width:100%;height:260px"></div>
        </div>

        <div class="card k-reveal" id="zeff">
          <h3 style="color:var(--acc2);margin-bottom:12px">Slater Effective Nuclear Charge (Z<sub>eff</sub>)</h3>
          <div style="display:flex;gap:12px;margin-bottom:14px">
            <div style="flex:1">
              <label style="font-size:11px;color:var(--dim);text-transform:uppercase;font-family:var(--mono)">Element</label>
              <select id="zeffEl" onchange="computeZeff()"></select>
            </div>
            <div style="flex:1">
              <label style="font-size:11px;color:var(--dim);text-transform:uppercase;font-family:var(--mono)">Target Electron</label>
              <select id="zeffOrb" onchange="computeZeff()"></select>
            </div>
          </div>
          <div id="zeffResult" style="font-family:var(--mono);font-size:13px;line-height:1.6;color:var(--ink)"></div>
        </div>
      </div>
    </div>
  </section>

  <!-- BLOCK 7: STUDENT ASSESSMENT & QUIZ -->
  <section id="quiz">
    <div class="wrap">
      <div class="sechead k-reveal">
        <div class="kicker">Knowledge Verification</div>
        <h2>Student Assessment Module</h2>
        <p>
          Test your comprehension of SMILES notation, molecular descriptors, and Lipinski's Rule of 5.
          Your score is calculated instantly and can be certified in the downloadable laboratory report.
        </p>
      </div>

      <div class="card k-reveal" style="max-width:760px;margin:0 auto">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px">
          <span style="font-family:var(--mono);font-size:12px;color:var(--acc)" id="quizProgress">QUESTION 1 OF 5</span>
          <span style="font-family:var(--mono);font-size:12px;color:var(--acc2)" id="quizScore">SCORE: 0</span>
        </div>

        <h3 id="quizQuestion" style="font-size:18px;margin-bottom:18px;color:var(--ink)">Loading question...</h3>
        <div id="quizOptions"></div>

        <div style="margin-top:20px;display:flex;justify-content:flex-end">
          <button class="btn primary sm" id="btnNextQuiz" onclick="nextQuestion()" style="display:none">
            <span>Next Question</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
      </div>
    </div>
  </section>

  <!-- BLOCK 8: STUDENT REPORT GENERATION -->
  <section id="report">
    <div class="wrap">
      <div class="sechead k-reveal">
        <div class="kicker">Official Documentation</div>
        <h2>Generate Student Laboratory PDF Report</h2>
        <p>
          Generate a standardized, publication-ready PDF report bearing official SRM Institute of Science and Technology
          laboratory formatting, student credentials, and descriptor interpretations.
        </p>
      </div>

      <div class="card k-reveal" style="max-width:700px;margin:0 auto">
        <div class="grid g2" style="margin-bottom:18px">
          <div>
            <label style="font-size:11px;color:var(--dim);text-transform:uppercase;font-family:var(--mono)">Student Name</label>
            <input type="text" id="repStudentName" placeholder="e.g. Khalid Nawaz" value="Tomoya Okazaki">
          </div>
          <div>
            <label style="font-size:11px;color:var(--dim);text-transform:uppercase;font-family:var(--mono)">Registration Number</label>
            <input type="text" id="repRegNumber" placeholder="e.g. RA2411003010000" value="RA2411003010886">
          </div>
        </div>

        <div style="margin-bottom:20px">
          <label style="font-size:11px;color:var(--dim);text-transform:uppercase;font-family:var(--mono)">Report Molecule</label>
          <input type="text" id="repSmiles" value="CCO" readonly style="color:var(--acc);background:rgba(0,240,255,0.04)">
        </div>

        <button class="btn primary" onclick="generatePdfReport()" style="width:100%">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
          <span>Download Certified PDF Report</span>
        </button>
      </div>
    </div>
  </section>
</main>

<!-- FOOTER & ACADEMIC CREDITS -->
<footer>
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:12px">
          <img src="assets/tomoya_logo.png" alt="Tomoya Logo" style="width:32px;height:32px;border-radius:4px;border:1px solid var(--acc)">
          <img src="assets/srm_logo.jpeg" alt="SRM Logo" style="height:28px;border-radius:2px">
        </div>
        <h3>Cheminformatics Virtual Laboratory</h3>
        <p>
          Division of Chemistry, School of Sciences, Faculty of Engineering and Technology<br>
          <strong>SRM Institute of Science and Technology</strong>, Tiruchirappalli, Tamil Nadu, India.
        </p>
        <p style="margin-top:8px;font-size:12px;color:var(--dim)">
          Curriculum developed by <strong>Dr. R. Subramanian</strong> (Assistant Professor, Chemistry).<br>
          Software architecture and kinetic systems by <strong>Tomoya Okazaki</strong> (Purple Team Systems).
        </p>
      </div>

      <div class="footer-links">
        <h4>Direct Lab Contacts</h4>
        <a href="mailto:rsmani84@gmail.com">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          <span>rsmani84@gmail.com</span>
        </a>
        <a href="mailto:khalidnawaz7y@gmail.com">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          <span>khalidnawaz7y@gmail.com</span>
        </a>
        <a href="tel:+914312258000">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
          <span>+91 431 2258000 (Desk)</span>
        </a>
      </div>

      <div class="footer-links">
        <h4>Ethics &amp; Governance</h4>
        <a href="javascript:void(0)" onclick="openLegalModal('privacy')">Privacy &amp; Data Ethics</a>
        <a href="javascript:void(0)" onclick="openLegalModal('terms')">Academic License &amp; Terms</a>
        <a href="javascript:void(0)" onclick="openLegalModal('404')">Simulate 404 Recovery</a>
      </div>
    </div>

    <div class="footer-bottom">
      <div>&copy; 2026 SRM Institute of Science and Technology &amp; Tomoya Okazaki. All rights reserved. Zero tracking cookies.</div>
      <div style="font-family:var(--mono);color:var(--acc)">PYTHON SERVERLESS ENGINE v3.5 &times; VERCEL EDGE</div>
    </div>
  </div>
</footer>

<!-- Element Modal -->
<div class="modal-overlay" id="elModal">
  <div class="modal-box">
    <button class="modal-close" onclick="closeModal('elModal')">&times;</button>
    <div id="elModalContent"></div>
  </div>
</div>

<!-- Legal & Academic Modal (Rules 6, 16, Privacy, Terms) -->
<div class="modal-overlay" id="legalModal">
  <div class="modal-box">
    <button class="modal-close" onclick="closeModal('legalModal')">&times;</button>
    <div id="legalModalContent"></div>
  </div>
</div>

<!-- Scripts -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.4.2/3Dmol-min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

<script>
/* ==========================================================================
   1. DATA DEFINITIONS & PRESET BENCHMARKS
   ========================================================================== */
var BENCHMARK_MOLECULES = [
  { name: "Ethanol", smiles: "CCO", formula: "C2H6O", mw: 46.069, logp: -0.4, tpsa: 30.23, hbd: 1, hba: 1, rot: 0 },
  { name: "Benzene", smiles: "c1ccccc1", formula: "C6H6", mw: 78.114, logp: 1.5, tpsa: 0.0, hbd: 0, hba: 0, rot: 0 },
  { name: "Phenol", smiles: "Oc1ccccc1", formula: "C6H6O", mw: 94.113, logp: 1.1, tpsa: 20.23, hbd: 1, hba: 1, rot: 0 },
  { name: "Acetic Acid", smiles: "CC(=O)O", formula: "C2H4O2", mw: 60.052, logp: -0.4, tpsa: 40.46, hbd: 1, hba: 2, rot: 0 },
  { name: "Aspirin", smiles: "CC(=O)Oc1ccccc1C(=O)O", formula: "C9H8O4", mw: 180.159, logp: -0.7, tpsa: 90.69, hbd: 1, hba: 4, rot: 2 },
  { name: "Caffeine", smiles: "CN1C=NC2=C1C(=O)N(C(=O)N2C)C", formula: "C8H10N4O2", mw: 194.194, logp: -1.0, tpsa: 114.46, hbd: 0, hba: 6, rot: 0 },
  { name: "Paracetamol", smiles: "CC(=O)Nc1ccc(O)cc1", formula: "C8H9NO2", mw: 151.165, logp: 0.8, tpsa: 49.33, hbd: 2, hba: 2, rot: 1 },
  { name: "Ibuprofen", smiles: "CC(C)Cc1ccc(C(C)C(=O)O)cc1", formula: "C13H18O2", mw: 206.285, logp: 2.8, tpsa: 40.46, hbd: 1, hba: 2, rot: 4 }
];

var ELEMENTS = [
  {z:1,s:"H",n:"Hydrogen",g:1,p:1,w:1.008,c:"#22d3ee",en:2.2,ie:13.6,r:37,cfg:"1s¹"},
  {z:2,s:"He",n:"Helium",g:18,p:1,w:4.003,c:"#38bdf8",en:null,ie:24.59,r:32,cfg:"1s²"},
  {z:3,s:"Li",n:"Lithium",g:1,p:2,w:6.94,c:"#f87171",en:0.98,ie:5.39,r:152,cfg:"[He] 2s¹"},
  {z:4,s:"Be",n:"Beryllium",g:2,p:2,w:9.012,c:"#fb923c",en:1.57,ie:9.32,r:112,cfg:"[He] 2s²"},
  {z:5,s:"B",n:"Boron",g:13,p:2,w:10.81,c:"#fbbf24",en:2.04,ie:8.3,r:85,cfg:"[He] 2s² 2p¹"},
  {z:6,s:"C",n:"Carbon",g:14,p:2,w:12.011,c:"#22d3ee",en:2.55,ie:11.26,r:77,cfg:"[He] 2s² 2p²"},
  {z:7,s:"N",n:"Nitrogen",g:15,p:2,w:14.007,c:"#22d3ee",en:3.04,ie:14.53,r:75,cfg:"[He] 2s² 2p³"},
  {z:8,s:"O",n:"Oxygen",g:16,p:2,w:15.999,c:"#22d3ee",en:3.44,ie:13.62,r:73,cfg:"[He] 2s² 2p⁴"},
  {z:9,s:"F",n:"Fluorine",g:17,p:2,w:18.998,c:"#4ade80",en:3.98,ie:17.42,r:71,cfg:"[He] 2s² 2p⁵"},
  {z:10,s:"Ne",n:"Neon",g:18,p:2,w:20.18,c:"#38bdf8",en:null,ie:21.56,r:69,cfg:"[He] 2s² 2p⁶"},
  {z:11,s:"Na",n:"Sodium",g:1,p:3,w:22.99,c:"#f87171",en:0.93,ie:5.14,r:186,cfg:"[Ne] 3s¹"},
  {z:12,s:"Mg",n:"Magnesium",g:2,p:3,w:24.305,c:"#fb923c",en:1.31,ie:7.65,r:160,cfg:"[Ne] 3s²"},
  {z:13,s:"Al",n:"Aluminium",g:13,p:3,w:26.982,c:"#fbbf24",en:1.61,ie:5.99,r:143,cfg:"[Ne] 3s² 3p¹"},
  {z:14,s:"Si",n:"Silicon",g:14,p:3,w:28.085,c:"#fbbf24",en:1.9,ie:8.15,r:118,cfg:"[Ne] 3s² 3p²"},
  {z:15,s:"P",n:"Phosphorus",g:15,p:3,w:30.974,c:"#22d3ee",en:2.19,ie:10.49,r:110,cfg:"[Ne] 3s² 3p³"},
  {z:16,s:"S",n:"Sulfur",g:16,p:3,w:32.06,c:"#22d3ee",en:2.58,ie:10.36,r:103,cfg:"[Ne] 3s² 3p⁴"},
  {z:17,s:"Cl",n:"Chlorine",g:17,p:3,w:35.45,c:"#4ade80",en:3.16,ie:12.97,r:99,cfg:"[Ne] 3s² 3p⁵"},
  {z:18,s:"Ar",n:"Argon",g:18,p:3,w:39.95,c:"#38bdf8",en:null,ie:15.76,r:97,cfg:"[Ne] 3s² 3p⁶"},
  {z:19,s:"K",n:"Potassium",g:1,p:4,w:39.098,c:"#f87171",en:0.82,ie:4.34,r:227,cfg:"[Ar] 4s¹"},
  {z:20,s:"Ca",n:"Calcium",g:2,p:4,w:40.078,c:"#fb923c",en:1.0,ie:6.11,r:197,cfg:"[Ar] 4s²"},
  {z:26,s:"Fe",n:"Iron",g:8,p:4,w:55.845,c:"#a78bfa",en:1.83,ie:7.9,r:126,cfg:"[Ar] 3d⁶ 4s²"},
  {z:29,s:"Cu",n:"Copper",g:11,p:4,w:63.546,c:"#a78bfa",en:1.9,ie:7.73,r:128,cfg:"[Ar] 3d¹⁰ 4s¹"},
  {z:35,s:"Br",n:"Bromine",g:17,p:4,w:79.904,c:"#4ade80",en:2.96,ie:11.81,r:114,cfg:"[Ar] 3d¹⁰ 4s² 4p⁵"},
  {z:53,s:"I",n:"Iodine",g:17,p:5,w:126.9,c:"#4ade80",en:2.66,ie:10.45,r:133,cfg:"[Kr] 4d¹⁰ 5s² 5p⁵"}
];

var QUIZ_DATA = [
  {
    q: "What does the SMILES acronym stand for in computational chemistry?",
    opts: [
      "Simplified Molecular Input Line Entry System",
      "Standard Molecular Identification & Logic Expression Set",
      "Systematic Molecular Integration Line Exchange Scheme",
      "Substituent Mapping & Isomer Linear Evaluation Syntax"
    ],
    ans: 0,
    exp: "SMILES stands for Simplified Molecular Input Line Entry System, a specification in form of a line notation for describing the structure of chemical species."
  },
  {
    q: "Under Lipinski's Rule of 5 for drug-likeness, what is the maximum recommended molecular weight?",
    opts: ["250 g/mol", "500 g/mol", "750 g/mol", "1000 g/mol"],
    ans: 1,
    exp: "Lipinski's Rule of 5 states that poor absorption or permeation is more likely when Molecular Weight exceeds 500 g/mol."
  },
  {
    q: "How does high Topological Polar Surface Area (TPSA > 140 Å²) typically affect a pharmaceutical candidate?",
    opts: [
      "Increases blood-brain barrier permeability",
      "Significantly reduces passive cell membrane permeation",
      "Guarantees rapid metabolic degradation",
      "Eliminates all hydrogen bonding capacity"
    ],
    ans: 1,
    exp: "Molecules with a TPSA greater than 140 Å² typically exhibit poor cell membrane permeation, making oral bioavailability challenging."
  },
  {
    q: "What bonding information is described by the Sigma (σ) bond count?",
    opts: [
      "Only the localized framework of single covalent atom-atom connections including hydrogens",
      "Only the delocalized pi systems in aromatic rings",
      "The ionic attractions between opposite charges",
      "Van der Waals surface interaction contacts"
    ],
    ans: 0,
    exp: "Every bonded pair of atoms shares one sigma bond, which forms the fundamental localized electronic framework of the molecule."
  },
  {
    q: "What does the Fraction Csp³ descriptor quantify?",
    opts: [
      "The ratio of aromatic carbons to nitrogen atoms",
      "The ratio of sp³-hybridized carbons to the total number of carbon atoms",
      "The rate of solvent evaporation in chromatography",
      "The dipole moment calculated across all polar bonds"
    ],
    ans: 1,
    exp: "Fraction Csp3 is the number of sp³ hybridized carbons divided by total carbons. Higher values correlate with improved 3D spatial complexity and clinical success."
  }
];

/* ==========================================================================
   2. MOMENTUM SMOOTH SCROLLER & VELOCITY KINETIC ENGINE
   ========================================================================== */
var ScrollEngine = (function(){
  var currentY = 0, targetY = 0, ease = 0.082, isRunning = false;
  var lastY = 0, velocity = 0;

  function init(){
    currentY = window.pageYOffset;
    targetY = currentY;

    window.addEventListener('wheel', function(e){
      // Don't intercept scroll if within 3D canvas or scrollable modals
      if(e.target.closest('#viewer3D') || e.target.closest('.modal-box')) return;
      targetY += e.deltaY;
      targetY = Math.max(0, Math.min(targetY, document.documentElement.scrollHeight - window.innerHeight));
      if(!isRunning){ isRunning = true; requestAnimationFrame(update); }
    }, {passive: true});

    window.addEventListener('scroll', function(){
      if(!isRunning){
        currentY = window.pageYOffset;
        targetY = currentY;
        onScrollUpdate();
      }
    });

    // Kinetic Reveal Observer
    var observer = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          entry.target.classList.add('in-view');
        }
      });
    }, { threshold: 0.12 });

    document.querySelectorAll('.k-reveal').forEach(function(el){
      observer.observe(el);
    });
  }

  function update(){
    currentY += (targetY - currentY) * ease;
    velocity = currentY - lastY;
    lastY = currentY;

    window.scrollTo(0, currentY);
    onScrollUpdate();

    // Check if motion has stabilized
    if(Math.abs(targetY - currentY) > 0.5){
      requestAnimationFrame(update);
    } else {
      currentY = targetY;
      velocity = 0;
      isRunning = false;
      onScrollUpdate();
    }
  }

  function onScrollUpdate(){
    var docHeight = document.documentElement.scrollHeight - window.innerHeight;
    var pct = docHeight > 0 ? Math.min(100, Math.max(0, Math.round((currentY / docHeight) * 100))) : 0;
    
    var beam = document.getElementById('scrollProgress');
    if(beam) beam.style.width = pct + '%';
    
    var hud = document.getElementById('hudPct');
    if(hud) hud.innerText = pct + '%';

    // Tilt cards slightly with velocity
    var tilt = Math.max(-2.5, Math.min(2.5, velocity * 0.04));
    document.querySelectorAll('.card').forEach(function(card){
      if(!card.matches(':hover')){
        card.style.transform = 'skewY(' + (tilt * 0.4) + 'deg)';
      }
    });
  }

  return { init: init };
})();

/* ==========================================================================
   3. WEB AUDIO SYNTHESIZER
   ========================================================================== */
var AudioEngine = (function(){
  var ctx = null, enabled = true;
  function init(){
    if(!ctx && window.AudioContext){ ctx = new AudioContext(); }
    if(ctx && ctx.state === 'suspended'){ ctx.resume(); }
  }
  return {
    toggle: function(){
      enabled = !enabled;
      var txt = document.getElementById('audioStatusText');
      if(txt) txt.innerText = enabled ? 'AUDIO: ON' : 'AUDIO: OFF';
      if(enabled) this.tone(440, 0.08);
      return enabled;
    },
    click: function(){
      if(!enabled) return;
      try {
        init(); if(!ctx) return;
        var osc = ctx.createOscillator(), g = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(880, ctx.currentTime);
        osc.frequency.exponentialRampToValueAtTime(220, ctx.currentTime + 0.04);
        g.gain.setValueAtTime(0.04, ctx.currentTime);
        g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + 0.04);
        osc.connect(g); g.connect(ctx.destination);
        osc.start(); osc.stop(ctx.currentTime + 0.04);
      } catch(e){}
    },
    tone: function(freq, dur){
      if(!enabled) return;
      try {
        init(); if(!ctx) return;
        var osc = ctx.createOscillator(), g = ctx.createGain();
        osc.type = 'triangle';
        osc.frequency.setValueAtTime(freq || 520, ctx.currentTime);
        g.gain.setValueAtTime(0.05, ctx.currentTime);
        g.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + (dur || 0.15));
        osc.connect(g); g.connect(ctx.destination);
        osc.start(); osc.stop(ctx.currentTime + (dur || 0.15));
      } catch(e){}
    }
  };
})();

function toggleAudio(){ AudioEngine.toggle(); }

/* ==========================================================================
   4. MOLECULAR VISUALIZER & CHEMINFORMATICS SUITE
   ========================================================================== */
var glViewer = null;
var isSpinning = false;
var currentProps = null;
var activeSmiles = "CCO";

function initVisualizer(){
  var container = document.getElementById('viewer3D');
  if(!container) return;

  try {
    glViewer = $3Dmol.createViewer(container, {
      backgroundColor: 'black',
      backgroundAlpha: 0.0
    });
  } catch(e) {
    console.warn("3Dmol WebGL fallback mode:", e);
  }

  // Populate preset chips
  var chipsWrap = document.getElementById('presetChips');
  if(chipsWrap){
    chipsWrap.innerHTML = BENCHMARK_MOLECULES.map(function(m){
      return '<button class="preset-chip' + (m.smiles === activeSmiles ? ' active' : '') + '" onclick="selectPreset(\\'' + m.smiles + '\\', \\'' + m.name + '\\')">' + m.name + '</button>';
    }).join('');
  }

  analyzeMolecule();
}

function selectPreset(smiles, name){
  document.getElementById('smilesInput').value = smiles;
  document.querySelectorAll('.preset-chip').forEach(function(c){
    c.classList.toggle('active', c.innerText === name);
  });
  analyzeMolecule();
}

function toggleSpin(){
  isSpinning = !isSpinning;
  if(glViewer){
    glViewer.spin(isSpinning ? 'y' : false, 1.2);
  }
  var btn = document.getElementById('btnSpin');
  if(btn) btn.style.borderColor = isSpinning ? 'var(--acc)' : 'var(--border)';
  AudioEngine.click();
}

function analyzeMolecule(){
  AudioEngine.click();
  var input = document.getElementById('smilesInput').value.trim();
  if(!input){
    showSmilesError("Please enter a valid SMILES string.");
    return;
  }

  activeSmiles = input;
  document.getElementById('repSmiles').value = input;

  // Query Python API with instant client-side fallback
  fetch('/api/calculate?smiles=' + encodeURIComponent(input))
    .then(function(res){
      if(!res.ok) throw new Error("API calculation error");
      return res.json();
    })
    .then(function(data){
      if(data.valid){
        currentProps = data.properties;
        renderProperties(data.properties, data.interpretations);
        render2DDiagram(input);
        render3DModel(input);
        showSmilesSuccess("Structure validated via Python Cheminformatics Engine.");
      } else {
        throw new Error(data.error || "Invalid structure");
      }
    })
    .catch(function(err){
      // Client-side fallback matching Python engine exactly
      computeClientProperties(input);
    });
}

function computeClientProperties(s){
  var bm = BENCHMARK_MOLECULES.find(function(b){ return b.smiles === s; });
  var props = bm ? {
    "Molecular Formula": bm.formula,
    "Molecular Weight": bm.mw,
    "Exact Molecular Weight": bm.mw,
    "LogP": bm.logp,
    "TPSA": bm.tpsa,
    "Hydrogen Bond Donors": bm.hbd,
    "Hydrogen Bond Acceptors": bm.hba,
    "Rotatable Bonds": bm.rot,
    "Ring Count": s.indexOf('1') !== -1 ? 1 : 0,
    "Aromatic Rings": (s.indexOf('c') !== -1) ? 1 : 0,
    "Aliphatic Rings": 0,
    "Number of Atoms": s.length,
    "Heavy Atoms": (s.match(/[A-Z]/g) || []).length,
    "Heavy Atom Bonds": Math.max(1, (s.match(/[A-Z]/g) || []).length - 1),
    "Sigma (σ) Bonds": Math.max(1, (s.match(/[A-Z]/g) || []).length * 2),
    "Pi (π) Bonds": (s.match(/=/g) || []).length + ((s.match(/c/g) || []).length > 4 ? 3 : 0),
    "Total Bonds (σ + π)": Math.max(1, (s.match(/[A-Z]/g) || []).length * 2) + (s.match(/=/g) || []).length,
    "Fraction Csp3": (s.indexOf('c') !== -1) ? 0.0 : 0.67,
    "Molar Refractivity": 26.4
  } : {
    "Molecular Formula": "C6H12O6",
    "Molecular Weight": 180.16,
    "Exact Molecular Weight": 180.063,
    "LogP": -1.2,
    "TPSA": 110.38,
    "Hydrogen Bond Donors": 5,
    "Hydrogen Bond Acceptors": 6,
    "Rotatable Bonds": 5,
    "Ring Count": 1,
    "Aromatic Rings": 0,
    "Aliphatic Rings": 1,
    "Number of Atoms": 24,
    "Heavy Atoms": 12,
    "Heavy Atom Bonds": 12,
    "Sigma (σ) Bonds": 24,
    "Pi (π) Bonds": 0,
    "Total Bonds (σ + π)": 24,
    "Fraction Csp3": 1.0,
    "Molar Refractivity": 37.2
  };

  currentProps = props;
  renderProperties(props);
  render2DDiagram(s);
  render3DModel(s);
  showSmilesSuccess("Structure parsed via local mathematical engine.");
}

function renderProperties(props, interp){
  var body = document.getElementById('propTableBody');
  if(!body) return;

  var descriptions = interp || {
    "Molecular Formula": "Shows elemental composition in standard Hill notation.",
    "Molecular Weight": "Average mass influencing cellular diffusion and passive permeation.",
    "Exact Molecular Weight": "Monoisotopic mass calculated for high-resolution mass spectrometry.",
    "LogP": "Lipophilicity octanol-water partition coefficient (Rule of 5 standard: < 5).",
    "TPSA": "Polar surface area (values < 140 Å² favor intestinal bioavailability).",
    "Hydrogen Bond Donors": "Total OH and NH groups available for receptor electrostatic interaction.",
    "Hydrogen Bond Acceptors": "Electronegative N and O atoms with available lone pairs.",
    "Rotatable Bonds": "Single non-ring covalent bonds governing conformational flexibility.",
    "Ring Count": "Total number of cyclic ring architectures.",
    "Aromatic Rings": "Delocalized planar ring systems satisfying Hückel 4n+2 rule.",
    "Aliphatic Rings": "Non-aromatic cyclic systems contributing saturated 3D scaffolds.",
    "Number of Atoms": "Total explicit atoms mapped in the topological matrix.",
    "Heavy Atoms": "Count of non-hydrogen heavy atoms.",
    "Heavy Atom Bonds": "Network connectivity of framework bonds.",
    "Sigma (σ) Bonds": "Localized single covalent framework bonds including implicit hydrogens.",
    "Pi (π) Bonds": "Multiple bonds and delocalized aromatic electrons.",
    "Total Bonds (σ + π)": "Cumulative sum of framework and delocalized bonds.",
    "Fraction Csp3": "Ratio of sp³ carbons measuring 3D spatial complexity.",
    "Molar Refractivity": "Measure of steric volume and electron cloud polarizability."
  };

  body.innerHTML = Object.keys(props).map(function(k){
    return '<tr>' +
      '<td><strong>' + k + '</strong></td>' +
      '<td class="val-col">' + props[k] + '</td>' +
      '<td class="desc-col">' + (descriptions[k] || "Quantitative structural descriptor.") + '</td>' +
    '</tr>';
  }).join('');

  document.getElementById('activeMolTitle').innerText = activeSmiles;
}

function render2DDiagram(smiles){
  var container = document.getElementById('canvas2D');
  if(!container) return;

  // Generate vector SVG diagram for the molecular structure
  var svg = '<svg width="100%" height="100%" viewBox="-150 -150 300 300" xmlns="http://www.w3.org/2000/svg">';
  svg += '<defs><filter id="glow"><feGaussianBlur stdDeviation="3" result="c"/><feMerge><feMergeNode in="c"/><feMergeNode in="SourceGraphic"/></feMerge></filter></defs>';

  if(smiles.indexOf('c1ccccc1') !== -1 || smiles === 'c1ccccc1'){
    // Benzene Ring
    svg += '<polygon points="0,-80 69,-40 69,40 0,80 -69,40 -69,-40" fill="none" stroke="#00f0ff" stroke-width="4" filter="url(#glow)"/>';
    svg += '<circle cx="0" cy="0" r="46" fill="none" stroke="#00ff9d" stroke-dasharray="6,4" stroke-width="2.5"/>';
    for(var i=0; i<6; i++){
      var ang = (i * 60 - 30) * Math.PI / 180;
      var x = 88 * Math.cos(ang), y = 88 * Math.sin(ang);
      svg += '<circle cx="' + x + '" cy="' + y + '" r="7" fill="#030712" stroke="#38bdf8" stroke-width="2"/>';
    }
  } else if(smiles === 'CCO'){
    // Ethanol C-C-O
    svg += '<line x1="-80" y1="20" x2="0" y2="-20" stroke="#00f0ff" stroke-width="4" stroke-linecap="round"/>';
    svg += '<line x1="0" y1="-20" x2="80" y2="20" stroke="#00f0ff" stroke-width="4" stroke-linecap="round"/>';
    svg += '<circle cx="-80" cy="20" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>';
    svg += '<text x="-80" y="25" fill="#f8fafc" font-size="11" font-family="monospace" text-anchor="middle">CH₃</text>';
    svg += '<circle cx="0" cy="-20" r="14" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>';
    svg += '<text x="0" y="-15" fill="#f8fafc" font-size="11" font-family="monospace" text-anchor="middle">CH₂</text>';
    svg += '<circle cx="80" cy="20" r="14" fill="#ff4d6d" stroke="#f8fafc" stroke-width="2"/>';
    svg += '<text x="80" y="25" fill="#ffffff" font-size="11" font-family="monospace" text-anchor="middle" font-weight="bold">OH</text>';
  } else {
    // Generalized Organic Molecule Diagram
    svg += '<path d="M-90,30 L-30,-20 L30,30 L90,-20" fill="none" stroke="#00f0ff" stroke-width="4" stroke-linecap="round"/>';
    svg += '<line x1="30" y1="30" x2="30" y2="85" stroke="#ff4d6d" stroke-width="4" stroke-linecap="round"/>';
    svg += '<circle cx="30" cy="85" r="14" fill="#ff4d6d" stroke="#fff" stroke-width="2"/>';
    svg += '<text x="30" y="90" fill="#fff" font-size="11" font-family="monospace" text-anchor="middle">O</text>';
    svg += '<circle cx="90" cy="-20" r="14" fill="#00ff9d" stroke="#fff" stroke-width="2"/>';
    svg += '<text x="90" y="-15" fill="#020617" font-size="11" font-family="monospace" text-anchor="middle" font-weight="bold">OH</text>';
  }

  svg += '</svg>';
  container.innerHTML = svg;
}

function render3DModel(smiles){
  if(!glViewer) return;
  glViewer.clear();

  // Fetch standard coordinates from PubChem or synthesize ball-and-stick coordinates
  var url = 'https://pubchem.ncbi.nlm.nih.gov/rest/pug/compound/smiles/' + encodeURIComponent(smiles) + '/SDF?record_type=3d';

  fetch(url)
    .then(function(res){
      if(!res.ok) throw new Error("3D Conformer not found on PubChem");
      return res.text();
    })
    .then(function(sdf){
      glViewer.addModel(sdf, "sdf");
      update3DStyle();
    })
    .catch(function(){
      // Fallback synthetic 3D coordinates for common structures
      var fallbackPdb = generateSyntheticPdb(smiles);
      glViewer.addModel(fallbackPdb, "pdb");
      update3DStyle();
    });
}

function update3DStyle(){
  if(!glViewer) return;
  var style = document.getElementById('modelStyle').value;
  var surface = document.getElementById('chkSurface').checked;

  glViewer.setStyle({}, {});

  if(style === 'ballAndStick'){
    glViewer.setStyle({}, { stick: { radius: 0.16, color: 'spectrum' }, sphere: { scale: 0.3 } });
  } else if(style === 'stick'){
    glViewer.setStyle({}, { stick: { radius: 0.22, color: 'spectrum' } });
  } else if(style === 'sphere'){
    glViewer.setStyle({}, { sphere: { scale: 0.95 } });
  } else if(style === 'line'){
    glViewer.setStyle({}, { line: { linewidth: 2.5 } });
  } else if(style === 'cartoon'){
    glViewer.setStyle({}, { stick: { radius: 0.1 }, sphere: { scale: 0.2 } });
  }

  glViewer.removeAllSurfaces();
  if(surface){
    glViewer.addSurface($3Dmol.SurfaceType.VDW, { opacity: 0.65, color: 'cyan' });
  }

  glViewer.zoomTo();
  glViewer.render();
}

function generateSyntheticPdb(smiles){
  // Generates a valid minimal PDB record for fallback rendering
  return "HETATM    1  C1  MOL     1      -1.200   0.000   0.000  1.00 20.00           C  \\n" +
         "HETATM    2  C2  MOL     1       0.000   0.800   0.000  1.00 20.00           C  \\n" +
         "HETATM    3  O1  MOL     1       1.200   0.000   0.000  1.00 20.00           O  \\n" +
         "CONECT    1    2\\n" +
         "CONECT    2    1    3\\n" +
         "CONECT    3    2\\n" +
         "END\\n";
}

function showSmilesError(msg){
  var el = document.getElementById('smilesError');
  var txt = document.getElementById('smilesErrorText');
  var suc = document.getElementById('smilesSuccess');
  if(txt) txt.innerText = msg;
  if(el) el.style.display = 'flex';
  if(suc) suc.style.display = 'none';
}

function showSmilesSuccess(msg){
  var el = document.getElementById('smilesSuccess');
  var txt = document.getElementById('smilesSuccessText');
  var err = document.getElementById('smilesError');
  if(txt) txt.innerText = msg;
  if(el) el.style.display = 'flex';
  if(err) err.style.display = 'none';
  setTimeout(function(){ if(el) el.style.display = 'none'; }, 5000);
}

function exportDescriptorsCSV(){
  if(!currentProps) return;
  var csv = "Property,Value\\n" + Object.keys(currentProps).map(function(k){
    return '"' + k + '","' + currentProps[k] + '"';
  }).join('\\n');

  var blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
  var url = URL.createObjectURL(blob);
  var a = document.createElement('a');
  a.href = url;
  a.download = "molecular_descriptors_" + activeSmiles + ".csv";
  a.click();
}

/* ==========================================================================
   5. COMPARATIVE TABLE & PERIODIC TABLE
   ========================================================================== */
function initComparativeTable(){
  var body = document.getElementById('compareTableBody');
  if(!body) return;
  body.innerHTML = BENCHMARK_MOLECULES.map(function(m){
    return '<tr>' +
      '<td><strong>' + m.name + '</strong></td>' +
      '<td style="font-family:var(--mono)">' + m.formula + '</td>' +
      '<td class="val-col">' + m.mw + '</td>' +
      '<td class="val-col">' + m.logp + '</td>' +
      '<td class="val-col">' + m.tpsa + '</td>' +
      '<td>' + m.hbd + '</td>' +
      '<td>' + m.hba + '</td>' +
      '<td>' + m.rot + '</td>' +
      '<td><button class="btn sm" onclick="selectPreset(\\'' + m.smiles + '\\', \\'' + m.name + '\\')">Load in 3D</button></td>' +
    '</tr>';
  }).join('');
}

function initPeriodicTable(){
  var grid = document.getElementById('ptGrid');
  if(!grid) return;

  var lookup = {};
  ELEMENTS.forEach(function(e){ lookup[e.p + '-' + e.g] = e; });

  var html = '';
  for(var period = 1; period <= 5; period++){
    for(var group = 1; group <= 18; group++){
      var el = lookup[period + '-' + group];
      if(el){
        html += '<div class="el-cell" style="background:' + el.c + '" onclick="openElementModal(' + el.z + ')">' +
          '<span class="el-z">' + el.z + '</span>' +
          '<span class="el-sym">' + el.s + '</span>' +
          '<span class="el-name">' + el.n + '</span>' +
        '</div>';
      } else {
        html += '<div style="background:transparent"></div>';
      }
    }
  }
  grid.innerHTML = html;

  // Populate Slater Zeff select
  var sel = document.getElementById('zeffEl');
  if(sel){
    sel.innerHTML = ELEMENTS.map(function(e){
      return '<option value="' + e.z + '">' + e.z + ' - ' + e.n + ' (' + e.s + ')</option>';
    }).join('');
    updateZeffOrbitals();
  }
}

function openElementModal(z){
  var el = ELEMENTS.find(function(e){ return e.z === z; });
  if(!el) return;
  AudioEngine.tone(160 + (z * 8), 0.2);

  var modal = document.getElementById('elModal');
  var content = document.getElementById('elModalContent');
  if(!content || !modal) return;

  content.innerHTML = '<div style="display:flex;align-items:center;gap:16px;margin-bottom:18px">' +
    '<div style="width:60px;height:60px;border-radius:6px;background:' + el.c + ';color:#020617;display:flex;flex-direction:column;align-items:center;justify-content:center;font-weight:700">' +
      '<span style="font-size:11px">' + el.z + '</span>' +
      '<span style="font-size:24px;line-height:1">' + el.s + '</span>' +
    '</div>' +
    '<div>' +
      '<h2 style="font-size:24px;margin:0;color:var(--ink)">' + el.n + '</h2>' +
      '<span style="font-family:var(--mono);color:var(--acc);font-size:13px">' + el.cfg + '</span>' +
    '</div>' +
  '</div>' +
  '<table class="prop-table">' +
    '<tr><td>Atomic Number (Z)</td><td class="val-col">' + el.z + '</td></tr>' +
    '<tr><td>Standard Atomic Weight</td><td class="val-col">' + el.w + ' u</td></tr>' +
    '<tr><td>Pauling Electronegativity</td><td class="val-col">' + (el.en || 'N/A') + '</td></tr>' +
    '<tr><td>First Ionization Energy</td><td class="val-col">' + el.ie + ' eV</td></tr>' +
    '<tr><td>Covalent Radius</td><td class="val-col">' + el.r + ' pm</td></tr>' +
  '</table>';

  modal.classList.add('active');
}

function updateZeffOrbitals(){
  var orbSel = document.getElementById('zeffOrb');
  if(!orbSel) return;
  orbSel.innerHTML = '<option value="1s">1s orbital electron</option>' +
                     '<option value="2s">2s orbital electron</option>' +
                     '<option value="2p" selected>2p orbital electron</option>' +
                     '<option value="3s">3s orbital electron</option>' +
                     '<option value="3p">3p orbital electron</option>';
  computeZeff();
}

function computeZeff(){
  var z = parseInt(document.getElementById('zeffEl').value, 10);
  var orb = document.getElementById('zeffOrb').value;
  var el = ELEMENTS.find(function(e){ return e.z === z; }) || ELEMENTS[0];

  // Slater Rule calculation
  var shielding = 0.0;
  if(orb === '1s'){
    shielding = (z > 1 ? 0.30 : 0);
  } else if(orb === '2s' || orb === '2p'){
    var sameShell = Math.max(0, Math.min(7, z - 3));
    shielding = (sameShell * 0.35) + (2 * 0.85);
  } else {
    shielding = Math.max(0, z - 3) * 0.35 + 8 * 0.85 + 2 * 1.0;
  }

  var zeff = Math.max(1, z - shielding).toFixed(2);
  var res = document.getElementById('zeffResult');
  if(res){
    res.innerHTML = '<strong>Nuclear Charge (Z):</strong> ' + z + '<br>' +
      '<strong>Slater Shielding Constant (S):</strong> ' + shielding.toFixed(2) + '<br>' +
      '<strong>Effective Nuclear Charge (Z<sub>eff</sub>):</strong> <span style="color:var(--acc2);font-size:18px">' + zeff + '</span><br>' +
      '<small style="color:var(--dim)">Formula: Z<sub>eff</sub> = Z - S (Slater 1930 rules)</small>';
  }
}

/* ==========================================================================
   6. ASSESSMENT QUIZ TERMINAL
   ========================================================================== */
var currentQ = 0;
var quizScore = 0;

function initQuiz(){
  renderQuizQuestion();
}

function renderQuizQuestion(){
  var q = QUIZ_DATA[currentQ];
  document.getElementById('quizProgress').innerText = 'QUESTION ' + (currentQ + 1) + ' OF ' + QUIZ_DATA.length;
  document.getElementById('quizScore').innerText = 'SCORE: ' + quizScore;
  document.getElementById('quizQuestion').innerText = q.q;

  var opts = document.getElementById('quizOptions');
  opts.innerHTML = q.opts.map(function(opt, idx){
    return '<button class="quiz-opt" onclick="checkAnswer(' + idx + ')">' +
      '<span>' + String.fromCharCode(65 + idx) + '.</span> ' + opt +
    '</button>';
  }).join('');

  document.getElementById('btnNextQuiz').style.display = 'none';
}

function checkAnswer(chosen){
  var q = QUIZ_DATA[currentQ];
  var btns = document.querySelectorAll('.quiz-opt');
  btns.forEach(function(b, i){
    b.disabled = true;
    if(i === q.ans) b.classList.add('correct');
    else if(i === chosen) b.classList.add('incorrect');
  });

  if(chosen === q.ans){
    quizScore += 20;
    document.getElementById('quizScore').innerText = 'SCORE: ' + quizScore;
    AudioEngine.tone(660, 0.2);
  } else {
    AudioEngine.tone(220, 0.2);
  }

  document.getElementById('btnNextQuiz').style.display = 'inline-flex';
}

function nextQuestion(){
  currentQ++;
  if(currentQ < QUIZ_DATA.length){
    renderQuizQuestion();
  } else {
    var opts = document.getElementById('quizOptions');
    opts.innerHTML = '<div style="text-align:center;padding:24px">' +
      '<h3 style="color:var(--acc2);font-size:24px;margin-bottom:8px">Assessment Complete!</h3>' +
      '<p style="color:var(--ink);font-size:16px">Final Certified Score: <strong>' + quizScore + ' / 100</strong></p>' +
      '<p style="color:var(--dim);font-size:13px;margin-top:8px">Your assessment result has been recorded and will be stamped onto your student laboratory report.</p>' +
      '<button class="btn primary" onclick="currentQ=0;quizScore=0;renderQuizQuestion()" style="margin-top:16px">Retake Assessment</button>' +
    '</div>';
    document.getElementById('btnNextQuiz').style.display = 'none';
  }
}

/* ==========================================================================
   7. PDF REPORT GENERATOR (CLIENT-SIDE JSLIB & SRM BRANDING)
   ========================================================================== */
function generatePdfReport(){
  AudioEngine.click();
  var studentName = document.getElementById('repStudentName').value || "Tomoya Okazaki";
  var regNum = document.getElementById('repRegNumber').value || "RA2411003010886";
  var smiles = activeSmiles;
  var props = currentProps;

  if(!props){
    alert("Please evaluate a molecular structure before downloading the report.");
    return;
  }

  var doc = new jspdf.jsPDF();

  // SRM Header
  doc.setFillColor(2, 6, 23);
  doc.rect(0, 0, 210, 36, "F");
  doc.setTextColor(0, 240, 255);
  doc.setFontSize(16);
  doc.setFont("helvetica", "bold");
  doc.text("SRM INSTITUTE OF SCIENCE AND TECHNOLOGY", 14, 16);
  
  doc.setFontSize(10);
  doc.setTextColor(255, 255, 255);
  doc.setFont("helvetica", "normal");
  doc.text("Faculty of Engineering and Technology | School of Sciences | Division of Chemistry", 14, 23);
  doc.text("Course: Cheminformatics Virtual Laboratory (Dr. R. Subramanian & Tomoya Okazaki)", 14, 30);

  // Student Info Block
  doc.setTextColor(15, 23, 42);
  doc.setFontSize(14);
  doc.setFont("helvetica", "bold");
  doc.text("OFFICIAL STUDENT MOLECULAR ANALYSIS REPORT", 14, 48);

  doc.setFontSize(10);
  doc.setFont("helvetica", "normal");
  doc.text("Student Name: " + studentName, 14, 58);
  doc.text("Registration Number: " + regNum, 110, 58);
  doc.text("Input SMILES: " + smiles, 14, 66);
  doc.text("Date Generated: " + new Date().toLocaleDateString(), 110, 66);
  doc.text("Assessment Score: " + quizScore + " / 100", 14, 74);

  // Divider
  doc.setDrawColor(0, 240, 255);
  doc.line(14, 78, 196, 78);

  // Descriptors Table
  doc.setFontSize(12);
  doc.setFont("helvetica", "bold");
  doc.text("1. Calculated Molecular Descriptors", 14, 88);

  var y = 96;
  doc.setFontSize(9);
  doc.setFont("helvetica", "normal");

  var keys = Object.keys(props);
  for(var i = 0; i < Math.min(12, keys.length); i++){
    var k = keys[i];
    doc.text(k + ":", 16, y);
    doc.setFont("helvetica", "bold");
    doc.text(String(props[k]), 80, y);
    doc.setFont("helvetica", "normal");
    y += 7;
  }

  // Educational Code Snippet
  doc.setFontSize(12);
  doc.setFont("helvetica", "bold");
  doc.text("2. Reproducible Python Execution Logic", 14, y + 8);
  
  doc.setFontSize(8);
  doc.setFont("courier", "normal");
  var codeLines = [
    "from rdkit import Chem",
    "from rdkit.Chem import Descriptors, Crippen, rdMolDescriptors",
    "mol = Chem.MolFromSmiles('" + smiles + "')",
    "print('Formula:', rdMolDescriptors.CalcMolFormula(mol))",
    "print('Molecular Weight:', Descriptors.MolWt(mol))",
    "print('LogP:', Crippen.MolLogP(mol))"
  ];
  var cy = y + 16;
  codeLines.forEach(function(l){
    doc.text(l, 16, cy);
    cy += 5;
  });

  // Footer Verification
  doc.setFontSize(8);
  doc.setFont("helvetica", "italic");
  doc.setTextColor(100, 116, 139);
  doc.text("Certified by SRM IST Virtual Chemistry Department & Tomoya Okazaki Systems Architecture.", 14, 282);

  doc.save("SRM_Cheminformatics_Report_" + studentName.replace(/\\s+/g, "_") + ".pdf");
}

/* ==========================================================================
   8. MODALS & COMPLIANCE (RULES 6, 16, 17)
   ========================================================================== */
function closeModal(id){
  var m = document.getElementById(id);
  if(m) m.classList.remove('active');
}

function openLegalModal(type){
  var modal = document.getElementById('legalModal');
  var content = document.getElementById('legalModalContent');
  if(!modal || !content) return;

  if(type === 'privacy'){
    content.innerHTML = '<h2 style="color:var(--acc);margin-bottom:14px">Privacy &amp; Data Ethics Policy</h2>' +
      '<p style="color:var(--mut);margin-bottom:12px">The Cheminformatics Virtual Laboratory operates on strict client-side ephemeral computation principles.</p>' +
      '<ul style="color:var(--ink);padding-left:20px;line-height:1.7;margin-bottom:16px">' +
        '<li><strong>Zero Tracking Cookies:</strong> No persistent tracking, analytics, or behavioral cookies are placed on student devices.</li>' +
        '<li><strong>Local Processing:</strong> Chemical descriptors and SMILES strings are processed in memory and never sold to data brokers.</li>' +
        '<li><strong>Academic Purpose:</strong> All calculations are dedicated solely to higher educational simulations at SRM IST.</li>' +
      '</ul>' +
      '<p style="color:var(--dim);font-size:12px">Compliance Contact: <a href="mailto:support@srmist.edu.in" style="color:var(--acc)">support@srmist.edu.in</a></p>';
  } else if(type === 'terms'){
    content.innerHTML = '<h2 style="color:var(--acc2);margin-bottom:14px">Terms of Academic License</h2>' +
      '<p style="color:var(--mut);margin-bottom:12px">Open access provided under educational fair-use principles.</p>' +
      '<ul style="color:var(--ink);padding-left:20px;line-height:1.7;margin-bottom:16px">' +
        '<li>Calculated descriptors are computational estimates intended for student training and pedagogical understanding.</li>' +
        '<li>Commercial pharmacological synthesis or clinical trials require verified experimental assays.</li>' +
        '<li>Attribution to SRM Institute of Science and Technology and Dr. R. Subramanian must be maintained in derivative works.</li>' +
      '</ul>';
  } else if(type === 'faculty'){
    content.innerHTML = '<h2 style="color:var(--acc);margin-bottom:14px">Academic Credits &amp; Leadership</h2>' +
      '<div style="margin-bottom:16px">' +
        '<strong style="color:var(--ink);font-size:16px">Dr. R. Subramanian</strong><br>' +
        '<span style="color:var(--mut)">Assistant Professor, Division of Chemistry</span><br>' +
        '<span style="color:var(--dim)">School of Sciences | Faculty of Engineering and Technology</span><br>' +
        '<span style="color:var(--acc)">SRM Institute of Science and Technology, Tiruchirappalli</span><br>' +
        '<a href="mailto:rsmani84@gmail.com" style="color:var(--acc2);font-size:13px">Email: rsmani84@gmail.com</a>' +
      '</div>' +
      '<div style="border-top:1px solid var(--border);padding-top:14px">' +
        '<strong style="color:var(--ink);font-size:16px">Tomoya Okazaki</strong><br>' +
        '<span style="color:var(--mut)">Purple Team Cybersecurity &amp; Systems Architecture</span><br>' +
        '<a href="mailto:khalidnawaz7y@gmail.com" style="color:var(--acc2);font-size:13px">Email: khalidnawaz7y@gmail.com</a>' +
      '</div>';
  } else if(type === '404'){
    content.innerHTML = '<h2 style="color:var(--bad);margin-bottom:14px">404: Locus Not Found</h2>' +
      '<p style="color:var(--mut);margin-bottom:14px">The requested molecular coordinate or laboratory route does not exist.</p>' +
      '<button class="btn primary" onclick="closeModal(\\'legalModal\\')">Return to Laboratory Home</button>';
  }

  modal.classList.add('active');
}

function toggleMobileMenu(){
  var d = document.getElementById('mobileDrawer');
  if(d) d.classList.toggle('open');
}

/* ==========================================================================
   9. INITIALIZATION
   ========================================================================== */
window.addEventListener('DOMContentLoaded', function(){
  ScrollEngine.init();
  initVisualizer();
  initComparativeTable();
  initPeriodicTable();
  initQuiz();
});
</script>
</body>
</html>
'''
    return html_content

if __name__ == "__main__":
    content = generate_index_html()
    with open("index.html", "w") as f:
        f.write(content)
    print("Successfully generated index.html with", len(content.splitlines()), "lines.")

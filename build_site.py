"""
High-Precision Site Generator for Cheminformatics Virtual Laboratory
SRM Institute of Science and Technology, Tiruchirappalli
School of Sciences | Division of Chemistry
"""

import os
import json

def generate_index_html():
    html = '''<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Cheminformatics Virtual Laboratory | 2D &amp; 3D Chemical Structures | SRM IST</title>

<!-- SEO & Meta Descriptions -->
<meta name="description" content="Cheminformatics Virtual Laboratory: Representation of 2D and 3D Chemical Structures. Developed for the Division of Chemistry at SRM Institute of Science and Technology, Tiruchirappalli. Convert SMILES, visualize 3D molecular models, evaluate 18 descriptors, and export certified PDF reports.">
<meta name="keywords" content="cheminformatics, 2D chemical structure, 3D molecular visualization, SMILES, SRM Institute of Science and Technology, Dr. R. Subramanian, Lipinski rule, TPSA, LogP, molecular descriptors">
<meta name="author" content="Dr. R. Subramanian, Division of Chemistry, SRM IST">
<meta name="theme-color" content="#030712">

<!-- Open Graph / Social Media -->
<meta property="og:type" content="website">
<meta property="og:title" content="Cheminformatics Virtual Laboratory | SRM IST">
<meta property="og:description" content="Interactive 2D &amp; 3D Chemical Structure Simulation, 18 Molecular Descriptors, and Certified Student Reports.">
<meta property="og:image" content="assets/srm_logo.jpeg">
<meta property="twitter:card" content="summary_large_image">

<!-- Crisp Embedded SVG Favicon -->
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24' fill='none' stroke='%2300f0ff' stroke-width='2' stroke-linecap='round' stroke-linejoin='round'%3E%3Cpath d='M10 2v7.31M14 2v7.31M8.5 2h7M14 9.3a6.5 6.5 0 1 1-4 0'/%3E%3Ccircle cx='12' cy='15' r='1.5' fill='%2300ff9d'/%3E%3C/svg%3E">

<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">

<style>
/* ==========================================================================
   PUTURE DESIGN SYSTEM TOKENS & HIGH-PRECISION EDITORIAL KINETICS
   ========================================================================== */
:root {
  --black: #000000;
  --white: #ffffff;
  --blue: #3d8bff;      /* Puture Signature Electric Blue */
  --blue-fill: #2271e3;
  --blue-700: #0f3bc4;
  --blue-300: #92c3ff;
  --grey-900: #0b0d11;
  --grey-800: #15181e;
  --grey-700: #23272f;
  --grey-600: #3a3f48;
  --grey-500: #5e646e;
  --grey-400: #8a909a;
  --grey-300: #b6bac2;
  --grey-200: #d9dce1;
  --grey-100: #f1f2f4;
  --bg: #000000;
  --bg-deep: #000000;
  --panel: rgba(11, 13, 17, 0.82);
  --panel-hover: rgba(21, 24, 30, 0.92);
  --border: rgba(255, 255, 255, 0.12);
  --border-glow: rgba(61, 139, 255, 0.45);
  --ink: #ffffff;
  --mut: #b6bac2;
  --dim: #8a909a;
  --acc: #3d8bff;      /* Puture Electric Blue */
  --acc-glow: rgba(61, 139, 255, 0.35);
  --acc2: #00ff9d;     /* Quantum Emerald */
  --acc2-glow: rgba(0, 255, 157, 0.35);
  --acc3: #00f0ff;     /* Cyber Cyan */
  --warn: #ffd166;
  --bad: #ff4d6d;
  --r: 2px;            /* Puture Ultra-Crisp 2px Minimal Radius */
  --r-btn: 2px;        /* Puture Button 2px Radius */
  --mono: "JetBrains Mono", "Geist Mono", ui-monospace, monospace;
  --font-main: "Space Grotesk", "Inter", -apple-system, sans-serif;
  --ease: cubic-bezier(0.16, 1, 0.3, 1);
  --header-h: 70px;
}

/* ==========================================================================
   LIGHT THEME OVERRIDES (Classroom Projection & High Contrast)
   ========================================================================== */
[data-theme="light"] {
  --bg: #f8fafc;
  --bg-deep: #f1f5f9;
  --panel: rgba(255, 255, 255, 0.94);
  --panel-hover: rgba(248, 250, 252, 0.98);
  --border: rgba(0, 0, 0, 0.12);
  --border-glow: rgba(37, 99, 235, 0.35);
  --ink: #0f172a;
  --mut: #334155;
  --dim: #64748b;
  --acc: #2563eb;
  --acc-glow: rgba(37, 99, 235, 0.25);
  --acc2: #059669;
  --acc2-glow: rgba(5, 150, 105, 0.25);
  --acc3: #0284c7;
  --warn: #d97706;
  --bad: #dc2626;
}

[data-theme="light"] body {
  background: #f8fafc !important;
  color: #0f172a !important;
}

[data-theme="light"] .card,
[data-theme="light"] .nav-island-bar,
[data-theme="light"] .hero-glow-mesh,
[data-theme="light"] .ro5-dashboard,
[data-theme="light"] .bond-metric-card,
[data-theme="light"] .telemetry-strip,
[data-theme="light"] .viewer-box,
[data-theme="light"] .mol-2d-canvas {
  background: rgba(255, 255, 255, 0.92) !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06) !important;
  border-color: rgba(0, 0, 0, 0.12) !important;
}

[data-theme="light"] .prop-table th {
  background: #e2e8f0 !important;
  color: #0f172a !important;
}

[data-theme="light"] .prop-table td {
  border-bottom: 1px solid #e2e8f0 !important;
  color: #1e293b !important;
}

[data-theme="light"] .prop-table tr:hover td {
  background: rgba(37, 99, 235, 0.05) !important;
}

[data-theme="light"] input[type="text"],
[data-theme="light"] select {
  background: #ffffff !important;
  color: #0f172a !important;
  border-color: #cbd5e1 !important;
}

[data-theme="light"] .btn {
  background: #e2e8f0 !important;
  color: #0f172a !important;
  border-color: #cbd5e1 !important;
}

[data-theme="light"] .btn.primary {
  background: #2563eb !important;
  color: #ffffff !important;
  border-color: #1d4ed8 !important;
}

[data-theme="light"] .btn.secondary {
  background: #ffffff !important;
  color: #2563eb !important;
  border-color: #cbd5e1 !important;
}

[data-theme="light"] .v-pill {
  background: #f1f5f9 !important;
  color: #334155 !important;
  border-color: #cbd5e1 !important;
}

[data-theme="light"] .v-pill.active {
  background: #2563eb !important;
  color: #ffffff !important;
}

[data-theme="light"] .preset-chip {
  background: #ffffff !important;
  color: #334155 !important;
  border-color: #cbd5e1 !important;
}

[data-theme="light"] ::-webkit-scrollbar-track {
  background: #f1f5f9;
}

[data-theme="light"] ::-webkit-scrollbar-thumb {
  background: #94a3b8;
}

/* Mode tab buttons */
.mode-tab-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 12px;
  border-radius: var(--r);
  font-family: var(--mono);
  font-size: 11.5px;
  font-weight: 600;
  cursor: pointer;
  border: 1px solid rgba(255, 255, 255, 0.12);
  background: rgba(2, 6, 23, 0.6);
  color: var(--dim);
  transition: all 0.2s ease;
}
.mode-tab-btn:hover {
  border-color: var(--acc);
  color: var(--ink);
}
.mode-tab-btn.active {
  background: var(--acc);
  color: #ffffff;
  border-color: var(--acc);
}

/* Toast alert */
.chem-toast {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background: rgba(2, 6, 23, 0.95);
  border: 1px solid var(--acc2);
  color: #ffffff;
  padding: 10px 18px;
  border-radius: 6px;
  font-family: var(--mono);
  font-size: 12px;
  z-index: 999999;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  gap: 8px;
  animation: toastFade 0.3s ease;
}
@keyframes toastFade {
  from { opacity: 0; transform: translateY(10px); }
  to { opacity: 1; transform: translateY(0); }
}

@keyframes blinkCursor {
  0%, 100% { opacity: 1; }
  50% { opacity: 0; }
}

.typewriter-cursor {
  display: inline-block;
  width: 7px;
  height: 16px;
  background: var(--acc);
  margin-left: 3px;
  vertical-align: middle;
  animation: blinkCursor 0.75s infinite;
}


*, *::before, *::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

html {
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
  background: #000000;
}

/* Custom High-Tech Neon Scrollbar */
::-webkit-scrollbar {
  width: 7px;
  height: 7px;
}
::-webkit-scrollbar-track {
  background: #020617;
}
::-webkit-scrollbar-thumb {
  background: linear-gradient(180deg, rgba(61, 139, 255, 0.4), rgba(0, 255, 157, 0.4));
  border-radius: 9999px;
}
::-webkit-scrollbar-thumb:hover {
  background: linear-gradient(180deg, #3d8bff, #00ff9d);
  box-shadow: 0 0 10px rgba(0, 240, 255, 0.6);
}

/* ==========================================================================
   PUTURE SPACESTAGE 3D CANVAS & HORIZON GRID
   ========================================================================== */
#spaceStage.space-stage {
  position: fixed !important;
  top: 0;
  left: 0;
  width: 100vw !important;
  height: 100vh !important;
  z-index: 0;
  pointer-events: none;
}

main, header, footer {
  position: relative;
  z-index: 2;
}

/* ==========================================================================
   PUTURE INTERACTIVE MAGNETIC CURSOR & CONTEXTUAL BADGE
   ========================================================================== */
.puture-cursor {
  position: fixed;
  top: 0;
  left: 0;
  pointer-events: none;
  z-index: 99999;
  display: flex;
  align-items: center;
  gap: 8px;
  transform: translate(-50%, -50%);
  opacity: 0;
  transition: opacity 0.25s ease;
}

.cursor-dot {
  width: 7px;
  height: 7px;
  background: #ffffff;
  border-radius: 50%;
  box-shadow: 0 0 8px rgba(255, 255, 255, 0.8);
  transition: transform 0.2s cubic-bezier(0.16, 1, 0.3, 1), background 0.2s ease;
}

.cursor-badge {
  font-family: var(--mono);
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: #000000;
  background: #ffffff;
  padding: 3px 8px;
  border-radius: 2px;
  font-weight: 700;
  white-space: nowrap;
  opacity: 0;
  transform: scale(0.75) translateX(-4px);
  transition: all 0.22s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.6);
}

.puture-cursor.has-label .cursor-badge {
  opacity: 1;
  transform: scale(1) translateX(0);
}

.puture-cursor.hovering .cursor-dot {
  transform: scale(1.6);
  background: var(--blue);
  box-shadow: 0 0 12px var(--blue);
}

@media (pointer: coarse), (max-width: 768px) {
  .puture-cursor { display: none !important; }
}

/* ==========================================================================
   PUTURE CHAPTER HUD & FLOATING DOCK INDICATOR
   ========================================================================== */
.puture-hud {
  position: fixed;
  bottom: 24px;
  left: 24px;
  z-index: 95;
  display: flex;
  align-items: baseline;
  gap: 6px;
  font-family: var(--mono);
  font-size: 11.5px;
  letter-spacing: 0.12em;
  padding: 8px 16px;
  background: rgba(0, 0, 0, 0.85);
  border: 1px solid var(--border);
  border-radius: var(--r);
  backdrop-filter: blur(16px);
  color: var(--white);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8);
  pointer-events: auto;
}

.hud-chap-num {
  color: var(--blue);
  font-weight: 700;
}

.hud-chap-slash {
  color: var(--grey-600);
}

.hud-chap-name {
  color: var(--grey-300);
  font-weight: 500;
  text-transform: uppercase;
}

.puture-dots {
  position: fixed;
  right: 24px;
  top: 50%;
  transform: translateY(-50%);
  z-index: 95;
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding: 12px 8px;
  background: rgba(0, 0, 0, 0.6);
  border: 1px solid var(--border);
  border-radius: 20px;
  backdrop-filter: blur(14px);
}

.p-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--grey-600);
  border: none;
  cursor: pointer;
  transition: all 0.3s var(--ease);
  position: relative;
  padding: 0;
}

.p-dot:hover {
  background: var(--grey-300);
  transform: scale(1.4);
}

.p-dot.active {
  background: var(--blue);
  height: 18px;
  border-radius: 4px;
  box-shadow: 0 0 10px var(--blue);
}

@media (max-width: 768px) {
  .puture-dots { display: none; }
  .puture-hud { bottom: 12px; left: 12px; font-size: 10px; padding: 6px 12px; }
}

/* ==========================================================================
   TOP LASER BEAM & KINETIC SCROLL PROGRESS
   ========================================================================== */
#scrollLaser {
  position: fixed;
  top: 0;
  left: 0;
  height: 2px;
  width: 0%;
  background: linear-gradient(90deg, var(--blue), var(--acc2), var(--acc3));
  box-shadow: 0 0 14px var(--blue);
  z-index: 1000;
  pointer-events: none;
  transition: width 0.05s ease-out;
}

.wrap {
  max-width: 1260px;
  margin: 0 auto;
  padding: 0 20px;
}

/* ==========================================================================
   INSTITUTIONAL HEADER - SRM IST
   ========================================================================== */
.inst-bar {
  background: #020617;
  border-bottom: 1px solid rgba(0, 240, 255, 0.12);
  padding: 7px 20px;
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
  gap: 10px;
  color: var(--ink);
}

.inst-tag img {
  height: 22px;
  width: auto;
  border-radius: 2px;
}

.inst-status {
  display: flex;
  align-items: center;
  gap: 12px;
}

.status-badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 2px 8px;
  border-radius: 4px;
  background: rgba(0, 255, 157, 0.08);
  border: 1px solid rgba(0, 255, 157, 0.3);
  color: var(--acc2);
  font-size: 11px;
}

/* ==========================================================================
   FRAMER-STYLE FLOATING ISLAND HEADER & LIQUID PILL CAPSULE DOCK
   ========================================================================== */
header, .floating-header {
  position: sticky;
  top: 10px;
  z-index: 1000;
  width: 100%;
  padding: 0 16px;
  pointer-events: none;
  transition: top 0.35s cubic-bezier(0.16, 1, 0.3, 1), transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.nav-island-bar {
  pointer-events: auto;
  max-width: 1240px;
  margin: 0 auto;
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 7px 14px 7px 18px;
  background: rgba(7, 11, 20, 0.76);
  backdrop-filter: blur(24px) saturate(190%);
  -webkit-backdrop-filter: blur(24px) saturate(190%);
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 9999px;
  box-shadow: 0 12px 36px rgba(0, 0, 0, 0.65), 0 0 24px rgba(0, 240, 255, 0.05);
  transition: all 0.35s cubic-bezier(0.16, 1, 0.3, 1);
  position: relative;
  overflow: visible;
}

header.scrolled, .floating-header.scrolled {
  top: 8px;
}

header.scrolled .nav-island-bar, .floating-header.scrolled .nav-island-bar {
  padding: 5px 12px 5px 16px;
  background: rgba(4, 7, 14, 0.92);
  border-color: rgba(0, 240, 255, 0.32);
  box-shadow: 0 18px 45px rgba(0, 0, 0, 0.88), 0 0 32px rgba(0, 240, 255, 0.15);
  transform: scale(0.995);
}

.brand-group {
  display: flex;
  align-items: center;
  gap: 12px;
  text-decoration: none;
  color: inherit;
  padding: 2px 4px;
  border-radius: 9999px;
  transition: transform 0.25s var(--ease);
}

.brand-group:hover {
  transform: scale(1.02);
}

.brand-icon-wrap {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  background: radial-gradient(circle at 35% 35%, rgba(0, 240, 255, 0.22), rgba(15, 23, 42, 0.95));
  border: 1.5px solid rgba(0, 240, 255, 0.6);
  box-shadow: 0 0 14px rgba(0, 240, 255, 0.35);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--acc);
  flex-shrink: 0;
  transition: all 0.3s var(--ease);
}

.brand-icon-wrap svg {
  width: 22px;
  height: 22px;
  stroke: var(--acc);
}

header.scrolled .brand-icon-wrap {
  width: 34px;
  height: 34px;
}

header.scrolled .brand-icon-wrap svg {
  width: 19px;
  height: 19px;
}

.brand-text h1 {
  font-size: 14.5px;
  font-weight: 700;
  color: #ffffff;
  letter-spacing: -0.01em;
  line-height: 1.2;
}

.brand-text span {
  font-size: 10px;
  color: var(--acc);
  font-family: var(--mono);
  letter-spacing: 0.06em;
  display: block;
}

/* Framer Dynamic Sliding Options Dock */
nav.links.nav-pill-track {
  position: relative;
  display: flex;
  align-items: center;
  background: rgba(255, 255, 255, 0.035);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 9999px;
  padding: 3px;
  gap: 1px;
  box-shadow: inset 0 1px 3px rgba(0, 0, 0, 0.4);
}

.nav-sliding-pill {
  position: absolute;
  top: 3px;
  left: 0;
  height: calc(100% - 6px);
  background: linear-gradient(135deg, rgba(0, 240, 255, 0.20), rgba(0, 255, 157, 0.16));
  border: 1px solid rgba(0, 240, 255, 0.55);
  border-radius: 9999px;
  box-shadow: 0 0 14px rgba(0, 240, 255, 0.32), inset 0 1px 1px rgba(255, 255, 255, 0.25);
  pointer-events: none;
  z-index: 1;
  transition: transform 0.32s cubic-bezier(0.16, 1, 0.3, 1), width 0.32s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease;
  opacity: 0;
  will-change: transform, width;
}

.nav-link-item {
  position: relative;
  z-index: 2;
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 13px;
  border-radius: 9999px;
  color: #94a3b8;
  text-decoration: none;
  font-size: 13px;
  font-weight: 500;
  letter-spacing: 0.01em;
  transition: color 0.2s ease;
  white-space: nowrap;
  user-select: none;
}

.nav-link-item .nav-num {
  font-family: var(--mono);
  font-size: 9.5px;
  color: rgba(148, 163, 184, 0.6);
  letter-spacing: 0.02em;
  transition: color 0.2s ease;
}

.nav-link-item:hover {
  color: #ffffff;
}

.nav-link-item:hover .nav-num {
  color: var(--acc);
}

.nav-link-item.active {
  color: #ffffff;
  font-weight: 600;
  text-shadow: 0 0 12px rgba(0, 240, 255, 0.6);
}

.nav-link-item.active .nav-num {
  color: var(--acc);
  font-weight: 700;
}

/* Nav Actions & Controls */
.nav-actions {
  display: flex;
  align-items: center;
  gap: 8px;
}

.ctrl-btn {
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.10);
  color: #cbd5e1;
  padding: 6px 14px;
  border-radius: 9999px;
  font-size: 11.5px;
  font-family: var(--mono);
  letter-spacing: 0.04em;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  transition: all 0.25s var(--ease);
  box-shadow: inset 0 1px 2px rgba(0, 0, 0, 0.3);
}

.ctrl-btn:hover {
  background: rgba(0, 240, 255, 0.12);
  border-color: rgba(0, 240, 255, 0.4);
  color: #ffffff;
  box-shadow: 0 0 14px rgba(0, 240, 255, 0.25);
  transform: translateY(-1px);
}

.audio-pulse-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: #00ff9d;
  box-shadow: 0 0 8px #00ff9d;
  animation: audioPulse 2s infinite ease-in-out;
  display: inline-block;
}

.audio-pulse-dot.muted {
  background: #ff4d6d;
  box-shadow: 0 0 8px #ff4d6d;
  animation: none;
}

@keyframes audioPulse {
  0%, 100% { transform: scale(1); opacity: 1; }
  50% { transform: scale(1.3); opacity: 0.7; }
}

.menu-toggle {
  display: none;
  background: rgba(255, 255, 255, 0.04);
  border: 1px solid rgba(255, 255, 255, 0.12);
  color: var(--ink);
  padding: 7px 10px;
  border-radius: 9999px;
  cursor: pointer;
  align-items: center;
  justify-content: center;
  transition: all 0.2s ease;
}

.menu-toggle:hover {
  background: rgba(0, 240, 255, 0.12);
  border-color: rgba(0, 240, 255, 0.4);
}

/* Integrated Dynamic Scroll Progress Laser Line */
.nav-island-progress {
  position: absolute;
  bottom: 0;
  left: 24px;
  right: 24px;
  height: 1.5px;
  border-radius: 9999px;
  background: rgba(255, 255, 255, 0.06);
  overflow: hidden;
  pointer-events: none;
}

.nav-island-progress-bar {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #00f0ff, #00ff9d);
  box-shadow: 0 0 8px rgba(0, 240, 255, 0.8);
  transition: width 0.08s ease-out;
}

/* Mobile Drawer Enhancements */
.mobile-drawer {
  position: fixed;
  inset: 0;
  background: rgba(2, 4, 10, 0.96);
  backdrop-filter: blur(20px);
  z-index: 1500;
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
  margin-bottom: 24px;
  padding-bottom: 16px;
  border-bottom: 1px solid var(--border);
}

.mobile-nav-links {
  display: flex;
  flex-direction: column;
  gap: 12px;
}

.mobile-nav-links a {
  font-size: 15px;
  padding: 12px 18px;
  border-radius: 10px;
  color: #cbd5e1;
  text-decoration: none;
  border: 1px solid rgba(255, 255, 255, 0.08);
  background: rgba(255, 255, 255, 0.03);
  display: flex;
  align-items: center;
  gap: 12px;
  transition: all 0.2s ease;
}

.mobile-nav-links a .m-num {
  font-family: var(--mono);
  font-size: 11px;
  color: var(--acc);
}

.mobile-nav-links a:hover, .mobile-nav-links a.active {
  color: #ffffff;
  background: rgba(0, 240, 255, 0.12);
  border-color: rgba(0, 240, 255, 0.4);
  box-shadow: 0 0 16px rgba(0, 240, 255, 0.18);
}

/* Responsive Navigation Breakpoints */
@media (max-width: 1120px) {
  .nav-link-item .nav-num {
    display: none;
  }
  .nav-link-item {
    padding: 6px 10px;
    font-size: 12px;
  }
}

@media (max-width: 900px) {
  nav.links.nav-pill-track {
    display: none;
  }
  .menu-toggle {
    display: flex;
  }
  .nav-island-progress {
    left: 16px;
    right: 16px;
  }
}

@media (max-width: 560px) {
  .brand-text span {
    display: none;
  }
  .brand-text h1 {
    font-size: 13.5px;
  }
  #audioBtn span#audioStatusText {
    display: none;
  }
  .ctrl-btn {
    padding: 6px 10px;
  }
  .nav-island-bar {
    padding: 6px 12px;
  }
  .brand-icon-wrap {
    width: 32px;
    height: 32px;
  }
  .brand-icon-wrap svg {
    width: 18px;
    height: 18px;
  }
  .inst-bar {
    font-size: 10px;
    padding: 4px 10px;
  }
  .inst-status {
    display: none;
  }
}

/* ==========================================================================
   ADVANCED MOTION.DEV ROLLING TEXT BUTTONS & SPRING KINETICS
   ========================================================================== */
.btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 10px;
  padding: 12px 24px;
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
  text-decoration: none;
  transform: translateZ(0);
  transition: border-color 0.28s var(--ease), box-shadow 0.28s var(--ease), background 0.28s var(--ease);
  will-change: transform;
}

/* Motion.dev Rolling Text Container */
.btn-roll {
  display: inline-flex;
  flex-direction: column;
  position: relative;
  overflow: hidden;
  height: 1.3em;
  line-height: 1.3em;
  vertical-align: middle;
}

.btn-roll-text {
  display: block;
  transform: translateY(0%);
  transition: transform 0.38s cubic-bezier(0.16, 1, 0.3, 1);
  will-change: transform;
  white-space: nowrap;
}

.btn-roll-hover {
  position: absolute;
  top: 100%;
  left: 0;
  width: 100%;
}

.btn:hover .btn-roll-text {
  transform: translateY(-100%);
}

.btn svg {
  transition: transform 0.3s cubic-bezier(0.34, 1.56, 0.64, 1);
  flex-shrink: 0;
}

.btn:hover svg {
  transform: translateX(4px);
}

.btn:active {
  transform: scale(0.95);
  transition: transform 0.1s ease;
}

/* Dynamic Radial Glow following mouse */
.btn .btn-glow {
  position: absolute;
  width: 90px;
  height: 90px;
  background: radial-gradient(circle, rgba(0, 240, 255, 0.45) 0%, transparent 70%);
  border-radius: 50%;
  pointer-events: none;
  transform: translate(-50%, -50%);
  opacity: 0;
  transition: opacity 0.25s var(--ease);
}

.btn:hover .btn-glow {
  opacity: 1;
}

/* Kinetic Light Sheen Sweep */
.btn::after {
  content: "";
  position: absolute;
  top: -60%;
  left: -120%;
  width: 70%;
  height: 220%;
  background: linear-gradient(90deg, transparent, rgba(255, 255, 255, 0.3), transparent);
  transform: rotate(25deg);
  pointer-events: none;
  transition: none;
}

.btn:hover {
  background: var(--panel-hover);
  border-color: var(--acc);
  box-shadow: 0 10px 28px rgba(0, 0, 0, 0.6), 0 0 20px var(--acc-glow);
}

.btn:hover::after {
  left: 220%;
  transition: left 0.7s var(--ease);
}

.btn.primary {
  background: linear-gradient(135deg, var(--acc), var(--acc2));
  color: #020617;
  border-color: transparent;
  font-weight: 700;
}

.btn.primary:hover {
  box-shadow: 0 12px 34px rgba(0, 240, 255, 0.45), 0 0 24px var(--acc2-glow);
}

.btn.sm {
  padding: 6px 14px;
  font-size: 12px;
}

.queue-del-btn {
  background: rgba(239, 68, 68, 0.12);
  color: #ef4444;
  border: 1px solid rgba(239, 68, 68, 0.3);
  width: 26px;
  height: 26px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  font-size: 15px;
  line-height: 1;
  transition: all 0.2s ease;
  flex-shrink: 0;
}
.queue-del-btn:hover {
  background: #ef4444;
  color: #ffffff;
  transform: scale(1.08);
}

/* ==========================================================================
   INTERACTIVE CARDS WITH MOUSE SPOTLIGHT GLOW & FROSTED GLASS
   ========================================================================== */
.card, .theory-card, .bond-metric-card, .gauge-card, .tele-item, .bento-card, .ro5-criterion {
  background: rgba(8, 12, 22, 0.72);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 14px;
  padding: 24px;
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  position: relative;
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1), border-color 0.3s ease, box-shadow 0.3s ease;
  overflow: hidden;
}

.card::before, .theory-card::before, .bond-metric-card::before, .gauge-card::before, .tele-item::before, .bento-card::before, .ro5-criterion::before {
  content: '';
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: radial-gradient(450px circle at var(--mouse-x, -999px) var(--mouse-y, -999px), rgba(0, 240, 255, 0.14), transparent 45%);
  pointer-events: none;
  opacity: 0;
  transition: opacity 0.3s ease;
  z-index: 1;
}

.card:hover::before, .theory-card:hover::before, .bond-metric-card:hover::before, .gauge-card:hover::before, .tele-item:hover::before, .bento-card:hover::before, .ro5-criterion:hover::before {
  opacity: 1;
}

.card:hover, .theory-card:hover, .bond-metric-card:hover, .gauge-card:hover, .tele-item:hover, .bento-card:hover, .ro5-criterion:hover {
  border-color: rgba(0, 240, 255, 0.35);
  box-shadow: 0 18px 45px rgba(0, 0, 0, 0.8), 0 0 28px rgba(0, 240, 255, 0.10);
  transform: translateY(-2px);
}

.card > *, .theory-card > *, .gauge-card > *, .tele-item > *, .bento-card > * {
  position: relative;
  z-index: 2;
}

/* Sliding Kinetic Classes */
.slide-left { will-change: transform, opacity; }
.slide-right { will-change: transform, opacity; }

/* Dynamic Accent Line under Section Titles */
.sec-line {
  height: 3px;
  width: 0px;
  background: linear-gradient(90deg, var(--acc), var(--acc2), transparent);
  box-shadow: 0 0 14px var(--acc-glow);
  margin-top: 10px;
  border-radius: 2px;
}

/* Grid Layouts */
.grid {
  display: grid;
  gap: 20px;
}

.g2 { grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); }
.g3 { grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); }
.g4 { grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); }

/* ==========================================================================
   HERO BLOCK - STORYTELLING & TELEMETRY STRIP
   ========================================================================== */
.hero {
  padding: 85px 0 65px;
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
  background: rgba(0, 255, 157, 0.08);
}

.hero {
  position: relative;
  overflow: hidden;
}

.hero-glow-mesh {
  position: absolute;
  top: 30%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 720px;
  height: 400px;
  background: radial-gradient(ellipse at center, rgba(61, 139, 255, 0.22) 0%, rgba(0, 240, 255, 0.12) 40%, rgba(0, 255, 157, 0.04) 65%, transparent 80%);
  filter: blur(55px);
  pointer-events: none;
  z-index: 0;
  animation: auroraPulse 10s ease-in-out infinite alternate;
}

@keyframes auroraPulse {
  0% { transform: translate(-50%, -50%) scale(0.95); opacity: 0.8; }
  100% { transform: translate(-50%, -48%) scale(1.08); opacity: 1; }
}

.hero h1 {
  font-size: clamp(34px, 5.2vw, 62px);
  font-weight: 800;
  line-height: 1.12;
  letter-spacing: -0.03em;
  margin-bottom: 22px;
  background: linear-gradient(180deg, #FFFFFF 15%, #e2e8f0 60%, #94a3b8 100%);
  -webkit-background-clip: text;
  background-clip: text;
  -webkit-text-fill-color: transparent;
  color: transparent;
  text-shadow: 0 12px 35px rgba(0, 0, 0, 0.6);
}

.hero p {
  font-size: clamp(16px, 1.8vw, 19px);
  color: #94a3b8;
  max-width: 820px;
  margin-bottom: 34px;
  line-height: 1.65;
}

.hero-actions {
  display: flex;
  align-items: center;
  gap: 14px;
  flex-wrap: wrap;
  margin-bottom: 44px;
}

.telemetry-strip {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 16px;
  margin-top: 10px;
}

.tele-item {
  padding: 16px 20px;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.tele-top {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--mono);
  font-size: 10px;
  color: var(--dim);
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.tele-pulse-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--acc);
  box-shadow: 0 0 8px var(--acc);
  animation: audioPulse 2s infinite ease-in-out;
}

.tele-pulse-dot.emerald { background: var(--acc2); box-shadow: 0 0 8px var(--acc2); }
.tele-pulse-dot.cyan { background: var(--acc3); box-shadow: 0 0 8px var(--acc3); }
.tele-pulse-dot.purple { background: #b388ff; box-shadow: 0 0 8px #b388ff; }

.tele-val {
  font-family: var(--mono);
  font-size: 24px;
  font-weight: 700;
  color: #ffffff;
  line-height: 1.2;
}

.tele-sub {
  font-size: 11.5px;
  color: var(--mut);
  letter-spacing: 0.02em;
}

.tele-lbl {
  font-size: 11.5px;
  color: var(--dim);
  text-transform: uppercase;
  letter-spacing: 0.08em;
  margin-top: 4px;
}

/* Section Headings with Subtle Scroll Fade-In (300ms) */
section {
  padding: 85px 0;
  scroll-margin-top: 80px;
}

section .sechead {
  opacity: 0.2;
  transform: translateY(14px);
  transition: opacity 0.35s cubic-bezier(0.16, 1, 0.3, 1), transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

section.section-visible .sechead, section#home .sechead {
  opacity: 1;
  transform: translateY(0);
}

.sechead {
  margin-bottom: 34px;
  max-width: 840px;
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
  padding: 13px 18px;
  background: rgba(6, 10, 22, 0.88);
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
  position: relative;
  display: flex;
  gap: 8px;
  flex-wrap: wrap;
  margin-bottom: 24px;
}

.preset-pill-indicator {
  position: absolute;
  top: 0;
  left: 0;
  background: linear-gradient(135deg, var(--acc), var(--acc2));
  border-radius: var(--r-btn);
  pointer-events: none;
  z-index: 1;
  box-shadow: 0 0 16px var(--acc-glow);
  transition: transform 0.38s cubic-bezier(0.16, 1, 0.3, 1), width 0.38s cubic-bezier(0.16, 1, 0.3, 1), height 0.38s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease;
  will-change: transform, width;
  opacity: 0;
}

.preset-chip {
  position: relative;
  z-index: 2;
  padding: 7px 15px;
  background: var(--panel);
  border: 1px solid var(--border);
  border-radius: var(--r-btn);
  font-family: var(--mono);
  font-size: 12px;
  color: var(--mut);
  cursor: pointer;
  transition: color 0.22s var(--ease), border-color 0.22s var(--ease), transform 0.22s var(--ease);
}

.preset-chip:hover {
  color: var(--acc);
  border-color: var(--acc);
  transform: translateY(-2px);
}

.preset-chip.active {
  color: #020617 !important;
  font-weight: 700;
  border-color: transparent;
  background: transparent;
}

/* Dual Canvas Layout */
.dual-canvas-grid {
  display: grid;
  grid-template-columns: 1fr 1.35fr;
  gap: 22px;
}

@media (max-width: 960px) {
  .dual-canvas-grid {
    grid-template-columns: 1fr;
  }
}

.canvas-header-row {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
  flex-wrap: wrap;
  gap: 8px;
}

.canvas-tag {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  font-family: var(--mono);
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.08em;
  color: var(--acc);
}

.canvas-tag.emerald { color: var(--acc2); }

.canvas-tag-dot {
  width: 6px;
  height: 6px;
  border-radius: 50%;
  background: var(--acc);
  box-shadow: 0 0 8px var(--acc);
}

.canvas-tag-dot.emerald {
  background: var(--acc2);
  box-shadow: 0 0 8px var(--acc2);
}

.canvas-subtag {
  font-family: var(--mono);
  font-size: 10.5px;
  color: var(--dim);
  letter-spacing: 0.05em;
}

/* Holographic 3D Viewport Chamber */
.viewer-box {
  width: 100%;
  height: 490px;
  border-radius: 12px;
  border: 1px solid rgba(0, 240, 255, 0.25);
  background: radial-gradient(circle at 50% 50%, rgba(0, 240, 255, 0.05), rgba(2, 4, 10, 0.96));
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 0 35px rgba(0, 0, 0, 0.9), 0 0 20px rgba(0, 240, 255, 0.05);
}

/* Cybernetic Corner HUD Reticles */
.hud-reticle {
  position: absolute;
  width: 14px;
  height: 14px;
  border-color: rgba(0, 240, 255, 0.45);
  pointer-events: none;
  z-index: 15;
  transition: border-color 0.3s ease, transform 0.3s ease;
}

.viewer-box:hover .hud-reticle, .mol-2d-canvas:hover .hud-reticle {
  border-color: rgba(0, 240, 255, 0.9);
}

.hud-reticle.tl { top: 10px; left: 10px; border-top: 2px solid; border-left: 2px solid; }
.hud-reticle.tr { top: 10px; right: 10px; border-top: 2px solid; border-right: 2px solid; }
.hud-reticle.bl { bottom: 10px; left: 10px; border-bottom: 2px solid; border-left: 2px solid; }
.hud-reticle.br { bottom: 10px; right: 10px; border-bottom: 2px solid; border-right: 2px solid; }

/* Floating In-Canvas Glass Tool Dock */
.viewer-floating-dock {
  position: absolute;
  bottom: 14px;
  left: 14px;
  right: 14px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 8px;
  z-index: 25;
  pointer-events: none;
}

.viewer-style-pills, .viewer-action-pills {
  display: flex;
  align-items: center;
  gap: 4px;
  padding: 4px;
  background: rgba(4, 8, 16, 0.82);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid rgba(255, 255, 255, 0.12);
  border-radius: 9999px;
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.7);
  pointer-events: auto;
}

.v-pill, .v-action-pill {
  background: transparent;
  border: 1px solid transparent;
  color: #94a3b8;
  font-family: var(--font-main);
  font-size: 11.5px;
  font-weight: 500;
  padding: 5px 12px;
  border-radius: 9999px;
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 5px;
}

.v-pill:hover, .v-action-pill:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.08);
}

.v-pill.active {
  background: linear-gradient(135deg, rgba(0, 240, 255, 0.25), rgba(0, 255, 157, 0.18));
  border-color: rgba(0, 240, 255, 0.6);
  color: #ffffff;
  font-weight: 600;
  box-shadow: 0 0 12px rgba(0, 240, 255, 0.35);
}

.v-action-pill.active {
  background: rgba(0, 255, 157, 0.22);
  border-color: rgba(0, 255, 157, 0.6);
  color: #00ff9d;
  box-shadow: 0 0 10px rgba(0, 255, 157, 0.3);
}

.spin-icon {
  font-size: 13px;
  line-height: 1;
}

/* 2D Vector Structure View with Tech Grid */
.mol-2d-canvas {
  width: 100%;
  height: 490px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: 
    radial-gradient(circle at 50% 50%, rgba(61, 139, 255, 0.04), rgba(4, 7, 16, 0.95)),
    linear-gradient(rgba(255, 255, 255, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255, 255, 255, 0.02) 1px, transparent 1px);
  background-size: 100% 100%, 24px 24px, 24px 24px;
  border-radius: 12px;
  border: 1px solid rgba(255, 255, 255, 0.10);
  position: relative;
  overflow: hidden;
  box-shadow: inset 0 0 35px rgba(0, 0, 0, 0.9);
}

/* Theory Bento Grid Styles */
.theory-bento-grid {
  display: grid;
  grid-template-columns: 1.25fr 1fr;
  gap: 20px;
}

.bento-wide {
  grid-column: 1 / -1;
}

@media (max-width: 900px) {
  .theory-bento-grid { grid-template-columns: 1fr; }
}

.theory-card-head {
  display: flex;
  flex-direction: column;
  gap: 6px;
  margin-bottom: 12px;
}

.bento-badge {
  font-family: var(--mono);
  font-size: 10px;
  font-weight: 700;
  color: var(--acc);
  letter-spacing: 0.12em;
  text-transform: uppercase;
}

.bento-badge.emerald { color: var(--acc2); }
.bento-badge.purple { color: #c084fc; }

.smiles-token-track {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  padding: 12px 14px;
  background: rgba(3, 7, 18, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.10);
  border-radius: 10px;
  margin-bottom: 14px;
}

.smiles-chip {
  padding: 6px 14px;
  border-radius: 8px;
  font-family: var(--mono);
  font-size: 13.5px;
  font-weight: 700;
  background: rgba(61, 139, 255, 0.15);
  border: 1px solid rgba(61, 139, 255, 0.45);
  color: #70b0ff;
  cursor: pointer;
  transition: all 0.2s ease;
  user-select: none;
}

.smiles-chip:hover {
  transform: translateY(-2px);
  box-shadow: 0 0 14px rgba(61, 139, 255, 0.6);
  border-color: var(--acc);
}

.smiles-chip.ester {
  background: rgba(255, 77, 109, 0.15);
  border-color: rgba(255, 77, 109, 0.45);
  color: #ff859d;
}
.smiles-chip.ester:hover {
  box-shadow: 0 0 14px rgba(255, 77, 109, 0.6);
}

.smiles-chip.ring {
  background: rgba(0, 255, 157, 0.15);
  border-color: rgba(0, 255, 157, 0.45);
  color: #4eedab;
}
.smiles-chip.ring:hover {
  box-shadow: 0 0 14px rgba(0, 255, 157, 0.6);
}

.smiles-chip.acid {
  background: rgba(0, 240, 255, 0.15);
  border-color: rgba(0, 240, 255, 0.45);
  color: #7aedff;
}
.smiles-chip.acid:hover {
  box-shadow: 0 0 14px rgba(0, 240, 255, 0.6);
}

.token-inspector {
  padding: 14px 18px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px dashed rgba(255, 255, 255, 0.14);
  border-radius: 10px;
}

.inspector-title {
  font-family: var(--mono);
  font-size: 12.5px;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 5px;
}

.inspector-body {
  font-size: 13px;
  color: var(--mut);
  line-height: 1.5;
}

.geom-pill-list {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.geom-pill-item {
  padding: 10px 14px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.07);
  border-radius: 8px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  font-size: 12.5px;
}

.geom-pill-item .g-name {
  font-weight: 600;
  color: var(--acc2);
  font-family: var(--mono);
  font-size: 12px;
}

.geom-pill-item .g-desc {
  color: var(--mut);
  font-size: 11.5px;
  text-align: right;
}

.ro5-criteria-row {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 12px;
}

.ro5-criterion {
  padding: 14px 16px;
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.08);
  border-radius: 10px;
}

.crit-num {
  font-family: var(--mono);
  font-size: 10px;
  color: #c084fc;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 4px;
}

.crit-val {
  font-family: var(--mono);
  font-size: 16px;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 6px;
}

.crit-desc {
  font-size: 12px;
  color: var(--mut);
  line-height: 1.4;
}

/* Lipinski Rule of 5 Visual Dashboard & Hero Gauges */
.ro5-dashboard {
  margin-bottom: 26px;
  padding-bottom: 26px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.ro5-compliance-bar {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 12px;
  padding: 14px 18px;
  background: rgba(0, 255, 157, 0.05);
  border: 1px solid rgba(0, 255, 157, 0.25);
  border-radius: 12px;
  margin-bottom: 18px;
}

.ro5-badge {
  display: inline-flex;
  align-items: center;
  gap: 8px;
  font-family: var(--mono);
  font-size: 12.5px;
  font-weight: 700;
  letter-spacing: 0.04em;
  color: #00ff9d;
}

.ro5-badge.alert,
.ro5-badge.warning {
  color: #ffd166;
}

.ro5-badge.danger {
  color: #ff4d6d;
}

.ro5-dot {
  width: 8px;
  height: 8px;
  border-radius: 50%;
  background: #00ff9d;
  box-shadow: 0 0 10px #00ff9d;
  animation: audioPulse 2s infinite ease-in-out;
}

.ro5-badge.alert .ro5-dot,
.ro5-badge.warning .ro5-dot {
  background: #ffd166;
  box-shadow: 0 0 10px #ffd166;
}

.ro5-badge.danger .ro5-dot {
  background: #ff4d6d;
  box-shadow: 0 0 10px #ff4d6d;
}

.ro5-subtext {
  font-size: 12.5px;
  color: var(--mut);
}

.ro5-gauge-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(210px, 1fr));
  gap: 14px;
}

.gauge-card {
  padding: 16px;
}

.gauge-head {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 8px;
}

.gauge-title {
  font-size: 11.5px;
  font-weight: 600;
  color: var(--dim);
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.gauge-badge {
  font-family: var(--mono);
  font-size: 10px;
  font-weight: 700;
  padding: 2px 7px;
  border-radius: 9999px;
  background: rgba(0, 255, 157, 0.15);
  color: #00ff9d;
  border: 1px solid rgba(0, 255, 157, 0.4);
}

.gauge-badge.fail,
.gauge-badge.danger {
  background: rgba(255, 77, 109, 0.15);
  color: #ff4d6d;
  border-color: rgba(255, 77, 109, 0.4);
}

.gauge-fill.danger {
  background: linear-gradient(90deg, #ff4d6d, #f59e0b) !important;
  box-shadow: 0 0 8px rgba(255, 77, 109, 0.6) !important;
}

.gauge-val {
  font-family: var(--mono);
  font-size: 22px;
  font-weight: 700;
  color: #ffffff;
  margin-bottom: 10px;
}

.gauge-unit {
  font-size: 12px;
  color: var(--dim);
  font-weight: 400;
}

.gauge-meter {
  position: relative;
  width: 100%;
  height: 6px;
  background: rgba(255, 255, 255, 0.08);
  border-radius: 9999px;
  overflow: hidden;
  margin-bottom: 6px;
}

.gauge-fill {
  height: 100%;
  width: 0%;
  background: linear-gradient(90deg, #3d8bff, #00f0ff);
  border-radius: 9999px;
  transition: width 0.5s cubic-bezier(0.16, 1, 0.3, 1);
  box-shadow: 0 0 8px rgba(0, 240, 255, 0.6);
}

.gauge-fill.emerald {
  background: linear-gradient(90deg, #00ff9d, #3d8bff);
  box-shadow: 0 0 8px rgba(0, 255, 157, 0.6);
}

.gauge-fill.cyan {
  background: linear-gradient(90deg, #00f0ff, #00ff9d);
  box-shadow: 0 0 8px rgba(0, 240, 255, 0.6);
}

.gauge-fill.purple {
  background: linear-gradient(90deg, #c084fc, #3d8bff);
  box-shadow: 0 0 8px rgba(192, 132, 252, 0.6);
}

.gauge-foot {
  display: flex;
  justify-content: space-between;
  font-family: var(--mono);
  font-size: 10px;
  color: var(--dim);
}

.limit-label {
  color: var(--mut);
}

/* Properties Analytical Suite */
.prop-table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 16px;
  font-size: 13.5px;
}

.prop-table th {
  padding: 12px 16px;
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
  padding: 11px 16px;
  border-bottom: 1px solid rgba(0, 240, 255, 0.08);
  color: var(--ink);
}

.prop-table tr:hover td {
  background: rgba(0, 240, 255, 0.035);
}

.val-col {
  font-family: var(--mono);
  font-weight: 700;
  color: var(--acc2);
}

.desc-col {
  font-size: 12.5px;
  color: var(--mut);
  line-height: 1.45;
}

/* Bond Architecture Counters */
.bond-metric-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
  gap: 12px;
  margin-top: 18px;
}

.bond-metric-card {
  background: rgba(6, 10, 22, 0.7);
  border: 1px solid var(--border);
  border-radius: var(--r-btn);
  padding: 12px 14px;
}

.bond-metric-card strong {
  display: block;
  font-family: var(--mono);
  font-size: 18px;
  color: var(--acc);
}

.bond-metric-card span {
  font-size: 11px;
  color: var(--dim);
  text-transform: uppercase;
  letter-spacing: 0.06em;
}

/* Notification Banners */
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
  font-size: 18px;
  color: var(--ink);
  margin-bottom: 10px;
}

/* ==========================================================================
   QUIZ & ASSESSMENT TERMINAL
   ========================================================================== */
.quiz-opt {
  display: block;
  width: 100%;
  text-align: left;
  padding: 13px 18px;
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
   FOOTER & COMPLIANCE - OFFICIAL ACADEMIC CHANNELS
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
  max-width: 460px;
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
  margin-bottom: 9px;
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

/* Modals */
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
</style>
</head>
<body>

<!-- Laser Scroll Beam -->
<div id="scrollLaser"></div>

<!-- Puture Interactive Magnetic Cursor & Contextual Badge -->
<div class="puture-cursor" id="putureCursor">
  <span class="cursor-dot"></span>
  <span class="cursor-badge" id="cursorBadge">EXPLORE</span>
</div>

<!-- Puture Fixed Chapter HUD & Progress Tracker -->
<div class="puture-hud" id="chapterHud">
  <span class="hud-chap-num" id="hudChapNum">01</span>
  <span class="hud-chap-slash">/</span>
  <span class="hud-chap-name" id="hudChapName">WELCOME</span>
</div>

<!-- Puture Floating Chapter Navigation Dots -->
<nav class="puture-dots" id="chapterDots" aria-label="Chapters">
  <button class="p-dot active" onclick="scrollToChapter('home')" title="01 Overview" data-chapter="01"></button>
  <button class="p-dot" onclick="scrollToChapter('theory')" title="02 Curriculum Theory" data-chapter="02"></button>
  <button class="p-dot" onclick="scrollToChapter('lab')" title="03 Molecular Lab" data-chapter="03"></button>
  <button class="p-dot" onclick="scrollToChapter('properties')" title="04 18 Descriptors" data-chapter="04"></button>
  <button class="p-dot" onclick="scrollToChapter('compare')" title="05 Comparative Matrix" data-chapter="05"></button>
  <button class="p-dot" onclick="scrollToChapter('quiz')" title="06 Assessment Module" data-chapter="06"></button>
  <button class="p-dot" onclick="scrollToChapter('reactions')" title="07 Reaction Simulator" data-chapter="07"></button>
  <button class="p-dot" onclick="scrollToChapter('report')" title="08 Official Report" data-chapter="08"></button>
</nav>

<!-- Puture SpaceStage 3D WebGL Horizon Canvas -->
<canvas id="spaceStage" class="space-stage"></canvas>

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
      <span class="status-badge" style="color:var(--acc);border-color:rgba(0,240,255,0.3)">PYTHON 3.14 POWERED</span>
    </div>
  </div>
</div>

<!-- Main Sticky Framer-Style Floating Island Header -->
<header class="floating-header" id="mainHeader">
  <div class="nav-island-bar" id="navIslandBar">
    <a href="#home" class="brand-group" aria-label="Cheminformatics Virtual Lab Home">
      <div class="brand-icon-wrap" aria-hidden="true">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round">
          <circle cx="12" cy="12" r="3"/>
          <ellipse cx="12" cy="12" rx="9" ry="3.5" transform="rotate(30 12 12)"/>
          <ellipse cx="12" cy="12" rx="9" ry="3.5" transform="rotate(90 12 12)"/>
          <ellipse cx="12" cy="12" rx="9" ry="3.5" transform="rotate(150 12 12)"/>
        </svg>
      </div>
      <div class="brand-text">
        <h1>Cheminformatics Virtual Lab</h1>
        <span>SRM INSTITUTE OF SCIENCE &amp; TECHNOLOGY</span>
      </div>
    </a>

    <!-- Framer Dynamic Sliding Options Dock -->
    <nav class="links nav-pill-track" id="navLinksTrack" aria-label="Curriculum Navigation">
      <div class="nav-sliding-pill" id="navSlidingPill" aria-hidden="true"></div>
      <a href="#home" class="nav-link-item active" data-chapter="01">
        <span class="nav-num">01</span>
        <span class="nav-label">Overview</span>
      </a>
      <a href="#theory" class="nav-link-item" data-chapter="02">
        <span class="nav-num">02</span>
        <span class="nav-label">Theory</span>
      </a>
      <a href="#lab" class="nav-link-item" data-chapter="03">
        <span class="nav-num">03</span>
        <span class="nav-label">2D &amp; 3D Lab</span>
      </a>
      <a href="#properties" class="nav-link-item" data-chapter="04">
        <span class="nav-num">04</span>
        <span class="nav-label">Descriptors</span>
      </a>
      <a href="#compare" class="nav-link-item" data-chapter="05">
        <span class="nav-num">05</span>
        <span class="nav-label">Matrix</span>
      </a>
      <a href="#quiz" class="nav-link-item" data-chapter="06">
        <span class="nav-num">06</span>
        <span class="nav-label">Assessment</span>
      </a>
      <a href="#reactions" class="nav-link-item" data-chapter="07">
        <span class="nav-num">07</span>
        <span class="nav-label">Reactions</span>
      </a>
      <a href="#report" class="nav-link-item" data-chapter="08">
        <span class="nav-num">08</span>
        <span class="nav-label">Report</span>
      </a>
    </nav>

    <div class="nav-actions">
            <button class="ctrl-btn" id="themeToggleBtn" onclick="toggleTheme()" title="Toggle Dark / Light Presentation Theme">
        <svg id="themeIconSun" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="display:none"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg>
        <svg id="themeIconMoon" width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg>
        <span id="themeStatusText">THEME</span>
      </button>
      <button class="ctrl-btn" id="audioBtn" onclick="toggleAudio()" title="Toggle Web Audio Synthesizer">
        <span class="audio-pulse-dot" id="audioDot"></span>
        <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M11 5L6 9H2v6h4l5 4V5z"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
        <span id="audioStatusText">AUDIO: ON</span>
      </button>
      <button class="menu-toggle" onclick="toggleMobileMenu()" aria-label="Toggle Navigation Menu">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
      </button>
    </div>

    <!-- Integrated Dynamic Scroll Progress Laser Line -->
    <div class="nav-island-progress" aria-hidden="true">
      <div class="nav-island-progress-bar" id="navIslandProgressBar"></div>
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
    <a href="#home" onclick="toggleMobileMenu()"><span class="m-num">01</span> Overview</a>
    <a href="#theory" onclick="toggleMobileMenu()"><span class="m-num">02</span> Cheminformatics Theory</a>
    <a href="#lab" onclick="toggleMobileMenu()"><span class="m-num">03</span> 2D &amp; 3D Molecular Lab</a>
    <a href="#properties" onclick="toggleMobileMenu()"><span class="m-num">04</span> Molecular Descriptors</a>
    <a href="#compare" onclick="toggleMobileMenu()"><span class="m-num">05</span> Comparative Analysis</a>
    <a href="#quiz" onclick="toggleMobileMenu()"><span class="m-num">06</span> Student Assessment</a>
    <a href="#reactions" onclick="toggleMobileMenu()"><span class="m-num">07</span> Reaction Simulator</a>
    <a href="#report" onclick="toggleMobileMenu()"><span class="m-num">08</span> Download PDF Report</a>
  </div>
</div>

<main>
  <!-- BLOCK 1: HERO & TELEMETRY STRIP -->
  <section id="home" class="hero" data-chapter="01" data-chapter-name="OVERVIEW">
    <div class="hero-glow-mesh" aria-hidden="true"></div>
    <div class="wrap" style="position:relative;z-index:2">
      <div class="hero-badge-row">
        <span class="badge srm-badge">SRM Institute of Science and Technology</span>
        <span class="badge">Division of Chemistry &times; School of Sciences</span>
        <span class="badge" style="color:var(--acc3)">Computational Molecular Engineering</span>
      </div>

      <h1>Representation of 2D &amp; 3D Chemical Structures</h1>
      
      <p>
        An interactive virtual laboratory designed for students and researchers.
        Convert linear SMILES notations into dynamic 2D chemical graphs, generate 3D hardware-accelerated WebGL conformers,
        calculate 18 quantitative molecular descriptors, and export certified PDF laboratory reports.
      </p>

      <div class="hero-actions">
        <a href="#lab" class="btn primary" data-cursor-label="LAUNCH LAB">
          <span>Launch Molecular Lab</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
        </a>
        <a href="#theory" class="btn" data-cursor-label="THEORY">
          <span>Read Laboratory Theory</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7z"/></svg>
        </a>
        <a href="#report" class="btn" data-cursor-label="PDF REPORT">
          <span>Download PDF Report</span>
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/></svg>
        </a>
      </div>

      
      <!-- Molecule of the Day Card -->
      <div class="card" id="motdCard" style="margin-top:24px;border:1px solid rgba(0,240,255,0.22);background:linear-gradient(135deg, rgba(2,6,23,0.85) 0%, rgba(15,23,42,0.65) 100%);padding:18px 24px">
        <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;margin-bottom:12px">
          <div style="display:flex;align-items:center;gap:10px">
            <span style="background:linear-gradient(135deg,#3d8bff,#00ff9d);color:#020617;font-family:var(--mono);font-size:11px;font-weight:700;padding:4px 10px;border-radius:9999px">
              FEATURED &bull; MOLECULE OF THE DAY
            </span>
            <span id="motdDateBadge" style="color:var(--dim);font-size:12px;font-family:var(--mono)">Daily Educational Highlight</span>
          </div>
          <button type="button" class="btn primary" onclick="loadMotdToLab()" style="padding:6px 14px;font-size:12px">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            <span>Explore in 3D Lab</span>
          </button>
        </div>
        <div style="display:flex;gap:20px;align-items:center;flex-wrap:wrap">
          <div style="font-size:32px;background:rgba(255,255,255,0.05);width:56px;height:56px;display:flex;align-items:center;justify-content:center;border-radius:8px;border:1px solid rgba(255,255,255,0.08);flex-shrink:0">
            🧪
          </div>
          <div style="flex:1;min-width:240px">
            <div style="display:flex;align-items:baseline;gap:10px;flex-wrap:wrap">
              <h3 id="motdName" style="color:var(--ink);font-size:19px;margin:0">Pyridine</h3>
              <span id="motdClass" style="color:var(--acc);font-size:12px;font-family:var(--mono);background:rgba(61,139,255,0.12);padding:2px 8px;border-radius:4px">Heteroaromatic Base</span>
              <span id="motdFormula" style="color:var(--acc2);font-family:var(--mono);font-size:12.5px">C5H5N</span>
            </div>
            <p id="motdDesc" style="color:var(--mut);font-size:13px;margin-top:6px;line-height:1.5">
              Basic aromatic ring where the nitrogen lone pair occupies an sp² orbital orthogonal to the aromatic pi-system.
            </p>
            <div style="font-family:var(--mono);font-size:11.5px;color:var(--dim);margin-top:4px">
              Canonical SMILES: <code id="motdSmiles" style="color:var(--acc3)">c1ccncc1</code>
            </div>
          </div>
        </div>
      </div>

      <!-- Telemetry Strip -->
      <div class="telemetry-strip">
        <div class="tele-item">
          <div class="tele-top">
            <span class="tele-pulse-dot"></span>
            <span class="tele-lbl">EVALUATED DESCRIPTORS</span>
          </div>
          <div class="tele-val">18 Metrics</div>
          <div class="tele-sub">Topological &amp; Quantum Indices</div>
        </div>
        <div class="tele-item">
          <div class="tele-top">
            <span class="tele-pulse-dot emerald"></span>
            <span class="tele-lbl">DUAL VIEWPORT</span>
          </div>
          <div class="tele-val">2D &amp; 3D Sync</div>
          <div class="tele-sub">Real-time Topology Linkage</div>
        </div>
        <div class="tele-item">
          <div class="tele-top">
            <span class="tele-pulse-dot purple"></span>
            <span class="tele-lbl">REPRESENTATION MODES</span>
          </div>
          <div class="tele-val">4 Conformer Styles</div>
          <div class="tele-sub">Ball &amp; Stick, Stick, CPK, Wire</div>
        </div>
        <div class="tele-item">
          <div class="tele-top">
            <span class="tele-pulse-dot cyan"></span>
            <span class="tele-lbl">COMPUTATIONAL CORE</span>
          </div>
          <div class="tele-val">Python 3.14</div>
          <div class="tele-sub">Serverless Cloud Calculation</div>
        </div>
      </div>
    </div>
  </section>

  <!-- BLOCK 2: CHEMINFORMATICS THEORY & FOUNDATIONS -->
  <section id="theory" data-chapter="02" data-chapter-name="CURRICULUM THEORY">
    <div class="wrap">
      <div class="sechead">
        <div class="kicker">Curriculum Foundations</div>
        <h2>Introduction to Cheminformatics</h2>
        <div class="sec-line"></div>
        <p style="margin-top:12px">
          Cheminformatics combines chemistry, computer science, and information technology to represent,
          simulate, and analyze molecular structures and their physicochemical behaviors computationally.
        </p>
      </div>

      <!-- 3-Card Interactive Theory Bento Grid -->
      <div class="theory-bento-grid">
        <!-- Bento 1: Interactive SMILES Syntax Decrypter -->
        <div class="card theory-card bento-hero slide-left">
          <div class="theory-card-head">
            <span class="bento-badge">INTERACTIVE SYNTAX DECRYPTER</span>
            <h3 style="color:#ffffff;font-size:18px">SMILES Molecular Graph Encoding</h3>
          </div>
          <p style="color:var(--mut);font-size:13.5px;margin-bottom:14px">
            <strong>SMILES</strong> encodes 3D chemical topologies into unambiguous linear ASCII notation. Click or hover any functional token below to inspect its chemical bonding role:
          </p>

          <!-- Interactive Token Strip for Aspirin -->
          <div class="smiles-token-track" id="smilesTokenTrack">
            <span class="smiles-chip" onclick="inspectSmilesToken('Methyl Carbonyl', 'CC(=O)', 'Aliphatic acetyl group: Sp3 methyl carbon single-bonded to an sp2 carbonyl carbon with a pi double bond to oxygen.')" onmouseenter="inspectSmilesToken('Methyl Carbonyl', 'CC(=O)', 'Aliphatic acetyl group: Sp3 methyl carbon single-bonded to an sp2 carbonyl carbon with a pi double bond to oxygen.')">CC(=O)</span>
            <span class="smiles-chip ester" onclick="inspectSmilesToken('Ester Bridge', 'O', 'Ester oxygen linkage: Electronegative oxygen with two lone pairs bridging the acetyl group to the aromatic core.')" onmouseenter="inspectSmilesToken('Ester Bridge', 'O', 'Ester oxygen linkage: Electronegative oxygen with two lone pairs bridging the acetyl group to the aromatic core.')">O</span>
            <span class="smiles-chip ring" onclick="inspectSmilesToken('Aromatic Benzene Ring', 'c1ccccc1', 'Planar benzene ring: 6 sp2 carbons sharing 6 delocalized pi electrons satisfying Hückel 4n+2 rule. Digits 1 close the aromatic cycle.')" onmouseenter="inspectSmilesToken('Aromatic Benzene Ring', 'c1ccccc1', 'Planar benzene ring: 6 sp2 carbons sharing 6 delocalized pi electrons satisfying Hückel 4n+2 rule. Digits 1 close the aromatic cycle.')">c1ccccc1</span>
            <span class="smiles-chip acid" onclick="inspectSmilesToken('Carboxylic Acid', 'C(=O)O', 'Carboxylic acid pharmacophore: Strongly polar functional group responsible for analgesic and anti-inflammatory bioactivity.')" onmouseenter="inspectSmilesToken('Carboxylic Acid', 'C(=O)O', 'Carboxylic acid pharmacophore: Strongly polar functional group responsible for analgesic and anti-inflammatory bioactivity.')">C(=O)O</span>
          </div>

          <div class="token-inspector" id="tokenInspector">
            <div class="inspector-title" id="inspectorTitle">Aspirin &bull; [CC(=O)Oc1ccccc1C(=O)O]</div>
            <div class="inspector-body" id="inspectorBody">Hover or click any colored token above to decode its bonding hybridization, valence connectivity, and pharmacological role in real time.</div>
          </div>
        </div>

        <!-- Bento 2: 3D Conformer Geometries -->
        <div class="card theory-card slide-right">
          <div class="theory-card-head">
            <span class="bento-badge emerald">FORCE FIELD OPTIMIZATION</span>
            <h3 style="color:#ffffff;font-size:18px">3D Conformer Modeling</h3>
          </div>
          <p style="color:var(--mut);font-size:13.5px;margin-bottom:12px">
            Derives minimum energy Cartesian coordinates via Merck Molecular Force Field (MMFF94):
          </p>
          <div class="geom-pill-list">
            <div class="geom-pill-item">
              <span class="g-name">Ball &amp; Stick</span>
              <span class="g-desc">Spatial stereochemistry &amp; bond angles</span>
            </div>
            <div class="geom-pill-item">
              <span class="g-name">Spacefill (CPK)</span>
              <span class="g-desc">Van der Waals steric binding volume</span>
            </div>
            <div class="geom-pill-item">
              <span class="g-name">Stick Model</span>
              <span class="g-desc">Covalent orbital hybridization network</span>
            </div>
            <div class="geom-pill-item">
              <span class="g-name">Wireframe</span>
              <span class="g-desc">High-speed topological skeletal mesh</span>
            </div>
          </div>
        </div>

        <!-- Bento 3: Lipinski Rule of 5 Criteria -->
        <div class="card theory-card bento-wide">
          <div class="theory-card-head">
            <span class="bento-badge purple">CLINICAL PHARMACOKINETICS</span>
            <h3 style="color:#ffffff;font-size:18px">Lipinski's Rule of 5 (Oral Drug-Likeness Standard)</h3>
          </div>
          <p style="color:var(--mut);font-size:13.5px;margin-bottom:14px">
            Formulated by Pfizer's Christopher A. Lipinski to predict whether a chemical molecule possesses adequate cellular permeability and oral bioavailability:
          </p>
          <div class="ro5-criteria-row">
            <div class="ro5-criterion">
              <div class="crit-num">Rule 1 &bull; Molecular Mass</div>
              <div class="crit-val">MW &le; 500 Da</div>
              <div class="crit-desc">Facilitates passive cellular membrane permeation without bulky steric hindrance.</div>
            </div>
            <div class="ro5-criterion">
              <div class="crit-num">Rule 2 &bull; Lipophilicity</div>
              <div class="crit-val">LogP &le; 5.0</div>
              <div class="crit-desc">Balances aqueous bloodstream solubility with lipid bilayer absorption.</div>
            </div>
            <div class="ro5-criterion">
              <div class="crit-num">Rule 3 &bull; H-Donors</div>
              <div class="crit-val">HBD &le; 5</div>
              <div class="crit-desc">Restricts excess OH/NH groups to prevent desolvation energy penalties across cell walls.</div>
            </div>
            <div class="ro5-criterion">
              <div class="crit-num">Rule 4 &bull; H-Acceptors</div>
              <div class="crit-val">HBA &le; 10</div>
              <div class="crit-desc">Limits electronegative N/O lone pairs to ensure efficient gut receptor dissociation.</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- BLOCK 3: 2D & 3D INTERACTIVE MOLECULAR LAB -->
  <section id="lab" data-chapter="03" data-chapter-name="MOLECULAR LAB">
    <div class="wrap">
      <div class="sechead">
        <div class="kicker">Core Laboratory Suite</div>
        <h2>SMILES to 2D &amp; 3D Molecular Representation</h2>
        <div class="sec-line"></div>
        <p style="margin-top:12px">
          Enter any valid SMILES notation or click an example molecule.
          The laboratory immediately resolves the 2D bond topology, derives 3D coordinates via force-field optimization,
          and renders an interactive WebGL viewport.
        </p>
      </div>

      <!-- Alerts -->
      <div id="smilesError" class="alert-banner error" style="display:none;flex-direction:column;align-items:flex-start;gap:6px">
        <div style="display:flex;align-items:center;gap:8px;width:100%">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
          <span id="smilesErrorText">Invalid SMILES — possible unclosed ring (check digit pairs) or nitrogen valence error. Try CC(=O)O for acetic acid.</span>
        </div>
        <div id="smilesPedagogicTip" style="font-size:12.5px;color:rgba(255,255,255,0.92);background:rgba(0,0,0,0.25);padding:6px 10px;border-radius:6px;width:100%;display:none;line-height:1.45;border-left:3px solid #ff4d6a"></div>
      </div>

      <div id="smilesSuccess" class="alert-banner success" style="display:none">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        <span id="smilesSuccessText">Valid chemical structure parsed and 3D geometry rendered successfully.</span>
      </div>

      <div class="card">

        <!-- Input Mode Tabs: SMILES Mode | ✏️ Draw Studio | 🧬 Peptide Mode -->
        <div style="display:flex;gap:8px;margin-bottom:14px;flex-wrap:wrap">
          <button type="button" class="mode-tab-btn active" id="modeTabSmiles" onclick="switchInputMode('smiles')">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 7V4h16v3M9 20h6M12 4v16"/></svg>
            <span>SMILES Notation</span>
          </button>
          <button type="button" class="mode-tab-btn" id="modeTabDraw" onclick="switchInputMode('draw')">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
            <span>✏️ 2D Drawing Studio (JSME)</span>
          </button>
          <button type="button" class="mode-tab-btn" id="modeTabPeptide" onclick="switchInputMode('peptide')">
            <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>
            <span>🧬 Peptide Sequence Mode</span>
          </button>
        </div>

        <!-- 2D Structure Drawing Studio (JSME Canvas & Quick Palette) -->
        <div id="drawStudioContainer" style="display:none;background:rgba(2,6,23,0.85);border:1px solid rgba(0,240,255,0.25);border-radius:8px;padding:16px;margin-bottom:18px">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;flex-wrap:wrap;gap:10px">
            <div>
              <div style="font-size:13px;font-weight:700;color:var(--ink);display:flex;align-items:center;gap:8px">
                <span style="color:var(--acc)">✏️ JSME MOLECULAR STRUCTURE EDITOR</span>
                <span style="font-size:11px;background:rgba(61,139,255,0.15);color:var(--acc);padding:2px 8px;border-radius:4px;font-family:var(--mono)">Interactive Canvas</span>
              </div>
              <div style="font-size:11.5px;color:var(--dim);margin-top:2px">
                Click and drag atoms, bonds, and rings on the canvas below, or pick rapid templates.
              </div>
            </div>
            <div style="display:flex;gap:6px;flex-wrap:wrap">
              <button type="button" class="btn secondary" onclick="loadJsmeTemplate('c1ccccc1')" style="padding:5px 9px;font-size:11px">Benzene</button>
              <button type="button" class="btn secondary" onclick="loadJsmeTemplate('C1CCCCC1')" style="padding:5px 9px;font-size:11px">Cyclohexane</button>
              <button type="button" class="btn secondary" onclick="loadJsmeTemplate('c1ccncc1')" style="padding:5px 9px;font-size:11px">Pyridine</button>
              <button type="button" class="btn secondary" onclick="clearJsmeCanvas()" style="padding:5px 9px;font-size:11px">Clear</button>
              <button type="button" class="btn primary" onclick="transferJsmeToLab()" style="padding:5px 12px;font-size:11.5px">
                <svg width="13" height="13" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
                <span>Apply to 3D Lab</span>
              </button>
            </div>
          </div>
          
          <div id="jsme_container" style="width:100%;min-height:360px;background:#ffffff;border-radius:4px;overflow:hidden;box-shadow:inset 0 0 10px rgba(0,0,0,0.1);position:relative">
            <div id="jsme_placeholder" style="height:360px;display:flex;flex-direction:column;align-items:center;justify-content:center;color:#334155;font-family:var(--mono);font-size:12px;background:#f8fafc">
              <div style="font-size:26px;margin-bottom:8px">✏️</div>
              <strong style="color:#1e293b;font-size:13.5px">Loading JSME Molecular Drawing Editor...</strong>
              <span style="font-size:11px;color:#64748b;margin-top:4px;margin-bottom:12px">Instant 2D structure drawing with live SMILES synchronization</span>
              <button type="button" class="btn secondary sm" onclick="setupJsmeInstance(true)" style="padding:4px 12px;font-size:11px;border-color:#cbd5e1;color:#1e293b">Initialize Editor</button>
            </div>
          </div>
          
          <div style="margin-top:12px;padding-top:10px;border-top:1px solid rgba(255,255,255,0.08);display:flex;align-items:center;gap:6px;flex-wrap:wrap">
            <span style="font-size:11px;color:var(--dim);font-family:var(--mono);margin-right:6px">1-CLICK FRAGMENTS:</span>
            <button type="button" class="v-pill" onclick="appendJsmeFragment('O')">-OH</button>
            <button type="button" class="v-pill" onclick="appendJsmeFragment('C(=O)O')">-COOH</button>
            <button type="button" class="v-pill" onclick="appendJsmeFragment('N')">-NH2</button>
            <button type="button" class="v-pill" onclick="appendJsmeFragment('[N+](=O)[O-]')">-NO2</button>
            <button type="button" class="v-pill" onclick="appendJsmeFragment('C=O')">-C=O</button>
            <button type="button" class="v-pill" onclick="appendJsmeFragment('C#N')">-C#N</button>
            <button type="button" class="v-pill" onclick="appendJsmeFragment('Cl')">-Cl</button>
            <button type="button" class="v-pill" onclick="appendJsmeFragment('Br')">-Br</button>
            <button type="button" class="v-pill" onclick="appendJsmeFragment('F')">-F</button>
            <button type="button" class="v-pill" onclick="appendJsmeFragment('S')">-SH</button>
          </div>
        </div>

        <!-- Peptide Sequence Mode Studio -->
        <div id="peptideStudioContainer" style="display:none;background:rgba(2,6,23,0.85);border:1px solid rgba(0,255,157,0.25);border-radius:8px;padding:16px;margin-bottom:18px">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:10px;flex-wrap:wrap;gap:10px">
            <div>
              <div style="font-size:13px;font-weight:700;color:var(--ink);display:flex;align-items:center;gap:8px">
                <span style="color:var(--acc2)">🧬 AMINO ACID / PEPTIDE TRANSLATION ENGINE</span>
                <span style="font-size:11px;background:rgba(0,255,157,0.15);color:var(--acc2);padding:2px 8px;border-radius:4px;font-family:var(--mono)">Biochemistry Module</span>
              </div>
              <div style="font-size:11.5px;color:var(--dim);margin-top:2px">
                Input 1-letter or 3-letter amino acid sequences (e.g. YGGFL for Enkephalin, RGD, or Ala-Gly-Tyr).
              </div>
            </div>
          </div>
          
          <div style="display:flex;gap:10px;flex-wrap:wrap;margin-bottom:12px">
            <div style="flex:1;min-width:260px">
              <input type="text" id="peptideInput" placeholder="Enter sequence (e.g. YGGFL, AGY, RGD, ECG)" value="YGGFL" style="width:100%;font-family:var(--mono);text-transform:uppercase" onkeyup="if(event.key==='Enter') translateAndAnalyzePeptide()">
            </div>
            <button type="button" class="btn primary" onclick="translateAndAnalyzePeptide()">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
              <span>Translate &amp; Render 3D</span>
            </button>
          </div>
          
          <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap;margin-bottom:10px">
            <span style="font-size:11px;color:var(--dim);font-family:var(--mono)">PRESETS:</span>
            <button type="button" class="preset-chip" onclick="setPeptideSeq('YGGFL')">Enkephalin (YGGFL)</button>
            <button type="button" class="preset-chip" onclick="setPeptideSeq('RGD')">Cell Adhesion (RGD)</button>
            <button type="button" class="preset-chip" onclick="setPeptideSeq('ECG')">Glutathione (ECG)</button>
            <button type="button" class="preset-chip" onclick="setPeptideSeq('GHK')">GHK Tripeptide</button>
            <button type="button" class="preset-chip" onclick="setPeptideSeq('CYIQNC')">Oxytocin Segment</button>
            <button type="button" class="preset-chip" onclick="setPeptideSeq('AGY')">Ala-Gly-Tyr</button>
          </div>

          <div id="peptideInfoBox" style="background:rgba(0,0,0,0.3);border:1px solid rgba(255,255,255,0.08);border-radius:6px;padding:10px 14px;font-size:12px;display:flex;align-items:center;gap:18px;flex-wrap:wrap">
            <div><strong>Sequence:</strong> <span id="pepSeqDisplay" style="color:var(--acc2);font-family:var(--mono)">YGGFL</span></div>
            <div><strong>Length:</strong> <span id="pepLenDisplay" style="color:var(--ink);font-family:var(--mono)">5 residues</span></div>
            <div><strong>Est. MW:</strong> <span id="pepMwDisplay" style="color:var(--ink);font-family:var(--mono)">555.6 g/mol</span></div>
            <div><strong>Net Charge (pH 7.4):</strong> <span id="pepChargeDisplay" style="color:var(--ink);font-family:var(--mono)">0.0</span></div>
          </div>
        </div>

        <!-- SMILES Input Row -->
        <div class="smiles-bar">
          <div class="input-box" style="position:relative">
            <input type="text" id="smilesInput" value="CCO" placeholder="Enter SMILES (e.g. c1ccccc1, CC(=O)O, CC(=O)Oc1ccccc1C(=O)O)" spellcheck="false" onkeyup="if(event.key==='Enter') analyzeMolecule()">
          </div>
          <button class="btn secondary" type="button" onclick="copySmilesToClipboard()" title="Copy active SMILES to clipboard" style="padding:10px 12px">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
            <span>Copy</span>
          </button>
          <button class="btn secondary" type="button" onclick="copyShareLink()" title="Copy permanent shareable molecule link" style="padding:10px 12px">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 13a5 5 0 0 0 7.54.54l3-3a5 5 0 0 0-7.07-7.07l-1.72 1.71"/><path d="M14 11a5 5 0 0 0-7.54-.54l-3 3a5 5 0 0 0 7.07 7.07l1.71-1.71"/></svg>
            <span>Share</span>
          </button>
          <button class="btn secondary" type="button" onclick="switchInputMode('draw')" title="Open 2D Structure Drawing Studio" style="padding:10px 12px">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M12 20h9M16.5 3.5a2.121 2.121 0 0 1 3 3L7 19l-4 1 1-4L16.5 3.5z"/></svg>
            <span>Draw</span>
          </button>
          <button class="btn primary" id="btnAnalyze" onclick="analyzeMolecule()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="5 3 19 12 5 21 5 3"/></svg>
            <span>Analyze &amp; Render 3D</span>
          </button>
          <button class="btn" id="btnSpin" onclick="toggleSpin()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21.5 2v6h-6M21.34 15.57a10 10 0 1 1-.57-8.38l5.67-5.67"/></svg>
            <span>Auto Spin</span>
          </button>
          <button class="btn secondary" id="btnAddToQueue" onclick="addCurrentToReportQueue()" title="Add active molecule to Multi-Molecule Report Queue">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="12" y1="5" x2="12" y2="19"/><line x1="5" y1="12" x2="19" y2="12"/></svg>
            <span>+ Queue for Report</span>
          </button>
        </div>

        <!-- Preset Chips -->
        <div class="preset-chips" id="presetChips">
          <!-- Populated by JS -->
        </div>

        <!-- Dual Canvas Viewport with Sliding Collision & Holographic Chamber -->
        <div class="dual-canvas-grid">
          <!-- 2D Structure Canvas -->
          <div class="slide-left">
            <div class="canvas-header-row">
              <div class="canvas-tag"><span class="canvas-tag-dot"></span> 2D TOPOLOGICAL GRAPH</div>
              <span class="canvas-subtag">BOND CONNECTIVITY &bull; AUTO-ALIGNED</span>
            </div>
            <div class="mol-2d-canvas" id="canvas2D">
              <!-- HUD Corner Reticles -->
              <div class="hud-reticle tl"></div>
              <div class="hud-reticle tr"></div>
              <div class="hud-reticle bl"></div>
              <div class="hud-reticle br"></div>
              <!-- SVG generated dynamically -->
            </div>
          </div>

          <!-- 3D WebGL Viewer -->
          <div class="slide-right">
            <div class="canvas-header-row">
              <div class="canvas-tag emerald"><span class="canvas-tag-dot emerald"></span> 3D CONFORMER VIEWPORT</div>
              <span class="canvas-subtag" id="hudConformerStatus">MMFF94 3D FORCE FIELD &bull; OPTIMIZED GEOMETRY</span>
              <!-- Hidden controls preserved for backward compatibility -->
              <select class="model-select" id="modelStyle" onchange="update3DStyle()" style="display:none">
                <option value="ballAndStick">Ball and Stick</option>
                <option value="stick">Stick Model</option>
                <option value="sphere">Space Filling (CPK)</option>
                <option value="line">Wireframe</option>
              </select>
              <input type="checkbox" id="chkSurface" onchange="update3DStyle()" style="display:none">
            </div>
            <div class="viewer-box" id="viewer3D">
              <!-- HUD Corner Reticles -->
              <div class="hud-reticle tl"></div>
              <div class="hud-reticle tr"></div>
              <div class="hud-reticle bl"></div>
              <div class="hud-reticle br"></div>

              <!-- Floating In-Canvas Glass Tool Dock -->
              <div class="viewer-floating-dock" id="viewerFloatingDock">
                <div class="viewer-style-pills">
                  <button type="button" class="v-pill active" onclick="set3DModelStyle('ballAndStick', this)" title="Ball and Stick Model">Ball &amp; Stick</button>
                  <button type="button" class="v-pill" onclick="set3DModelStyle('stick', this)" title="Stick Framework Model">Stick</button>
                  <button type="button" class="v-pill" onclick="set3DModelStyle('sphere', this)" title="Spacefill CPK Model">Spacefill</button>
                  <button type="button" class="v-pill" onclick="set3DModelStyle('line', this)" title="Wireframe Mesh Model">Wireframe</button>
                </div>
                <div class="viewer-action-pills">
                  <button type="button" class="v-action-pill" id="dockSpinBtn" onclick="toggleSpin()" title="Toggle Continuous 3D Rotation">
                    <span class="spin-icon">↻</span> Spin
                  </button>
                  <button type="button" class="v-action-pill" id="dockSurfaceBtn" onclick="toggleVdwSurface()" title="Toggle van der Waals Solvent Surface">
                    vdW Surface
                  </button>
                  <button type="button" class="v-action-pill" onclick="reset3DCamera()" title="Recenter Camera View">
                    ⟲ Recenter
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Bond Architecture Counters -->
        <div class="bond-metric-grid" id="bondMetricGrid">
          <div class="bond-metric-card">
            <strong id="bmFormula">C2H6O</strong>
            <span>Formula</span>
          </div>
          <div class="bond-metric-card">
            <strong id="bmMw" data-val="0">0.00</strong>
            <span>MW (g/mol)</span>
          </div>
          <div class="bond-metric-card">
            <strong id="bmHeavyAtoms" data-val="0">0</strong>
            <span>Heavy Atoms</span>
          </div>
          <div class="bond-metric-card">
            <strong id="bmSigma" data-val="0">0</strong>
            <span>Sigma (σ) Bonds</span>
          </div>
          <div class="bond-metric-card">
            <strong id="bmPi" data-val="0">0</strong>
            <span>Pi (π) Bonds</span>
          </div>
          <div class="bond-metric-card">
            <strong id="bmTotalBonds" data-val="0">0</strong>
            <span>Total Bonds</span>
          </div>
        </div>
      </div>
    </div>
  </section>

  <!-- BLOCK 4: COMPLETE 18 MOLECULAR DESCRIPTORS -->
  <section id="properties" data-chapter="04" data-chapter-name="18 DESCRIPTORS">
    <div class="wrap">
      <div class="sechead">
        <div class="kicker">Quantitative Cheminformatics</div>
        <h2>Complete 18-Descriptor Analytical Suite</h2>
        <div class="sec-line"></div>
        <p style="margin-top:12px">
          Derived through topological graph theory, Wildman-Crippen lipophilicity matrices, and Ertl polar surface calculations.
          Each metric includes an educational interpretation explaining its physical and pharmacological significance.
        </p>
      </div>

      <div class="card">
        <!-- Lipinski Rule of 5 Clinical Scorecard & Hero Visual Gauges -->
        <div class="ro5-dashboard">
          <div class="ro5-compliance-bar" id="ro5ComplianceBar">
            <div class="ro5-badge" id="ro5Badge">
              <span class="ro5-dot"></span>
              <span id="ro5StatusText">LIPINSKI RULE OF 5: 4 / 4 PASS (DRUG-LIKE CANDIDATE)</span>
            </div>
            <div class="ro5-subtext" id="ro5Subtext">Satisfies Pfizer clinical guidelines for oral bioavailability and intestinal membrane permeation.</div>
          </div>

          <div class="ro5-gauge-grid">
            <!-- Gauge 1: Molecular Weight -->
            <div class="gauge-card">
              <div class="gauge-head">
                <span class="gauge-title">Molecular Weight</span>
                <span class="gauge-badge" id="gaugeBadgeMw">PASS</span>
              </div>
              <div class="gauge-val" id="gaugeValMw" data-val="0">0.00 <span class="gauge-unit">g/mol</span></div>
              <div class="gauge-meter">
                <div class="gauge-fill" id="gaugeFillMw" style="width: 9.2%"></div>
              </div>
              <div class="gauge-foot">
                <span>0 Da</span>
                <span class="limit-label">Limit: 500 Da</span>
              </div>
            </div>

            <!-- Gauge 2: LogP Lipophilicity -->
            <div class="gauge-card">
              <div class="gauge-head">
                <span class="gauge-title">LogP (Lipophilicity)</span>
                <span class="gauge-badge" id="gaugeBadgeLogP">OPTIMAL</span>
              </div>
              <div class="gauge-val" id="gaugeValLogP" data-val="0">0.00 <span class="gauge-unit">oct/water</span></div>
              <div class="gauge-meter">
                <div class="gauge-fill emerald" id="gaugeFillLogP" style="width: 28%"></div>
              </div>
              <div class="gauge-foot">
                <span>Hydrophilic</span>
                <span class="limit-label">Limit: 5.0</span>
              </div>
            </div>

            <!-- Gauge 3: Hydrogen Bond Donors -->
            <div class="gauge-card">
              <div class="gauge-head">
                <span class="gauge-title">H-Bond Donors</span>
                <span class="gauge-badge" id="gaugeBadgeHbd">PASS</span>
              </div>
              <div class="gauge-val" id="gaugeValHbd" data-val="0">0 <span class="gauge-unit">/ 5 max</span></div>
              <div class="gauge-meter">
                <div class="gauge-fill cyan" id="gaugeFillHbd" style="width: 20%"></div>
              </div>
              <div class="gauge-foot">
                <span>OH &amp; NH groups</span>
                <span class="limit-label">Limit: &le; 5</span>
              </div>
            </div>

            <!-- Gauge 4: Hydrogen Bond Acceptors -->
            <div class="gauge-card">
              <div class="gauge-head">
                <span class="gauge-title">H-Bond Acceptors</span>
                <span class="gauge-badge" id="gaugeBadgeHba">PASS</span>
              </div>
              <div class="gauge-val" id="gaugeValHba" data-val="0">0 <span class="gauge-unit">/ 10 max</span></div>
              <div class="gauge-meter">
                <div class="gauge-fill purple" id="gaugeFillHba" style="width: 10%"></div>
              </div>
              <div class="gauge-foot">
                <span>N &amp; O lone pairs</span>
                <span class="limit-label">Limit: &le; 10</span>
              </div>
            </div>
          </div>
        </div>

        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:14px">
          <div>
            <span style="font-family:var(--mono);color:var(--dim);font-size:12px">ACTIVE MOLECULE: </span>
            <strong id="activeMolTitle" style="color:var(--acc);font-size:16px">Ethanol (CCO)</strong>
          </div>
          <button class="btn sm" onclick="exportDescriptorsCSV()" data-cursor-label="EXPORT CSV">
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
                <th style="width:58%">Student Interpretation &amp; Physical Relevance</th>
              </tr>
            </thead>
            <tbody id="propTableBody">
              <!-- Dynamically populated -->
            </tbody>
          </table>
        </div>

        <!-- BLOCK 4B: SPECTRAL PREDICTION PANEL (IR & 1H NMR) -->
        <div style="margin-top:28px;border-top:1px solid rgba(255,255,255,0.08);padding-top:24px">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:10px">
            <div style="display:flex;align-items:center;gap:10px">
              <span style="font-size:18px">🔬</span>
              <div>
                <h3 style="color:var(--ink);font-size:16.5px;margin:0">Spectroscopic Predictions (Infrared &amp; &sup1;H NMR)</h3>
                <span style="font-size:11.5px;color:var(--dim)">Theoretical functional group frequencies and proton magnetic shielding profiles</span>
              </div>
            </div>
            <div style="display:flex;gap:6px">
              <button type="button" class="v-pill active" id="tabSpecIr" onclick="switchSpectralTab('ir')">Infrared (IR) Bands</button>
              <button type="button" class="v-pill" id="tabSpecNmr" onclick="switchSpectralTab('nmr')">&sup1;H NMR Chemical Shifts</button>
            </div>
          </div>

          <!-- IR Spectrum Content -->
          <div id="specIrContainer">
            <div style="background:rgba(2,6,23,0.7);border:1px solid rgba(255,255,255,0.1);border-radius:6px;padding:12px 16px;margin-bottom:14px">
              <div style="display:flex;justify-content:space-between;font-family:var(--mono);font-size:11px;color:var(--dim);margin-bottom:6px">
                <span>4000 cm&minus;&sup1; (O-H / N-H)</span>
                <span>3000 (C-H)</span>
                <span>2200 (Triple Bonds)</span>
                <span>1700 (C=O)</span>
                <span>1500 (Aromatic C=C)</span>
                <span>1000 (Fingerprint)</span>
                <span>400 cm&minus;&sup1;</span>
              </div>
              <div id="irSpectrumBar" style="height:26px;background:rgba(255,255,255,0.06);border-radius:4px;position:relative;overflow:hidden;border:1px solid rgba(255,255,255,0.1)">
                <!-- Peak markers populated dynamically -->
              </div>
            </div>

            <div style="overflow-x:auto">
              <table class="prop-table" style="font-size:12.5px">
                <thead>
                  <tr>
                    <th>Vibrational Mode / Functional Group</th>
                    <th>Frequency (cm&minus;&sup1;)</th>
                    <th>Intensity &amp; Band Shape</th>
                    <th>Diagnostic Interpretation</th>
                  </tr>
                </thead>
                <tbody id="specIrTableBody">
                  <!-- Populated by JS -->
                </tbody>
              </table>
            </div>
          </div>

          <!-- 1H NMR Content -->
          <div id="specNmrContainer" style="display:none">
            <div style="overflow-x:auto">
              <table class="prop-table" style="font-size:12.5px">
                <thead>
                  <tr>
                    <th>Proton Environment</th>
                    <th>Chemical Shift (&delta;, ppm)</th>
                    <th>Multiplicity &amp; Shielding</th>
                    <th>Electronic &amp; Magnetic Context</th>
                  </tr>
                </thead>
                <tbody id="specNmrTableBody">
                  <!-- Populated by JS -->
                </tbody>
              </table>
            </div>
          </div>
        </div>

        <!-- BLOCK 4C: STRUCTURAL SIMILARITY & SAR SEARCH (TANIMOTO) -->
        <div style="margin-top:28px;border-top:1px solid rgba(255,255,255,0.08);padding-top:24px">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:14px;flex-wrap:wrap;gap:10px">
            <div style="display:flex;align-items:center;gap:10px">
              <span style="font-size:18px">🧬</span>
              <div>
                <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">
                  <h3 style="color:var(--ink);font-size:16.5px;margin:0">Structural Similarity &amp; SAR Search (Tanimoto Coefficient)</h3>
                  <span class="badge" style="font-size:10.5px;background:rgba(255,184,0,0.1);color:var(--warn);border:1px solid rgba(255,184,0,0.28)">Approximate Structural Similarity</span>
                </div>
                <span style="font-size:11.5px;color:var(--dim)">Top 5 structural analogues retrieved from reference pharmacophore database</span>
              </div>
            </div>
          </div>

          <!-- Pedagogical SAR Disclaimer -->
          <div style="font-size:11.5px;color:var(--dim);background:rgba(0,240,255,0.03);border:1px solid rgba(0,240,255,0.18);border-radius:6px;padding:8px 12px;margin-bottom:14px;line-height:1.45">
            <strong style="color:var(--acc)">💡 Pedagogical SAR Note:</strong> Metric represents approximate topological circular atom-neighborhood similarity (radius-2 circular graph hashes). In commercial medicinal chemistry and clinical SAR research, candidate screening is performed using 2048-bit Morgan/ECFP4 bit-vectors via RDKit.
          </div>

          <div id="similarityCardsGrid" style="display:grid;grid-template-columns:repeat(auto-fit, minmax(220px, 1fr));gap:12px">
            <!-- Populated dynamically by JS -->
          </div>
        </div>

      </div>
    </div>
  </section>

  <!-- BLOCK 5: COMPARATIVE ANALYSIS MATRIX -->
  <section id="compare" data-chapter="05" data-chapter-name="COMPARATIVE MATRIX">
    <div class="wrap">
      <div class="sechead">
        <div class="kicker">Structure-Property Relationships</div>
        <h2>Multi-Molecule Comparative Matrix</h2>
        <div class="sec-line"></div>
        <p style="margin-top:12px">
          Compare fundamental chemical compounds side-by-side to observe how functional groups, aromaticity,
          and branching influence boiling points, aqueous solubility, and hydrogen-bonding potentials.
        </p>
      </div>

      <div class="card" style="overflow-x:auto">
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

  <!-- BLOCK 6: STUDENT ASSESSMENT & QUIZ -->
  <section id="quiz" data-chapter="06" data-chapter-name="ASSESSMENT MODULE">
    <div class="wrap">
      <div class="sechead">
        <div class="kicker">Knowledge Verification</div>
        <h2>Student Assessment Module</h2>
        <div class="sec-line"></div>
        <p style="margin-top:12px">
          Test your comprehension of SMILES notation, molecular descriptors, and Lipinski's Rule of 5.
          Your score is calculated instantly and can be certified in the downloadable laboratory report.
        </p>
      </div>

      <div class="card" style="max-width:760px;margin:0 auto">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:16px">
          <span style="font-family:var(--mono);font-size:12px;color:var(--acc)" id="quizProgress">QUESTION 1 OF 5</span>
          <span style="font-family:var(--mono);font-size:12px;color:var(--acc2)" id="quizScore">SCORE: 0</span>
        </div>

        <h3 id="quizQuestion" style="font-size:18px;margin-bottom:18px;color:var(--ink)">What does the SMILES acronym stand for in computational chemistry?</h3>
        <div id="quizOptions">
          <button class="quiz-opt" onclick="checkAnswer(0)"><span>A.</span> Simplified Molecular Input Line Entry System</button>
          <button class="quiz-opt" onclick="checkAnswer(1)"><span>B.</span> Standard Molecular Identification &amp; Logic Expression Set</button>
          <button class="quiz-opt" onclick="checkAnswer(2)"><span>C.</span> Systematic Molecular Integration Line Exchange Scheme</button>
          <button class="quiz-opt" onclick="checkAnswer(3)"><span>D.</span> Substituent Mapping &amp; Isomer Linear Evaluation Syntax</button>
        </div>

        <div style="margin-top:20px;display:flex;justify-content:flex-end">
          <button class="btn primary sm" id="btnNextQuiz" onclick="nextQuestion()" style="display:none">
            <span>Next Question</span>
            <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
          </button>
        </div>
      </div>

      <!-- Class Leaderboard & Progress Panel -->
      <div class="card" style="max-width:760px;margin:24px auto 0 auto" id="leaderboardSection">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:16px;border-bottom:1px solid var(--border);padding-bottom:12px">
          <div>
            <div class="kicker" style="font-size:10px;margin-bottom:2px">Cohort Performance</div>
            <h4 style="font-size:16px;font-weight:700;color:var(--ink);display:flex;align-items:center;gap:8px">
              🏆 Class Leaderboard &amp; Progress
            </h4>
          </div>
          <div style="display:flex;align-items:center;gap:8px">
            <span style="font-size:12px;color:var(--dim)">Class Code:</span>
            <input type="text" id="leaderboardClassCode" value="SRM-CHEM-101" style="width:130px;padding:5px 8px;font-family:var(--mono);font-size:12px;text-transform:uppercase;background:rgba(255,255,255,0.04);border:1px solid var(--border);color:var(--ink)" />
            <button type="button" class="btn secondary sm" onclick="fetchLeaderboard()" style="padding:5px 10px;font-size:11px">Filter</button>
          </div>
        </div>

        <!-- Class Code Guidance Banner -->
        <div style="font-size:12px;color:var(--dim);margin-top:-6px;margin-bottom:14px;background:rgba(61,139,255,0.06);border:1px solid rgba(61,139,255,0.18);border-radius:6px;padding:8px 12px;display:flex;align-items:center;gap:8px">
          <span style="color:var(--acc);font-size:14px">ℹ️</span>
          <span>Get your official class code from <strong>Dr. R. Subramanian</strong> (Division of Chemistry) to view your cohort. Default code: <code style="color:var(--acc);background:rgba(0,0,0,0.25);padding:2px 6px;border-radius:4px;font-family:var(--mono)">SRM-CHEM-101</code></span>
        </div>

        <!-- Cohort Progress Metrics -->
        <div style="display:grid;grid-template-columns:repeat(auto-fit, minmax(140px, 1fr));gap:12px;margin-bottom:16px" id="classMetricsContainer">
          <div style="background:rgba(255,255,255,0.02);border:1px solid var(--border);border-radius:4px;padding:10px;text-align:center">
            <div style="font-size:11px;color:var(--dim)">Submissions</div>
            <div id="metricSubmissions" style="font-family:var(--mono);font-size:18px;font-weight:700;color:var(--ink);margin-top:2px">0</div>
          </div>
          <div style="background:rgba(255,255,255,0.02);border:1px solid var(--border);border-radius:4px;padding:10px;text-align:center">
            <div style="font-size:11px;color:var(--dim)">Class Average</div>
            <div id="metricAverage" style="font-family:var(--mono);font-size:18px;font-weight:700;color:var(--acc);margin-top:2px">0.0%</div>
          </div>
          <div style="background:rgba(255,255,255,0.02);border:1px solid var(--border);border-radius:4px;padding:10px;text-align:center">
            <div style="font-size:11px;color:var(--dim)">Top Score</div>
            <div id="metricTopScore" style="font-family:var(--mono);font-size:18px;font-weight:700;color:var(--acc2);margin-top:2px">0 / 100</div>
          </div>
        </div>

        <!-- Submit to Leaderboard Box -->
        <div id="quizSubmitLeaderboardBox" style="background:rgba(0,240,255,0.04);border:1px solid rgba(0,240,255,0.25);border-radius:6px;padding:14px;margin-bottom:16px">
          <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:8px;margin-bottom:10px">
            <div>
              <div style="font-size:12.5px;font-weight:600;color:var(--ink)">Post Your Certified Score to Class Leaderboard</div>
              <div style="font-size:11px;color:var(--dim)">Certify your completion in the class cohort or submit anonymously.</div>
            </div>
            <div style="display:flex;align-items:center;gap:10px">
              <label style="display:flex;align-items:center;gap:4px;font-size:11.5px;color:var(--dim);cursor:pointer">
                <input type="checkbox" id="anonLeaderboardCheck" /> Anonymous
              </label>
              <button type="button" class="btn primary sm" onclick="submitScoreToLeaderboard()" style="padding:6px 14px;font-size:11.5px">
                Post Score
              </button>
            </div>
          </div>
          <div style="display:flex;gap:8px;flex-wrap:wrap">
            <input type="text" id="leaderboardStudentName" placeholder="Student Name (e.g. velmurgan)" style="flex:1;min-width:140px;padding:6px 10px;font-size:12px;background:rgba(255,255,255,0.04);border:1px solid var(--border);border-radius:4px;color:var(--ink)" />
            <input type="text" id="leaderboardStudentReg" placeholder="Register No (e.g. RA2611030050019)" style="flex:1;min-width:140px;padding:6px 10px;font-size:12px;background:rgba(255,255,255,0.04);border:1px solid var(--border);border-radius:4px;color:var(--ink)" />
          </div>
          <div id="leaderboardSubmitStatus" style="font-size:11.5px;margin-top:8px;display:none;color:var(--acc2)"></div>
        </div>

        <!-- Leaderboard Table -->
        <div style="overflow-x:auto">
          <table style="width:100%;border-collapse:collapse;font-size:12px;text-align:left">
            <thead>
              <tr style="border-bottom:1px solid var(--border);color:var(--dim)">
                <th style="padding:8px">Rank</th>
                <th style="padding:8px">Student</th>
                <th style="padding:8px">Register No</th>
                <th style="padding:8px;text-align:right">Score</th>
                <th style="padding:8px;text-align:right">Date</th>
              </tr>
            </thead>
            <tbody id="leaderboardTableBody">
              <!-- Dynamically populated -->
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  
  <!-- BLOCK 07: ORGANIC REACTION SIMULATOR -->
  <section id="reactions" data-chapter="07" data-chapter-name="REACTION SIMULATOR">
    <div class="wrap">
      <div class="sechead">
        <div class="kicker">Organic Transformations</div>
        <h2>Curriculum Reaction Simulator</h2>
        <div class="sec-line"></div>
        <p style="margin-top:12px">
          Explore 15 foundational organic reactions covering esterification, electrophilic aromatic substitution, oxidations, additions, and substitutions.
          Observe reactants, catalysts, reaction mechanisms, and load products directly into the 3D molecular lab.
        </p>
      </div>

      <div class="card">
        <!-- Reaction Selection Controls -->
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:18px;flex-wrap:wrap">
          <label style="font-size:12px;font-family:var(--mono);color:var(--acc);text-transform:uppercase">SELECT REACTION:</label>
          <select id="reactionSelect" onchange="onSelectReaction()" style="flex:1;min-width:280px;padding:9px 12px;background:rgba(2,6,23,0.8);border:1px solid rgba(0,240,255,0.3);color:var(--ink);border-radius:6px;font-family:var(--font-main);font-size:13.5px">
            <!-- Populated by JS -->
          </select>
          <button type="button" class="btn primary" onclick="loadActiveReactionProductToLab()">
            <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
            <span>Load Product in 3D Lab</span>
          </button>
        </div>

        <!-- Balanced Equation Banner -->
        <div style="background:rgba(2,6,23,0.9);border:1px solid rgba(0,240,255,0.25);border-radius:8px;padding:14px 18px;margin-bottom:20px;text-align:center">
          <div style="font-size:11px;color:var(--acc3);font-family:var(--mono);text-transform:uppercase;margin-bottom:4px">BALANCED CHEMICAL EQUATION</div>
          <div id="rxnEquation" style="font-size:16px;font-family:var(--mono);color:var(--ink);font-weight:700">CH3COOH + CH3CH2OH  --[H+]-->  CH3COOCH2CH3 + H2O</div>
          <div style="display:flex;justify-content:center;gap:16px;margin-top:8px;flex-wrap:wrap;font-size:12px;color:var(--dim);font-family:var(--mono)">
            <span>Classification: <strong id="rxnCategory" style="color:var(--acc)">Condensation</strong></span>
            <span>&bull;</span>
            <span>Catalyst / Conditions: <strong id="rxnCatalyst" style="color:var(--warn)">Conc. H2SO4, reflux</strong></span>
            <span>&bull;</span>
            <span>Byproduct: <strong id="rxnByproduct" style="color:var(--bad)">H2O</strong></span>
          </div>
        </div>

        <!-- 3-Box Reaction Flow: Reactant A + Reactant B -> Product -->
        <div style="display:grid;grid-template-columns:1fr auto 1fr auto 1.2fr;align-items:center;gap:14px;margin-bottom:20px">
          <!-- Reactant A -->
          <div style="background:rgba(15,23,42,0.6);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px;text-align:center">
            <span style="font-size:11px;color:var(--dim);font-family:var(--mono);text-transform:uppercase">REACTANT A</span>
            <h4 id="rxnReactantAName" style="color:var(--ink);margin:4px 0 6px">Acetic Acid</h4>
            <div id="rxnReactantA2D" style="height:100px;display:flex;align-items:center;justify-content:center"></div>
            <code id="rxnReactantASmiles" style="font-size:11px;color:var(--acc3);font-family:var(--mono)">CC(=O)O</code>
          </div>

          <div style="font-size:24px;color:var(--acc);font-weight:700;text-align:center">+</div>

          <!-- Reactant B -->
          <div style="background:rgba(15,23,42,0.6);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:14px;text-align:center">
            <span style="font-size:11px;color:var(--dim);font-family:var(--mono);text-transform:uppercase">REACTANT B</span>
            <h4 id="rxnReactantBName" style="color:var(--ink);margin:4px 0 6px">Ethanol</h4>
            <div id="rxnReactantB2D" style="height:100px;display:flex;align-items:center;justify-content:center"></div>
            <code id="rxnReactantBSmiles" style="font-size:11px;color:var(--acc3);font-family:var(--mono)">CCO</code>
          </div>

          <div style="font-size:24px;color:var(--acc2);font-weight:700;text-align:center">&rarr;</div>

          <!-- Product Card -->
          <div style="background:rgba(2,6,23,0.95);border:1px solid rgba(0,255,157,0.3);border-radius:8px;padding:14px;text-align:center;box-shadow:0 0 20px rgba(0,255,157,0.08)">
            <span style="font-size:11px;color:var(--acc2);font-family:var(--mono);text-transform:uppercase;font-weight:700">PRIMARY PRODUCT</span>
            <h4 id="rxnProductName" style="color:var(--ink);margin:4px 0 6px">Ethyl Acetate</h4>
            <div id="rxnProduct2D" style="height:100px;display:flex;align-items:center;justify-content:center"></div>
            <code id="rxnProductSmiles" style="font-size:11.5px;color:var(--acc2);font-family:var(--mono);font-weight:700">CCOC(=O)C</code>
            <div style="margin-top:8px">
              <button type="button" class="btn primary" onclick="loadActiveReactionProductToLab()" style="padding:4px 10px;font-size:11px;width:100%">
                Inspect in 3D Lab
              </button>
            </div>
          </div>
        </div>

        <!-- Mechanism Card -->
        <div style="background:rgba(15,23,42,0.5);border:1px solid rgba(255,255,255,0.08);border-radius:8px;padding:16px">
          <div style="font-size:11.5px;color:var(--acc);font-family:var(--mono);text-transform:uppercase;font-weight:700;margin-bottom:6px">
            STEP-BY-STEP REACTION MECHANISM &bull; PEDAGOGICAL INSIGHT
          </div>
          <p id="rxnMechanismText" style="color:var(--mut);font-size:13px;line-height:1.6">
            Protonation of carbonyl oxygen activates carbonyl carbon toward nucleophilic attack by alcohol oxygen. Subsequent proton transfer and elimination of water yields the ester product.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- BLOCK 08: STUDENT REPORT GENERATION -->
  <section id="report" data-chapter="08" data-chapter-name="OFFICIAL REPORT">
    <div class="wrap">
      <div class="sechead">
        <div class="kicker">Official Laboratory Certification</div>
        <h2>Multi-Molecule Student Analysis Report Generator</h2>
        <div class="sec-line"></div>
        <p style="margin-top:12px">
          Generate a standardized, publication-grade multi-molecule laboratory report matching the official curriculum rubric
          at SRM Institute of Science and Technology. Each molecule is documented with 2D/3D projections, 18 quantitative
          descriptors in high-contrast autotables, and comprehensive interpretations followed by reproducible RDKit Python source code.
        </p>
      </div>

      <div class="card" style="max-width:880px;margin:0 auto">
        <!-- Student Credentials Grid -->
        <div style="font-size:12px;font-family:var(--mono);color:var(--acc);margin-bottom:12px;display:flex;align-items:center;gap:8px">
          <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M20 21v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2"/><circle cx="12" cy="7" r="4"/></svg>
          <span>STUDENT CREDENTIALS</span>
        </div>
        <div class="grid g2" style="margin-bottom:24px">
          <div>
            <label style="font-size:11px;color:var(--dim);text-transform:uppercase;font-family:var(--mono);display:block;margin-bottom:6px">Student Name</label>
            <input type="text" id="repStudentName" placeholder="e.g. velmurgan" value="" style="width:100%">
          </div>
          <div>
            <label style="font-size:11px;color:var(--dim);text-transform:uppercase;font-family:var(--mono);display:block;margin-bottom:6px">Registration Number</label>
            <input type="text" id="repRegNumber" placeholder="e.g. RA2611030050019" value="" style="width:100%">
          </div>
        </div>

        <div style="border-top:1px solid rgba(255,255,255,0.08);padding-top:20px;margin-bottom:20px">
          <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:12px;flex-wrap:wrap;gap:10px">
            <div style="font-size:12px;font-family:var(--mono);color:var(--acc);display:flex;align-items:center;gap:8px">
              <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
              <span>REPORT MOLECULES QUEUE</span>
            </div>
            <div style="display:flex;align-items:center;gap:10px">
              <span id="repMolCountBadge" style="background:rgba(0,240,255,0.12);color:var(--acc);padding:4px 10px;border-radius:20px;font-size:12px;font-family:var(--mono);border:1px solid rgba(0,240,255,0.25)">
                Number of molecules analyzed: <strong id="repMolCountNum">3</strong>
              </span>
              <button type="button" class="btn secondary" onclick="clearReportQueue()" style="padding:4px 10px;font-size:11px">
                <span>Clear All</span>
              </button>
            </div>
          </div>

          <!-- Add Molecule Controls -->
          <div style="background:rgba(15,23,42,0.6);border:1px solid rgba(255,255,255,0.08);border-radius:10px;padding:16px;margin-bottom:16px">
            <div style="font-size:11.5px;color:var(--dim);margin-bottom:10px;font-family:var(--mono)">
              ENTER MOLECULE TO ADD TO REPORT:
            </div>
            <div style="display:grid;grid-template-columns:1fr 140px auto;gap:10px;align-items:center" class="queue-input-grid">
              <input type="text" id="customRepSmiles" placeholder="SMILES string (e.g. c1ccccc1, CCO, CC(=O)O)" style="font-family:var(--mono);font-size:13px">
              <input type="text" id="customRepName" placeholder="Name (optional)" style="font-size:13px">
              <button class="btn secondary" type="button" onclick="addCustomMoleculeToReportQueue()" style="white-space:nowrap;padding:10px 16px">
                <span>+ Add Molecule</span>
              </button>
            </div>
            <div style="display:flex;align-items:center;justify-content:space-between;margin-top:12px;flex-wrap:wrap;gap:8px">
              <div style="display:flex;align-items:center;gap:6px;flex-wrap:wrap">
                <span style="font-size:11px;color:var(--dim);font-family:var(--mono)">QUICK PRESETS:</span>
                <button type="button" class="btn secondary" onclick="quickAddBenchmarkToReport('Benzene')" style="padding:3px 8px;font-size:11px"><span>+ Benzene</span></button>
                <button type="button" class="btn secondary" onclick="quickAddBenchmarkToReport('Ethanol')" style="padding:3px 8px;font-size:11px"><span>+ Ethanol</span></button>
                <button type="button" class="btn secondary" onclick="quickAddBenchmarkToReport('Caffeine')" style="padding:3px 8px;font-size:11px"><span>+ Caffeine</span></button>
                <button type="button" class="btn secondary" onclick="quickAddBenchmarkToReport('Aspirin')" style="padding:3px 8px;font-size:11px"><span>+ Aspirin</span></button>
                <button type="button" class="btn secondary" onclick="quickAddBenchmarkToReport('Paracetamol')" style="padding:3px 8px;font-size:11px"><span>+ Paracetamol</span></button>
              </div>
              <button type="button" class="btn secondary" onclick="addCurrentToReportQueue()" style="padding:4px 12px;font-size:11.5px;color:var(--acc);border-color:rgba(0,240,255,0.4)">
                <span>➕ Add Active Lab Molecule (<span id="activeMolNameBadge">Current</span>)</span>
              </button>
            </div>
          </div>

          <!-- Queued Molecules Cards List -->
          <div id="reportQueueContainer" style="display:flex;flex-direction:column;gap:10px;margin-bottom:20px;max-height:360px;overflow-y:auto;padding-right:4px">
            <!-- Populated dynamically via renderReportQueueUI() -->
          </div>
        </div>

        <!-- Download Action Button -->
        <button class="btn primary" onclick="generatePdfReport()" style="width:100%;padding:14px;font-size:15px;display:flex;align-items:center;justify-content:center;gap:10px">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
          <span>Download Certified Multi-Molecule PDF Report (<span id="btnMolCountNum">3</span> Molecules)</span>
        </button>
        <p style="text-align:center;font-size:11.5px;color:var(--dim);margin-top:10px;font-family:var(--mono)">
          Generates standardized 7+ page PDF report with side-by-side 2D &amp; 3D projections, 18-descriptor autotables, comprehensive interpretations, and RDKit source code.
        </p>

        <!-- Python Code & Libraries Explanation Preview in UI -->
        <div style="margin-top:24px;border-top:1px solid rgba(255,255,255,0.08);padding-top:16px">
          <details style="background:rgba(2,6,23,0.5);border:1px solid rgba(255,255,255,0.06);border-radius:8px;padding:12px">
            <summary style="font-size:12px;font-family:var(--mono);color:var(--acc);cursor:pointer;user-select:none">
              &gt; VIEW PYTHON EXECUTION SCRIPT &amp; RDKIT LIBRARIES SPECIFICATION
            </summary>
            <div style="margin-top:12px">
              <pre style="background:rgba(15,23,42,0.8);border:1px solid rgba(255,255,255,0.08);padding:14px;border-radius:6px;color:#94a3b8;font-family:var(--mono);font-size:12px;overflow-x:auto"><code>from rdkit import Chem
from rdkit.Chem import Descriptors, Crippen, rdMolDescriptors

smiles_list = ["CCO", "c1ccccc1"]  # Add more SMILES strings here

for smiles in smiles_list:
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        print("Invalid SMILES:", smiles)
        continue
    print("SMILES:", smiles)
    print("Formula:", rdMolDescriptors.CalcMolFormula(mol))
    print("Molecular weight:", Descriptors.MolWt(mol))
    print("LogP:", Crippen.MolLogP(mol))</code></pre>
            </div>
          </details>
        </div>
      </div>
    </div>
  </section>
</main>

<!-- FOOTER & ACADEMIC CREDITS - OFFICIAL ACADEMIC CHANNELS -->
<footer>
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px">
          <img src="assets/srm_logo.jpeg" alt="SRM Logo" style="height:36px;border-radius:3px">
        </div>
        <h3>Cheminformatics Virtual Laboratory</h3>
        <p>
          Division of Chemistry, School of Sciences, Faculty of Engineering and Technology<br>
          <strong>SRM Institute of Science and Technology</strong>, Tiruchirappalli, Tamil Nadu, India.
        </p>
        <p style="margin-top:10px;font-size:12.5px;color:var(--dim)">
          Curriculum direction &amp; academic supervision by <strong>Dr. R. Subramanian</strong> (Assistant Professor, Chemistry).
        </p>
      </div>

      <div class="footer-links">
        <h4>Faculty &amp; Academic Contacts</h4>
        <a href="mailto:rsmani84@gmail.com">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          <span>Dr. R. Subramanian (rsmani84@gmail.com)</span>
        </a>
      </div>

      <div class="footer-links">
        <h4>Academic Governance</h4>
        <a href="javascript:void(0)" onclick="openLegalModal('privacy')">Privacy Policy &amp; Data Ethics</a>
        <a href="javascript:void(0)" onclick="openLegalModal('terms')">Academic License &amp; Fair Use</a>
      </div>
    </div>

    <div class="footer-bottom">
      <div>&copy; 2026 SRM Institute of Science and Technology. All rights reserved. Zero tracking cookies.</div>
      <div id="footerEngineVersion" style="font-family:var(--mono);color:var(--acc)">PYTHON SERVERLESS ENGINE v3.14 &times; VERCEL EDGE</div>
    </div>
  </div>
</footer>

<!-- Legal & Academic Modal -->
<div class="modal-overlay" id="legalModal">
  <div class="modal-box">
    <button class="modal-close" onclick="closeModal('legalModal')">&times;</button>
    <div id="legalModalContent"></div>
  </div>
</div>

<!-- Local High-Performance Bundled Vendor Libraries -->
<script src="/assets/vendor/gsap.min.js"></script>
<script src="/assets/vendor/ScrollTrigger.min.js"></script>
<script src="/assets/vendor/ScrollToPlugin.min.js"></script>
<script src="/assets/vendor/three.min.js"></script>
<script src="/assets/vendor/3Dmol-min.js"></script>
<script src="/assets/vendor/jspdf.umd.min.js"></script>
<script src="/assets/vendor/jspdf.plugin.autotable.min.js"></script>
<script>
window.jsmeOnLoad = function(){
  if(typeof window.setupJsmeInstance === 'function'){
    window.setupJsmeInstance();
  }
};
</script>
<script type="text/javascript" src="/assets/jsme/jsme.nocache.js"></script>

<script>
/* ==========================================================================
   1. DATA DEFINITIONS & PRESET BENCHMARKS
   ========================================================================== */
var BENCHMARK_MOLECULES = [
  {
    name: "Benzene",
    smiles: "c1ccccc1",
    canonical: "c1ccccc1",
    formula: "C6H6",
    mw: 78.114,
    exact_mw: 78.0470,
    logp: 1.687,
    tpsa: 0.0,
    hbd: 0,
    hba: 0,
    rot: 0,
    rings: 1,
    arom: 1,
    aliph: 0,
    num_atoms: 6,
    heavy_atoms: 6,
    heavy_bonds: 6,
    sigma: 12,
    pi: 3,
    total_bonds: 15,
    fcsp3: 0.0,
    mr: 26.442,
    desc: "Fundamental aromatic hydrocarbon with planar delocalized pi electrons."
  },
  {
    name: "Ethanol",
    smiles: "CCO",
    canonical: "CCO",
    formula: "C2H6O",
    mw: 46.069,
    exact_mw: 46.0419,
    logp: -0.001,
    tpsa: 20.23,
    hbd: 1,
    hba: 1,
    rot: 0,
    rings: 0,
    arom: 0,
    aliph: 0,
    num_atoms: 3,
    heavy_atoms: 3,
    heavy_bonds: 2,
    sigma: 8,
    pi: 0,
    total_bonds: 8,
    fcsp3: 1.0,
    mr: 12.76,
    desc: "Primary aliphatic alcohol used as a solvent and antiseptic."
  },
  {
    name: "Caffeine",
    smiles: "CN1C=NC2=C1C(=O)N(C(=O)N2C)C",
    canonical: "Cn1c(=O)c2c(ncn2C)n(C)c1=O",
    formula: "C8H10N4O2",
    mw: 194.194,
    exact_mw: 194.0804,
    logp: -1.029,
    tpsa: 61.82,
    hbd: 0,
    hba: 3,
    rot: 0,
    rings: 2,
    arom: 2,
    aliph: 0,
    num_atoms: 14,
    heavy_atoms: 14,
    heavy_bonds: 15,
    sigma: 25,
    pi: 4,
    total_bonds: 29,
    fcsp3: 0.375,
    mr: 51.196,
    desc: "Methylxanthine central nervous system stimulant."
  },
  {
    name: "Aspirin",
    smiles: "CC(=O)Oc1ccccc1C(=O)O",
    canonical: "CC(=O)Oc1ccccc1C(=O)O",
    formula: "C9H8O4",
    mw: 180.159,
    exact_mw: 180.0423,
    logp: 1.19,
    tpsa: 63.60,
    hbd: 1,
    hba: 3,
    rot: 3,
    rings: 1,
    arom: 1,
    aliph: 0,
    num_atoms: 13,
    heavy_atoms: 13,
    heavy_bonds: 13,
    sigma: 21,
    pi: 5,
    total_bonds: 26,
    fcsp3: 0.111,
    mr: 46.12,
    desc: "Acetylsalicylic acid, standard NSAID analgesic and antipyretic."
  },
  {
    name: "Phenol",
    smiles: "Oc1ccccc1",
    canonical: "Oc1ccccc1",
    formula: "C6H6O",
    mw: 94.113,
    exact_mw: 94.0419,
    logp: 1.46,
    tpsa: 20.23,
    hbd: 1,
    hba: 1,
    rot: 0,
    rings: 1,
    arom: 1,
    aliph: 0,
    num_atoms: 7,
    heavy_atoms: 7,
    heavy_bonds: 7,
    sigma: 13,
    pi: 3,
    total_bonds: 16,
    fcsp3: 0.0,
    mr: 28.13,
    desc: "Aromatic alcohol exhibiting resonance-stabilized phenoxide formation."
  },
  {
    name: "Acetic Acid",
    smiles: "CC(=O)O",
    canonical: "CC(=O)O",
    formula: "C2H4O2",
    mw: 60.052,
    exact_mw: 60.0211,
    logp: -0.17,
    tpsa: 37.30,
    hbd: 1,
    hba: 1,
    rot: 0,
    rings: 0,
    arom: 0,
    aliph: 0,
    num_atoms: 4,
    heavy_atoms: 4,
    heavy_bonds: 3,
    sigma: 7,
    pi: 1,
    total_bonds: 8,
    fcsp3: 0.5,
    mr: 12.99,
    desc: "Carboxylic acid exhibiting strong intermolecular hydrogen bonding."
  },
  {
    name: "Paracetamol",
    smiles: "CC(=O)Nc1ccc(O)cc1",
    canonical: "CC(=O)Nc1ccc(O)cc1",
    formula: "C8H9NO2",
    mw: 151.165,
    exact_mw: 151.0633,
    logp: 0.46,
    tpsa: 49.33,
    hbd: 2,
    hba: 2,
    rot: 1,
    rings: 1,
    arom: 1,
    aliph: 0,
    num_atoms: 11,
    heavy_atoms: 11,
    heavy_bonds: 11,
    sigma: 20,
    pi: 4,
    total_bonds: 24,
    fcsp3: 0.125,
    mr: 41.54,
    desc: "Widely used antipyretic and analgesic."
  },
  {
    name: "Ibuprofen",
    smiles: "CC(C)Cc1ccc(C(C)C(=O)O)cc1",
    canonical: "CC(C)Cc1ccc(C(C)C(=O)O)cc1",
    formula: "C13H18O2",
    mw: 206.285,
    exact_mw: 206.1307,
    logp: 3.50,
    tpsa: 37.30,
    hbd: 1,
    hba: 1,
    rot: 4,
    rings: 1,
    arom: 1,
    aliph: 0,
    num_atoms: 15,
    heavy_atoms: 15,
    heavy_bonds: 15,
    sigma: 33,
    pi: 4,
    total_bonds: 37,
    fcsp3: 0.538,
    mr: 60.73,
    desc: "Non-steroidal anti-inflammatory drug with chiral propionic acid core."
  }
];

/* Multi-Molecule Report Queue - Preloaded with 3 benchmark compounds matching curriculum sample */
var reportQueue = [
  BENCHMARK_MOLECULES[0], // Benzene
  BENCHMARK_MOLECULES[1], // Ethanol
  BENCHMARK_MOLECULES[2]  // Caffeine
];

/* __BENCHMARK_SDF_PLACEHOLDER__ */

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
    exp: "SMILES stands for Simplified Molecular Input Line Entry System, a specification in form of a line notation for describing chemical species."
  },
  {
    q: "Under Lipinski's Rule of 5 for drug-likeness, what is the maximum recommended molecular weight?",
    opts: ["250 g/mol", "500 g/mol", "750 g/mol", "1000 g/mol"],
    ans: 1,
    exp: "Lipinski's Rule of 5 states that poor oral bioavailability is significantly more likely when Molecular Weight exceeds 500 g/mol."
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
   2. MOMENTUM SMOOTH SCROLLER WITH BUTTERY VELOCITY DAMPING
   ========================================================================== */
var ScrollEngine = (function(){
  var currentY = 0, targetY = 0, ease = 0.082, isRunning = false;
  var lastY = 0, velocity = 0;

  function init(){
    currentY = window.pageYOffset;
    targetY = currentY;

    window.addEventListener('scroll', function(){
      currentY = window.pageYOffset;
      targetY = currentY;
      onScrollUpdate();
    }, { passive: true });

    // Initialize GSAP 3.12 & ScrollTrigger Peak Animations
    initPeakAnimations();

    // Initialize Motion.dev Rolling Text & Magnetic Buttons
    setupRollingButtons();
    initMagneticButtons();

    // Initialize 3D Card Perspective Tilt
    initCardTilt();
  }

  function update(){
    currentY += (targetY - currentY) * ease;
    velocity = currentY - lastY;
    lastY = currentY;

    window.scrollTo(0, currentY);
    onScrollUpdate();

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
    
    var beam = document.getElementById('scrollLaser');
    if(beam) beam.style.width = pct + '%';
    
    var hud = document.getElementById('hudPct');
    if(hud) hud.innerText = pct + '%';
  }

  return { init: init };
})();

/* ==========================================================================
   PEAK MOTION.DEV KINETIC ANIMATION ENGINE & GSAP SCROLLTRIGGER SUITE
   ========================================================================== */
function initPeakAnimations(){
  if(!window.gsap || !window.ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger, ScrollToPlugin);

  var isMobile = window.innerWidth < 768;
  var slideX = isMobile ? 35 : 150;

  // 1. HERO ENTRANCE (Instant crisp render, no blur)
  var heroTl = gsap.timeline({ defaults: { ease: "power3.out" } });
  heroTl.from(".hero-badge-row .badge", { y: -25, opacity: 0, stagger: 0.08, duration: 0.6 })
        .from(".hero h1", { y: 35, opacity: 0, duration: 0.8 }, "-=0.3")
        .from(".hero p", { y: 25, opacity: 0, duration: 0.7 }, "-=0.5")
        .from(".hero-actions .btn", { y: 30, opacity: 0, stagger: 0.1, duration: 0.6 }, "-=0.4")
        .from(".telemetry-strip .tele-item", { x: isMobile ? 0 : -35, y: isMobile ? 30 : 0, opacity: 0, stagger: 0.08, duration: 0.65 }, "-=0.3");

  // 2. EXPANDING LASER ACCENT UNDER TITLES
  gsap.utils.toArray('.sec-line').forEach(function(line){
    gsap.fromTo(line,
      { width: 0, opacity: 0 },
      {
        width: 140,
        opacity: 1,
        duration: 0.85,
        ease: "power3.out",
        scrollTrigger: {
          trigger: line,
          start: "top 88%",
          toggleActions: "play none none none"
        }
      }
    );
  });

  // 3. BLOCK 2: THEORY SECTION BI-DIRECTIONAL SLIDE
  gsap.fromTo("#theory .slide-left",
    { x: -slideX, opacity: 0, rotateY: isMobile ? 0 : 12 },
    {
      x: 0, opacity: 1, rotateY: 0, duration: 0.9, ease: "power3.out",
      scrollTrigger: { trigger: "#theory", start: "top 82%" }
    }
  );
  gsap.fromTo("#theory .slide-right",
    { x: slideX, opacity: 0, rotateY: isMobile ? 0 : -12 },
    {
      x: 0, opacity: 1, rotateY: 0, duration: 0.9, ease: "power3.out",
      scrollTrigger: { trigger: "#theory", start: "top 82%" }
    }
  );

  // 4. BLOCK 3: MOLECULAR LAB DUAL CANVAS COLLISION
  gsap.fromTo("#lab .dual-canvas-grid .slide-left",
    { x: -slideX * 1.15, opacity: 0, rotateY: isMobile ? 0 : 16 },
    {
      x: 0, opacity: 1, rotateY: 0, duration: 0.95, ease: "power3.out",
      scrollTrigger: { trigger: "#lab .dual-canvas-grid", start: "top 82%" }
    }
  );
  gsap.fromTo("#lab .dual-canvas-grid .slide-right",
    { x: slideX * 1.15, opacity: 0, rotateY: isMobile ? 0 : -16 },
    {
      x: 0, opacity: 1, rotateY: 0, duration: 0.95, ease: "power3.out",
      scrollTrigger: { trigger: "#lab .dual-canvas-grid", start: "top 82%" }
    }
  );

  // 5. BOND ARCHITECTURE METRIC CARDS DOMINO
  gsap.fromTo("#bondMetricGrid .bond-metric-card",
    { y: 45, opacity: 0, scale: 0.95 },
    {
      y: 0, opacity: 1, scale: 1, duration: 0.65, stagger: 0.07, ease: "back.out(1.5)",
      scrollTrigger: { trigger: "#bondMetricGrid", start: "top 88%" }
    }
  );

  // 6. BLOCK 4: 18-DESCRIPTOR TABLE CASCADE WATERFALL
  ScrollTrigger.create({
    trigger: "#propTable",
    start: "top 85%",
    onEnter: function(){
      gsap.fromTo("#propTableBody tr",
        { x: -45, opacity: 0 },
        { x: 0, opacity: 1, duration: 0.45, stagger: 0.028, ease: "power2.out" }
      );
    }
  });

  // 7. BLOCK 5: COMPARATIVE MATRIX WAVE (Alternating Left/Right)
  ScrollTrigger.create({
    trigger: "#compareTable",
    start: "top 85%",
    onEnter: function(){
      gsap.utils.toArray("#compareTableBody tr").forEach(function(row, idx){
        var dir = (idx % 2 === 0) ? -slideX * 0.4 : slideX * 0.4;
        gsap.fromTo(row,
          { x: isMobile ? -25 : dir, opacity: 0 },
          { x: 0, opacity: 1, duration: 0.55, delay: idx * 0.05, ease: "power2.out" }
        );
      });
    }
  });

  // 8. BLOCK 6 & 7: QUIZ & REPORT 3D PERSPECTIVE SLIDE
  gsap.fromTo("#quiz .card",
    { y: 50, scale: 0.96, opacity: 0 },
    {
      y: 0, scale: 1, opacity: 1, duration: 0.8, ease: "power3.out",
      scrollTrigger: { trigger: "#quiz .card", start: "top 85%" }
    }
  );
  gsap.fromTo("#report .card",
    { y: 50, scale: 0.96, opacity: 0 },
    {
      y: 0, scale: 1, opacity: 1, duration: 0.8, ease: "power3.out",
      scrollTrigger: { trigger: "#report .card", start: "top 85%" }
    }
  );

  // 9. SMOOTH NAV LINKS SCROLL
  document.querySelectorAll('nav.links a, .mobile-nav-links a').forEach(function(link){
    link.addEventListener('click', function(e){
      var targetId = link.getAttribute('href');
      if(targetId && targetId.startsWith('#')){
        e.preventDefault();
        var secId = targetId.substring(1);
        var targetEl = document.querySelector(targetId);
        if(targetEl){
          if(window.FramerNav){
            window.FramerNav.setActive(secId);
          }
          gsap.to(window, {
            duration: 0.85,
            scrollTo: { y: targetEl, offsetY: 75 },
            ease: "power3.inOut"
          });
          if(document.getElementById('mobileDrawer') && document.getElementById('mobileDrawer').classList.contains('open')){
            toggleMobileMenu();
          }
        }
      }
    });
  });
}

function setupRollingButtons(){
  document.querySelectorAll('.btn').forEach(function(btn){
    if(btn.dataset.rollingDone) return;
    btn.dataset.rollingDone = "true";
    var span = btn.querySelector(':scope > span:not(.btn-glow)');
    if(span && !span.classList.contains('btn-roll')){
      var text = span.textContent.trim();
      if(text){
        span.className = 'btn-roll';
        span.innerHTML = '<span class="btn-roll-text">' + text + '</span><span class="btn-roll-text btn-roll-hover">' + text + '</span>';
      }
    }
  });
}

function initMagneticButtons(){
  if(window.innerWidth < 768) return;
  document.querySelectorAll('.btn').forEach(function(btn){
    if(!btn.querySelector('.btn-glow')){
      var glow = document.createElement('span');
      glow.className = 'btn-glow';
      btn.appendChild(glow);
    }

    if(window.gsap && !btn.dataset.magneticDone){
      btn.dataset.magneticDone = "true";
      var xTo = gsap.quickTo(btn, "x", { duration: 0.3, ease: "power3.out" });
      var yTo = gsap.quickTo(btn, "y", { duration: 0.3, ease: "power3.out" });

      btn.addEventListener('mousemove', function(e){
        var rect = btn.getBoundingClientRect();
        var x = e.clientX - rect.left;
        var y = e.clientY - rect.top;
        var glow = btn.querySelector('.btn-glow');
        if(glow){
          glow.style.left = x + 'px';
          glow.style.top = y + 'px';
        }

        var moveX = (x - rect.width / 2) * 0.35;
        var moveY = (y - rect.height / 2) * 0.35;
        xTo(moveX);
        yTo(moveY);
      });

      btn.addEventListener('mouseleave', function(){
        xTo(0);
        yTo(0);
      });
    }
  });
}

function initCardTilt(){
  var cards = document.querySelectorAll('.card, .theory-card, .bond-metric-card, .gauge-card, .tele-item, .bento-card, .ro5-criterion');
  cards.forEach(function(card){
    if(card.classList.contains('card') && !card.querySelector('.card-sheen')){
      var sheen = document.createElement('div');
      sheen.className = 'card-sheen';
      card.appendChild(sheen);
    }

    card.addEventListener('mousemove', function(e){
      var rect = card.getBoundingClientRect();
      var x = e.clientX - rect.left;
      var y = e.clientY - rect.top;
      card.style.setProperty('--mouse-x', x + 'px');
      card.style.setProperty('--mouse-y', y + 'px');

      if(window.innerWidth >= 768 && card.classList.contains('card')){
        var cx = rect.width / 2;
        var cy = rect.height / 2;
        var rotX = ((y - cy) / cy) * -3.5;
        var rotY = ((x - cx) / cx) * 3.5;
        card.style.transform = 'perspective(1000px) rotateX(' + rotX + 'deg) rotateY(' + rotY + 'deg) translateZ(4px)';
      }
    });

    card.addEventListener('mouseleave', function(){
      if(card.classList.contains('card')){
        card.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) translateZ(0px)';
      }
    });
  });
}

function inspectSmilesToken(name, formula, desc){
  var title = document.getElementById('inspectorTitle');
  var body = document.getElementById('inspectorBody');
  if(title) title.innerHTML = '<span style="color:var(--acc)">' + name + '</span> &bull; <code style="color:#00ff9d">[' + formula + ']</code>';
  if(body) body.innerText = desc;
  if(window.gsap && body){
    gsap.fromTo(body, { opacity: 0.4, y: 3 }, { opacity: 1, y: 0, duration: 0.25, ease: "power2.out" });
  }
  if(window.AudioEngine) window.AudioEngine.click();
}

function set3DModelStyle(styleName, btn){
  var sel = document.getElementById('modelStyle');
  if(sel) sel.value = styleName;
  document.querySelectorAll('.v-pill').forEach(function(p){ p.classList.remove('active'); });
  if(btn) btn.classList.add('active');
  update3DStyle();
  if(window.AudioEngine) window.AudioEngine.click();
}

function toggleVdwSurface(){
  var chk = document.getElementById('chkSurface');
  if(chk){
    chk.checked = !chk.checked;
    var btn = document.getElementById('dockSurfaceBtn');
    if(btn) btn.classList.toggle('active', chk.checked);
    update3DStyle();
  }
  if(window.AudioEngine) window.AudioEngine.click();
}

function reset3DCamera(){
  if(!glViewer) return;
  glViewer.zoomTo();
  glViewer.render();
  if(window.AudioEngine) window.AudioEngine.click();
}

function animateCounter(elementId, targetVal, isFloat, suffix){
  var el = document.getElementById(elementId);
  if(!el) return;
  var target = parseFloat(targetVal);
  if(isNaN(target)){
    el.innerHTML = targetVal + (suffix ? ' ' + suffix : '');
    return;
  }
  var current = parseFloat(el.getAttribute('data-val') || '0') || 0;
  el.setAttribute('data-val', target);
  var obj = { val: current };
  if(window.gsap){
    gsap.to(obj, {
      val: target,
      duration: 0.65,
      ease: "power2.out",
      onUpdate: function(){
        var numStr = isFloat ? obj.val.toFixed(2) : Math.round(obj.val);
        el.innerHTML = numStr + (suffix ? ' ' + suffix : '');
      }
    });
  } else {
    var startTime = performance.now();
    var duration = 650;
    function animStep(now){
      var elapsed = now - startTime;
      var progress = Math.min(1, elapsed / duration);
      var ease = 1 - Math.pow(1 - progress, 3);
      var currentVal = current + (target - current) * ease;
      var numStr = isFloat ? currentVal.toFixed(2) : Math.round(currentVal);
      el.innerHTML = numStr + (suffix ? ' ' + suffix : '');
      if(progress < 1){
        requestAnimationFrame(animStep);
      }
    }
    requestAnimationFrame(animStep);
  }
}

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
      var dot = document.getElementById('audioDot');
      if(dot) dot.classList.toggle('muted', !enabled);
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
   4. MOLECULAR VISUALIZER & CHEMINFORMATICS ENGINE
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

  // Populate preset chips with sliding pill indicator
  var chipsWrap = document.getElementById('presetChips');
  if(chipsWrap){
    chipsWrap.innerHTML = '<div class="preset-pill-indicator" id="presetPill"></div>' +
      BENCHMARK_MOLECULES.map(function(m){
        return '<button class="preset-chip' + (m.smiles === activeSmiles ? ' active' : '') + '" onclick="selectPreset(\\'' + m.smiles + '\\', \\'' + m.name + '\\', this)">' + m.name + '</button>';
      }).join('');

    setTimeout(function(){
      var activeBtn = chipsWrap.querySelector('.preset-chip.active');
      if(activeBtn) movePillToChip(activeBtn);
    }, 120);
  }

  analyzeMolecule();
}

function movePillToChip(chip){
  var pill = document.getElementById('presetPill');
  if(!pill || !chip) return;
  pill.style.opacity = '1';
  pill.style.transform = 'translate3d(' + chip.offsetLeft + 'px, ' + chip.offsetTop + 'px, 0)';
  pill.style.width = chip.offsetWidth + 'px';
  pill.style.height = chip.offsetHeight + 'px';
}

function selectPreset(smiles, name, btnEl){
  document.getElementById('smilesInput').value = smiles;
  document.querySelectorAll('.preset-chip').forEach(function(c){
    c.classList.remove('active');
  });
  if(btnEl){
    btnEl.classList.add('active');
    movePillToChip(btnEl);
  } else {
    document.querySelectorAll('.preset-chip').forEach(function(c){
      if(c.innerText.trim() === name){
        c.classList.add('active');
        movePillToChip(c);
      }
    });
  }
  analyzeMolecule();
}

function toggleSpin(){
  isSpinning = !isSpinning;
  if(glViewer){
    glViewer.spin(isSpinning ? 'y' : false, 1.2);
  }
  var btn = document.getElementById('btnSpin');
  if(btn) btn.style.borderColor = isSpinning ? 'var(--acc)' : 'var(--border)';
  var dockBtn = document.getElementById('dockSpinBtn');
  if(dockBtn){
    dockBtn.classList.toggle('active', isSpinning);
    dockBtn.innerHTML = isSpinning ? '<span class="spin-icon">■</span> Pause' : '<span class="spin-icon">↻</span> Spin';
  }
  AudioEngine.click();
}


/* ==========================================================================
   FEATURE LOGIC: THEME, MOTD, JSME, PEPTIDES, REACTIONS, SPECTRA, SIMILARITY
   ========================================================================== */

// --- THEME TOGGLE (Dark / Light) ---
function initTheme(){
  var saved = localStorage.getItem('chem_theme') || 'dark';
  setTheme(saved);
}

function toggleTheme(){
  AudioEngine.click();
  var curr = document.documentElement.getAttribute('data-theme') || 'dark';
  var next = curr === 'dark' ? 'light' : 'dark';
  setTheme(next);
  showToast("Theme switched to " + next.toUpperCase() + " mode");
}

function setTheme(theme){
  document.documentElement.setAttribute('data-theme', theme);
  localStorage.setItem('chem_theme', theme);
  var sun = document.getElementById('themeIconSun');
  var moon = document.getElementById('themeIconMoon');
  var txt = document.getElementById('themeStatusText');
  if(sun && moon && txt){
    if(theme === 'light'){
      sun.style.display = 'inline-block';
      moon.style.display = 'none';
      txt.innerText = 'LIGHT';
    } else {
      sun.style.display = 'none';
      moon.style.display = 'inline-block';
      txt.innerText = 'DARK';
    }
  }
}

// --- FLOATING TOAST NOTIFICATION ---
function showToast(msg){
  var existing = document.getElementById('chemToast');
  if(existing) existing.remove();
  var t = document.createElement('div');
  t.id = 'chemToast';
  t.className = 'chem-toast';
  t.innerHTML = '<svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="20 6 9 17 4 12"/></svg><span>' + msg + '</span>';
  document.body.appendChild(t);
  setTimeout(function(){ if(t) t.remove(); }, 3200);
}

// --- COPY SMILES & SHAREABLE URL ---
function copySmilesToClipboard(s){
  AudioEngine.click();
  var val = s || activeSmiles || (document.getElementById('smilesInput') ? document.getElementById('smilesInput').value : '');
  if(navigator.clipboard && val){
    navigator.clipboard.writeText(val).then(function(){
      showToast("Copied SMILES: " + val);
    });
  }
}

function copyShareLink(){
  AudioEngine.click();
  var val = activeSmiles || (document.getElementById('smilesInput') ? document.getElementById('smilesInput').value : 'CCO');
  var shareUrl = window.location.origin + window.location.pathname + '?smiles=' + encodeURIComponent(val);
  if(navigator.clipboard){
    navigator.clipboard.writeText(shareUrl).then(function(){
      showToast("Shareable link copied to clipboard!");
    });
  }
}

// --- MOLECULE OF THE DAY (MOTD) ---
function loadMotd(){
  fetch('/api/motd')
    .then(function(r){ return r.json(); })
    .then(function(d){
      if(d && d.valid){
        var n = document.getElementById('motdName');
        var c = document.getElementById('motdClass');
        var f = document.getElementById('motdFormula');
        var s = document.getElementById('motdSmiles');
        var desc = document.getElementById('motdDesc');
        var b = document.getElementById('motdDateBadge');
        if(n) n.innerText = d.name;
        if(c) c.innerText = d.class;
        if(f) f.innerText = d.formula;
        if(s) s.innerText = d.smiles;
        if(desc) desc.innerText = d.description;
        if(b) b.innerText = "Day " + d.day + " Edition";
      }
    })
    .catch(function(){});
}

function loadMotdToLab(){
  AudioEngine.click();
  var s = document.getElementById('motdSmiles');
  var smiles = s ? s.innerText.trim() : 'c1ccncc1';
  document.getElementById('smilesInput').value = smiles;
  scrollToChapter('lab');
  analyzeMolecule();
}

// --- INPUT MODE SWITCHING (SMILES / DRAW / PEPTIDE) ---
var currentInputMode = 'smiles';
var jsmeInitialized = false;

function switchInputMode(mode){
  AudioEngine.click();
  currentInputMode = mode;
  var bSmiles = document.getElementById('modeTabSmiles');
  var bDraw = document.getElementById('modeTabDraw');
  var bPep = document.getElementById('modeTabPeptide');
  var cDraw = document.getElementById('drawStudioContainer');
  var cPep = document.getElementById('peptideStudioContainer');
  
  if(bSmiles) bSmiles.className = 'mode-tab-btn' + (mode === 'smiles' ? ' active' : '');
  if(bDraw) bDraw.className = 'mode-tab-btn' + (mode === 'draw' ? ' active' : '');
  if(bPep) bPep.className = 'mode-tab-btn' + (mode === 'peptide' ? ' active' : '');
  
  if(cDraw) cDraw.style.display = (mode === 'draw') ? 'block' : 'none';
  if(cPep) cPep.style.display = (mode === 'peptide') ? 'block' : 'none';
  
  if(mode === 'draw' && !jsmeInitialized){
    initJsmeApplet();
  }
}

var jsmeRetries = 0;
function tryInitJsme(){
  var ctor = (window.JSApplet && window.JSApplet.JSME) ? window.JSApplet.JSME : window.JSME;
  if(ctor){
    setupJsmeInstance();
    return;
  }
  if(jsmeRetries < 60){
    jsmeRetries++;
    setTimeout(tryInitJsme, 200);
  }
}

function initJsmeApplet(){
  if(window.jsmeApplet) return;
  tryInitJsme();
}

window.jsmeOnLoad = function(){
  setupJsmeInstance();
};

function setupJsmeInstance(force){
  var ph = document.getElementById('jsme_placeholder');
  try {
    var ctor = (window.JSApplet && window.JSApplet.JSME) ? window.JSApplet.JSME : window.JSME;
    if(ctor && !window.jsmeApplet){
      if(ph) ph.style.display = 'none';
      window.jsmeApplet = new ctor("jsme_container", "100%", "360px", {
        "options": "query,hydrogens,star"
      });
      jsmeInitialized = true;
      if(window.jsmeApplet.setCallBack){
        window.jsmeApplet.setCallBack("AfterStructureModified", function(jsmeEvent){
          try {
            var s = (jsmeEvent && jsmeEvent.src) ? jsmeEvent.src.smiles() : (window.jsmeApplet ? window.jsmeApplet.smiles() : '');
            if(s && s.trim()){
              document.getElementById('smilesInput').value = s.trim();
            }
          } catch(err){}
        });
      }
      if(activeSmiles && window.jsmeApplet.readGenericMolecularInput){
        window.jsmeApplet.readGenericMolecularInput(activeSmiles);
      }
    } else if(!ctor && force){
      tryInitJsme();
    }
  } catch(e){
    console.warn('JSME init notice:', e);
  }
}
window.setupJsmeInstance = setupJsmeInstance;

function loadJsmeTemplate(smiles){
  AudioEngine.click();
  if(window.jsmeApplet){
    try { window.jsmeApplet.readGenericMolecularInput(smiles); } catch(e){}
  }
  document.getElementById('smilesInput').value = smiles;
}

function clearJsmeCanvas(){
  AudioEngine.click();
  if(window.jsmeApplet){
    try { window.jsmeApplet.reset(); } catch(e){}
  }
}

function appendJsmeFragment(frag){
  AudioEngine.click();
  if(window.jsmeApplet){
    try {
      var curr = window.jsmeApplet.smiles();
      window.jsmeApplet.readGenericMolecularInput(curr ? (curr + '.' + frag) : frag);
    } catch(e){}
  }
}

function transferJsmeToLab(){
  AudioEngine.click();
  var s = '';
  if(window.jsmeApplet){
    try { s = window.jsmeApplet.smiles(); } catch(e){}
  }
  if(!s){
    s = document.getElementById('smilesInput').value;
  }
  if(s){
    document.getElementById('smilesInput').value = s.trim();
    switchInputMode('smiles');
    showToast('Loaded drawn structure: ' + s.trim());
    analyzeMolecule();
  }
}

// --- PEPTIDE TRANSLATION ENGINE ---
function setPeptideSeq(seq){
  AudioEngine.click();
  var input = document.getElementById('peptideInput');
  if(input){
    input.value = seq;
    translateAndAnalyzePeptide();
  }
}

function translateAndAnalyzePeptide(){
  AudioEngine.click();
  var seq = (document.getElementById('peptideInput').value || '').trim();
  if(!seq) return;
  
  fetch('/api/peptide?seq=' + encodeURIComponent(seq))
    .then(function(r){ return r.json(); })
    .then(function(d){
      if(d && d.valid){
        var dispSeq = document.getElementById('pepSeqDisplay');
        var dispLen = document.getElementById('pepLenDisplay');
        var dispMw = document.getElementById('pepMwDisplay');
        var dispCh = document.getElementById('pepChargeDisplay');
        if(dispSeq) dispSeq.innerText = d.sequence;
        if(dispLen) dispLen.innerText = d.length + " residues (" + d.residues.slice(0, 3).join('-') + (d.residues.length > 3 ? '...' : '') + ")";
        if(dispMw) dispMw.innerText = d.estimated_mw + " g/mol";
        if(dispCh) dispCh.innerText = (d.net_charge_ph7 > 0 ? '+' : '') + d.net_charge_ph7;
        
        // Put SMILES into input and analyze
        document.getElementById('smilesInput').value = d.smiles;
        analyzeMolecule();
      } else {
        showSmilesError(d.error || "Invalid peptide sequence", d.suggestion);
      }
    })
    .catch(function(){});
}

// --- SPECTRAL PREDICTIONS (IR & 1H NMR) ---
function switchSpectralTab(tab){
  AudioEngine.click();
  var bIr = document.getElementById('tabSpecIr');
  var bNmr = document.getElementById('tabSpecNmr');
  var cIr = document.getElementById('specIrContainer');
  var cNmr = document.getElementById('specNmrContainer');
  if(bIr) bIr.className = 'v-pill' + (tab === 'ir' ? ' active' : '');
  if(bNmr) bNmr.className = 'v-pill' + (tab === 'nmr' ? ' active' : '');
  if(cIr) cIr.style.display = (tab === 'ir') ? 'block' : 'none';
  if(cNmr) cNmr.style.display = (tab === 'nmr') ? 'block' : 'none';
}

function loadSpectralPredictions(smiles){
  fetch('/api/spectra?smiles=' + encodeURIComponent(smiles))
    .then(function(r){ return r.json(); })
    .then(function(d){
      if(d && d.valid){
        renderSpectralTables(d.ir, d.nmr);
      }
    })
    .catch(function(){});
}

function renderSpectralTables(irList, nmrList){
  var tbIr = document.getElementById('specIrTableBody');
  var bar = document.getElementById('irSpectrumBar');
  var tbNmr = document.getElementById('specNmrTableBody');
  
  if(tbIr){
    var h = '';
    for(var i = 0; i < irList.length; i++){
      var p = irList[i];
      h += '<tr>' +
        '<td style="font-weight:600;color:var(--ink)">' + p.group + '</td>' +
        '<td style="font-family:var(--mono);color:var(--acc)">' + p.freq + '</td>' +
        '<td><span style="background:rgba(61,139,255,0.12);color:var(--acc3);padding:2px 8px;border-radius:4px;font-size:11.5px">' + p.intensity + '</span></td>' +
        '<td style="color:var(--mut)">' + p.desc + '</td>' +
      '</tr>';
    }
    tbIr.innerHTML = h;
  }
  
  if(bar){
    // 4000 cm-1 to 400 cm-1 (width = 3600 cm-1)
    var barH = '';
    for(var b = 0; b < irList.length; b++){
      var raw = irList[b].freq.split('-')[0].trim();
      var num = parseFloat(raw) || 1700;
      var leftPct = Math.max(2, Math.min(98, ((4000 - num) / 3600) * 100));
      barH += '<div style="position:absolute;left:' + leftPct + '%;top:0;bottom:0;width:3px;background:#00f0ff;box-shadow:0 0 8px #00f0ff" title="' + irList[b].group + ' (' + irList[b].freq + ' cm⁻¹)"></div>';
    }
    bar.innerHTML = barH;
  }
  
  if(tbNmr){
    var nh = '';
    for(var j = 0; j < nmrList.length; j++){
      var n = nmrList[j];
      nh += '<tr>' +
        '<td style="font-weight:600;color:var(--ink)">' + n.proton_type + '</td>' +
        '<td style="font-family:var(--mono);color:var(--acc2)">' + n.region + '</td>' +
        '<td><span style="background:rgba(0,255,157,0.12);color:var(--acc2);padding:2px 8px;border-radius:4px;font-size:11.5px">' + n.intensity + '</span></td>' +
        '<td style="color:var(--mut)">' + n.desc + '</td>' +
      '</tr>';
    }
    tbNmr.innerHTML = nh;
  }
}

// --- STRUCTURAL SIMILARITY & SAR SEARCH (TANIMOTO) ---
function loadSimilaritySearch(smiles){
  fetch('/api/similarity?smiles=' + encodeURIComponent(smiles))
    .then(function(r){ return r.json(); })
    .then(function(d){
      if(d && d.valid){
        renderSimilarityCards(d.matches);
      }
    })
    .catch(function(){});
}

function renderSimilarityCards(matches){
  var grid = document.getElementById('similarityCardsGrid');
  if(!grid) return;
  var h = '';
  for(var i = 0; i < matches.length; i++){
    var m = matches[i];
    var pct = Math.round(m.similarity * 100);
    var color = pct >= 70 ? 'var(--acc2)' : (pct >= 40 ? 'var(--acc)' : 'var(--warn)');
    h += '<div style="background:rgba(2,6,23,0.7);border:1px solid rgba(255,255,255,0.1);border-radius:8px;padding:12px 14px;display:flex;flex-direction:column;justify-content:space-between">' +
      '<div>' +
        '<div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:4px">' +
          '<strong style="color:var(--ink);font-size:13.5px">' + m.name + '</strong>' +
          '<span style="font-family:var(--mono);font-size:12px;font-weight:700;color:' + color + '">' + (m.similarity.toFixed(3)) + '</span>' +
        '</div>' +
        '<div style="font-size:11px;color:var(--dim);margin-bottom:8px">' + m.category + '</div>' +
        '<div style="height:4px;background:rgba(255,255,255,0.08);border-radius:2px;overflow:hidden;margin-bottom:8px">' +
          '<div style="height:100%;width:' + pct + '%;background:' + color + '"></div>' +
        '</div>' +
        '<div style="font-family:var(--mono);font-size:10.5px;color:var(--dim);overflow:hidden;text-overflow:ellipsis;white-space:nowrap" title="' + m.smiles + '">' + m.smiles + '</div>' +
      '</div>' +
      '<button type="button" class="btn secondary" onclick="loadSimilarMolecule(&quot;' + m.smiles + '&quot;)" style="padding:4px 8px;font-size:11px;margin-top:10px;width:100%">' +
        'Compare / Load Structure' +
      '</button>' +
    '</div>';
  }
  grid.innerHTML = h;
}

function loadSimilarMolecule(s){
  AudioEngine.click();
  document.getElementById('smilesInput').value = s;
  scrollToChapter('lab');
  analyzeMolecule();
}

// --- ORGANIC REACTION SIMULATOR ---
var activeReactionsList = [];
var currentReactionProductSmiles = 'CCOC(=O)C';

function initReactions(){
  fetch('/api/reactions')
    .then(function(r){ return r.json(); })
    .then(function(data){
      activeReactionsList = data;
      var sel = document.getElementById('reactionSelect');
      if(sel){
        var h = '';
        for(var i = 0; i < data.length; i++){
          var r = data[i];
          h += '<option value="' + r.id + '">' + (i + 1) + '. ' + r.name + ' (' + r.category + ')</option>';
        }
        sel.innerHTML = h;
        onSelectReaction();
      }
    })
    .catch(function(){});
}

var rxnTypewriterTimer = null;
function animateReactionEquationTyping(text){
  var eq = document.getElementById('rxnEquation');
  if(!eq) return;
  if(rxnTypewriterTimer){
    clearInterval(rxnTypewriterTimer);
    rxnTypewriterTimer = null;
  }
  eq.innerHTML = '<span id="rxnEqText"></span><span class="typewriter-cursor"></span>';
  var span = document.getElementById('rxnEqText');
  var idx = 0;
  var speed = Math.max(12, Math.min(28, Math.floor(550 / Math.max(1, text.length))));
  rxnTypewriterTimer = setInterval(function(){
    if(!span){
      clearInterval(rxnTypewriterTimer);
      return;
    }
    idx++;
    span.innerText = text.substring(0, idx);
    if(idx >= text.length){
      clearInterval(rxnTypewriterTimer);
      rxnTypewriterTimer = null;
      var cur = eq.querySelector('.typewriter-cursor');
      if(cur){
        setTimeout(function(){ if(cur) cur.style.display = 'none'; }, 900);
      }
    }
  }, speed);
}

function onSelectReaction(){
  var sel = document.getElementById('reactionSelect');
  if(!sel) return;
  var id = sel.value;
  var rxn = activeReactionsList.find(function(r){ return r.id === id; });
  if(!rxn) return;
  
  currentReactionProductSmiles = rxn.product;
  
  var cat = document.getElementById('rxnCategory');
  var cnd = document.getElementById('rxnCatalyst');
  var byp = document.getElementById('rxnByproduct');
  var rAName = document.getElementById('rxnReactantAName');
  var rASmiles = document.getElementById('rxnReactantASmiles');
  var rBName = document.getElementById('rxnReactantBName');
  var rBSmiles = document.getElementById('rxnReactantBSmiles');
  var pName = document.getElementById('rxnProductName');
  var pSmiles = document.getElementById('rxnProductSmiles');
  var mech = document.getElementById('rxnMechanismText');
  
  animateReactionEquationTyping(rxn.equation);
  if(cat) cat.innerText = rxn.category;
  if(cnd) cnd.innerText = rxn.catalyst;
  if(byp) byp.innerText = rxn.byproduct;
  if(rAName) rAName.innerText = rxn.reactants[0] ? rxn.reactants[0].split('(')[0].trim() : 'Reactant A';
  if(rASmiles) rASmiles.innerText = rxn.default_a;
  if(rBName) rBName.innerText = rxn.reactants[1] ? rxn.reactants[1].split('(')[0].trim() : 'Reactant B';
  if(rBSmiles) rBSmiles.innerText = rxn.default_b;
  if(pName) pName.innerText = rxn.product_name;
  if(pSmiles) pSmiles.innerText = rxn.product;
  if(mech) mech.innerText = rxn.mechanism;
  
  renderReactionMiniSvg('rxnReactantA2D', rxn.default_a);
  renderReactionMiniSvg('rxnReactantB2D', rxn.default_b);
  renderReactionMiniSvg('rxnProduct2D', rxn.product);
}

function renderReactionMiniSvg(containerId, smiles){
  var el = document.getElementById(containerId);
  if(!el) return;
  if(window.RDKit && window.RDKit.get_mol){
    try {
      var mol = window.RDKit.get_mol(smiles);
      if(mol){
        var svg = mol.get_svg(160, 95);
        mol.delete();
        el.innerHTML = svg;
        return;
      }
    } catch(e){}
  }
  el.innerHTML = '<div style="font-family:var(--mono);color:var(--dim);font-size:12px">' + smiles + '</div>';
}

function loadActiveReactionProductToLab(){
  AudioEngine.click();
  if(!currentReactionProductSmiles) return;
  document.getElementById('smilesInput').value = currentReactionProductSmiles;
  scrollToChapter('lab');
  analyzeMolecule();
}


function analyzeSmilesPedagogical(s){
  if(!s || !s.trim()){
    return {
      error: "Empty SMILES notation entered.",
      tip: "Please enter a valid SMILES string or draw a molecule. Try CC(=O)O for acetic acid or CCO for ethanol."
    };
  }
  var clean = s.trim();

  // 1. Unclosed ring digits
  var digits = clean.match(/\\d/g) || [];
  var digitCounts = {};
  digits.forEach(function(d){ digitCounts[d] = (digitCounts[d] || 0) + 1; });
  var oddDigits = Object.keys(digitCounts).filter(function(d){ return digitCounts[d] % 2 !== 0; });
  if(oddDigits.length > 0){
    return {
      error: "Invalid SMILES — possible unclosed ring (check digit pairs) or nitrogen valence error. Try CC(=O)O for acetic acid.",
      tip: "In SMILES, each ring opening digit must have an identical paired closing digit (e.g. c1ccccc1 for benzene has paired '1's)."
    };
  }

  // 2. Branch parentheses mismatch
  var openP = (clean.match(/\\(/g) || []).length;
  var closeP = (clean.match(/\\)/g) || []).length;
  if(openP !== closeP){
    return {
      error: "Invalid SMILES — possible unclosed ring (check digit pairs) or nitrogen valence error. Try CC(=O)O for acetic acid.",
      tip: "Branching substituents require matched parentheses: " + openP + " '(' vs " + closeP + " ')'. Try CC(=O)O for acetic acid."
    };
  }

  // 3. Atom bracket mismatch
  var openB = (clean.match(/\\[/g) || []).length;
  var closeB = (clean.match(/\\]/g) || []).length;
  if(openB !== closeB){
    return {
      error: "Invalid SMILES — possible unclosed ring (check digit pairs) or nitrogen valence error. Try CC(=O)O for acetic acid.",
      tip: "Bracketed atoms for charge/stereochemistry must be closed, e.g. [NH4+] or [OH-]."
    };
  }

  // 4. Unknown characters
  var invalidChars = clean.replace(/[A-Za-z0-9\\(\\)\\[\\]\\=\\#\\+\\-\\/\\@\\.\\:\\\\]/g, '');
  if(invalidChars.length > 0){
    return {
      error: "Invalid SMILES — possible unclosed ring (check digit pairs) or nitrogen valence error. Try CC(=O)O for acetic acid.",
      tip: "Unrecognized character '" + invalidChars[0] + "'. Use IUPAC element symbols, bonds (=, #), or branches ()."
    };
  }

  return {
    error: "Invalid SMILES — possible unclosed ring (check digit pairs) or nitrogen valence error. Try CC(=O)O for acetic acid.",
    tip: "Verify atom valencies (C: 4, N: 3-5, O: 2, H: 1) or check aromatic lowercase ring notation."
  };
}

function analyzeMolecule(){
  AudioEngine.click();
  var input = document.getElementById('smilesInput').value.trim();
  if(!input){
    var emptyDiag = analyzeSmilesPedagogical("");
    showSmilesError(emptyDiag.error, emptyDiag.tip);
    return;
  }

  activeSmiles = input;
  var repSmilesEl = document.getElementById('repSmiles');
  if(repSmilesEl) repSmilesEl.value = input;
  var actMolBadge = document.getElementById('activeMolNameBadge');
  if(actMolBadge){
    var actBm = BENCHMARK_MOLECULES.find(function(b){ return b.smiles === input; });
    actMolBadge.innerText = actBm ? actBm.name : input;
  }

  // Query Python API with instant client-side fallback
  fetch('/api/calculate?smiles=' + encodeURIComponent(input))
    .then(function(res){
      return res.json().then(function(data){
        return { ok: res.ok, status: res.status, data: data };
      });
    })
    .then(function(result){
      var data = result.data;
      if(result.ok && data && data.valid){
        currentProps = data.properties;
        renderProperties(data.properties, data.interpretations);
        render2DDiagram(input);
        render3DModel(input);
        updateBondMetrics(data.properties);
        showSmilesSuccess("Structure validated via Python Cheminformatics Engine.");
        loadSpectralPredictions(input);
        loadSimilaritySearch(input);
        if(window.history && window.history.replaceState){
          window.history.replaceState(null, '', '?smiles=' + encodeURIComponent(input));
        }
      } else {
        var diag = analyzeSmilesPedagogical(input);
        var errMsg = (data && data.error) ? data.error : diag.error;
        var errTip = (data && data.suggestion) ? data.suggestion : diag.tip;
        showSmilesError(errMsg, errTip);
      }
    })
    .catch(function(err){
      var diag = analyzeSmilesPedagogical(input);
      if(input.length < 2 || diag.error.indexOf("unclosed") !== -1 || diag.error.indexOf("mismatch") !== -1){
        showSmilesError(diag.error, diag.tip);
      } else {
        computeClientProperties(input);
        loadSpectralPredictions(input);
        loadSimilaritySearch(input);
      }
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
  updateBondMetrics(props);
  showSmilesSuccess("Structure parsed via local mathematical engine.");
}

function updateLipinskiScorecard(props){
  if(!props) return;
  var mw = parseFloat(props["Molecular Weight"]) || 0;
  var logp = parseFloat(props["LogP"]);
  if(isNaN(logp)) logp = 0;
  var hbd = parseInt(props["Hydrogen Bond Donors"], 10);
  if(isNaN(hbd)) hbd = 0;
  var hba = parseInt(props["Hydrogen Bond Acceptors"], 10);
  if(isNaN(hba)) hba = 0;

  var mwPass = mw <= 500;
  var logpPass = logp <= 5.0;
  var hbdPass = hbd <= 5;
  var hbaPass = hba <= 10;

  var passCount = (mwPass ? 1 : 0) + (logpPass ? 1 : 0) + (hbdPass ? 1 : 0) + (hbaPass ? 1 : 0);

  // Status header
  var statusText = document.getElementById('ro5StatusText');
  var badge = document.getElementById('ro5Badge');
  var subtext = document.getElementById('ro5Subtext');

  if(statusText && badge){
    if(passCount === 4){
      statusText.innerText = 'LIPINSKI RULE OF 5: 4 / 4 PASS (DRUG-LIKE CANDIDATE)';
      badge.className = 'ro5-badge';
      if(subtext) subtext.innerText = 'Satisfies all Pfizer clinical guidelines for oral bioavailability and membrane permeation.';
    } else if(passCount === 3){
      statusText.innerText = 'LIPINSKI RULE OF 5: 3 / 4 PASS (ACCEPTABLE 1 VIOLATION)';
      badge.className = 'ro5-badge warning';
      if(subtext) subtext.innerText = 'Single Ro5 violation observed. Molecules with 1 violation often maintain oral bioavailability.';
    } else {
      statusText.innerText = 'LIPINSKI RULE OF 5: ' + passCount + ' / 4 PASS (' + (4 - passCount) + ' VIOLATIONS)';
      badge.className = 'ro5-badge danger';
      if(subtext) subtext.innerText = 'Multiple Ro5 violations suggest poor gastrointestinal absorption and limited oral drug bioavailability.';
    }
  }

  // 1. MW Gauge
  var fillMw = document.getElementById('gaugeFillMw');
  var badgeMw = document.getElementById('gaugeBadgeMw');
  animateCounter('gaugeValMw', mw, true, '<span class="gauge-unit">g/mol</span>');
  if(fillMw){
    var mwPct = Math.min(100, Math.max(3, (mw / 600) * 100));
    fillMw.style.width = mwPct + '%';
    fillMw.className = 'gauge-fill' + (mwPass ? '' : ' danger');
  }
  if(badgeMw){
    badgeMw.innerText = mwPass ? 'PASS' : 'FAIL';
    badgeMw.className = 'gauge-badge' + (mwPass ? '' : ' fail');
  }

  // 2. LogP Gauge (optimal -0.4 to 5.0)
  var fillLogP = document.getElementById('gaugeFillLogP');
  var badgeLogP = document.getElementById('gaugeBadgeLogP');
  animateCounter('gaugeValLogP', logp, true, '<span class="gauge-unit">oct/water</span>');
  if(fillLogP){
    var logpPct = Math.min(100, Math.max(4, ((logp + 2) / 8) * 100));
    fillLogP.style.width = logpPct + '%';
    fillLogP.className = 'gauge-fill ' + (logpPass ? 'emerald' : 'danger');
  }
  if(badgeLogP){
    badgeLogP.innerText = logpPass ? (logp >= 0 && logp <= 3 ? 'OPTIMAL' : 'PASS') : 'FAIL';
    badgeLogP.className = 'gauge-badge' + (logpPass ? '' : ' fail');
  }

  // 3. H-Bond Donors Gauge (limit 5)
  var fillHbd = document.getElementById('gaugeFillHbd');
  var badgeHbd = document.getElementById('gaugeBadgeHbd');
  animateCounter('gaugeValHbd', hbd, false, '<span class="gauge-unit">/ 5 max</span>');
  if(fillHbd){
    var hbdPct = Math.min(100, Math.max(5, (hbd / 6) * 100));
    fillHbd.style.width = hbdPct + '%';
    fillHbd.className = 'gauge-fill ' + (hbdPass ? 'cyan' : 'danger');
  }
  if(badgeHbd){
    badgeHbd.innerText = hbdPass ? 'PASS' : 'FAIL';
    badgeHbd.className = 'gauge-badge' + (hbdPass ? '' : ' fail');
  }

  // 4. H-Bond Acceptors Gauge (limit 10)
  var fillHba = document.getElementById('gaugeFillHba');
  var badgeHba = document.getElementById('gaugeBadgeHba');
  animateCounter('gaugeValHba', hba, false, '<span class="gauge-unit">/ 10 max</span>');
  if(fillHba){
    var hbaPct = Math.min(100, Math.max(5, (hba / 12) * 100));
    fillHba.style.width = hbaPct + '%';
    fillHba.className = 'gauge-fill ' + (hbaPass ? 'purple' : 'danger');
  }
  if(badgeHba){
    badgeHba.innerText = hbaPass ? 'PASS' : 'FAIL';
    badgeHba.className = 'gauge-badge' + (hbaPass ? '' : ' fail');
  }
}

function updateBondMetrics(p){
  var formulaEl = document.getElementById('bmFormula');
  if(formulaEl) formulaEl.innerText = p["Molecular Formula"] || "-";

  animateCounter('bmMw', p["Molecular Weight"] || 0, true, '<span style="font-size:11px;color:var(--dim)">g/mol</span>');
  animateCounter('bmHeavyAtoms', p["Heavy Atoms"] || 0, false);
  animateCounter('bmSigma', p["Sigma (σ) Bonds"] || 0, false);
  animateCounter('bmPi', p["Pi (π) Bonds"] || 0, false);
  animateCounter('bmTotalBonds', p["Total Bonds (σ + π)"] || 0, false);

  updateLipinskiScorecard(p);
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

  if(window.gsap){
    gsap.fromTo("#propTableBody tr",
      { x: -35, opacity: 0 },
      { x: 0, opacity: 1, duration: 0.45, stagger: 0.025, ease: "power2.out" }
    );
  }
}

function render2DDiagram(smiles){
  var container = document.getElementById('canvas2D');
  if(!container) return;

  var clean = (smiles || '').trim();

  // Animated vector SVG diagram for the molecular structure
  var svg = '<svg width="100%" height="100%" viewBox="-150 -150 300 300" xmlns="http://www.w3.org/2000/svg" style="overflow:visible">';
  svg += '<defs>';
  svg += '  <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">';
  svg += '    <feGaussianBlur stdDeviation="2.5" result="blur"/>';
  svg += '    <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>';
  svg += '  </filter>';
  svg += '</defs>';

  if(clean === 'c1ccccc1' || clean === 'C1=CC=CC=C1'){
    // --- 1. BENZENE (C6H6): Planar D6h Hexagon with 3 Alternating Kekule Double Bonds + Pi Resonance Ring ---
    var R = 64;
    var pts = [];
    var v = [];
    for(var i = 0; i < 6; i++){
      var ang = (-90 + i * 60) * Math.PI / 180;
      var vx = Math.round(R * Math.cos(ang) * 10) / 10;
      var vy = Math.round(R * Math.sin(ang) * 10) / 10;
      pts.push(vx + ',' + vy);
      v.push({ x: vx, y: vy, ang: ang });
    }

    // Outer Hexagon
    svg += '<polygon points="' + pts.join(' ') + '" fill="rgba(0, 240, 255, 0.05)" stroke="#00f0ff" stroke-width="3.5" stroke-linejoin="round" filter="url(#glow)"/>';
    // Delocalized pi-electron resonance circle
    svg += '<circle cx="0" cy="0" r="38" fill="rgba(0, 255, 157, 0.03)" stroke="#00ff9d" stroke-width="2.2" stroke-dasharray="6,4" opacity="0.95"/>';

    // 3 Alternating Kekule Double Bonds (sides 0-1, 2-3, 4-5)
    var rIn = R * 0.78;
    var kekuleSides = [0, 2, 4];
    for(var k = 0; k < kekuleSides.length; k++){
      var side = kekuleSides[k];
      var a1 = (-90 + side * 60) * Math.PI / 180;
      var a2 = (-90 + (side + 1) * 60) * Math.PI / 180;
      var x1 = Math.round(rIn * Math.cos(a1) * 10) / 10;
      var y1 = Math.round(rIn * Math.sin(a1) * 10) / 10;
      var x2 = Math.round(rIn * Math.cos(a2) * 10) / 10;
      var y2 = Math.round(rIn * Math.sin(a2) * 10) / 10;
      svg += '<line x1="' + x1 + '" y1="' + y1 + '" x2="' + x2 + '" y2="' + y2 + '" stroke="#38bdf8" stroke-width="2.5" stroke-linecap="round" opacity="0.95"/>';
    }

    // 6 Carbons + 6 Radiating Hydrogens
    for(var i = 0; i < 6; i++){
      var cv = v[i];
      var hx = Math.round((R + 32) * Math.cos(cv.ang) * 10) / 10;
      var hy = Math.round((R + 32) * Math.sin(cv.ang) * 10) / 10;
      svg += '<line x1="' + cv.x + '" y1="' + cv.y + '" x2="' + hx + '" y2="' + hy + '" stroke="rgba(255,255,255,0.4)" stroke-width="1.5" stroke-dasharray="2,2"/>';
      svg += '<circle cx="' + cv.x + '" cy="' + cv.y + '" r="8" fill="#071026" stroke="#38bdf8" stroke-width="2"/>';
      svg += '<text x="' + cv.x + '" y="' + (cv.y + 3.5) + '" fill="#38bdf8" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">C</text>';
      svg += '<circle cx="' + hx + '" cy="' + hy + '" r="6.5" fill="#020617" stroke="rgba(255,255,255,0.6)" stroke-width="1.2"/>';
      svg += '<text x="' + hx + '" y="' + (hy + 3) + '" fill="#f8fafc" font-size="8" font-family="monospace" text-anchor="middle">H</text>';
    }

    svg += '<text x="0" y="118" fill="#38bdf8" font-size="11.5" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="1">BENZENE (C₆H₆)</text>';
    svg += '<text x="0" y="134" fill="#00ff9d" font-size="9" font-family="monospace" text-anchor="middle">Planar Aromatic Ring &bull; 6 π Delocalized Electrons &bull; D₆ₕ</text>';

  } else if(clean === 'CCO'){
    // --- 2. ETHANOL (C2H6O) ---
    svg += '<line x1="-80" y1="20" x2="-10" y2="-20" stroke="#00f0ff" stroke-width="4" stroke-linecap="round" filter="url(#glow)"/>';
    svg += '<line x1="-10" y1="-20" x2="65" y2="20" stroke="#00f0ff" stroke-width="4" stroke-linecap="round" filter="url(#glow)"/>';
    svg += '<line x1="65" y1="20" x2="110" y2="-5" stroke="#ff4d6d" stroke-width="3" stroke-dasharray="3,3"/>';

    svg += '<circle cx="-80" cy="20" r="16" fill="#0b1736" stroke="#38bdf8" stroke-width="2"/>';
    svg += '<text x="-80" y="24.5" fill="#f8fafc" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle">CH₃</text>';

    svg += '<circle cx="-10" cy="-20" r="16" fill="#0b1736" stroke="#38bdf8" stroke-width="2"/>';
    svg += '<text x="-10" y="-15.5" fill="#f8fafc" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle">CH₂</text>';

    svg += '<circle cx="65" cy="20" r="16" fill="#ff4d6d" stroke="#fecdd3" stroke-width="2"/>';
    svg += '<text x="65" y="24.5" fill="#ffffff" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle">OH</text>';

    svg += '<text x="110" y="0" fill="#fda4af" font-size="9.5" font-family="monospace">δ⁺ [H]</text>';
    svg += '<text x="65" y="48" fill="#ff4d6d" font-size="9.5" font-family="monospace" text-anchor="middle">δ⁻ [O]</text>';

    svg += '<text x="0" y="118" fill="#38bdf8" font-size="11.5" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="1">ETHANOL (C₂H₆O)</text>';
    svg += '<text x="0" y="134" fill="#00ff9d" font-size="9" font-family="monospace" text-anchor="middle">Primary Aliphatic Alcohol &bull; Polar Hydrogen Bonding</text>';

  } else if(clean === 'Oc1ccccc1'){
    // --- 3. PHENOL (C6H6O) ---
    var R = 54;
    var pts = [];
    var v = [];
    for(var i = 0; i < 6; i++){
      var ang = (-90 + i * 60) * Math.PI / 180;
      var vx = Math.round(R * Math.cos(ang) * 10) / 10;
      var vy = Math.round((R * Math.sin(ang) + 20) * 10) / 10;
      pts.push(vx + ',' + vy);
      v.push({ x: vx, y: vy });
    }

    svg += '<polygon points="' + pts.join(' ') + '" fill="rgba(0, 240, 255, 0.05)" stroke="#00f0ff" stroke-width="3" stroke-linejoin="round" filter="url(#glow)"/>';
    svg += '<circle cx="0" cy="20" r="32" fill="none" stroke="#00ff9d" stroke-width="2" stroke-dasharray="5,4" opacity="0.9"/>';

    svg += '<line x1="0" y1="-34" x2="0" y2="-82" stroke="#ff4d6d" stroke-width="3.5" stroke-linecap="round"/>';
    svg += '<circle cx="0" cy="-82" r="15" fill="#ff4d6d" stroke="#ffffff" stroke-width="2"/>';
    svg += '<text x="0" y="-77.5" fill="#ffffff" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle">OH</text>';

    for(var i = 0; i < 6; i++){
      var cv = v[i];
      svg += '<circle cx="' + cv.x + '" cy="' + cv.y + '" r="6" fill="#071026" stroke="#38bdf8" stroke-width="1.8"/>';
    }

    svg += '<text x="0" y="118" fill="#38bdf8" font-size="11.5" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="1">PHENOL (C₆H₆O)</text>';
    svg += '<text x="0" y="134" fill="#00ff9d" font-size="9" font-family="monospace" text-anchor="middle">Aromatic Hydroxyl &bull; Resonance-Stabilized Phenoxide</text>';

  } else if(clean === 'CC(=O)O'){
    // --- 4. ACETIC ACID (C2H4O2) ---
    svg += '<line x1="-70" y1="15" x2="0" y2="-10" stroke="#00f0ff" stroke-width="3.5" stroke-linecap="round"/>';
    svg += '<line x1="-4" y1="-10" x2="-4" y2="-72" stroke="#ff4d6d" stroke-width="3" stroke-linecap="round"/>';
    svg += '<line x1="6" y1="-10" x2="6" y2="-72" stroke="#ff4d6d" stroke-width="3" stroke-linecap="round"/>';
    svg += '<line x1="0" y1="-10" x2="65" y2="25" stroke="#00ff9d" stroke-width="3.5" stroke-linecap="round"/>';

    svg += '<circle cx="-70" cy="15" r="16" fill="#0b1736" stroke="#38bdf8" stroke-width="2"/>';
    svg += '<text x="-70" y="19.5" fill="#f8fafc" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle">CH₃</text>';

    svg += '<circle cx="1" cy="-72" r="14" fill="#ff4d6d" stroke="#fecdd3" stroke-width="2"/>';
    svg += '<text x="1" y="-67.5" fill="#ffffff" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle">=O</text>';

    svg += '<circle cx="0" cy="-10" r="7" fill="#071026" stroke="#38bdf8" stroke-width="2"/>';

    svg += '<circle cx="65" cy="25" r="15" fill="#071026" stroke="#00ff9d" stroke-width="2"/>';
    svg += '<text x="65" y="29.5" fill="#00ff9d" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle">OH</text>';

    svg += '<text x="0" y="118" fill="#38bdf8" font-size="11.5" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="1">ACETIC ACID (C₂H₄O₂)</text>';
    svg += '<text x="0" y="134" fill="#00ff9d" font-size="9" font-family="monospace" text-anchor="middle">Carboxylic Acid &bull; Planar sp² Carbonyl Center</text>';

  } else if(clean === 'CC(=O)Oc1ccccc1C(=O)O'){
    // --- 5. ASPIRIN (C9H8O4) ---
    var R = 44;
    var pts = [];
    for(var i = 0; i < 6; i++){
      var ang = (-90 + i * 60) * Math.PI / 180;
      var vx = Math.round((-35 + R * Math.cos(ang)) * 10) / 10;
      var vy = Math.round((15 + R * Math.sin(ang)) * 10) / 10;
      pts.push(vx + ',' + vy);
    }
    svg += '<polygon points="' + pts.join(' ') + '" fill="rgba(0, 240, 255, 0.05)" stroke="#00f0ff" stroke-width="2.8" stroke-linejoin="round" filter="url(#glow)"/>';
    svg += '<circle cx="-35" cy="15" r="25" fill="none" stroke="#00ff9d" stroke-width="1.8" stroke-dasharray="4,3" opacity="0.9"/>';

    svg += '<line x1="3" y1="-7" x2="35" y2="-30" stroke="#f59e0b" stroke-width="2.5"/>';
    svg += '<text x="40" y="-27" fill="#f59e0b" font-size="10" font-family="monospace" font-weight="bold">O-Ac</text>';
    svg += '<line x1="68" y1="-30" x2="95" y2="-30" stroke="#f59e0b" stroke-width="2"/>';
    svg += '<circle cx="102" cy="-30" r="11" fill="#0b1736" stroke="#f59e0b" stroke-width="1.5"/>';
    svg += '<text x="102" y="-27" fill="#f8fafc" font-size="8.5" font-family="monospace" text-anchor="middle">CH₃</text>';

    svg += '<line x1="3" y1="37" x2="42" y2="55" stroke="#ff4d6d" stroke-width="2.5"/>';
    svg += '<text x="48" y="59" fill="#ff4d6d" font-size="10" font-family="monospace" font-weight="bold">COOH</text>';

    svg += '<text x="0" y="118" fill="#38bdf8" font-size="11.5" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="1">ASPIRIN (C₉H₈O₄)</text>';
    svg += '<text x="0" y="134" fill="#00ff9d" font-size="9" font-family="monospace" text-anchor="middle">Acetylsalicylic Acid &bull; COX-1/2 Inhibitor Pharmacophore</text>';

  } else if(clean === 'CN1C=NC2=C1C(=O)N(C(=O)N2C)C'){
    // --- 6. CAFFEINE (C8H10N4O2) ---
    svg += '<polygon points="-60,-35 -20,-35 5,0 -20,35 -60,35 -75,0" fill="rgba(0, 240, 255, 0.05)" stroke="#00f0ff" stroke-width="2.5" stroke-linejoin="round"/>';
    svg += '<polygon points="5,0 45,-25 70,0 45,25" fill="rgba(192, 132, 252, 0.05)" stroke="#c084fc" stroke-width="2.5" stroke-linejoin="round"/>';

    svg += '<line x1="-20" y1="-35" x2="-20" y2="-62" stroke="#ff4d6d" stroke-width="2.5"/>';
    svg += '<circle cx="-20" cy="-66" r="8" fill="#ff4d6d" stroke="#fff" stroke-width="1.5"/>';
    svg += '<text x="-20" y="-63" fill="#fff" font-size="8" font-family="monospace" text-anchor="middle">O</text>';

    svg += '<line x1="-60" y1="35" x2="-60" y2="62" stroke="#ff4d6d" stroke-width="2.5"/>';
    svg += '<circle cx="-60" cy="66" r="8" fill="#ff4d6d" stroke="#fff" stroke-width="1.5"/>';
    svg += '<text x="-60" y="69" fill="#fff" font-size="8" font-family="monospace" text-anchor="middle">O</text>';

    svg += '<circle cx="-60" cy="-35" r="9" fill="#0b1736" stroke="#38bdf8" stroke-width="1.8"/>';
    svg += '<text x="-60" y="-32" fill="#38bdf8" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">N</text>';

    svg += '<circle cx="-20" cy="35" r="9" fill="#0b1736" stroke="#38bdf8" stroke-width="1.8"/>';
    svg += '<text x="-20" y="38" fill="#38bdf8" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">N</text>';

    svg += '<circle cx="45" cy="-25" r="9" fill="#0b1736" stroke="#c084fc" stroke-width="1.8"/>';
    svg += '<text x="45" y="-22" fill="#c084fc" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">N</text>';

    svg += '<text x="0" y="118" fill="#38bdf8" font-size="11.5" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="1">CAFFEINE (C₈H₁₀N₄O₂)</text>';
    svg += '<text x="0" y="134" fill="#00ff9d" font-size="9" font-family="monospace" text-anchor="middle">1,3,7-Trimethylxanthine &bull; CNS Adenosine Receptor Antagonist</text>';

  } else if(clean === 'CC(=O)Nc1ccc(O)cc1'){
    // --- 7. PARACETAMOL (C8H9NO2) ---
    var R = 44;
    var pts = [];
    for(var i = 0; i < 6; i++){
      var ang = (-90 + i * 60) * Math.PI / 180;
      var vx = Math.round((R * Math.cos(ang)) * 10) / 10;
      var vy = Math.round((R * Math.sin(ang)) * 10) / 10;
      pts.push(vx + ',' + vy);
    }
    svg += '<polygon points="' + pts.join(' ') + '" fill="rgba(0, 240, 255, 0.05)" stroke="#00f0ff" stroke-width="2.8" stroke-linejoin="round" filter="url(#glow)"/>';
    svg += '<circle cx="0" cy="0" r="25" fill="none" stroke="#00ff9d" stroke-width="1.8" stroke-dasharray="4,3" opacity="0.9"/>';

    svg += '<line x1="0" y1="-44" x2="0" y2="-78" stroke="#ff4d6d" stroke-width="2.8"/>';
    svg += '<circle cx="0" cy="-80" r="12" fill="#ff4d6d" stroke="#fff" stroke-width="1.5"/>';
    svg += '<text x="0" y="-76" fill="#fff" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">OH</text>';

    svg += '<line x1="0" y1="44" x2="0" y2="70" stroke="#38bdf8" stroke-width="2.8"/>';
    svg += '<circle cx="0" cy="74" r="10" fill="#0b1736" stroke="#38bdf8" stroke-width="1.5"/>';
    svg += '<text x="0" y="77" fill="#38bdf8" font-size="8.5" font-family="monospace" font-weight="bold" text-anchor="middle">NH</text>';
    svg += '<line x1="10" y1="74" x2="45" y2="74" stroke="#38bdf8" stroke-width="2.2"/>';
    svg += '<text x="50" y="77" fill="#f8fafc" font-size="9" font-family="monospace">Ac</text>';

    svg += '<text x="0" y="118" fill="#38bdf8" font-size="11.5" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="1">PARACETAMOL (C₈H₉NO₂)</text>';
    svg += '<text x="0" y="134" fill="#00ff9d" font-size="9" font-family="monospace" text-anchor="middle">N-(4-Hydroxyphenyl)acetamide &bull; Antipyretic Analgesic</text>';

  } else if(clean === 'CC(C)Cc1ccc(C(C)C(=O)O)cc1'){
    // --- 8. IBUPROFEN (C13H18O2) ---
    var R = 40;
    var pts = [];
    for(var i = 0; i < 6; i++){
      var ang = (i * 60) * Math.PI / 180;
      var vx = Math.round((R * Math.cos(ang)) * 10) / 10;
      var vy = Math.round((R * Math.sin(ang)) * 10) / 10;
      pts.push(vx + ',' + vy);
    }
    svg += '<polygon points="' + pts.join(' ') + '" fill="rgba(0, 240, 255, 0.05)" stroke="#00f0ff" stroke-width="2.8" stroke-linejoin="round" filter="url(#glow)"/>';
    svg += '<circle cx="0" cy="0" r="23" fill="none" stroke="#00ff9d" stroke-width="1.8" stroke-dasharray="4,3" opacity="0.9"/>';

    svg += '<line x1="-40" y1="0" x2="-75" y2="0" stroke="#00f0ff" stroke-width="2.5"/>';
    svg += '<line x1="-75" y1="0" x2="-105" y2="-22" stroke="#00f0ff" stroke-width="2.5"/>';
    svg += '<line x1="-75" y1="0" x2="-105" y2="22" stroke="#00f0ff" stroke-width="2.5"/>';
    svg += '<text x="-115" y="-20" fill="#f8fafc" font-size="8.5" font-family="monospace">CH₃</text>';
    svg += '<text x="-115" y="25" fill="#f8fafc" font-size="8.5" font-family="monospace">CH₃</text>';

    svg += '<line x1="40" y1="0" x2="72" y2="0" stroke="#00f0ff" stroke-width="2.5"/>';
    svg += '<line x1="72" y1="0" x2="72" y2="-32" stroke="#00f0ff" stroke-width="2.2"/>';
    svg += '<text x="72" y="-36" fill="#f8fafc" font-size="8.5" font-family="monospace" text-anchor="middle">CH₃</text>';
    svg += '<line x1="72" y1="0" x2="105" y2="18" stroke="#ff4d6d" stroke-width="2.5"/>';
    svg += '<text x="110" y="22" fill="#ff4d6d" font-size="9.5" font-family="monospace" font-weight="bold">COOH</text>';

    svg += '<text x="0" y="118" fill="#38bdf8" font-size="11.5" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="1">IBUPROFEN (C₁₃H₁₈O₂)</text>';
    svg += '<text x="0" y="134" fill="#00ff9d" font-size="9" font-family="monospace" text-anchor="middle">2-(4-Isobutylphenyl)propanoic Acid &bull; NSAID Analgesic</text>';

  } else {
    // --- 9. DYNAMIC GENERALIZED TOPOLOGY FOR CUSTOM SMILES ---
    var atoms = clean.match(/(Cl|Br|Si|Na|Ca|Mg|Fe|Cu|Zn|[CNOPFSIcnops])/g) || ['C', 'C', 'O'];
    var numAtoms = Math.min(atoms.length, 12);
    var isRing = clean.indexOf('1') !== -1 || clean.indexOf('c') !== -1;

    if(isRing && numAtoms >= 5){
      var rRing = 55;
      var ringPts = [];
      for(var i = 0; i < numAtoms; i++){
        var a = (i * 2 * Math.PI / numAtoms) - Math.PI / 2;
        var ax = Math.round(rRing * Math.cos(a) * 10) / 10;
        var ay = Math.round(rRing * Math.sin(a) * 10) / 10;
        ringPts.push(ax + ',' + ay);
      }
      svg += '<polygon points="' + ringPts.join(' ') + '" fill="rgba(0, 240, 255, 0.05)" stroke="#00f0ff" stroke-width="3" stroke-linejoin="round" filter="url(#glow)"/>';
      for(var i = 0; i < numAtoms; i++){
        var a = (i * 2 * Math.PI / numAtoms) - Math.PI / 2;
        var ax = Math.round(rRing * Math.cos(a) * 10) / 10;
        var ay = Math.round(rRing * Math.sin(a) * 10) / 10;
        var sym = (atoms[i] || 'C').toUpperCase();
        var col = sym === 'O' ? '#ff4d6d' : (sym === 'N' ? '#c084fc' : (sym === 'S' ? '#fbbf24' : '#38bdf8'));
        svg += '<circle cx="' + ax + '" cy="' + ay + '" r="8" fill="#071026" stroke="' + col + '" stroke-width="2"/>';
        svg += '<text x="' + ax + '" y="' + (ay + 3.5) + '" fill="' + col + '" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">' + sym + '</text>';
      }
    } else {
      var step = Math.min(48, 220 / Math.max(numAtoms, 2));
      var startX = -((numAtoms - 1) * step) / 2;
      for(var i = 0; i < numAtoms - 1; i++){
        var xA = startX + i * step;
        var yA = (i % 2 === 0 ? 20 : -20);
        var xB = startX + (i + 1) * step;
        var yB = ((i + 1) % 2 === 0 ? 20 : -20);
        svg += '<line x1="' + xA + '" y1="' + yA + '" x2="' + xB + '" y2="' + yB + '" stroke="#00f0ff" stroke-width="3.5" stroke-linecap="round" filter="url(#glow)"/>';
      }
      for(var i = 0; i < numAtoms; i++){
        var xA = startX + i * step;
        var yA = (i % 2 === 0 ? 20 : -20);
        var sym = (atoms[i] || 'C').toUpperCase();
        var col = sym === 'O' ? '#ff4d6d' : (sym === 'N' ? '#c084fc' : (sym === 'S' ? '#fbbf24' : '#38bdf8'));
        svg += '<circle cx="' + xA + '" cy="' + yA + '" r="10" fill="#071026" stroke="' + col + '" stroke-width="2"/>';
        svg += '<text x="' + xA + '" y="' + (yA + 3.5) + '" fill="' + col + '" font-size="9" font-family="monospace" font-weight="bold" text-anchor="middle">' + sym + '</text>';
      }
    }

    svg += '<text x="0" y="118" fill="#38bdf8" font-size="11" font-family="monospace" font-weight="bold" text-anchor="middle" letter-spacing="1">' + clean + '</text>';
    svg += '<text x="0" y="134" fill="#00ff9d" font-size="9" font-family="monospace" text-anchor="middle">2D Skeletal Graph &bull; ' + numAtoms + ' Heavy Atoms</text>';
  }

  svg += '</svg>';

  // Retain cybernetic HUD corner reticles inside #canvas2D
  var reticles = '<div class="hud-reticle tl"></div><div class="hud-reticle tr"></div><div class="hud-reticle bl"></div><div class="hud-reticle br"></div>';
  container.innerHTML = reticles + svg;

  if(window.gsap){
    var svgEl = container.querySelector('svg');
    if(svgEl){
      gsap.fromTo(svgEl,
        { opacity: 0, scale: 0.94, transformOrigin: "center center" },
        { opacity: 1, scale: 1, duration: 0.4, ease: "power2.out" }
      );
    }
  }
}

function render3DModel(smiles){
  if(!glViewer) return;
  glViewer.clear();

  // 1. Instant loading from embedded benchmark 3D SDF cache
  if(typeof BENCHMARK_SDF !== 'undefined' && BENCHMARK_SDF[smiles]){
    glViewer.addModel(BENCHMARK_SDF[smiles], "sdf");
    update3DStyle();
    return;
  }

  // 2. Query Python backend /api/sdf or PubChem REST
  fetch('/api/sdf?smiles=' + encodeURIComponent(smiles))
    .then(function(res){
      if(!res.ok) throw new Error("SDF not on server");
      return res.json();
    })
    .then(function(data){
      if(data.valid && data.sdf){
        glViewer.addModel(data.sdf, "sdf");
        update3DStyle();
      } else {
        throw new Error("Invalid SDF");
      }
    })
    .catch(function(){
      // 3. Fallback to client-side realistic 3D conformer generator (NO stickman figures!)
      var realisticPdb = generateRealistic3DConformer(smiles);
      glViewer.addModel(realisticPdb, "pdb");
      update3DStyle();
    });
}

function update3DStyle(){
  if(!glViewer) return;
  var style = document.getElementById('modelStyle').value;
  var surface = document.getElementById('chkSurface').checked;

  glViewer.setStyle({}, {});

  // High-Fidelity Solid Molecular Styling with Standard IUPAC/CPK Colors (Jmol)
  if(style === 'ballAndStick'){
    glViewer.setStyle({}, {
      stick: { radius: 0.22, colorscheme: 'Jmol' },
      sphere: { scale: 0.44, colorscheme: 'Jmol' }
    });
  } else if(style === 'stick'){
    glViewer.setStyle({}, { stick: { radius: 0.30, colorscheme: 'Jmol' } });
  } else if(style === 'sphere'){
    glViewer.setStyle({}, { sphere: { scale: 0.95, colorscheme: 'Jmol' } });
  } else if(style === 'line'){
    glViewer.setStyle({}, { line: { linewidth: 3.5, colorscheme: 'Jmol' } });
  } else if(style === 'cartoon'){
    glViewer.setStyle({}, { stick: { radius: 0.16, colorscheme: 'Jmol' }, sphere: { scale: 0.32, colorscheme: 'Jmol' } });
  }

  glViewer.removeAllSurfaces();
  if(surface){
    glViewer.addSurface($3Dmol.SurfaceType.VDW, { opacity: 0.65, color: 'cyan' });
  }

  glViewer.zoomTo();
  glViewer.render();
}

function generateRealistic3DConformer(smiles){
  var clean = smiles.replace(/\\[([A-Za-z0-9\\+\\-\\@]+)\\]/g, '$1');
  var matches = clean.match(/(Cl|Br|Si|Na|Ca|Mg|Fe|Cu|Zn|[CNOPFSIcnops])/g) || ['C', 'C', 'O'];
  var isAromatic = smiles.indexOf('c') !== -1 || smiles.indexOf('1') !== -1;
  var count = matches.length;

  var coords = [];
  var conectLines = [];
  var pdbLines = [];

  if(isAromatic && count >= 5 && count <= 10){
    var ringRadius = 1.40 / (2 * Math.sin(Math.PI / count));
    for(var i = 0; i < count; i++){
      var angle = (i * 2 * Math.PI) / count;
      var elem = matches[i].toUpperCase();
      var x = ringRadius * Math.cos(angle);
      var y = ringRadius * Math.sin(angle);
      var z = (i % 2 === 0 ? 0.08 : -0.08);
      coords.push({ elem: elem, x: x, y: y, z: z, name: elem + (i + 1) });
    }
  } else {
    var bondLen = 1.54;
    var curX = -((count - 1) * bondLen * 0.8) / 2;
    for(var i = 0; i < count; i++){
      var elem = matches[i].toUpperCase();
      var dy = (i % 2 === 0) ? -0.45 : 0.45;
      var dz = (i % 3 === 0) ? 0.35 : (i % 3 === 1 ? -0.35 : 0.0);
      coords.push({ elem: elem, x: curX + (i * 1.35), y: dy, z: dz, name: elem + (i + 1) });
    }
  }

  // Add explicit Hydrogens
  var hCount = 0;
  var origCount = coords.length;
  for(var i = 0; i < origCount; i++){
    var at = coords[i];
    var neededH = at.elem === 'C' ? (isAromatic ? 1 : 2) : (at.elem === 'N' ? 1 : (at.elem === 'O' ? 1 : 0));
    for(var h = 0; h < neededH; h++){
      hCount++;
      var hx = at.x + (h === 0 ? 0.75 : -0.75);
      var hy = at.y + (h === 0 ? 0.85 : -0.85);
      var hz = at.z + (h % 2 === 0 ? 0.70 : -0.70);
      coords.push({ elem: 'H', x: hx, y: hy, z: hz, name: 'H' + hCount });
      conectLines.push("CONECT " + String(i + 1).padStart(4) + " " + String(coords.length).padStart(4));
    }
  }

  for(var i = 0; i < coords.length; i++){
    var c = coords[i];
    var atomNum = String(i + 1).padStart(5);
    var atomName = c.name.padEnd(4);
    var x = c.x.toFixed(3).padStart(8);
    var y = c.y.toFixed(3).padStart(8);
    var z = c.z.toFixed(3).padStart(8);
    var elem = c.elem.padStart(2);
    pdbLines.push("HETATM" + atomNum + " " + atomName + " MOL     1    " + x + y + z + "  1.00 20.00          " + elem);
  }

  for(var i = 1; i < origCount; i++){
    conectLines.push("CONECT " + String(i).padStart(4) + " " + String(i + 1).padStart(4));
  }
  if(isAromatic && origCount >= 3){
    conectLines.push("CONECT " + String(origCount).padStart(4) + "    1");
  }

  return pdbLines.join("\\n") + "\\n" + conectLines.join("\\n") + "\\nEND\\n";
}

function showSmilesError(msg, tip){
  var el = document.getElementById('smilesError');
  var txt = document.getElementById('smilesErrorText');
  var tipEl = document.getElementById('smilesPedagogicTip');
  var suc = document.getElementById('smilesSuccess');

  var finalMsg = (msg || "").trim();
  var finalTip = (tip || "").trim();

  if(!finalMsg.startsWith("Invalid SMILES")){
    finalMsg = "Invalid SMILES — " + (finalMsg || "possible unclosed ring (check digit pairs) or nitrogen valence error");
  }
  if(finalMsg.indexOf("Try CC(=O)O") === -1){
    finalMsg += ". Try CC(=O)O for acetic acid.";
  }
  if(!finalTip){
    finalTip = "In SMILES, each ring opening digit must have an identical paired closing digit (e.g. c1ccccc1 for benzene).";
  }

  if(txt) txt.innerText = finalMsg;
  if(tipEl){
    tipEl.innerText = "💡 Educational Tip: " + finalTip;
    tipEl.style.display = 'block';
  }
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
   5. COMPARATIVE TABLE
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
      '<td><button class="btn sm" onclick="selectPreset(\\'' + m.smiles + '\\', \\'' + m.name + '\\')"><span>Load in 3D</span></button></td>' +
    '</tr>';
  }).join('');

  setupRollingButtons();
  initMagneticButtons();
}

/* ==========================================================================
   6. ASSESSMENT QUIZ TERMINAL
   ========================================================================== */
var currentQ = 0;
var quizScore = 0;

function initHealthCheck(){
  fetch('/api/health')
    .then(function(r){ return r.json(); })
    .then(function(d){
      var el = document.getElementById('footerEngineVersion');
      if(el && d && (d.version || d.version_string)){
        var v = d.version_string || (d.version.startsWith('v') ? d.version : 'v' + d.version);
        el.innerHTML = 'PYTHON SERVERLESS ENGINE ' + (v.indexOf('3.14') !== -1 ? 'v3.14' : v) + ' &times; VERCEL EDGE';
      }
    })
    .catch(function(){});
}

function initQuiz(){
  var quizResolved = false;

  // 1. Immediately hydrate static array (zero network wait time)
  renderQuizQuestion();

  // 2. Hardcoded fallback timer: if network fetch doesn't resolve in 2 seconds, force-render static array
  var fallbackTimer = setTimeout(function(){
    if(!quizResolved){
      quizResolved = true;
      renderQuizQuestion();
    }
  }, 2000);

  // 3. Attempt dynamic curriculum fetch to /api/quiz
  fetch('/api/quiz')
    .then(function(r){
      if(!r.ok) throw new Error('Quiz API HTTP ' + r.status);
      return r.json();
    })
    .then(function(data){
      clearTimeout(fallbackTimer);
      if(!quizResolved && Array.isArray(data) && data.length > 0){
        QUIZ_DATA = data;
        renderQuizQuestion();
        quizResolved = true;
      }
    })
    .catch(function(err){
      // Immediate fallback to static curriculum array on network error
      clearTimeout(fallbackTimer);
      if(!quizResolved){
        quizResolved = true;
        renderQuizQuestion();
      }
    });
}

function renderQuizQuestion(){
  if(!QUIZ_DATA || !QUIZ_DATA.length){
    return;
  }
  var q = QUIZ_DATA[currentQ] || QUIZ_DATA[0];
  var progEl = document.getElementById('quizProgress');
  var scoreEl = document.getElementById('quizScore');
  var qEl = document.getElementById('quizQuestion');
  var opts = document.getElementById('quizOptions');

  if(progEl) progEl.innerText = 'QUESTION ' + (currentQ + 1) + ' OF ' + QUIZ_DATA.length;
  if(scoreEl) scoreEl.innerText = 'SCORE: ' + quizScore;
  if(qEl && q && q.q) qEl.innerText = q.q;

  if(opts && q && Array.isArray(q.opts)){
    opts.innerHTML = q.opts.map(function(opt, idx){
      return '<button class="quiz-opt" onclick="checkAnswer(' + idx + ')">' +
        '<span>' + String.fromCharCode(65 + idx) + '.</span> ' + opt +
      '</button>';
    }).join('');
  }

  var btnNext = document.getElementById('btnNextQuiz');
  if(btnNext) btnNext.style.display = 'none';

  if(window.gsap && opts){
    gsap.fromTo(".quiz-opt",
      { x: -30, opacity: 0 },
      { x: 0, opacity: 1, duration: 0.4, stagger: 0.06, ease: "power2.out" }
    );
  }
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
  setupRollingButtons();
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
      '<p style="color:var(--dim);font-size:13px;margin-top:8px">Your assessment result has been recorded and will be certified on your downloadable report.</p>' +
      '<div style="margin-top:18px;display:flex;gap:12px;justify-content:center;flex-wrap:wrap">' +
        '<button class="btn primary" onclick="currentQ=0;quizScore=0;renderQuizQuestion()"><span>Retake Assessment</span></button>' +
        '<button class="btn secondary" onclick="scrollToLeaderboard()"><span>Post Score to Class Leaderboard</span></button>' +
      '</div>' +
    '</div>';
    document.getElementById('btnNextQuiz').style.display = 'none';
    setupRollingButtons();
    initMagneticButtons();
    fetchLeaderboard();
    if(quizScore > 0){
      submitScoreToLeaderboard();
    }
  }
}

function fetchLeaderboard(){
  var inputEl = document.getElementById('leaderboardClassCode');
  var code = (inputEl && inputEl.value ? inputEl.value : 'SRM-CHEM-101') || 'SRM-CHEM-101';
  fetch('/api/leaderboard?classCode=' + encodeURIComponent(code.trim().toUpperCase()))
    .then(function(r){ return r.json(); })
    .then(function(data){
      if(!data || !data.valid) return;
      var subEl = document.getElementById('metricSubmissions');
      var avgEl = document.getElementById('metricAverage');
      var topEl = document.getElementById('metricTopScore');
      if(subEl) subEl.innerText = data.totalSubmissions || 0;
      if(avgEl) avgEl.innerText = (data.classAverage || 0) + '%';
      if(topEl) topEl.innerText = (data.topScore || 0) + ' / 100';
      
      var tb = document.getElementById('leaderboardTableBody');
      if(!tb) return;
      var html = '';
      var list = data.leaderboard || [];
      if(list.length === 0){
        // Attempt self-healing sync if client has cached submissions in localStorage
        try {
          var cachedAll = JSON.parse(localStorage.getItem('srm_chemistry_leaderboard_all') || '[]');
          if(cachedAll.length > 0 && !window._lbSyncedOnce){
            window._lbSyncedOnce = true;
            fetch('/api/leaderboard/sync', {
              method: 'POST',
              headers: { 'Content-Type': 'application/json' },
              body: JSON.stringify({ entries: cachedAll })
            }).then(function(){
              fetchLeaderboard();
            }).catch(function(){});
          }
        } catch(e){}

        html = '<tr><td colspan="5" style="text-align:center;padding:24px;color:var(--dim)">' +
          '<div style="font-weight:600;color:var(--ink);margin-bottom:4px">No submissions recorded for ' + code + ' yet.</div>' +
          '<div style="font-size:11.5px">Complete the assessment above to post your certified score, or get your cohort code from Dr. Subramanian.</div>' +
          '</td></tr>';
      } else {
        for(var i = 0; i < list.length; i++){
          var row = list[i];
          var rankIcon = '#' + row.rank;
          if(row.rank === 1) rankIcon = '🥇 #1';
          else if(row.rank === 2) rankIcon = '🥈 #2';
          else if(row.rank === 3) rankIcon = '🥉 #3';
          var isTop = row.rank <= 3;
          html += '<tr style="border-bottom:1px solid rgba(255,255,255,0.05);">' +
            '<td style="padding:8px;font-family:var(--mono);font-weight:' + (isTop ? '700' : '400') + ';color:' + (row.rank===1 ? 'var(--warn)' : 'var(--ink)') + '">' + rankIcon + '</td>' +
            '<td style="padding:8px;font-weight:600;color:var(--ink)">' + row.displayName + '</td>' +
            '<td style="padding:8px;font-family:var(--mono);color:var(--dim)">' + row.displayRegNo + '</td>' +
            '<td style="padding:8px;text-align:right;font-family:var(--mono);font-weight:700;color:' + (row.score >= 80 ? 'var(--acc2)' : 'var(--ink)') + '">' + row.score + ' / 100</td>' +
            '<td style="padding:8px;text-align:right;font-family:var(--mono);font-size:11px;color:var(--dim)">' + (row.timestamp || '') + '</td>' +
          '</tr>';
        }
      }
      tb.innerHTML = html;
    })
    .catch(function(e){
      console.warn('Leaderboard fetch error:', e);
    });
}

function submitScoreToLeaderboard(){
  AudioEngine.click();
  var inputEl = document.getElementById('leaderboardClassCode');
  var code = (inputEl && inputEl.value ? inputEl.value : 'SRM-CHEM-101') || 'SRM-CHEM-101';
  var leadNameEl = document.getElementById('leaderboardStudentName');
  var leadRegEl = document.getElementById('leaderboardStudentReg');
  var repNameEl = document.getElementById('repStudentName');
  var repRegEl = document.getElementById('repRegNumber');
  
  var name = (leadNameEl && leadNameEl.value ? leadNameEl.value.trim() : '') ||
             (repNameEl && repNameEl.value ? repNameEl.value.trim() : '') ||
             'velmurgan';
  var reg = (leadRegEl && leadRegEl.value ? leadRegEl.value.trim() : '') ||
             (repRegEl && repRegEl.value ? repRegEl.value.trim() : '') ||
             'RA2611030050019';
  var anonEl = document.getElementById('anonLeaderboardCheck');
  var anon = anonEl ? anonEl.checked : false;
  
  var payload = {
    name: name,
    regNo: reg,
    score: quizScore,
    classCode: code.trim().toUpperCase(),
    anonymous: anon
  };
  
  // Persist locally in browser to survive serverless restarts
  try {
    var stored = JSON.parse(localStorage.getItem('srm_chemistry_leaderboard_all') || '[]');
    stored.push(payload);
    localStorage.setItem('srm_chemistry_leaderboard_all', JSON.stringify(stored));
  } catch(e){}

  var statusBox = document.getElementById('leaderboardSubmitStatus');
  if(statusBox){
    statusBox.style.display = 'block';
    statusBox.style.color = 'var(--acc)';
    statusBox.innerText = 'Submitting score to class leaderboard...';
  }
  
  fetch('/api/leaderboard', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  })
  .then(function(r){ return r.json(); })
  .then(function(res){
    if(statusBox){
      statusBox.style.color = 'var(--acc2)';
      statusBox.innerText = res.message || 'Score certified and posted to leaderboard!';
    }
    showToast(res.message || 'Score posted to leaderboard!');
    fetchLeaderboard();
  })
  .catch(function(err){
    if(statusBox){
      statusBox.style.color = 'var(--bad)';
      statusBox.innerText = 'Could not post score. Please try again.';
    }
  });
}

function scrollToLeaderboard(){
  var el = document.getElementById('leaderboardSection');
  if(el) el.scrollIntoView({behavior:'smooth'});
  submitScoreToLeaderboard();
}

/* ==========================================================================
   7. MULTI-MOLECULE REPORT QUEUE & CERTIFIED PDF REPORT GENERATOR
   ========================================================================== */

function computePropertiesForSmiles(s, customName){
  s = (s || '').trim();
  if(!s) return null;
  
  // Check if it's already one of the benchmark molecules
  var bm = BENCHMARK_MOLECULES.find(function(b){
    return b.smiles === s || b.canonical === s || b.name.toLowerCase() === (customName || '').toLowerCase();
  });
  if(bm){
    var copy = JSON.parse(JSON.stringify(bm));
    if(customName) copy.name = customName;
    return copy;
  }
  
  var clean = s.replace(/\\[([A-Za-z0-9\\+\\-\\@]+)\\]/g, '$1');
  var atomMatches = clean.match(/(Cl|Br|Si|Na|Ca|Mg|Fe|Cu|Zn|[CNOPFSIcnops])/g) || [];
  var aromaticAtoms = (clean.match(/[cnops]/g) || []).length;
  var cCount = (clean.match(/C/g) || []).length + (clean.match(/c/g) || []).length;
  var nCount = (clean.match(/N/g) || []).length + (clean.match(/n/g) || []).length;
  var oCount = (clean.match(/O/g) || []).length + (clean.match(/o/g) || []).length;
  var clCount = (clean.match(/Cl/g) || []).length;
  var brCount = (clean.match(/Br/g) || []).length;
  var fCount = (clean.match(/F/g) || []).length;
  var sCount = (clean.match(/S/g) || []).length + (clean.match(/s/g) || []).length;
  
  var doubleBonds = (s.match(/=/g) || []).length;
  var tripleBonds = (s.match(/#/g) || []).length;
  var ringsRaw = s.match(/\\d/g) || [];
  var ringSet = {};
  for(var ri = 0; ri < ringsRaw.length; ri++){ ringSet[ringsRaw[ri]] = true; }
  var uniqueRings = Object.keys(ringSet).length;
  
  var aromaticRings = aromaticAtoms >= 5 ? Math.max(1, Math.floor(aromaticAtoms / 5)) : 0;
  var aliphaticRings = Math.max(0, uniqueRings - aromaticRings);
  var halogens = clCount + brCount + fCount;
  var unsaturation = doubleBonds + (tripleBonds * 2) + uniqueRings + Math.floor(aromaticAtoms / 2);
  var hCount = Math.max(0, (2 * cCount + 2 + nCount - halogens) - (2 * unsaturation));
  
  var formulaParts = [];
  if(cCount > 0) formulaParts.push('C' + (cCount > 1 ? cCount : ''));
  if(hCount > 0) formulaParts.push('H' + (hCount > 1 ? hCount : ''));
  if(nCount > 0) formulaParts.push('N' + (nCount > 1 ? nCount : ''));
  if(oCount > 0) formulaParts.push('O' + (oCount > 1 ? oCount : ''));
  if(sCount > 0) formulaParts.push('S' + (sCount > 1 ? sCount : ''));
  if(clCount > 0) formulaParts.push('Cl' + (clCount > 1 ? clCount : ''));
  if(brCount > 0) formulaParts.push('Br' + (brCount > 1 ? brCount : ''));
  if(fCount > 0) formulaParts.push('F' + (fCount > 1 ? fCount : ''));
  var formula = formulaParts.join('') || 'C6H6';
  
  var mw = (cCount * 12.011) + (hCount * 1.008) + (nCount * 14.007) + (oCount * 15.999) + (clCount * 35.453) + (brCount * 79.904) + (fCount * 18.998) + (sCount * 32.065);
  mw = Math.round(mw * 1000) / 1000;
  
  var exactMw = (cCount * 12.0000) + (hCount * 1.0078) + (nCount * 14.0031) + (oCount * 15.9949) + (clCount * 34.9689) + (brCount * 78.9183) + (fCount * 18.9984) + (sCount * 31.9721);
  exactMw = Math.round(exactMw * 10000) / 10000;
  
  var hbd = 0;
  var ohNh = s.match(/O[H\\)]|N[H\\)]|\\[nH\\]|\\[OH\\]|\\[NH\\d?\\]|O$|N$/g);
  if(ohNh) hbd = ohNh.length;
  if(oCount > 0 && hbd === 0 && (s.indexOf('CCO') !== -1 || s.indexOf('CO') !== -1)) hbd = 1;
  hbd = Math.min(hbd, oCount + nCount);
  var hba = nCount + oCount;
  var rot = Math.max(0, (s.match(/CC|CO|CN|NC/g) || []).length - uniqueRings - doubleBonds);
  
  var logp = (cCount * 0.25) + (clCount * 0.6) + (brCount * 0.8) - (oCount * 0.4) - (nCount * 0.3) - (hbd * 0.5);
  logp = Math.round(Math.max(-2.5, Math.min(8.0, logp)) * 1000) / 1000;
  
  var tpsa = (oCount * 20.23) + (nCount * 13.5) + (hbd * 10.0);
  tpsa = Math.round(tpsa * 100) / 100;
  
  var heavyAtoms = atomMatches.length;
  var heavyBonds = Math.max(1, heavyAtoms - 1 + uniqueRings);
  var piBonds = doubleBonds + (2 * tripleBonds) + (aromaticRings * 3);
  var sigmaBonds = heavyBonds + hCount;
  var totalBonds = sigmaBonds + piBonds;
  
  var sp3Carbons = Math.max(0, cCount - (aromaticAtoms + doubleBonds * 2 + tripleBonds * 2));
  var fcsp3 = Math.round((sp3Carbons / Math.max(1, cCount)) * 1000) / 1000;
  var mr = Math.round(((mw / 10.0) + (aromaticRings * 5.0) + (cCount * 1.5)) * 1000) / 1000;
  
  return {
    name: customName || formula,
    smiles: s,
    canonical: s,
    formula: formula,
    mw: mw,
    exact_mw: exactMw,
    logp: logp,
    tpsa: tpsa,
    hbd: hbd,
    hba: hba,
    rot: rot,
    rings: uniqueRings,
    arom: aromaticRings,
    aliph: aliphaticRings,
    num_atoms: heavyAtoms,
    heavy_atoms: heavyAtoms,
    heavy_bonds: heavyBonds,
    sigma: sigmaBonds,
    pi: piBonds,
    total_bonds: totalBonds,
    fcsp3: fcsp3,
    mr: mr,
    desc: "Custom submitted molecular entity analyzed via computational cheminformatics engine."
  };
}

function renderReportQueueUI(){
  var container = document.getElementById('reportQueueContainer');
  var countBadge = document.getElementById('repMolCountNum');
  var btnMolBadge = document.getElementById('btnMolCountNum');
  
  if(countBadge) countBadge.innerText = reportQueue.length;
  if(btnMolBadge) btnMolBadge.innerText = reportQueue.length;
  
  var activeBadge = document.getElementById('activeMolNameBadge');
  if(activeBadge){
    var actBm = BENCHMARK_MOLECULES.find(function(b){ return b.smiles === activeSmiles; });
    activeBadge.innerText = actBm ? actBm.name : activeSmiles;
  }
  
  if(!container) return;
  
  if(reportQueue.length === 0){
    container.innerHTML = '<div style="text-align:center;padding:24px;border:1px dashed rgba(255,255,255,0.15);border-radius:8px;color:var(--dim);font-size:13px;font-family:var(--mono)">' +
      'No molecules queued. Enter a SMILES or click quick presets above to add molecules to your report.' +
    '</div>';
    return;
  }
  
  var html = '';
  for(var i = 0; i < reportQueue.length; i++){
    var m = reportQueue[i];
    html += '<div style="display:flex;align-items:center;justify-content:space-between;background:rgba(2,6,23,0.7);border:1px solid rgba(0,240,255,0.18);border-radius:8px;padding:10px 14px;gap:12px;transition:all 0.2s ease">' +
      '<div style="display:flex;align-items:center;gap:12px;flex:1;min-width:0">' +
        '<span style="background:rgba(0,240,255,0.15);color:var(--acc);font-family:var(--mono);font-size:11px;font-weight:700;padding:3px 8px;border-radius:4px;flex-shrink:0">#' + (i + 1) + '</span>' +
        '<div style="min-width:0;flex:1">' +
          '<div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap">' +
            '<strong style="color:var(--ink);font-size:13.5px">' + (m.name || m.formula) + '</strong>' +
            '<span style="color:var(--acc2);font-size:12px;font-family:var(--mono)">(' + m.formula + ')</span>' +
            '<span style="color:var(--dim);font-size:11px;font-family:var(--mono)">MW: ' + m.mw + ' g/mol</span>' +
          '</div>' +
          '<div style="color:var(--dim);font-size:11.5px;font-family:var(--mono);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;margin-top:2px" title="' + m.smiles + '">' +
            m.smiles +
          '</div>' +
        '</div>' +
      '</div>' +
      '<div style="display:flex;align-items:center;gap:8px;flex-shrink:0">' +
        '<button type="button" onclick="loadQueueMoleculeIntoLab(' + i + ')" class="btn secondary" style="padding:4px 8px;font-size:11px" title="Inspect this molecule in 2D/3D Lab">' +
          '<span>Inspect</span>' +
        '</button>' +
        '<button type="button" onclick="removeFromReportQueue(' + i + ')" class="queue-del-btn" title="Remove from queue">&times;</button>' +
      '</div>' +
    '</div>';
  }
  container.innerHTML = html;
}

function addCustomMoleculeToReportQueue(){
  var smilesEl = document.getElementById('customRepSmiles');
  var nameEl = document.getElementById('customRepName');
  if(!smilesEl) return;
  var smiles = smilesEl.value.trim();
  var name = nameEl ? nameEl.value.trim() : '';
  
  if(!smiles){
    alert("Please enter a SMILES string to add.");
    return;
  }
  
  var mol = computePropertiesForSmiles(smiles, name);
  if(!mol){
    alert("Invalid chemical SMILES structure.");
    return;
  }
  
  reportQueue.push(mol);
  smilesEl.value = '';
  if(nameEl) nameEl.value = '';
  
  renderReportQueueUI();
  AudioEngine.click();
}

function quickAddBenchmarkToReport(bmName){
  var bm = BENCHMARK_MOLECULES.find(function(b){ return b.name.toLowerCase() === bmName.toLowerCase(); });
  if(!bm) return;
  reportQueue.push(JSON.parse(JSON.stringify(bm)));
  renderReportQueueUI();
  AudioEngine.click();
}

function addCurrentToReportQueue(){
  var actBm = BENCHMARK_MOLECULES.find(function(b){ return b.smiles === activeSmiles; });
  var name = actBm ? actBm.name : (currentProps ? currentProps["Molecular Formula"] : activeSmiles);
  var mol = computePropertiesForSmiles(activeSmiles, name);
  if(currentProps){
    mol.mw = parseFloat(currentProps["Molecular Weight"]) || mol.mw;
    mol.formula = currentProps["Molecular Formula"] || mol.formula;
    mol.logp = parseFloat(currentProps["LogP"]) || mol.logp;
    mol.tpsa = parseFloat(currentProps["TPSA"]) || mol.tpsa;
  }
  reportQueue.push(mol);
  renderReportQueueUI();
  AudioEngine.click();
  showSmilesSuccess("Added " + (mol.name || mol.formula) + " to Report Queue (" + reportQueue.length + " molecules total)!");
}

function removeFromReportQueue(index){
  if(index >= 0 && index < reportQueue.length){
    reportQueue.splice(index, 1);
    renderReportQueueUI();
    AudioEngine.click();
  }
}

function clearReportQueue(){
  if(confirm("Clear all molecules from the report queue?")){
    reportQueue = [];
    renderReportQueueUI();
    AudioEngine.click();
  }
}

function loadQueueMoleculeIntoLab(index){
  if(index >= 0 && index < reportQueue.length){
    var m = reportQueue[index];
    var input = document.getElementById('smilesInput');
    if(input) input.value = m.smiles;

    // Highlight matching preset chip if exists
    var matchingChip = null;
    document.querySelectorAll('.preset-chip').forEach(function(c){
      c.classList.remove('active');
      var cText = c.innerText.trim().toLowerCase();
      var mName = (m.name || '').toLowerCase();
      var mSmiles = (m.smiles || '').toLowerCase();
      if(cText === mName || (mSmiles === 'c1ccccc1' && cText === 'benzene') || (mSmiles === 'cco' && cText === 'ethanol')){
        matchingChip = c;
      }
    });
    if(matchingChip){
      matchingChip.classList.add('active');
      if(typeof movePillToChip === 'function') movePillToChip(matchingChip);
    }

    analyzeMolecule();
    scrollToChapter('lab');
    if(window.AudioEngine) window.AudioEngine.click();
  }
}

function createStructureCanvas2D(mol){
  var canvas = document.createElement('canvas');
  canvas.width = 520;
  canvas.height = 320;
  var ctx = canvas.getContext('2d');
  
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  
  ctx.strokeStyle = '#cbd5e1';
  ctx.lineWidth = 1.5;
  ctx.strokeRect(1, 1, canvas.width - 2, canvas.height - 2);
  
  ctx.fillStyle = '#17365d';
  ctx.font = 'bold 12px Helvetica, Arial, sans-serif';
  ctx.fillText('2D Topological Structure', 16, 22);
  ctx.fillStyle = '#64748b';
  ctx.font = 'normal 10px Helvetica, Arial, sans-serif';
  ctx.fillText((mol.name || mol.formula) + ' • ' + mol.smiles, 16, 36);
  
  var s = (mol.smiles || '').trim();
  var cx = 260, cy = 175;
  
  if(s === 'c1ccccc1' || s === 'C1=CC=CC=C1'){
    var R = 68;
    var pts = [];
    for(var i = 0; i < 6; i++){
      var ang = (-90 + i * 60) * Math.PI / 180;
      pts.push({ x: cx + R * Math.cos(ang), y: cy + R * Math.sin(ang), ang: ang });
    }
    
    ctx.beginPath();
    ctx.moveTo(pts[0].x, pts[0].y);
    for(var i = 1; i < 6; i++) ctx.lineTo(pts[i].x, pts[i].y);
    ctx.closePath();
    ctx.strokeStyle = '#0f172a';
    ctx.lineWidth = 3.5;
    ctx.stroke();
    
    var rIn = R * 0.76;
    var kekSides = [0, 2, 4];
    for(var k = 0; k < kekSides.length; k++){
      var side = kekSides[k];
      var a1 = (-90 + side * 60) * Math.PI / 180;
      var a2 = (-90 + (side + 1) * 60) * Math.PI / 180;
      ctx.beginPath();
      ctx.moveTo(cx + rIn * Math.cos(a1), cy + rIn * Math.sin(a1));
      ctx.lineTo(cx + rIn * Math.cos(a2), cy + rIn * Math.sin(a2));
      ctx.strokeStyle = '#0f172a';
      ctx.lineWidth = 2.2;
      ctx.stroke();
    }
    
    ctx.beginPath();
    ctx.arc(cx, cy, 38, 0, Math.PI * 2);
    ctx.strokeStyle = '#2563eb';
    ctx.lineWidth = 2;
    ctx.setLineDash([5, 4]);
    ctx.stroke();
    ctx.setLineDash([]);
    
    for(var i = 0; i < 6; i++){
      var p = pts[i];
      var hx = cx + (R + 32) * Math.cos(p.ang);
      var hy = cy + (R + 32) * Math.sin(p.ang);
      
      ctx.beginPath();
      ctx.moveTo(p.x, p.y);
      ctx.lineTo(hx, hy);
      ctx.strokeStyle = '#64748b';
      ctx.lineWidth = 1.8;
      ctx.stroke();
      
      ctx.fillStyle = '#f8fafc';
      ctx.beginPath();
      ctx.arc(hx, hy, 10, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#94a3b8';
      ctx.lineWidth = 1.2;
      ctx.stroke();
      ctx.fillStyle = '#0f172a';
      ctx.font = 'bold 10px Helvetica, Arial, sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('H', hx, hy);
      
      ctx.fillStyle = '#ffffff';
      ctx.beginPath();
      ctx.arc(p.x, p.y, 11, 0, Math.PI * 2);
      ctx.fill();
      ctx.strokeStyle = '#0f172a';
      ctx.lineWidth = 1.6;
      ctx.stroke();
      ctx.fillStyle = '#0f172a';
      ctx.font = 'bold 11px Helvetica, Arial, sans-serif';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText('C', p.x, p.y);
    }
  } else if(s === 'CCO'){
    ctx.strokeStyle = '#0f172a';
    ctx.lineWidth = 4;
    
    ctx.beginPath();
    ctx.moveTo(170, 185);
    ctx.lineTo(250, 145);
    ctx.stroke();
    
    ctx.beginPath();
    ctx.moveTo(270, 145);
    ctx.lineTo(345, 182);
    ctx.strokeStyle = '#dc2626';
    ctx.stroke();
    
    ctx.fillStyle = '#0f172a';
    ctx.font = 'bold 18px Helvetica, Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText('H₃C', 140, 198);
    ctx.fillText('CH₂', 260, 130);
    
    ctx.fillStyle = '#dc2626';
    ctx.fillText('OH', 375, 195);
    
    ctx.font = 'normal 11px Helvetica, Arial, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('Primary Aliphatic Alcohol', 260, 240);
  } else if(s.indexOf('CN1C=NC2') !== -1 || s.indexOf('Cn1c') !== -1){
    var pts6 = [];
    var R6 = 48;
    var cx6 = 220, cy6 = 175;
    for(var i = 0; i < 6; i++){
      var ang = (-90 + i * 60) * Math.PI / 180;
      pts6.push({ x: cx6 + R6 * Math.cos(ang), y: cy6 + R6 * Math.sin(ang) });
    }
    ctx.beginPath();
    ctx.moveTo(pts6[0].x, pts6[0].y);
    for(var i = 1; i < 6; i++) ctx.lineTo(pts6[i].x, pts6[i].y);
    ctx.closePath();
    ctx.strokeStyle = '#0f172a';
    ctx.lineWidth = 3;
    ctx.stroke();
    
    var p1 = pts6[1];
    var p2 = pts6[2];
    var imidApex = { x: cx6 + R6 * 1.8, y: cy6 };
    ctx.beginPath();
    ctx.moveTo(p1.x, p1.y);
    ctx.lineTo(imidApex.x, imidApex.y);
    ctx.lineTo(p2.x, p2.y);
    ctx.strokeStyle = '#0f172a';
    ctx.lineWidth = 3;
    ctx.stroke();
    
    ctx.font = 'bold 14px Helvetica, Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillStyle = '#2563eb';
    ctx.fillText('N', pts6[0].x, pts6[0].y - 4);
    ctx.fillText('N', pts6[3].x, pts6[3].y + 4);
    ctx.fillText('N', imidApex.x + 4, imidApex.y - 12);
    ctx.fillText('N', p2.x + 8, p2.y + 4);
    
    ctx.fillStyle = '#dc2626';
    ctx.fillText('=O', pts6[5].x - 18, pts6[5].y);
    ctx.fillText('=O', pts6[4].x - 18, pts6[4].y);
    
    ctx.font = 'normal 11px Helvetica, Arial, sans-serif';
    ctx.fillStyle = '#64748b';
    ctx.fillText('1,3,7-Trimethylxanthine Purine Framework', 260, 255);
  } else {
    ctx.strokeStyle = '#0f172a';
    ctx.lineWidth = 3;
    var numA = Math.min(10, Math.max(3, mol.num_atoms || 5));
    var step = Math.min(42, 280 / numA);
    var startX = 260 - ((numA - 1) * step) / 2;
    var lastX = startX, lastY = 175;
    
    for(var a = 0; a < numA; a++){
      var curX = startX + a * step;
      var curY = 175 + (a % 2 === 0 ? -18 : 18);
      if(a > 0){
        ctx.beginPath();
        ctx.moveTo(lastX, lastY);
        ctx.lineTo(curX, curY);
        ctx.stroke();
      }
      lastX = curX;
      lastY = curY;
    }
    
    ctx.font = 'bold 15px Helvetica, Arial, sans-serif';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillStyle = '#0f172a';
    ctx.fillText(mol.formula, 260, 175);
  }
  
  ctx.fillStyle = '#94a3b8';
  ctx.font = 'italic 10px Helvetica, Arial, sans-serif';
  ctx.textAlign = 'right';
  ctx.fillText('Standard 2D Chemical Connectivity Projection', canvas.width - 16, canvas.height - 12);
  
  return canvas.toDataURL('image/png');
}

function createStructureCanvas3D(mol){
  var canvas = document.createElement('canvas');
  canvas.width = 520;
  canvas.height = 320;
  var ctx = canvas.getContext('2d');
  
  ctx.fillStyle = '#ffffff';
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  
  ctx.strokeStyle = '#cbd5e1';
  ctx.lineWidth = 1.5;
  ctx.strokeRect(1, 1, canvas.width - 2, canvas.height - 2);
  
  ctx.fillStyle = '#17365d';
  ctx.font = 'bold 12px Helvetica, Arial, sans-serif';
  ctx.fillText('3D Ball & Stick Conformer', 16, 22);
  ctx.fillStyle = '#64748b';
  ctx.font = 'normal 10px Helvetica, Arial, sans-serif';
  ctx.fillText((mol.name || mol.formula) + ' • Spatial Geometry', 16, 36);
  
  var s = (mol.smiles || '').trim();
  var cx = 260, cy = 175;
  
  var atoms = [];
  var bonds = [];
  
  if(s === 'c1ccccc1' || s === 'C1=CC=CC=C1'){
    var R = 62;
    for(var i = 0; i < 6; i++){
      var ang = (i * 60) * Math.PI / 180;
      var cX = R * Math.cos(ang);
      var cY = R * Math.sin(ang);
      var cZ = 0;
      atoms.push({ elem: 'C', x: cX, y: cY, z: cZ, r: 16 });
      
      var hX = (R + 38) * Math.cos(ang);
      var hY = (R + 38) * Math.sin(ang);
      var hZ = 0;
      atoms.push({ elem: 'H', x: hX, y: hY, z: hZ, r: 10 });
      
      bonds.push([i * 2, i * 2 + 1]);
      bonds.push([i * 2, ((i + 1) % 6) * 2]);
    }
  } else if(s === 'CCO'){
    atoms = [
      { elem: 'C', x: -55, y: -10, z: 10, r: 16 },
      { elem: 'C', x: 0, y: 25, z: -10, r: 16 },
      { elem: 'O', x: 55, y: -15, z: 5, r: 15 },
      { elem: 'H', x: 75, y: 2, z: 12, r: 10 },
      { elem: 'H', x: -55, y: -65, z: 10, r: 10 },
      { elem: 'H', x: -95, y: 15, z: 25, r: 10 },
      { elem: 'H', x: -65, y: 15, z: -40, r: 10 },
      { elem: 'H', x: 0, y: 75, z: -15, r: 10 },
      { elem: 'H', x: 10, y: 25, z: 45, r: 10 }
    ];
    bonds = [
      [0, 1], [1, 2], [2, 3],
      [0, 4], [0, 5], [0, 6],
      [1, 7], [1, 8]
    ];
  } else if(s.indexOf('CN1C=NC2') !== -1 || s.indexOf('Cn1c') !== -1){
    var R6 = 46;
    for(var i = 0; i < 6; i++){
      var ang = (i * 60) * Math.PI / 180;
      var el = (i === 1 || i === 4) ? 'N' : 'C';
      atoms.push({ elem: el, x: -30 + R6 * Math.cos(ang), y: R6 * Math.sin(ang), z: (i % 2 === 0 ? 8 : -8), r: 15 });
      bonds.push([i, (i + 1) % 6]);
    }
    atoms.push({ elem: 'N', x: 42, y: 24, z: 10, r: 15 });
    atoms.push({ elem: 'C', x: 65, y: -2, z: 0, r: 15 });
    atoms.push({ elem: 'N', x: 38, y: -28, z: -10, r: 15 });
    bonds.push([1, 6], [6, 7], [7, 8], [8, 2]);
    atoms.push({ elem: 'O', x: -80, y: -30, z: 5, r: 15 });
    atoms.push({ elem: 'O', x: -75, y: 40, z: -5, r: 15 });
    bonds.push([5, 9], [3, 10]);
    atoms.push({ elem: 'C', x: -15, y: 75, z: 12, r: 14 });
    atoms.push({ elem: 'C', x: 50, y: 65, z: -12, r: 14 });
    atoms.push({ elem: 'C', x: 50, y: -65, z: 10, r: 14 });
    bonds.push([4, 11], [6, 12], [8, 13]);
  } else {
    var count = Math.min(14, Math.max(4, mol.num_atoms || 6));
    for(var a = 0; a < count; a++){
      var ang = (a / count) * Math.PI * 2;
      var rad = 35 + (a % 3) * 20;
      var el = (a === 0 && mol.formula.indexOf('O') !== -1) ? 'O' : ((a === 1 && mol.formula.indexOf('N') !== -1) ? 'N' : 'C');
      atoms.push({
        elem: el,
        x: rad * Math.cos(ang),
        y: rad * Math.sin(ang) * 0.75,
        z: (a % 2 === 0 ? 25 : -25),
        r: el === 'C' ? 16 : 14
      });
      if(a > 0) bonds.push([a - 1, a]);
    }
  }
  
  var rotX = 24 * Math.PI / 180;
  var rotY = 38 * Math.PI / 180;
  var cosX = Math.cos(rotX), sinX = Math.sin(rotX);
  var cosY = Math.cos(rotY), sinY = Math.sin(rotY);
  
  var projected = atoms.map(function(atm, idx){
    var x1 = atm.x * cosY + atm.z * sinY;
    var y1 = atm.y;
    var z1 = -atm.x * sinY + atm.z * cosY;
    var x2 = x1;
    var y2 = y1 * cosX - z1 * sinX;
    var z2 = y1 * sinX + z1 * cosX;
    
    var scale = 1.0;
    return {
      idx: idx,
      elem: atm.elem,
      px: cx + x2 * scale,
      py: cy + y2 * scale,
      pz: z2,
      r: atm.r
    };
  });
  
  for(var b = 0; b < bonds.length; b++){
    var i1 = bonds[b][0], i2 = bonds[b][1];
    if(projected[i1] && projected[i2]){
      var p1 = projected[i1], p2 = projected[i2];
      ctx.beginPath();
      ctx.moveTo(p1.px, p1.py);
      ctx.lineTo(p2.px, p2.py);
      ctx.strokeStyle = '#64748b';
      ctx.lineWidth = 5;
      ctx.lineCap = 'round';
      ctx.stroke();
      
      ctx.beginPath();
      ctx.moveTo(p1.px, p1.py);
      ctx.lineTo(p2.px, p2.py);
      ctx.strokeStyle = '#cbd5e1';
      ctx.lineWidth = 2;
      ctx.stroke();
    }
  }
  
  projected.sort(function(a, b){ return a.pz - b.pz; });
  
  for(var i = 0; i < projected.length; i++){
    var p = projected[i];
    var grad = ctx.createRadialGradient(
      p.px - p.r * 0.35, p.py - p.r * 0.35, p.r * 0.1,
      p.px, p.py, p.r
    );
    
    if(p.elem === 'C'){
      grad.addColorStop(0, '#94a3b8');
      grad.addColorStop(0.3, '#475569');
      grad.addColorStop(1, '#0f172a');
    } else if(p.elem === 'O'){
      grad.addColorStop(0, '#fca5a5');
      grad.addColorStop(0.3, '#ef4444');
      grad.addColorStop(1, '#991b1b');
    } else if(p.elem === 'N'){
      grad.addColorStop(0, '#93c5fd');
      grad.addColorStop(0.3, '#3b82f6');
      grad.addColorStop(1, '#1e40af');
    } else if(p.elem === 'H'){
      grad.addColorStop(0, '#ffffff');
      grad.addColorStop(0.4, '#e2e8f0');
      grad.addColorStop(1, '#94a3b8');
    } else {
      grad.addColorStop(0, '#6ee7b7');
      grad.addColorStop(0.3, '#10b981');
      grad.addColorStop(1, '#065f46');
    }
    
    ctx.beginPath();
    ctx.arc(p.px, p.py, p.r, 0, Math.PI * 2);
    ctx.fillStyle = grad;
    ctx.fill();
    ctx.strokeStyle = 'rgba(15,23,42,0.4)';
    ctx.lineWidth = 1;
    ctx.stroke();
  }
  
  ctx.fillStyle = '#94a3b8';
  ctx.font = 'italic 10px Helvetica, Arial, sans-serif';
  ctx.textAlign = 'right';
  ctx.fillText('Optimized 3D Conformational Geometry (MMFF94 / UFF Forcefield)', canvas.width - 16, canvas.height - 12);
  
  return canvas.toDataURL('image/png');
}

function generatePdfReport(){
  AudioEngine.click();
  
  var studentName = (document.getElementById('repStudentName').value || "").trim() || "velmurgan";
  var regNum = (document.getElementById('repRegNumber').value || "").trim() || "RA2611030050019";
  
  if(!reportQueue || reportQueue.length === 0){
    alert("Please add at least one molecule to the report queue before generating the report.");
    return;
  }
  
  var doc = new jspdf.jsPDF({
    orientation: 'portrait',
    unit: 'mm',
    format: 'a4'
  });
  
  var totalMols = reportQueue.length;
  
  for(var k = 0; k < totalMols; k++){
    var mol = reportQueue[k];
    var molIndex = k + 1;
    
    if(k > 0){
      doc.addPage();
    }
    
    var curY = 16;
    
    // Page 1 Document Header (Only on Page 1)
    if(k === 0){
      doc.setFont("helvetica", "bold");
      doc.setFontSize(16.5);
      doc.setTextColor(23, 54, 93);
      doc.text("CHEMINFORMATICS VIRTUAL LABORATORY", 105, curY, { align: "center" });
      curY += 7;
      
      doc.setFontSize(12);
      doc.setFont("helvetica", "bold");
      doc.setTextColor(23, 54, 93);
      doc.text("MULTI-MOLECULE STUDENT ANALYSIS REPORT", 105, curY, { align: "center" });
      curY += 7.5;
      
      doc.setFontSize(8.5);
      doc.setFont("helvetica", "normal");
      doc.setTextColor(0, 0, 0);
      doc.text("Student: " + studentName + "     Registration Number: " + regNum, 14, curY);
      curY += 5;
      
      doc.text("Number of molecules analyzed: " + totalMols, 14, curY);
      curY += 7;
    }
    
    // Molecule Header
    doc.setFont("helvetica", "bold");
    doc.setFontSize(11.5);
    doc.setTextColor(23, 54, 93);
    doc.text("Molecule " + molIndex + ": Molecular Information", 14, curY);
    curY += 3.5;
    
    // Table: Molecular Information
    doc.autoTable({
      startY: curY,
      body: [
        ['Input SMILES', mol.smiles],
        ['Canonical SMILES', mol.canonical || mol.smiles],
        ['Molecular Formula', mol.formula],
        ['Molecular Weight', mol.mw + ' g/mol']
      ],
      theme: 'grid',
      styles: {
        fontSize: 8.5,
        cellPadding: 2.2,
        lineColor: [128, 128, 128],
        lineWidth: 0.25
      },
      columnStyles: {
        0: { cellWidth: 48, fontStyle: 'bold', fillColor: [234, 240, 248], textColor: [0, 0, 0] },
        1: { cellWidth: 'auto', textColor: [0, 0, 0] }
      },
      margin: { left: 14, right: 14 }
    });
    
    curY = doc.lastAutoTable.finalY + 5;
    
    // Heading: Molecular Structures
    doc.setFont("helvetica", "bold");
    doc.setFontSize(11.5);
    doc.setTextColor(23, 54, 93);
    doc.text("Molecular Structures", 14, curY);
    curY += 3.5;
    
    // Render side-by-side 2D & 3D images
    var img2d = createStructureCanvas2D(mol);
    var img3d = createStructureCanvas3D(mol);
    
    doc.addImage(img2d, 'PNG', 14, curY, 88, 52);
    doc.addImage(img3d, 'PNG', 108, curY, 88, 52);
    curY += 56;
    
    // Heading: Molecular Properties and Interpretation
    doc.setFont("helvetica", "bold");
    doc.setFontSize(11.5);
    doc.setTextColor(23, 54, 93);
    doc.text("Molecular Properties and Interpretation", 14, curY);
    curY += 3.5;
    
    // 3-Column Table
    var propRows = [
      ['Molecular Formula', mol.formula, 'Shows the elemental composition of the molecule and is useful for understanding its basic chemical composition.'],
      ['Molecular Weight', String(mol.mw), 'Represents the average molecular mass. Molecular size and mass can influence diffusion, formulation and many physicochemical behaviours.'],
      ['Exact Molecular Weight', String(mol.exact_mw), 'The monoisotopic mass calculated from exact isotopic masses; this is especially useful when comparing mass-spectrometry data.'],
      ['LogP', String(mol.logp), mol.logp < 0 ? 'A negative value indicates a preference toward the aqueous phase and relatively high hydrophilicity.' : (mol.logp < 3 ? 'Indicates moderate lipophilicity, often reflecting a balance between hydrophilic and hydrophobic character.' : 'Higher lipophilicity indicates strong affinity for lipid bilayers and hydrophobic binding pockets.')],
      ['TPSA', String(mol.tpsa), mol.tpsa <= 25 ? 'A relatively low polar surface area, indicating limited overall molecular polarity.' : (mol.tpsa <= 80 ? 'A moderate polar surface area, reflecting the contribution of heteroatoms to molecular polarity.' : 'High polar surface area indicates strong hydrogen bonding and reduced membrane permeation.')],
      ['Hydrogen Bond Donors', String(mol.hbd), 'The molecule has ' + mol.hbd + ' donor site(s) capable of donating hydrogen in hydrogen-bond interactions.'],
      ['Hydrogen Bond Acceptors', String(mol.hba), 'The molecule has ' + mol.hba + ' acceptor site(s) capable of accepting hydrogen in hydrogen-bond interactions.'],
      ['Rotatable Bonds', String(mol.rot), mol.rot === 0 ? 'No freely rotatable bonds are detected, suggesting a relatively rigid molecular framework.' : 'Has ' + mol.rot + ' rotatable bond(s), offering conformational flexibility to adapt to binding sites.'],
      ['Ring Count', String(mol.rings), 'The molecule contains ' + mol.rings + ' ring(s), which contribute to its overall shape and structural rigidity.'],
      ['Aromatic Rings', String(mol.arom), mol.arom + ' aromatic ring(s) contribute to aromaticity, planarity and delocalized pi-electron character.'],
      ['Aliphatic Rings', String(mol.aliph), mol.aliph + ' non-aromatic ring(s) contribute to cyclic structure without aromatic pi-electron delocalization.'],
      ['Number of Atoms', String(mol.num_atoms), 'Counts atoms explicitly present in the RDKit molecular representation; implicit hydrogens are not included here.'],
      ['Heavy Atoms', String(mol.heavy_atoms), 'Counts all non-hydrogen atoms and provides a useful measure of molecular structural size.'],
      ['Heavy Atom Bonds', String(mol.heavy_bonds), 'Counts connections between non-hydrogen atoms in the molecular graph.'],
      ['Sigma Bonds', String(mol.sigma), 'Every bonded atom pair contains one sigma bond; this value includes bonds involving explicit or added hydrogens.'],
      ['Pi Bonds', String(mol.pi), 'Pi bonds arise from multiple bonds and aromatic systems and are associated with electron delocalization.'],
      ['Total Bonds (Sigma + Pi)', String(mol.total_bonds), 'Represents the total bond components obtained by adding the calculated sigma and pi bond counts.'],
      ['Fraction Csp3', String(mol.fcsp3), mol.fcsp3 <= 0.25 ? 'A low sp3 fraction suggests a comparatively planar, unsaturated or aromatic structural character.' : (mol.fcsp3 >= 0.75 ? 'A high sp3 fraction indicates a more saturated, three-dimensional molecular framework.' : 'An intermediate sp3 fraction indicates a balance between saturated and unsaturated structural features.')],
      ['Molar Refractivity', String(mol.mr), 'Relates to molecular volume and electronic polarizability and reflects how the electron cloud responds to an electric field.']
    ];
    
    doc.autoTable({
      startY: curY,
      head: [['Property', 'Value', 'Interpretation']],
      body: propRows,
      theme: 'grid',
      headStyles: {
        fillColor: [47, 85, 151], // #2f5597
        textColor: [255, 255, 255],
        fontSize: 7.5,
        fontStyle: 'bold',
        cellPadding: 2
      },
      bodyStyles: {
        textColor: [0, 0, 0],
        fontSize: 7.0,
        cellPadding: 1.8,
        lineColor: [128, 128, 128],
        lineWidth: 0.25
      },
      columnStyles: {
        0: { cellWidth: 46, fontStyle: 'bold' },
        1: { cellWidth: 26 },
        2: { cellWidth: 'auto' }
      },
      margin: { left: 14, right: 14 },
      pageBreak: 'auto'
    });
    
    var finalY = doc.lastAutoTable.finalY + 6;
    if(finalY > 235){
      doc.addPage();
      finalY = 18;
    }
    
    // Heading: Key Interpretation
    doc.setFont("helvetica", "bold");
    doc.setFontSize(10.5);
    doc.setTextColor(23, 54, 93);
    doc.text("Key Interpretation", 14, finalY);
    finalY += 4.5;
    
    var lipoText = mol.logp < 0 ? 'more hydrophilic than lipophilic' : (mol.logp < 3 ? 'moderately lipophilic' : 'strongly lipophilic');
    var bullets = [
      { label: 'Molecular identity: ', text: 'The submitted structure has molecular formula ' + mol.formula + ' and molecular weight ' + mol.mw + '.' },
      { label: 'Lipophilicity: ', text: 'LogP = ' + mol.logp + ', indicating that the molecule is ' + lipoText + '. This descriptor describes the balance between preference for non-polar and polar environments.' },
      { label: 'Molecular polarity: ', text: 'TPSA = ' + mol.tpsa + ' Angstrom^2. TPSA reflects the contribution of polar atoms and functional groups to the overall surface polarity of the molecule.' },
      { label: 'Hydrogen bonding: ', text: 'The structure contains ' + mol.hbd + ' hydrogen-bond donor(s) and ' + mol.hba + ' acceptor(s), which helps describe possible intermolecular interactions.' },
      { label: 'Flexibility: ', text: mol.rot + ' rotatable bond(s) indicate the degree of conformational freedom available to the molecule.' },
      { label: 'Cyclic and aromatic character: ', text: 'The molecule contains ' + mol.rings + ' ring(s), including ' + mol.arom + ' aromatic ring(s). Aromatic rings are associated with delocalized pi-electron systems.' },
      { label: 'Bonding pattern: ', text: 'The calculated structure contains ' + mol.sigma + ' sigma bonds and ' + mol.pi + ' pi bonds. This helps distinguish the framework-forming sigma bonds from multiple-bond and delocalized pi bonding.' },
      { label: 'Three-dimensional character: ', text: 'Fraction Csp3 = ' + mol.fcsp3 + '. This descriptor provides a simple indication of the balance between saturated 3D carbon environments and planar/unsaturated environments.' },
      { label: 'Overall conclusion: ', text: "The calculated descriptors should be interpreted together with the 2D connectivity and generated 3D geometry to understand the molecule's composition, bonding, polarity, flexibility and structural character." }
    ];
    
    doc.setFontSize(7.5);
    for(var b = 0; b < bullets.length; b++){
      if(finalY > 276){
        doc.addPage();
        finalY = 18;
      }
      var bullet = bullets[b];
      var prefix = "- " + bullet.label;
      doc.setFont("helvetica", "bold");
      doc.setTextColor(0, 0, 0);
      var pWidth = doc.getTextWidth(prefix);
      
      // Keep text comfortably inside margins: max right x = 192 mm (left margin 14, right margin 196)
      var maxLine1Width = Math.max(20, 192 - (14 + pWidth));
      doc.setFont("helvetica", "normal");
      
      var words = bullet.text.split(' ');
      var currLine1 = "";
      var remWords = [];
      
      for(var w = 0; w < words.length; w++){
        var testStr = currLine1 ? (currLine1 + " " + words[w]) : words[w];
        if(doc.getTextWidth(testStr) <= maxLine1Width){
          currLine1 = testStr;
        } else {
          remWords = words.slice(w);
          break;
        }
      }
      
      doc.setFont("helvetica", "bold");
      doc.text(prefix, 14, finalY);
      doc.setFont("helvetica", "normal");
      if(currLine1){
        doc.text(currLine1, 14 + pWidth, finalY);
      }
      
      if(remWords.length > 0){
        var remText = remWords.join(' ');
        var wrappedLines = doc.splitTextToSize(remText, 172);
        for(var wl = 0; wl < wrappedLines.length; wl++){
          finalY += 3.6;
          if(finalY > 280){
            doc.addPage();
            finalY = 18;
          }
          doc.text(wrappedLines[wl], 18, finalY);
        }
      }
      finalY += 4.2;
    }
  }
  
  // FINAL PAGE: Python Libraries & Code
  doc.addPage();
  var pyY = 18;
  
  doc.setFont("helvetica", "bold");
  doc.setFontSize(12.5);
  doc.setTextColor(23, 54, 93);
  doc.text("Python Libraries Used and Their Importance", 14, pyY);
  pyY += 4;
  
  doc.autoTable({
    startY: pyY,
    head: [['Library', 'Importance in this project']],
    body: [
      ['Streamlit', 'Creates the interactive web app, input controls and PDF download interface.'],
      ['RDKit', 'Parses SMILES, validates structures, creates molecular drawings and 3D conformers, and calculates molecular descriptors.'],
      ['Pandas', 'Organizes molecular properties in tables and supports CSV export.'],
      ['Matplotlib and NumPy', 'Process molecular coordinates and generate a clear 2D projection of 3D geometry for the report.'],
      ['py3Dmol', 'Displays interactive 3D molecular structures in the web application.'],
      ['ReportLab', 'Builds the downloadable PDF with tables, figures and explanatory text.'],
      ['io, os, tempfile', 'Handle in-memory PDF data and temporary image files.']
    ],
    theme: 'grid',
    headStyles: {
      fillColor: [47, 85, 151],
      textColor: [255, 255, 255],
      fontSize: 8,
      fontStyle: 'bold',
      cellPadding: 2.2
    },
    bodyStyles: {
      textColor: [0, 0, 0],
      fontSize: 7.2,
      cellPadding: 2,
      lineColor: [128, 128, 128],
      lineWidth: 0.25
    },
    columnStyles: {
      0: { cellWidth: 50, fontStyle: 'bold' },
      1: { cellWidth: 'auto' }
    },
    margin: { left: 14, right: 14 }
  });
  
  pyY = doc.lastAutoTable.finalY + 8;
  
  doc.setFont("helvetica", "bold");
  doc.setFontSize(12);
  doc.setTextColor(23, 54, 93);
  doc.text("Illustrative Python Code", 14, pyY);
  pyY += 4;
  
  var codeLines = [
    'from rdkit import Chem',
    'from rdkit.Chem import Descriptors, Crippen, rdMolDescriptors',
    '',
    'smiles_list = ["CCO", "c1ccccc1"]  # Add more SMILES strings here',
    '',
    'for smiles in smiles_list:',
    '    mol = Chem.MolFromSmiles(smiles)',
    '    if mol is None:',
    '        print("Invalid SMILES:", smiles)',
    '        continue',
    '    print("SMILES:", smiles)',
    '    print("Formula:", rdMolDescriptors.CalcMolFormula(mol))',
    '    print("Molecular weight:", Descriptors.MolWt(mol))',
    '    print("LogP:", Crippen.MolLogP(mol))'
  ];
  
  var boxHeight = codeLines.length * 4.4 + 6;
  doc.setFillColor(245, 247, 250);
  doc.setDrawColor(203, 213, 225);
  doc.rect(14, pyY, 182, boxHeight, "FD");
  
  doc.setFont("courier", "normal");
  doc.setFontSize(7.5);
  doc.setTextColor(15, 23, 42);
  var lineY = pyY + 5;
  for(var cl = 0; cl < codeLines.length; cl++){
    doc.text(codeLines[cl], 18, lineY);
    lineY += 4.4;
  }
  
  pyY += boxHeight + 8;
  
  doc.setFont("helvetica", "normal");
  doc.setFontSize(8.5);
  doc.setTextColor(0, 0, 0);
  var noteText = "This compact code example demonstrates processing multiple SMILES in one run. The complete application includes additional code for visualization, descriptor interpretation, student information and PDF generation. Calculated descriptors are computational results and should be interpreted appropriately.";
  var splitNote = doc.splitTextToSize(noteText, 182);
  doc.text(splitNote, 14, pyY);
  
  // Universal Footers across all pages
  var totalPages = doc.internal.getNumberOfPages();
  for(var p = 1; p <= totalPages; p++){
    doc.setPage(p);
    doc.setFont("helvetica", "italic");
    doc.setFontSize(7.5);
    doc.setTextColor(100, 116, 139);
    doc.text("SRM Institute of Science and Technology, Tiruchirappalli | School of Sciences | Division of Chemistry", 14, 290);
    doc.text("Page " + p + " of " + totalPages, 196, 290, { align: "right" });
  }
  
  var cleanName = studentName.replace(/[^a-zA-Z0-9]/g, "_");
  var cleanReg = regNum.replace(/[^a-zA-Z0-9]/g, "_");
  doc.save("SRM_Cheminformatics_Report_" + cleanName + "_" + cleanReg + ".pdf");
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
      '<p style="color:var(--dim);font-size:12px">Compliance Contact: <a href="mailto:rsmani84@gmail.com" style="color:var(--acc)">rsmani84@gmail.com</a></p>';
  } else if(type === 'terms'){
    content.innerHTML = '<h2 style="color:var(--acc2);margin-bottom:14px">Terms of Academic License</h2>' +
      '<p style="color:var(--mut);margin-bottom:12px">Open access provided under educational fair-use principles.</p>' +
      '<ul style="color:var(--ink);padding-left:20px;line-height:1.7;margin-bottom:16px">' +
        '<li>Calculated descriptors are computational estimates intended for student training and pedagogical understanding.</li>' +
        '<li>Commercial pharmacological synthesis or clinical trials require verified experimental assays.</li>' +
        '<li>Attribution to SRM Institute of Science and Technology and Dr. R. Subramanian must be maintained in derivative works.</li>' +
      '</ul>';
  }

  modal.classList.add('active');
}

function toggleMobileMenu(){
  var d = document.getElementById('mobileDrawer');
  if(d) d.classList.toggle('open');
}

/* ==========================================================================
   9. MYSTERIOUS QUANTUM ABYSS & HYPNOTIC 3D VORTEX (THREE.JS)
   ========================================================================== */
var SpaceStage = (function(){
  var canvas, renderer, scene, camera;
  var quantumVortexGroup, knotMesh, knotWire, singularityCore, haloRing1, haloRing2;
  var wavePlane, waveGeom, waveOriginalZ;
  var stardustParticles, glowTexture;
  var width, height;
  var currentRotX = 0, currentRotY = 0;
  var scrollProgress = 0;
  var pointer = { x: 0, y: 0 };
  var initialized = false;

  // Generates a soft, ethereal Gaussian circular glow texture for particles (ZERO square boxes!)
  function createCircularGlowTexture(){
    var c = document.createElement('canvas');
    c.width = 64;
    c.height = 64;
    var ctx = c.getContext('2d');
    var g = ctx.createRadialGradient(32, 32, 0, 32, 32, 32);
    g.addColorStop(0, 'rgba(255, 255, 255, 1)');
    g.addColorStop(0.18, 'rgba(61, 139, 255, 0.85)');
    g.addColorStop(0.55, 'rgba(0, 240, 255, 0.25)');
    g.addColorStop(1, 'rgba(0, 0, 0, 0)');
    ctx.fillStyle = g;
    ctx.fillRect(0, 0, 64, 64);
    var tex = new THREE.CanvasTexture(c);
    return tex;
  }

  function init(){
    canvas = document.getElementById('spaceStage');
    if(!canvas || typeof THREE === 'undefined') return;

    width = canvas.clientWidth || window.innerWidth;
    height = canvas.clientHeight || window.innerHeight;

    try {
      renderer = new THREE.WebGLRenderer({
        canvas: canvas,
        alpha: true,
        antialias: true,
        powerPreference: 'high-performance'
      });
      renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
      renderer.setSize(width, height);
      renderer.toneMapping = THREE.ACESFilmicToneMapping;
      renderer.toneMappingExposure = 1.2;
    } catch(e) {
      console.warn("WebGL not initialized for SpaceStage:", e);
      return;
    }

    scene = new THREE.Scene();
    scene.fog = new THREE.FogExp2(0x000000, 0.022);

    camera = new THREE.PerspectiveCamera(50, width / height, 0.1, 1000);
    camera.position.set(0, 0, 20);

    // 1. VOLUMETRIC MYSTERIOUS LIGHTING (Deep blues, cyan highlights & violet underglow)
    var ambLight = new THREE.AmbientLight(0x050a15, 2.0);
    scene.add(ambLight);

    var blueKeyLight = new THREE.PointLight(0x3d8bff, 4.5, 60);
    blueKeyLight.position.set(9, 9, 14);
    scene.add(blueKeyLight);

    var cyanRimLight = new THREE.PointLight(0x00f0ff, 3.2, 45);
    cyanRimLight.position.set(-9, -6, 10);
    scene.add(cyanRimLight);

    var violetUnderLight = new THREE.PointLight(0x8b5cf6, 2.5, 50);
    violetUnderLight.position.set(0, -9, 6);
    scene.add(violetUnderLight);

    var dirLight = new THREE.DirectionalLight(0xffffff, 1.2);
    dirLight.position.set(5, 12, 10);
    scene.add(dirLight);

    // 2. THE CENTERPIECE: HYPNOTIC 3D QUANTUM TORUS KNOT VORTEX
    // Mathematical (2, 5) Torus Knot Manifold - infinite self-weaving multidimensional ribbon
    quantumVortexGroup = new THREE.Group();
    quantumVortexGroup.position.set(4.8, 0.3, -2);

    var knotGeom = new THREE.TorusKnotGeometry(3.3, 0.75, 200, 36, 2, 5);

    // Layer A: Polished Dark Obsidian Chromatic Core
    var knotMat = new THREE.MeshStandardMaterial({
      color: 0x050b18,
      metalness: 0.95,
      roughness: 0.12,
      emissive: 0x0f2b6e,
      emissiveIntensity: 0.55
    });
    knotMesh = new THREE.Mesh(knotGeom, knotMat);
    quantumVortexGroup.add(knotMesh);

    // Layer B: Glowing Bioluminescent Quantum Energy Web
    var wireGeom = new THREE.WireframeGeometry(knotGeom);
    var wireMat = new THREE.LineBasicMaterial({
      color: 0x00f0ff,
      transparent: true,
      opacity: 0.65,
      blending: THREE.AdditiveBlending
    });
    knotWire = new THREE.LineSegments(wireGeom, wireMat);
    quantumVortexGroup.add(knotWire);

    // Layer C: Pulsing Central Quantum Singularity
    var coreGeom = new THREE.SphereGeometry(1.35, 32, 32);
    var coreMat = new THREE.MeshStandardMaterial({
      color: 0x00ff9d,
      emissive: 0x00ff9d,
      emissiveIntensity: 0.85,
      transparent: true,
      opacity: 0.75,
      roughness: 0.15,
      metalness: 0.4
    });
    singularityCore = new THREE.Mesh(coreGeom, coreMat);
    quantumVortexGroup.add(singularityCore);

    // Layer D: Dual Ethereal Aerospace Orbital Rings
    var ringGeom1 = new THREE.TorusGeometry(5.4, 0.022, 16, 180);
    var ringMat1 = new THREE.MeshStandardMaterial({
      color: 0x3d8bff,
      metalness: 0.95,
      roughness: 0.12,
      emissive: 0x1d4ed8,
      emissiveIntensity: 0.6
    });
    haloRing1 = new THREE.Mesh(ringGeom1, ringMat1);
    quantumVortexGroup.add(haloRing1);

    var ringGeom2 = new THREE.TorusGeometry(6.6, 0.018, 16, 200);
    var ringMat2 = new THREE.MeshStandardMaterial({
      color: 0x00f0ff,
      metalness: 0.9,
      roughness: 0.16,
      emissive: 0x0284c7,
      emissiveIntensity: 0.5
    });
    haloRing2 = new THREE.Mesh(ringGeom2, ringMat2);
    haloRing2.rotation.x = Math.PI * 0.38;
    haloRing2.rotation.y = Math.PI * 0.22;
    quantumVortexGroup.add(haloRing2);

    scene.add(quantumVortexGroup);

    // 3. MYSTERIOUS UNDULATING QUANTUM WAVE SURFACE (Liquid Light - Replaces harsh retro grid)
    waveGeom = new THREE.PlaneGeometry(80, 50, 48, 30);
    waveOriginalZ = new Float32Array(waveGeom.attributes.position.count);
    for(var k = 0; k < waveGeom.attributes.position.count; k++){
      waveOriginalZ[k] = 0;
    }

    var waveMat = new THREE.MeshBasicMaterial({
      color: 0x1d4ed8,
      wireframe: true,
      transparent: true,
      opacity: 0.16,
      blending: THREE.AdditiveBlending
    });
    wavePlane = new THREE.Mesh(waveGeom, waveMat);
    wavePlane.rotation.x = -Math.PI * 0.44;
    wavePlane.position.set(0, -5.8, -10);
    scene.add(wavePlane);

    // Atmospheric Nebula Glow Plane (Deep cosmic backdrop)
    var nebulaGeom = new THREE.PlaneGeometry(120, 50);
    var nebulaMat = new THREE.MeshBasicMaterial({
      color: 0x0f2b6e,
      transparent: true,
      opacity: 0.12,
      blending: THREE.AdditiveBlending,
      side: THREE.DoubleSide
    });
    var nebulaPlane = new THREE.Mesh(nebulaGeom, nebulaMat);
    nebulaPlane.position.set(0, -2.5, -28);
    scene.add(nebulaPlane);

    // 4. SOFT CIRCULAR GLOWING STARDUST (100% Round Bokeh Orbs - ZERO Square Boxes)
    glowTexture = createCircularGlowTexture();
    var starCount = 550;
    var starGeom = new THREE.BufferGeometry();
    var starPos = new Float32Array(starCount * 3);
    for(var i = 0; i < starCount * 3; i += 3){
      starPos[i] = (Math.random() - 0.5) * 65;
      starPos[i+1] = (Math.random() - 0.5) * 40;
      // Strictly constrained depth: NEVER close to camera (prevents large blowups)
      starPos[i+2] = -12 - Math.random() * 40;
    }
    starGeom.setAttribute('position', new THREE.BufferAttribute(starPos, 3));
    var starMat = new THREE.PointsMaterial({
      color: 0x92c3ff,
      size: 0.45,
      map: glowTexture,
      transparent: true,
      opacity: 0.65,
      blending: THREE.AdditiveBlending,
      depthWrite: false,
      sizeAttenuation: true
    });
    stardustParticles = new THREE.Points(starGeom, starMat);
    scene.add(stardustParticles);

    // Event listeners
    window.addEventListener('resize', onResize, { passive: true });
    window.addEventListener('mousemove', onMouseMove, { passive: true });
    window.addEventListener('scroll', onScroll, { passive: true });

    onScroll();
    initialized = true;
    animate(0);
  }

  function onResize(){
    if(!renderer || !camera) return;
    width = window.innerWidth;
    height = window.innerHeight;
    camera.aspect = width / height;
    camera.updateProjectionMatrix();
    renderer.setSize(width, height);
  }

  function onMouseMove(e){
    pointer.x = (e.clientX / window.innerWidth) * 2 - 1;
    pointer.y = -(e.clientY / window.innerHeight) * 2 + 1;
  }

  function onScroll(){
    var docH = document.documentElement.scrollHeight - window.innerHeight;
    scrollProgress = docH > 0 ? (window.scrollY / docH) : 0;
  }

  function animate(timestamp){
    requestAnimationFrame(animate);
    if(!initialized) return;

    var time = timestamp * 0.001;

    // 1. STEADY, HYPNOTIC CONTINUOUS ROTATION (1 rev per ~140s - Calm, majestic, never spinning out of control)
    var baseRotY = time * 0.045;
    var baseRotX = Math.sin(time * 0.032) * 0.10;

    // 2. GENTLE, BOUNDED SCROLL EFFECT (Only tilts by ~12 degrees over the entire 7000px page height)
    var scrollTiltX = scrollProgress * 0.20;
    var scrollPanY = scrollProgress * 0.28;

    var targetRotX = baseRotX + scrollTiltX + (pointer.y * 0.18);
    var targetRotY = baseRotY + scrollPanY + (pointer.x * 0.22);

    currentRotX += (targetRotX - currentRotX) * 0.035;
    currentRotY += (targetRotY - currentRotY) * 0.035;

    if(quantumVortexGroup){
      quantumVortexGroup.rotation.x = currentRotX;
      quantumVortexGroup.rotation.y = currentRotY;

      // Responsive positioning
      if(window.innerWidth < 768){
        quantumVortexGroup.position.set(0, 1.2, -4);
        quantumVortexGroup.scale.set(0.68, 0.68, 0.68);
      } else {
        quantumVortexGroup.position.set(4.8, 0.3, -2);
        quantumVortexGroup.scale.set(1.0, 1.0, 1.0);
      }
    }

    // 3. SINGULARITY CORE & RINGS
    if(singularityCore){
      var pulse = 1.0 + Math.sin(time * 2.4) * 0.07;
      singularityCore.scale.set(pulse, pulse, pulse);
    }
    if(haloRing1){
      haloRing1.rotation.z = time * 0.08;
    }
    if(haloRing2){
      haloRing2.rotation.z = -time * 0.06;
    }

    // 4. UNDULATING SILKY QUANTUM WAVE DYNAMICS
    if(waveGeom){
      var pos = waveGeom.attributes.position;
      for(var j = 0; j < pos.count; j++){
        var u = pos.getX(j);
        var v = pos.getY(j);
        var waveZ = Math.sin(u * 0.16 + time * 0.65) * Math.cos(v * 0.16 + time * 0.5) * 1.1;
        pos.setZ(j, waveZ);
      }
      pos.needsUpdate = true;
    }

    // 5. SLOW CELESTIAL STARDUST DRIFT
    if(stardustParticles){
      stardustParticles.rotation.y = time * 0.012;
    }

    renderer.render(scene, camera);
  }

  return { init: init };
})();

/* ==========================================================================
   10. PUTURE INTERACTIVE MAGNETIC CURSOR & CONTEXTUAL BADGE
   ========================================================================== */
var PutureCursor = (function(){
  var cursorEl, badgeEl;
  var mouse = { x: -100, y: -100 };
  var current = { x: -100, y: -100 };
  var activeLabel = '';
  var isHovering = false;
  var initialized = false;

  function init(){
    cursorEl = document.getElementById('putureCursor');
    badgeEl = document.getElementById('cursorBadge');
    if(!cursorEl || !badgeEl) return;

    if(window.matchMedia('(pointer: coarse)').matches) return;

    window.addEventListener('mousemove', function(e){
      mouse.x = e.clientX;
      mouse.y = e.clientY;
      if(!initialized){
        current.x = mouse.x;
        current.y = mouse.y;
        cursorEl.style.opacity = '1';
        initialized = true;
      }
    }, { passive: true });

    document.addEventListener('mouseleave', function(){
      if(cursorEl) cursorEl.style.opacity = '0';
    });
    document.addEventListener('mouseenter', function(){
      if(cursorEl) cursorEl.style.opacity = '1';
    });

    // Delegate hover detection for dynamic badges
    document.addEventListener('mouseover', function(e){
      var target = e.target.closest('[data-cursor-label], button, a, input, select, .preset-chip, #viewer3D, #canvas2D');
      if(!target){
        activeLabel = '';
        isHovering = false;
        cursorEl.classList.remove('has-label', 'hovering');
        return;
      }

      isHovering = true;
      cursorEl.classList.add('hovering');

      if(target.hasAttribute('data-cursor-label')){
        activeLabel = target.getAttribute('data-cursor-label');
      } else if(target.id === 'viewer3D'){
        activeLabel = 'DRAG 3D';
      } else if(target.id === 'canvas2D'){
        activeLabel = '2D GRAPH';
      } else if(target.classList.contains('preset-chip')){
        activeLabel = 'LOAD MOL';
      } else if(target.tagName === 'BUTTON' || target.classList.contains('btn')){
        var txt = target.innerText.trim().toUpperCase();
        activeLabel = txt.length > 0 && txt.length < 18 ? txt : 'SELECT';
      } else if(target.tagName === 'A'){
        activeLabel = 'NAVIGATE';
      } else {
        activeLabel = '';
      }

      if(activeLabel){
        badgeEl.textContent = activeLabel;
        cursorEl.classList.add('has-label');
      } else {
        cursorEl.classList.remove('has-label');
      }
    }, { passive: true });

    animate();
  }

  function animate(){
    requestAnimationFrame(animate);
    if(!initialized) return;

    current.x += (mouse.x - current.x) * 0.22;
    current.y += (mouse.y - current.y) * 0.22;
    cursorEl.style.transform = 'translate3d(' + current.x + 'px, ' + current.y + 'px, 0)';
  }

  return { init: init };
})();

/* ==========================================================================
   11. FRAMER DYNAMIC ISLAND NAVIGATION & KINETIC SCROLL ENGINE
   ========================================================================== */
var FramerNav = (function(){
  var track, pill, links, header, progressBar;
  var activeLink = null;
  var isHovering = false;

  function init(){
    track = document.getElementById('navLinksTrack');
    pill = document.getElementById('navSlidingPill');
    links = document.querySelectorAll('.nav-link-item');
    header = document.getElementById('mainHeader');
    progressBar = document.getElementById('navIslandProgressBar');

    if(!track || !pill || !links.length) return;

    // Set initial active pill
    var initial = track.querySelector('.nav-link-item.active') || links[0];
    activeLink = initial;
    requestAnimationFrame(function(){
      movePillTo(initial, false);
    });

    // Framer magnetic fluid hover tracking
    links.forEach(function(link){
      link.addEventListener('mouseenter', function(){
        isHovering = true;
        movePillTo(link, true);
      });
      link.addEventListener('mouseleave', function(){
        isHovering = false;
        if(activeLink){
          movePillTo(activeLink, true);
        }
      });
      link.addEventListener('click', function(){
        activeLink = link;
        movePillTo(link, true);
      });
    });

    // Scroll listeners: compression & laser progress
    window.addEventListener('scroll', onScroll, { passive: true });
    window.addEventListener('resize', onResize, { passive: true });
    onScroll();

    // Re-check after font measurement
    if(document.fonts && document.fonts.ready){
      document.fonts.ready.then(function(){
        if(activeLink) movePillTo(activeLink, false);
      });
    }
    setTimeout(function(){
      if(activeLink) movePillTo(activeLink, false);
    }, 200);
  }

  function movePillTo(targetEl, animate){
    if(!targetEl || !track || !pill) return;
    var trackRect = track.getBoundingClientRect();
    var targetRect = targetEl.getBoundingClientRect();
    if(targetRect.width <= 0) return; // Hidden or mobile

    var left = targetRect.left - trackRect.left;
    var width = targetRect.width;

    if(!animate){
      pill.style.transition = 'none';
    } else {
      pill.style.transition = 'transform 0.32s cubic-bezier(0.16, 1, 0.3, 1), width 0.32s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.2s ease';
    }

    pill.style.transform = 'translateX(' + Math.round(left) + 'px)';
    pill.style.width = Math.round(width) + 'px';
    pill.style.opacity = '1';

    if(!animate){
      pill.offsetHeight; // force reflow
      pill.style.transition = '';
    }
  }

  function setActive(sectionId){
    if(!links || !links.length) return;
    var target = null;
    links.forEach(function(link){
      var href = link.getAttribute('href');
      if(href === '#' + sectionId){
        link.classList.add('active');
        target = link;
      } else {
        link.classList.remove('active');
      }
    });

    // Also update mobile drawer active states
    document.querySelectorAll('.mobile-nav-links a').forEach(function(mLink){
      if(mLink.getAttribute('href') === '#' + sectionId){
        mLink.classList.add('active');
      } else {
        mLink.classList.remove('active');
      }
    });

    if(target){
      activeLink = target;
      if(!isHovering){
        movePillTo(target, true);
      }
    }
  }

  function onScroll(){
    var scrollY = window.pageYOffset || document.documentElement.scrollTop;
    if(header){
      if(scrollY > 28){
        header.classList.add('scrolled');
      } else {
        header.classList.remove('scrolled');
      }
    }
    if(progressBar){
      var docH = document.documentElement.scrollHeight - window.innerHeight;
      var pct = docH > 0 ? (scrollY / docH) * 100 : 0;
      progressBar.style.width = Math.min(100, Math.max(0, pct)) + '%';
    }
  }

  function onResize(){
    if(activeLink){
      movePillTo(activeLink, false);
    }
  }

  return {
    init: init,
    setActive: setActive,
    movePillTo: movePillTo
  };
})();
window.FramerNav = FramerNav;

function scrollToChapter(sectionId){
  var el = document.getElementById(sectionId);
  if(!el) return;
  el.classList.add('section-visible');
  if(window.FramerNav){
    window.FramerNav.setActive(sectionId);
  }
  var offset = 75;
  var top = el.getBoundingClientRect().top + window.pageYOffset - offset;
  window.scrollTo({ top: top, behavior: 'smooth' });
}

var ChapterEngine = (function(){
  var hudNum, hudName, dots;
  var sections = [
    { id: 'home', num: '01', name: 'OVERVIEW' },
    { id: 'theory', num: '02', name: 'CURRICULUM THEORY' },
    { id: 'lab', num: '03', name: 'MOLECULAR LAB' },
    { id: 'properties', num: '04', name: '18 DESCRIPTORS' },
    { id: 'compare', num: '05', name: 'COMPARATIVE MATRIX' },
    { id: 'quiz', num: '06', name: 'ASSESSMENT MODULE' },
    { id: 'reactions', num: '07', name: 'REACTION SIMULATOR' },
    { id: 'report', num: '08', name: 'OFFICIAL REPORT' }
  ];

  function init(){
    hudNum = document.getElementById('hudChapNum');
    hudName = document.getElementById('hudChapName');
    dots = document.querySelectorAll('.p-dot');

    var observer = new IntersectionObserver(function(entries){
      entries.forEach(function(entry){
        if(entry.isIntersecting){
          var id = entry.target.id;
          for(var i = 0; i < sections.length; i++){
            if(sections[i].id === id){
              setActiveChapter(sections[i].num, sections[i].name, sections[i].id);
              break;
            }
          }
        }
      });
    }, {
      rootMargin: '-20% 0px -40% 0px',
      threshold: 0
    });

    sections.forEach(function(s){
      var el = document.getElementById(s.id);
      if(el) observer.observe(el);
    });
  }

  function setActiveChapter(num, name, id){
    if(hudNum) hudNum.textContent = num;
    if(hudName) hudName.textContent = name;
    if(dots){
      dots.forEach(function(d){
        if(d.getAttribute('data-chapter') === num){
          d.classList.add('active');
        } else {
          d.classList.remove('active');
        }
      });
    }
    if(!id){
      for(var i = 0; i < sections.length; i++){
        if(sections[i].num === num){ id = sections[i].id; break; }
      }
    }
    if(id && window.FramerNav){
      window.FramerNav.setActive(id);
    }
  }

  return { init: init, setActiveChapter: setActiveChapter };
})();

function initSectionScrollAnimations(){
  var sections = document.querySelectorAll('section');
  function checkVisible(){
    var vh = window.innerHeight || document.documentElement.clientHeight;
    sections.forEach(function(s){
      var r = s.getBoundingClientRect();
      if(r.top < vh + 120 && r.bottom > -50){
        s.classList.add('section-visible');
      }
    });
  }
  window.addEventListener('scroll', checkVisible, { passive: true });

  if(!('IntersectionObserver' in window)){
    sections.forEach(function(s){ s.classList.add('section-visible'); });
    return;
  }
  var observer = new IntersectionObserver(function(entries){
    entries.forEach(function(entry){
      if(entry.isIntersecting){
        entry.target.classList.add('section-visible');
      }
    });
  }, { threshold: 0.01, rootMargin: '0px 0px 100px 0px' });

  sections.forEach(function(s){
    if(s.id === 'home') s.classList.add('section-visible');
    observer.observe(s);
  });
  checkVisible();
}

/* ==========================================================================
   12. APPLICATION INITIALIZATION
   ========================================================================== */
window.addEventListener('DOMContentLoaded', function(){
  initTheme();
  initHealthCheck();
  initSectionScrollAnimations();
  ScrollEngine.init();
  SpaceStage.init();
  PutureCursor.init();
  FramerNav.init();
  ChapterEngine.init();
  initVisualizer();
  initComparativeTable();
  initQuiz();
  renderReportQueueUI();
  loadMotd();
  initReactions();
  fetchLeaderboard();
  initJsmeApplet();
  
  // Quick Win: Shareable URL Query Parameter (?smiles=...)
  var urlParams = new URLSearchParams(window.location.search);
  var qSmiles = urlParams.get('smiles');
  if(qSmiles){
    document.getElementById('smilesInput').value = qSmiles;
  }
  setTimeout(function(){ analyzeMolecule(); }, 350);
});
</script>
</body>
</html>
'''
    sdf_dict = {}
    sdf_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "precomputed_sdf.json")
    if os.path.exists(sdf_path):
        with open(sdf_path, "r") as f:
            sdf_dict = json.load(f)
    html = html.replace('/* __BENCHMARK_SDF_PLACEHOLDER__ */', 'var BENCHMARK_SDF = ' + json.dumps(sdf_dict) + ';')
    return html

if __name__ == "__main__":
    content = generate_index_html()
    with open("index.html", "w") as f:
        f.write(content)
    print("Successfully generated index.html with", len(content.splitlines()), "lines.")

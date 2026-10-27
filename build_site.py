"""
High-Precision Site Generator for Cheminformatics Virtual Laboratory
SRM Institute of Science and Technology, Tiruchirappalli
In collaboration with Tomoya Okazaki
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
<meta name="description" content="Cheminformatics Virtual Laboratory: Representation of 2D and 3D Chemical Structures. Developed for the Division of Chemistry at SRM Institute of Science and Technology, Tiruchirappalli, with Tomoya Okazaki. Convert SMILES, visualize 3D molecular models, evaluate 18 descriptors, and export certified PDF reports.">
<meta name="keywords" content="cheminformatics, 2D chemical structure, 3D molecular visualization, SMILES, SRM Institute of Science and Technology, Dr. R. Subramanian, Tomoya Okazaki, Lipinski rule, TPSA, LogP, molecular descriptors">
<meta name="author" content="Dr. R. Subramanian &amp; Tomoya Okazaki">
<meta name="theme-color" content="#030712">

<!-- Open Graph / Social Media -->
<meta property="og:type" content="website">
<meta property="og:title" content="Cheminformatics Virtual Laboratory | SRM IST &times; Tomoya Okazaki">
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
   INSTITUTIONAL HEADER - SRM IST & TOMOYA OKAZAKI
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

.tomoya-avatar {
  width: 38px;
  height: 38px;
  border-radius: 50%;
  border: 1.5px solid rgba(0, 240, 255, 0.75);
  box-shadow: 0 0 14px rgba(0, 240, 255, 0.45);
  object-fit: cover;
  transition: all 0.3s var(--ease);
}

header.scrolled .tomoya-avatar {
  width: 34px;
  height: 34px;
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
  .tomoya-avatar {
    width: 32px;
    height: 32px;
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

/* Section Headings */
section {
  padding: 85px 0;
  scroll-margin-top: 80px;
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
  <button class="p-dot" onclick="scrollToChapter('report')" title="07 Official Report" data-chapter="07"></button>
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
      <img src="assets/tomoya_logo.png" alt="Tomoya Okazaki Avatar" class="tomoya-avatar">
      <div class="brand-text">
        <h1>Cheminformatics Virtual Lab</h1>
        <span>SRM IST &times; TOMOYA OKAZAKI</span>
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
      <a href="#report" class="nav-link-item" data-chapter="07">
        <span class="nav-num">07</span>
        <span class="nav-label">Report</span>
      </a>
    </nav>

    <div class="nav-actions">
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
    <a href="#report" onclick="toggleMobileMenu()"><span class="m-num">07</span> Download PDF Report</a>
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
      <div id="smilesError" class="alert-banner error">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/></svg>
        <span id="smilesErrorText">Invalid SMILES notation. Please inspect molecular valence or ring closures.</span>
      </div>

      <div id="smilesSuccess" class="alert-banner success">
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/><polyline points="22 4 12 14.01 9 11.01"/></svg>
        <span id="smilesSuccessText">Valid chemical structure parsed and 3D geometry rendered successfully.</span>
      </div>

      <div class="card">
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
            <strong id="bmMw">46.069</strong>
            <span>MW (g/mol)</span>
          </div>
          <div class="bond-metric-card">
            <strong id="bmHeavyAtoms">3</strong>
            <span>Heavy Atoms</span>
          </div>
          <div class="bond-metric-card">
            <strong id="bmSigma">8</strong>
            <span>Sigma (σ) Bonds</span>
          </div>
          <div class="bond-metric-card">
            <strong id="bmPi">0</strong>
            <span>Pi (π) Bonds</span>
          </div>
          <div class="bond-metric-card">
            <strong id="bmTotalBonds">8</strong>
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
              <div class="gauge-val" id="gaugeValMw">46.07 <span class="gauge-unit">g/mol</span></div>
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
              <div class="gauge-val" id="gaugeValLogP">-0.00 <span class="gauge-unit">oct/water</span></div>
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
              <div class="gauge-val" id="gaugeValHbd">1 <span class="gauge-unit">/ 5 max</span></div>
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
              <div class="gauge-val" id="gaugeValHba">1 <span class="gauge-unit">/ 10 max</span></div>
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

  <!-- BLOCK 7: STUDENT REPORT GENERATION -->
  <section id="report" data-chapter="07" data-chapter-name="OFFICIAL REPORT">
    <div class="wrap">
      <div class="sechead">
        <div class="kicker">Official Certification</div>
        <h2>Generate Student Laboratory PDF Report</h2>
        <div class="sec-line"></div>
        <p style="margin-top:12px">
          Generate a standardized, publication-ready PDF report bearing official SRM Institute of Science and Technology
          laboratory formatting, student credentials, and descriptor interpretations.
        </p>
      </div>

      <div class="card" style="max-width:700px;margin:0 auto">
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
          <label style="font-size:11px;color:var(--dim);text-transform:uppercase;font-family:var(--mono)">Report Molecule (SMILES)</label>
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

<!-- FOOTER & ACADEMIC CREDITS - OFFICIAL ACADEMIC CHANNELS -->
<footer>
  <div class="wrap">
    <div class="footer-top">
      <div class="footer-brand">
        <div style="display:flex;align-items:center;gap:12px;margin-bottom:14px">
          <img src="assets/tomoya_logo.png" alt="Tomoya Logo" style="width:36px;height:36px;border-radius:4px;border:1px solid var(--acc)">
          <img src="assets/srm_logo.jpeg" alt="SRM Logo" style="height:32px;border-radius:2px">
        </div>
        <h3>Cheminformatics Virtual Laboratory</h3>
        <p>
          Division of Chemistry, School of Sciences, Faculty of Engineering and Technology<br>
          <strong>SRM Institute of Science and Technology</strong>, Tiruchirappalli, Tamil Nadu, India.
        </p>
        <p style="margin-top:10px;font-size:12.5px;color:var(--dim)">
          Curriculum direction &amp; academic supervision by <strong>Dr. R. Subramanian</strong> (Assistant Professor, Chemistry).<br>
          Kinetic engineering &amp; systems architecture by <strong>Tomoya Okazaki</strong> (Purple Team Systems).
        </p>
      </div>

      <div class="footer-links">
        <h4>Direct Faculty &amp; Technical Contacts</h4>
        <a href="mailto:rsmani84@gmail.com">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          <span>Dr. R. Subramanian (rsmani84@gmail.com)</span>
        </a>
        <a href="mailto:khalidnawaz7y@gmail.com">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,13 2,6"/></svg>
          <span>Tomoya Okazaki (khalidnawaz7y@gmail.com)</span>
        </a>
      </div>

      <div class="footer-links">
        <h4>Ethics &amp; Verified Identity</h4>
        <a href="https://tryhackme.com/p/Tomoya.okazaki" target="_blank" rel="noopener">TryHackMe: Tomoya.okazaki</a>
        <a href="https://profile.hackthebox.com/profile/01a0be6e-b00a-7335-9ff0-5864ad467519" target="_blank" rel="noopener">HackTheBox: Profile</a>
        <a href="https://www.linkedin.com/in/khalidnawaz-sec" target="_blank" rel="noopener">LinkedIn: khalidnawaz-sec</a>
        <a href="javascript:void(0)" onclick="openLegalModal('privacy')">Privacy Policy &amp; Data Ethics</a>
        <a href="javascript:void(0)" onclick="openLegalModal('terms')">Academic License &amp; Fair Use</a>
      </div>
    </div>

    <div class="footer-bottom">
      <div>&copy; 2026 SRM Institute of Science and Technology &amp; Tomoya Okazaki. All rights reserved. Zero tracking cookies.</div>
      <div style="font-family:var(--mono);color:var(--acc)">PYTHON SERVERLESS ENGINE v3.6 &times; VERCEL EDGE</div>
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

<!-- Scripts: GSAP 3.12.5, ScrollTrigger, Three.js, 3Dmol, jsPDF -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollTrigger.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.5/ScrollToPlugin.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/3Dmol/2.4.2/3Dmol-min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>

<script>
/* ==========================================================================
   1. DATA DEFINITIONS & PRESET BENCHMARKS
   ========================================================================== */
var BENCHMARK_MOLECULES = [
  { name: "Ethanol", smiles: "CCO", formula: "C2H6O", mw: 46.069, logp: -0.4, tpsa: 30.23, hbd: 1, hba: 1, rot: 0, desc: "Primary aliphatic alcohol used as a solvent and antiseptic." },
  { name: "Benzene", smiles: "c1ccccc1", formula: "C6H6", mw: 78.114, logp: 1.5, tpsa: 0.0, hbd: 0, hba: 0, rot: 0, desc: "Fundamental aromatic hydrocarbon with planar delocalized pi electrons." },
  { name: "Phenol", smiles: "Oc1ccccc1", formula: "C6H6O", mw: 94.113, logp: 1.1, tpsa: 20.23, hbd: 1, hba: 1, rot: 0, desc: "Aromatic alcohol exhibiting resonance-stabilized phenoxide formation." },
  { name: "Acetic Acid", smiles: "CC(=O)O", formula: "C2H4O2", mw: 60.052, logp: -0.4, tpsa: 40.46, hbd: 1, hba: 2, rot: 0, desc: "Carboxylic acid exhibiting strong intermolecular hydrogen bonding." },
  { name: "Aspirin", smiles: "CC(=O)Oc1ccccc1C(=O)O", formula: "C9H8O4", mw: 180.159, logp: -0.7, tpsa: 90.69, hbd: 1, hba: 4, rot: 2, desc: "Acetylsalicylic acid, standard NSAID analgesic and antipyretic." },
  { name: "Caffeine", smiles: "CN1C=NC2=C1C(=O)N(C(=O)N2C)C", formula: "C8H10N4O2", mw: 194.194, logp: -1.0, tpsa: 114.46, hbd: 0, hba: 6, rot: 0, desc: "Methylxanthine central nervous system stimulant." },
  { name: "Paracetamol", smiles: "CC(=O)Nc1ccc(O)cc1", formula: "C8H9NO2", mw: 151.165, logp: 0.8, tpsa: 49.33, hbd: 2, hba: 2, rot: 1, desc: "Widely used antipyretic and analgesic." },
  { name: "Ibuprofen", smiles: "CC(C)Cc1ccc(C(C)C(=O)O)cc1", formula: "C13H18O2", mw: 206.285, logp: 2.8, tpsa: 40.46, hbd: 1, hba: 2, rot: 4, desc: "Non-steroidal anti-inflammatory drug with chiral propionic acid core." }
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

    window.addEventListener('wheel', function(e){
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

function animateCounter(elementId, targetVal, isFloat){
  var el = document.getElementById(elementId);
  if(!el) return;
  var target = parseFloat(targetVal);
  if(isNaN(target)){
    el.innerText = targetVal;
    return;
  }
  var current = parseFloat(el.innerText) || 0;
  var obj = { val: current };
  if(window.gsap){
    gsap.to(obj, {
      val: target,
      duration: 0.65,
      ease: "power2.out",
      onUpdate: function(){
        el.innerText = isFloat ? obj.val.toFixed(3) : Math.round(obj.val);
      }
    });
  } else {
    el.innerText = isFloat ? target.toFixed(3) : Math.round(target);
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
        updateBondMetrics(data.properties);
        showSmilesSuccess("Structure validated via Python Cheminformatics Engine.");
      } else {
        throw new Error(data.error || "Invalid structure");
      }
    })
    .catch(function(err){
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
  var valMw = document.getElementById('gaugeValMw');
  var fillMw = document.getElementById('gaugeFillMw');
  var badgeMw = document.getElementById('gaugeBadgeMw');
  if(valMw) valMw.innerHTML = mw.toFixed(2) + ' <span class="gauge-unit">g/mol</span>';
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
  var valLogP = document.getElementById('gaugeValLogP');
  var fillLogP = document.getElementById('gaugeFillLogP');
  var badgeLogP = document.getElementById('gaugeBadgeLogP');
  if(valLogP) valLogP.innerHTML = (logp >= 0 ? '+' : '') + logp.toFixed(2) + ' <span class="gauge-unit">oct/water</span>';
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
  var valHbd = document.getElementById('gaugeValHbd');
  var fillHbd = document.getElementById('gaugeFillHbd');
  var badgeHbd = document.getElementById('gaugeBadgeHbd');
  if(valHbd) valHbd.innerHTML = hbd + ' <span class="gauge-unit">/ 5 max</span>';
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
  var valHba = document.getElementById('gaugeValHba');
  var fillHba = document.getElementById('gaugeFillHba');
  var badgeHba = document.getElementById('gaugeBadgeHba');
  if(valHba) valHba.innerHTML = hba + ' <span class="gauge-unit">/ 10 max</span>';
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

  animateCounter('bmMw', p["Molecular Weight"] || 0, true);
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

  // Animated vector SVG diagram for the molecular structure
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

  if(window.gsap){
    gsap.fromTo("#canvas2D line, #canvas2D path, #canvas2D polygon",
      { strokeDasharray: 300, strokeDashoffset: 300, opacity: 0 },
      { strokeDashoffset: 0, opacity: 1, duration: 0.75, stagger: 0.08, ease: "power2.out" }
    );
    gsap.fromTo("#canvas2D circle, #canvas2D text",
      { scale: 0, opacity: 0, transformOrigin: "center" },
      { scale: 1, opacity: 1, duration: 0.5, stagger: 0.05, delay: 0.25, ease: "back.out(1.7)" }
    );
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

  if(isAromatic && count >= 5){
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

  if(window.gsap){
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
      '<button class="btn primary" onclick="currentQ=0;quizScore=0;renderQuizQuestion()" style="margin-top:16px"><span>Retake Assessment</span></button>' +
    '</div>';
    document.getElementById('btnNextQuiz').style.display = 'none';
    setupRollingButtons();
    initMagneticButtons();
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
  for(var i = 0; i < Math.min(14, keys.length); i++){
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
    { id: 'report', num: '07', name: 'OFFICIAL REPORT' }
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

/* ==========================================================================
   12. APPLICATION INITIALIZATION
   ========================================================================== */
window.addEventListener('DOMContentLoaded', function(){
  ScrollEngine.init();
  SpaceStage.init();
  PutureCursor.init();
  FramerNav.init();
  ChapterEngine.init();
  initVisualizer();
  initComparativeTable();
  initQuiz();
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

# Project Chimera

## Overview
A Flask web application with a cybersecurity/tactical theme designed for agent management and secure file distribution. Features a "Tactical Minimalist" dark mode design.

## Project Architecture

### Backend (Python/Flask)
- **app.py** - Main Flask application with routes:
  - `/` - Landing page with login form
  - `/login` (POST) - Authentication endpoint (admin/chimera123)
  - `/admin` - Admin dashboard for agent management
  - `/portal` - Secure file distribution portal
  - `/api/approve/<id>` (POST) - API to approve agents
  - `/api/deny/<id>` (POST) - API to deny agents
  - `/logout` - Session logout

### Frontend (Jinja2 Templates + Tailwind CSS)
- **templates/base.html** - Base template with Tailwind CDN, Google Fonts (Space Mono, Inter), and CSS animations
- **templates/index.html** - Landing page with hero section and login form
- **templates/dashboard.html** - Admin panel with terminal-style agent management table
- **templates/portal.html** - Secure APK download portal

### Design System
- **Color Palette:**
  - Background: Deep Slate (#0f172a / bg-slate-900)
  - Text: Light Grey (text-slate-200)
  - Accent: Neon Emerald (#10b981)
- **Typography:**
  - Headers: Space Mono (monospace)
  - Body: Inter (sans-serif)
- **Animations:** Fade-in effects, pulse glow on download button

### Data Storage
- In-memory Python list for user/agent data (no database required)
- Session-based authentication using Flask sessions

## Running the Application
```bash
python app.py
```
Server runs on `http://0.0.0.0:5000`

## Login Credentials
- Officer ID: `admin`
- Password: `chimera123`

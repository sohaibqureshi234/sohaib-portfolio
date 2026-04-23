# Muhammad Sohaib Qureshi — Portfolio

A Flask-based portfolio website built for Vercel deployment.

## Project Structure

```
sohaib-portfolio/
├── api/
│   └── index.py          ← Flask app (Vercel serverless entry point)
├── templates/
│   └── index.html        ← Jinja2 HTML template
├── static/
│   ├── css/style.css     ← All styles
│   └── js/main.js        ← Animations & interactions
├── requirements.txt      ← Python dependencies
├── vercel.json           ← Vercel configuration
└── README.md
```

## Run Locally

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run the dev server
python api/index.py

# 3. Open in browser
# http://localhost:5000
```

## Deploy to Vercel (Free)

### Option A — Vercel CLI (recommended)
```bash
# 1. Install Vercel CLI
npm install -g vercel

# 2. Push your project to GitHub first, then:
vercel

# Follow the prompts — done in ~1 minute
```

### Option B — Vercel Dashboard
1. Go to https://vercel.com and sign up (free)
2. Click "Add New Project"
3. Import your GitHub repository
4. Vercel auto-detects Python — click **Deploy**
5. Your site is live at `yourname.vercel.app` ✓

## Customize Your Info

All your personal data is in one place: `api/index.py`

Edit the `PORTFOLIO_DATA` dictionary to update:
- Name, title, contact details
- Skills and categories
- Work experience
- Projects (name, description, App Store / Play Store links)
- Stats

No need to touch the HTML or CSS for content changes.

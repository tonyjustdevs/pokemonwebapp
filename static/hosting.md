1. Tony's Local Environment
Local Build Process:
- `python3 -m venv .venv`
- `source .venv/bin/activate`
- `python -m pip install pip-tools`
- `echo "Flask" > requirements.in`
- `pip-compile requirements.in`
- `pip-sync requirements.txt`

2. Netlify: Introduction
- Netlify must recreate it's **own virtual environment** on its servers with Tony's repo.
- Tony's `.venv` is not uploaded to Git (correctly) because:
    - `.venv.` is system-specific, therefore,
    - `.venv` is not portable


3. Netlify: Build Process
- Commit `requirements.txt`
- Build Settings:
    - Build Command:        `python app.py`
    - Python Version:       `python 3.10`
    - Install Dependencies: `pip install -r requirements.txt`

Hosting Options
1. Glitch - cant load site.
2. Vercel, Flyio - credit card requirement.
3.  - credit card requirement.
3. Netlify - static, not suitable with dynamic backend.


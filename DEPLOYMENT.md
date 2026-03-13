# Deployment Guide

This guide covers the easiest ways to deploy your Flask application.

## 🚀 Option 1: Render (EASIEST - Recommended)

**Render** is the simplest option with a free tier and excellent Flask support.

### Steps:

1. **Create a Render account**
   - Go to [render.com](https://render.com)
   - Sign up with GitHub (recommended) or email

2. **Push your code to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

3. **Deploy on Render**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: first-defender-protective-services (or your choice)
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:create_app()` (or leave blank to use Procfile)
     - **Instance Type**: Free (or paid for better performance)
   
4. **Set Environment Variables** (optional)
   - Go to Environment tab
   - Add: `FLASK_ENV=production`
   - Add: `SECRET_KEY=<your-secret-key>` (generate a random string)

5. **Deploy!**
   - Click "Create Web Service"
   - Wait 2-3 minutes for deployment
   - Your site will be live at: `https://your-app-name.onrender.com`

**Pros:**
- ✅ Free tier available
- ✅ Automatic HTTPS
- ✅ Easy GitHub integration
- ✅ Auto-deploys on git push
- ✅ Simple setup

---

## 🚂 Option 2: Railway

**Railway** is another easy option with a generous free tier.

### Steps:

1. **Sign up** at [railway.app](https://railway.app)

2. **Create new project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Connect your repository

3. **Configure**
   - Railway auto-detects Flask apps
   - It will use the `Procfile` automatically
   - Add environment variable: `FLASK_ENV=production`

4. **Deploy**
   - Railway automatically deploys
   - Your site will be live at: `https://your-app-name.up.railway.app`

**Pros:**
- ✅ Very easy setup
- ✅ Free tier with $5 credit/month
- ✅ Auto-detects Flask apps
- ✅ Great documentation

---

## 🐍 Option 3: PythonAnywhere

**PythonAnywhere** is great for beginners and has a free tier.

### Steps:

1. **Sign up** at [pythonanywhere.com](https://www.pythonanywhere.com)

2. **Upload your files**
   - Go to "Files" tab
   - Upload all project files (or use Git)

3. **Create Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose Flask
   - Select Python 3.10

4. **Configure**
   - Set source code path: `/home/yourusername/first-defender-protective-services`
   - Set WSGI file path: `/var/www/yourusername_pythonanywhere_com_wsgi.py`
   - Edit WSGI file to point to your app

5. **Install dependencies**
   - Go to "Tasks" tab
   - Run: `pip3.10 install --user -r requirements.txt`

6. **Reload**
   - Click "Reload" button
   - Your site will be live at: `https://yourusername.pythonanywhere.com`

**Pros:**
- ✅ Free tier available
- ✅ Beginner-friendly
- ✅ Built-in Python environment

---

## 🔧 Option 4: Fly.io

**Fly.io** offers global deployment with a free tier.

### Steps:

1. **Install Fly CLI**
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Sign up** at [fly.io](https://fly.io)

3. **Initialize**
   ```bash
   fly launch
   ```
   - Follow the prompts
   - It will create a `fly.toml` file

4. **Deploy**
   ```bash
   fly deploy
   ```

**Pros:**
- ✅ Global edge deployment
- ✅ Free tier available
- ✅ Fast performance

---

## 📋 Pre-Deployment Checklist

Before deploying, make sure:

- [ ] All dependencies are in `requirements.txt`
- [ ] `Procfile` is created (for Render/Railway)
- [ ] Environment variables are set (SECRET_KEY, FLASK_ENV)
- [ ] Debug mode is disabled in production
- [ ] Code is pushed to GitHub/GitLab

---

## 🔐 Environment Variables

Set these in your deployment platform:

- `FLASK_ENV=production` - Disables debug mode
- `SECRET_KEY=<random-string>` - For CSRF protection (generate with: `python -c "import secrets; print(secrets.token_hex(32))"`)

---

## 🎯 Recommended: Render

For the easiest deployment experience, **use Render**:
- Free tier is generous
- Setup takes ~5 minutes
- Automatic HTTPS
- Auto-deploys on git push
- Great documentation

Just connect your GitHub repo and deploy!

---

## 📞 Need Help?

- Render Docs: https://render.com/docs
- Railway Docs: https://docs.railway.app
- PythonAnywhere Docs: https://help.pythonanywhere.com

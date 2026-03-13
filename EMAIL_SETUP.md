# Email Setup Guide

This guide explains how to configure email functionality for the contact form.

## 📧 Quick Setup

### Option 1: Gmail (Easiest)

1. **Enable 2-Factor Authentication** on your Gmail account
   - Go to [Google Account Security](https://myaccount.google.com/security)
   - Enable 2-Step Verification

2. **Generate App Password**
   - Go to [App Passwords](https://myaccount.google.com/apppasswords)
   - Select "Mail" and "Other (Custom name)"
   - Enter "First Defender Flask App"
   - Copy the generated 16-character password

3. **Create `.env` file** in project root:
   ```bash
   cp .env.example .env
   ```

4. **Edit `.env` file** with your credentials:
   ```env
   MAIL_SERVER=smtp.gmail.com
   MAIL_PORT=587
   MAIL_USE_TLS=True
   MAIL_USERNAME=your-email@gmail.com
   MAIL_PASSWORD=your-16-char-app-password
   MAIL_DEFAULT_SENDER=your-email@gmail.com
   CONTACT_EMAIL=info@fdpservices.com
   ```

5. **Install dependencies** (if not already installed):
   ```bash
   pip install -r requirements.txt
   ```

6. **Test the form** - Submit a contact form and check your email!

---

## 🔧 Other Email Providers

### Outlook/Office 365

```env
MAIL_SERVER=smtp.office365.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@outlook.com
MAIL_PASSWORD=your-password
```

### Yahoo Mail

```env
MAIL_SERVER=smtp.mail.yahoo.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@yahoo.com
MAIL_PASSWORD=your-app-password
```

### SendGrid (Recommended for Production)

1. Sign up at [SendGrid](https://sendgrid.com) (free tier available)
2. Create API Key
3. Configure:

```env
MAIL_SERVER=smtp.sendgrid.net
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=apikey
MAIL_PASSWORD=your-sendgrid-api-key
MAIL_DEFAULT_SENDER=your-verified-sender@yourdomain.com
```

### Mailgun (Great for Production)

1. Sign up at [Mailgun](https://www.mailgun.com) (free tier available)
2. Get SMTP credentials from dashboard
3. Configure:

```env
MAIL_SERVER=smtp.mailgun.org
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-mailgun-username
MAIL_PASSWORD=your-mailgun-password
```

---

## 🚀 Deployment Setup

### Render / Railway / Fly.io

Set these as **Environment Variables** in your deployment platform:

```
MAIL_SERVER=smtp.gmail.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=your-email@gmail.com
MAIL_PASSWORD=your-app-password
MAIL_DEFAULT_SENDER=your-email@gmail.com
CONTACT_EMAIL=info@fdpservices.com
```

**Important:** Never commit your `.env` file to Git! It's already in `.gitignore`.

---

## 🧪 Testing Email Locally

1. Make sure `.env` file exists with correct credentials
2. Run the Flask app:
   ```bash
   python app.py
   ```
3. Go to `http://localhost:5000`
4. Fill out and submit the contact form
5. Check:
   - Your inbox (CONTACT_EMAIL) - should receive notification
   - Sender's inbox - should receive confirmation email

---

## 🔒 Security Notes

- **Never commit `.env` file** - it contains sensitive credentials
- Use **App Passwords** for Gmail, not your regular password
- For production, use **SendGrid** or **Mailgun** instead of personal email
- Set `FLASK_ENV=production` in production to disable debug mode

---

## 🐛 Troubleshooting

### "Authentication failed" error
- Check username/password are correct
- For Gmail: Make sure you're using an App Password, not your regular password
- Verify 2FA is enabled on Gmail

### "Connection refused" error
- Check firewall isn't blocking port 587
- Verify MAIL_SERVER and MAIL_PORT are correct
- Try MAIL_PORT=465 with MAIL_USE_SSL=True

### Emails going to spam
- Use a professional email service (SendGrid/Mailgun) for production
- Set up SPF/DKIM records for your domain
- Use a verified sender email address

### No emails received
- Check spam folder
- Verify CONTACT_EMAIL is set correctly
- Check Flask logs for error messages
- Test with a different email provider

---

## 📝 Email Templates

The email templates are in `utils/email_service.py`. You can customize:
- HTML formatting
- Email subject lines
- Confirmation message content
- Email styling

---

## ✅ Quick Checklist

- [ ] Created `.env` file from `.env.example`
- [ ] Set MAIL_USERNAME and MAIL_PASSWORD
- [ ] Set CONTACT_EMAIL (where form submissions go)
- [ ] Installed dependencies (`pip install -r requirements.txt`)
- [ ] Tested form submission locally
- [ ] Set environment variables in production deployment

---

Need help? Check the Flask-Mail documentation: https://pythonhosted.org/Flask-Mail/

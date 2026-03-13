"""
WSGI entry point for production deployment
Railway will use this file to start the application with gunicorn
"""
import os
from app import create_app

# Get environment or default to production
# Railway sets FLASK_ENV=production automatically, but we default to it for safety
config_name = os.environ.get('FLASK_ENV', 'production')

# Validate required environment variables for production
if config_name == 'production':
    required_vars = ['SECRET_KEY']
    missing_vars = [var for var in required_vars if not os.environ.get(var)]
    if missing_vars:
        raise ValueError(f"Missing required environment variables for production: {', '.join(missing_vars)}")

app = create_app(config_name)

# This is only used if running directly (not via gunicorn)
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)

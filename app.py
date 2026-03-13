"""
Flask application entry point
"""
from flask import Flask
from config import config
from controllers.main_controller import main_bp
import os

def create_app(config_name='default'):
    """Application factory pattern"""
    app = Flask(__name__)
    
    # Load environment variables from .env file if it exists
    try:
        from dotenv import load_dotenv
        load_dotenv()
    except ImportError:
        pass  # dotenv not installed, skip
    
    # Load configuration
    app.config.from_object(config[config_name])
    
    # Register Blueprints
    app.register_blueprint(main_bp)
    
    return app


if __name__ == '__main__':
    import os
    config_name = os.environ.get('FLASK_ENV', 'development')
    app = create_app(config_name)
    app.run(debug=(config_name == 'development'), host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))

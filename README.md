# First Defender Protective Services

A modern, professional one-page responsive website built with Python Flask and MVC architecture.

## Features

- **MVC Architecture**: Clean separation of models, views, and controllers
- **Responsive Design**: Mobile-first approach with breakpoints at 480px, 768px, and 1024px
- **Dark Theme**: Professional charcoal background (#0F1115) with orange accents (#F28C28)
- **Contact Form**: Server-side validation using Flask-WTF with email notifications
- **Email Functionality**: Automatic email notifications when contact form is submitted
- **Smooth Scrolling**: Enhanced navigation experience
- **Mobile Menu**: Hamburger menu for mobile devices

## Project Structure

```
project_root/
│
├── app.py                 # Flask application entry point
├── config.py              # Configuration settings
├── requirements.txt       # Python dependencies
│
├── models/
│   └── contact.py         # Contact form model
│
├── controllers/
│   └── main_controller.py # Main routes controller
│
├── templates/
│   ├── base.html          # Base template
│   ├── index.html         # Main page template
│   └── partials/
│       ├── navbar.html    # Navigation partial
│       └── footer.html    # Footer partial
│
├── static/
│   ├── css/
│   │   └── styles.css     # Main stylesheet
│   ├── js/
│   │   └── script.js      # JavaScript functionality
│   └── images/            # Image assets directory
│
└── README.md              # This file
```

## Installation

1. **Clone or navigate to the project directory**

2. **Create a virtual environment (recommended)**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Set Flask environment variables (optional)**
   ```bash
   export FLASK_APP=app.py
   export FLASK_ENV=development  # Optional: enables debug mode
   ```

2. **Run the Flask application**
   ```bash
   flask run
   ```
   
   Or directly:
   ```bash
   python app.py
   ```

3. **Open your browser**
   Navigate to `http://localhost:5000` or `http://127.0.0.1:5000`

## Configuration

The application uses environment-based configuration. You can modify settings in `config.py`:

- **Development**: Debug mode enabled, uses default secret key
- **Production**: Debug mode disabled, requires `SECRET_KEY` environment variable

To set a production secret key:
```bash
export SECRET_KEY='your-secret-key-here'
```

## Features Overview

### Sections

1. **Hero Section**: Full-width hero with call-to-action
2. **Why Choose Us**: Feature list with icons
3. **Services**: 6 service cards in responsive grid
4. **How We Work**: 4-step process visualization
5. **Contact Form**: Validated contact form with server-side processing

### Responsive Breakpoints

- **Mobile**: < 768px (single column, hamburger menu)
- **Tablet**: 768px - 1024px (2 columns for services)
- **Desktop**: > 1024px (3 columns for services, side-by-side layouts)

## Technologies Used

- **Backend**: Python 3.x, Flask 3.0.0
- **Forms**: Flask-WTF, WTForms
- **Templates**: Jinja2
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Fonts**: Google Fonts (Inter)
- **Icons**: FontAwesome 6.4.0

## Development Notes

- The contact form uses Flask-WTF for CSRF protection and validation
- Form submissions are currently simulated (no database integration)
- Flash messages display success/error notifications
- All routes are handled through Blueprints for better organization
- CSS uses CSS variables for easy theming

## Email Setup

The contact form can send email notifications. See [EMAIL_SETUP.md](EMAIL_SETUP.md) for detailed instructions.

**Quick Setup:**
1. Copy `.env.example` to `.env`
2. Configure your email settings in `.env`
3. For Gmail: Use an App Password (see EMAIL_SETUP.md)
4. Install dependencies: `pip install -r requirements.txt`

## Future Enhancements

- Database integration for contact form submissions
- Admin panel for managing contacts
- Image optimization and lazy loading
- Additional animations and transitions

## License

This project is proprietary software for First Defender Protective Services.

## Support

For issues or questions, please contact the development team.

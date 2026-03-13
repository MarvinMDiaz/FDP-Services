"""
Contact form model for handling form submissions
"""
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    """Contact form with validation"""
    first_name = StringField(
        'First Name',
        validators=[
            DataRequired(message='This field is required.'),
            Length(min=2, max=50, message='First name must be between 2 and 50 characters')
        ],
        render_kw={'placeholder': 'First name here'}
    )
    
    email = StringField(
        'Email Address',
        validators=[
            DataRequired(message='This field is required.'),
            Email(message='Please enter a valid email address'),
            Length(max=100, message='Email must be less than 100 characters')
        ],
        render_kw={'placeholder': 'example@example.com', 'type': 'email'}
    )
    
    phone = StringField(
        'Phone (Optional)',
        validators=[
            Length(max=20, message='Phone must be less than 20 characters')
        ],
        render_kw={'placeholder': 'Phone number (optional)', 'type': 'tel'}
    )
    
    subject = StringField(
        'Subject',
        validators=[
            DataRequired(message='This field is required.'),
            Length(min=5, max=200, message='Subject must be between 5 and 200 characters')
        ],
        render_kw={'placeholder': 'How can we help you?'}
    )
    
    message = TextAreaField(
        'Comments / Questions',
        validators=[
            DataRequired(message='This field is required.'),
            Length(min=10, max=2000, message='Message must be between 10 and 2000 characters')
        ],
        render_kw={'placeholder': 'Comments', 'rows': 6}
    )

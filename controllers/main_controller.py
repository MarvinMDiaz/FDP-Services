"""
Main controller for handling routes
"""
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app
from models.contact import ContactForm
from utils.email_service import send_contact_email, send_confirmation_email
import logging

logger = logging.getLogger(__name__)

# Create Blueprint
main_bp = Blueprint('main', __name__)


@main_bp.route('/', methods=['GET', 'POST'])
def index():
    """Main page route - handles both GET and POST for contact form"""
    form = ContactForm()
    
    if request.method == 'POST':
        if form.validate_on_submit():
            try:
                # Send email notification to site owner
                email_sent = send_contact_email(
                    name=form.first_name.data,
                    email=form.email.data,
                    phone=form.phone.data if form.phone.data else None,
                    message=form.message.data,
                    subject=form.subject.data
                )
                
                # Send confirmation email to user (optional - disabled in SES sandbox mode)
                # Uncomment below when SES is out of sandbox mode or recipient emails are verified
                # try:
                #     send_confirmation_email(
                #         first_name=form.first_name.data,
                #         email=form.email.data
                #     )
                # except Exception as e:
                #     logger.warning(f"Failed to send confirmation email: {str(e)}")
                #     # Don't fail the whole request if confirmation email fails
                
                if email_sent:
                    flash('Thank you for your message! We will get back to you soon.', 'success')
                    # Reset form after successful submission to prevent resubmission
                    form = ContactForm()
                else:
                    flash('Your message was received, but there was an issue sending the notification. Please try again or contact us directly.', 'error')
                
            except Exception as e:
                logger.error(f"Error processing contact form: {str(e)}")
                flash('An error occurred while processing your message. Please try again later or contact us directly.', 'error')
        else:
            # Flash validation errors
            for field, errors in form.errors.items():
                for error in errors:
                    # Handle CSRF errors with a more user-friendly message
                    if 'csrf' in field.lower() or 'csrf' in error.lower():
                        flash('Your session has expired. Please refresh the page and try again.', 'error')
                        logger.warning(f"CSRF validation failed: {error}")
                    else:
                        flash(f'{field.replace("_", " ").title()}: {error}', 'error')
    
    return render_template('index.html', form=form)

"""
Main controller for handling routes
"""
from flask import Blueprint, render_template, request, flash, redirect, url_for, current_app, Response
from models.contact import ContactForm
from utils.email_service import send_contact_email, send_confirmation_email
from datetime import datetime
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
                    # Redirect after successful submission to clear form and refresh page
                    # Scroll to contact section to show success message
                    return redirect(url_for('main.index', _anchor='contact'))
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


@main_bp.route('/sitemap.xml')
def sitemap():
    """Generate XML sitemap for search engines"""
    base_url = request.url_root.rstrip('/')
    
    # Get current date in W3C format
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    # Define all routes with their priorities and change frequencies
    routes = [
        {
            'loc': f'{base_url}/',
            'changefreq': 'weekly',
            'priority': '1.0',
            'lastmod': current_date
        }
    ]
    
    # Generate XML sitemap
    sitemap_xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    sitemap_xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    
    for route in routes:
        sitemap_xml += '  <url>\n'
        sitemap_xml += f'    <loc>{route["loc"]}</loc>\n'
        sitemap_xml += f'    <lastmod>{route["lastmod"]}</lastmod>\n'
        sitemap_xml += f'    <changefreq>{route["changefreq"]}</changefreq>\n'
        sitemap_xml += f'    <priority>{route["priority"]}</priority>\n'
        sitemap_xml += '  </url>\n'
    
    sitemap_xml += '</urlset>'
    
    return Response(sitemap_xml, mimetype='application/xml')


@main_bp.route('/robots.txt')
def robots():
    """Generate robots.txt file"""
    base_url = request.url_root.rstrip('/')
    robots_txt = f"""User-agent: *
Allow: /

Sitemap: {base_url}/sitemap.xml
"""
    return Response(robots_txt, mimetype='text/plain')

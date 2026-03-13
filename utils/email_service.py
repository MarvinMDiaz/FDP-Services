"""
Email service for sending contact form emails using Amazon SES
"""
import os
import boto3
import logging
from botocore.exceptions import ClientError, BotoCoreError

logger = logging.getLogger(__name__)


def _get_ses_client():
    """
    Create and return a boto3 SES client configured with environment variables
    
    Returns:
        boto3.client: Configured SES client
    """
    return boto3.client(
        'ses',
        region_name=os.getenv('AWS_REGION'),
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )


def send_contact_email(name, email, phone=None, message=None, subject=None):
    """
    Send contact form email notification using Amazon SES
    
    Args:
        name: Sender's name
        email: Sender's email address
        phone: Sender's phone number (optional)
        message: Email message content
        subject: Email subject line (optional)
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        # Get email configuration from environment variables
        from_email = os.getenv('SES_FROM_EMAIL')
        to_email = os.getenv('CONTACT_TO_EMAIL')
        
        if not from_email:
            logger.error("SES_FROM_EMAIL environment variable not set")
            return False
        
        if not to_email:
            logger.error("CONTACT_TO_EMAIL environment variable not set")
            return False
        
        # Validate required fields
        if not name or not email or not message:
            logger.error("Missing required fields: name, email, or message")
            return False
        
        # Build email body (plain text version)
        phone_text = phone if phone else "Not provided"
        subject_text = f"\nSubject: {subject}" if subject else ""
        email_body_text = f"""New Contact Form Submission

Name: {name}
Email: {email}
Phone: {phone_text}{subject_text}

Message:
{message}

---
First Defender Protective Services
Elite Protection, Anytime, Anywhere
"""
        
        # Build HTML email body with branding
        # Use text-only branding - works reliably in all email clients
        logo_html = '''<h1 style="color: #E5E5E5; margin: 0; font-size: 32px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase;">FDP</h1>
                        <p style="color: #F28C28; margin: 8px 0 0 0; font-size: 16px; letter-spacing: 2px; text-transform: uppercase; font-weight: 600;">Services</p>'''
        
        email_body_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f5f5f5;">
    <table role="presentation" style="width: 100%; border-collapse: collapse; background-color: #f5f5f5;">
        <tr>
            <td style="padding: 40px 20px;">
                <table role="presentation" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <!-- Header with Logo/Branding -->
                    <tr>
                        <td style="background-color: #0F1115; padding: 30px 40px; text-align: center;">
                            {logo_html}
                        </td>
                    </tr>
                    
                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="color: #F28C28; margin: 0 0 20px 0; font-size: 24px; font-weight: 600;">New Contact Form Submission</h2>
                            
                            <table role="presentation" style="width: 100%; border-collapse: collapse; margin: 20px 0;">
                                <tr>
                                    <td style="padding: 12px 0; border-bottom: 1px solid #e5e7eb;">
                                        <strong style="color: #111827; display: inline-block; width: 100px;">Name:</strong>
                                        <span style="color: #4B5563;">{name}</span>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 12px 0; border-bottom: 1px solid #e5e7eb;">
                                        <strong style="color: #111827; display: inline-block; width: 100px;">Email:</strong>
                                        <span style="color: #4B5563;">{email}</span>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="padding: 12px 0; border-bottom: 1px solid #e5e7eb;">
                                        <strong style="color: #111827; display: inline-block; width: 100px;">Phone:</strong>
                                        <span style="color: #4B5563;">{phone_text}</span>
                                    </td>
                                </tr>
                                {f'<tr><td style="padding: 12px 0; border-bottom: 1px solid #e5e7eb;"><strong style="color: #111827; display: inline-block; width: 100px;">Subject:</strong><span style="color: #4B5563;">{subject}</span></td></tr>' if subject else ''}
                            </table>
                            
                            <div style="margin-top: 30px;">
                                <h3 style="color: #111827; margin: 0 0 10px 0; font-size: 18px; font-weight: 600;">Message:</h3>
                                <div style="color: #4B5563; line-height: 1.6; white-space: pre-wrap; background-color: #F7F8FA; padding: 20px; border-radius: 5px; border-left: 3px solid #F28C28;">{message}</div>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #0F1115; padding: 30px 40px; text-align: center;">
                            <p style="color: #E5E5E5; margin: 0 0 10px 0; font-size: 16px; font-weight: 600;">First Defender Protective Services</p>
                            <p style="color: #B0B0B0; margin: 0 0 15px 0; font-size: 14px;">Elite Protection, Anytime, Anywhere</p>
                            <p style="color: #6B7280; margin: 0; font-size: 12px;">This email was sent from the contact form on your website.<br>You can reply directly to this email to respond to {name}.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""
        
        # Create SES client
        ses_client = _get_ses_client()
        
        # Send email via SES with both HTML and text versions
        response = ses_client.send_email(
            Source=from_email,
            Destination={
                'ToAddresses': [to_email]
            },
            Message={
                'Subject': {
                    'Data': 'New Contact Form Submission',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Html': {
                        'Data': email_body_html,
                        'Charset': 'UTF-8'
                    },
                    'Text': {
                        'Data': email_body_text,
                        'Charset': 'UTF-8'
                    }
                }
            },
            ReplyToAddresses=[email]
        )
        
        logger.info(f"Contact email sent successfully via SES. MessageId: {response.get('MessageId', 'N/A')}")
        return True
        
    except ClientError as e:
        # Log AWS-specific errors safely
        error_code = e.response.get('Error', {}).get('Code', 'Unknown')
        error_message = e.response.get('Error', {}).get('Message', 'No details available')
        logger.error(f"AWS SES error ({error_code}): Failed to send contact email - {error_message}")
        
        # Log additional context for common issues
        if error_code == 'MessageRejected':
            logger.error("Common causes: Email not verified in SES, account in sandbox mode, or invalid email format")
        
        return False
        
    except BotoCoreError as e:
        # Log boto3 core errors safely
        logger.error(f"Boto3 error: Failed to send contact email - {str(e)}")
        return False
        
    except Exception as e:
        # Log any other errors safely (don't expose stack traces to user)
        logger.error(f"Unexpected error sending contact email: {str(e)}")
        return False


def send_confirmation_email(first_name, email):
    """
    Send confirmation email to the person who submitted the form using Amazon SES
    
    Args:
        name: Recipient's name
        email: Recipient's email address
    
    Returns:
        bool: True if email sent successfully, False otherwise
    """
    try:
        # Get email configuration from environment variables
        from_email = os.getenv('SES_FROM_EMAIL')
        
        if not from_email:
            logger.error("SES_FROM_EMAIL environment variable not set")
            return False
        
        if not first_name or not email:
            logger.error("Missing required fields: first_name or email")
            return False
        
        # Build email body (plain text version)
        email_body_text = f"""Thank You, {first_name}!

We have received your message and will get back to you within 24 hours.

Our team is reviewing your inquiry and will respond as soon as possible.

First Defender Protective Services
Elite Protection, Anytime, Anywhere

If you have any urgent security concerns, please call us directly.
"""
        
        # Build HTML email body with branding
        # Use text-only branding - works reliably in all email clients
        logo_html = '''<h1 style="color: #E5E5E5; margin: 0; font-size: 32px; font-weight: 700; letter-spacing: 3px; text-transform: uppercase;">FDP</h1>
                        <p style="color: #F28C28; margin: 8px 0 0 0; font-size: 16px; letter-spacing: 2px; text-transform: uppercase; font-weight: 600;">Services</p>'''
        
        email_body_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body style="margin: 0; padding: 0; font-family: Arial, sans-serif; background-color: #f5f5f5;">
    <table role="presentation" style="width: 100%; border-collapse: collapse; background-color: #f5f5f5;">
        <tr>
            <td style="padding: 40px 20px;">
                <table role="presentation" style="max-width: 600px; margin: 0 auto; background-color: #ffffff; border-radius: 8px; overflow: hidden; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
                    <!-- Header with Logo/Branding -->
                    <tr>
                        <td style="background-color: #0F1115; padding: 30px 40px; text-align: center;">
                            {logo_html}
                        </td>
                    </tr>
                    
                    <!-- Content -->
                    <tr>
                        <td style="padding: 40px;">
                            <h2 style="color: #F28C28; margin: 0 0 20px 0; font-size: 24px; font-weight: 600;">Thank You, {first_name}!</h2>
                            
                            <p style="color: #4B5563; line-height: 1.6; margin: 0 0 20px 0; font-size: 16px;">
                                We have received your message and will get back to you within 24 hours.
                            </p>
                            
                            <p style="color: #4B5563; line-height: 1.6; margin: 0 0 30px 0; font-size: 16px;">
                                Our team is reviewing your inquiry and will respond as soon as possible.
                            </p>
                            
                            <div style="background-color: #F7F8FA; padding: 20px; border-radius: 5px; border-left: 3px solid #F28C28; margin-top: 30px;">
                                <p style="color: #111827; margin: 0 0 10px 0; font-weight: 600; font-size: 14px;">Need Immediate Assistance?</p>
                                <p style="color: #4B5563; margin: 0; font-size: 14px;">If you have any urgent security concerns, please call us directly at <strong style="color: #111827;">240-729-3439</strong>.</p>
                            </div>
                        </td>
                    </tr>
                    
                    <!-- Footer -->
                    <tr>
                        <td style="background-color: #0F1115; padding: 30px 40px; text-align: center;">
                            <p style="color: #E5E5E5; margin: 0 0 10px 0; font-size: 16px; font-weight: 600;">First Defender Protective Services</p>
                            <p style="color: #B0B0B0; margin: 0 0 15px 0; font-size: 14px;">Elite Protection, Anytime, Anywhere</p>
                            <p style="color: #6B7280; margin: 0; font-size: 12px;">We appreciate your interest in our services.</p>
                        </td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>
</html>
"""
        
        # Create SES client
        ses_client = _get_ses_client()
        
        # Send email via SES with both HTML and text versions
        response = ses_client.send_email(
            Source=from_email,
            Destination={
                'ToAddresses': [email]
            },
            Message={
                'Subject': {
                    'Data': 'Thank You for Contacting First Defender Protective Services',
                    'Charset': 'UTF-8'
                },
                'Body': {
                    'Html': {
                        'Data': email_body_html,
                        'Charset': 'UTF-8'
                    },
                    'Text': {
                        'Data': email_body_text,
                        'Charset': 'UTF-8'
                    }
                }
            }
        )
        
        logger.info(f"Confirmation email sent successfully via SES. MessageId: {response.get('MessageId', 'N/A')}")
        return True
        
    except ClientError as e:
        # Log AWS-specific errors safely
        error_code = e.response.get('Error', {}).get('Code', 'Unknown')
        error_message = e.response.get('Error', {}).get('Message', 'No details available')
        logger.warning(f"AWS SES error ({error_code}): Failed to send confirmation email - {error_message}")
        return False
        
    except BotoCoreError as e:
        # Log boto3 core errors safely
        logger.warning(f"Boto3 error: Failed to send confirmation email - {str(e)}")
        return False
        
    except Exception as e:
        # Log any other errors safely
        logger.warning(f"Unexpected error sending confirmation email: {str(e)}")
        return False

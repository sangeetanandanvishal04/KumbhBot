from passlib.context import CryptContext
import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from .config import settings

pwd_context = CryptContext(schemes=["bcrypt"],deprecated="auto")

def hash(password: str):
    return pwd_context.hash(password)

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password,hashed_password)

def generate_otp():
    return str(random.randint(1000, 9999))

def send_email(subject: str, recipient_email: str, html_content: str):
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = settings.email
    password = settings.smtp_password

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    msg.attach(MIMEText(html_content, 'html'))

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, recipient_email, msg.as_string())

def send_signup_email(recipient_email: str):
    subject = "Welcome to the Maha Kumbh Mela 2025 Chatbot!"
    html_content = """
    <html>
    <body>
        <h2 style="color: #2e6c80;">Welcome to the Maha Kumbh Mela 2025 Chatbot!</h2>
        <p>Dear User,</p>
        <p>Thank you for joining the official chatbot service for Maha Kumbh Mela 2025. We are here to assist you during this extraordinary spiritual event.</p>
        <p>With the chatbot, you can easily:</p>
        <ul>
            <li><strong>Get real-time event information:</strong> Receive updates about schedules, locations, and important announcements.</li>
            <li><strong>Find accommodation and travel options:</strong> Get recommendations for hotels, buses, trains, and more.</li>
            <li><strong>Multilingual support:</strong> Interact with the chatbot in multiple languages for better accessibility.</li>
        </ul>
        <p>Feel free to explore all the features and make your Kumbh Mela experience smoother and more enjoyable.</p>
        <p>If you have any questions or need assistance, we're here to help!</p>
        <p>Best regards,<br/>The Maha Kumbh Mela Chatbot Team</p>
        <p style="font-size: small; color: gray;">This is a system-generated email. Please do not respond.</p>
    </body>
    </html>
    """
    send_email(subject, recipient_email, html_content)

def send_otp_email(recipient_email: str, otp: str):
    subject = "Your OTP for Password Reset - Maha Kumbh Mela Chatbot"
    html_content = f"""
    <html>
    <body>
        <h2 style="color: #2e6c80;">Password Reset OTP</h2>
        <p>Dear User,</p>
        <p>Your OTP for resetting your password in the Maha Kumbh Mela 2025 Chatbot is:</p>
        <h1 style="color: #d9534f;">{otp}</h1>
        <p>Please use this OTP to proceed with resetting your password.</p>
        <p>If you did not request a password reset, please contact our support team immediately.</p>
        <p>Best regards,<br/>The Maha Kumbh Mela Chatbot Team</p>
        <p style="font-size: small; color: gray;">This is a system-generated email. Please do not respond.</p>
    </body>
    </html>
    """
    send_email(subject, recipient_email, html_content)
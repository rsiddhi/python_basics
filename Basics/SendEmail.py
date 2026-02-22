import smtplib
from email.message import EmailMessage

msg = EmailMessage()
msg["Subject"] = "Python Test Email"
msg["From"] = "your_email@gmail.com"
msg["To"] = "receiver@gmail.com"
msg.set_content("Hello! This is a test email sent using SMTP.")

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
    server.login("your_email@gmail.com", "your_app_password")
    server.send_message(msg)

print("Email has been sent successfully!")

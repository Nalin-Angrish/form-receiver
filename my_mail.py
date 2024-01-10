"""
This file will act as a mailing engine for this website
"""
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import dotenv
dotenv.load_dotenv()

def send(to_email, message):
    """
    A Function to send an email with the given details
    """
    try:
        #Configure message
        msg = MIMEMultipart()
        msg['From'] = os.getenv("BOT_MAIL")
        msg['To'] = to_email
        msg['Subject'] = "Your form submission"
        msg.attach(MIMEText(message, 'plain'))
        print("Message formed")

        #Start communicating with smtp server
        session = smtplib.SMTP("smtp.zoho.com", 587)
        print("Session created")
        session.starttls()
        print("TLS started")
        print(os.getenv("BOT_MAIL") is None, os.getenv("BOT_PASS") is None)
        session.login(os.getenv("BOT_MAIL"), os.getenv("BOT_PASS"))
        print("Logged in")

        #Send the mail
        body = msg.as_string()
        session.sendmail(os.getenv("BOT_MAIL"), to_email, body)
        print("Email sent")
        session.quit()
    except Exception as error:
        raise error



if __name__ == "__main__":
    print("Sending a mail")
    send("nalinangrish2005@gmail.com", "Testing email sender...")

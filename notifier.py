# notifier.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure your sender credentials
SENDER_EMAIL = "d99689408@gmail.com"
SENDER_PASSWORD = "zlhd txvl iwze bacg"  # Use App Password if using Gmail with 2FA

def send_email_alert(to_email, alerts):
    if not alerts:
        return

    subject = "Crypto Alert: Price within your range!"
    body = "\n".join([f"{coin.upper()} is now ${price}" for coin, price in alerts])

    msg = MIMEMultipart()
    msg['From'] = SENDER_EMAIL
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        print(f"Email sent to {to_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

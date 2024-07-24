import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# List of hosts to check
hosts = ['8.8.8.8', '1.1.1.1']

# Email configuration
smtp_server = 'smtp.your-email-provider.com'
smtp_port = 587
email_user = 'your-email@example.com'
email_password = 'your-email-password'
email_to = 'alert-recipient@example.com'

def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = email_user
    msg['To'] = email_to
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(email_user, email_password)
        server.sendmail(email_user, email_to, msg.as_string())
        server.close()
    except Exception as e:
        print(f"Failed to send email: {e}")

def check_connectivity():
    for host in hosts:
        response = os.system(f"ping -c 1 {host}")

        if response == 0:
            print(f"{host} is up!")
        else:
            print(f"{host} is down!")
            send_email("Network Connectivity Alert", f"{host} is down!")

if __name__ == "__main__":
    check_connectivity()

import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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

def get_disk_usage():
    disk_usage = os.popen("df -h").read()
    return disk_usage

def main():
    disk_usage_report = get_disk_usage()
    print(disk_usage_report)
    send_email("Disk Usage Report", disk_usage_report)

if __name__ == "__main__":
    main()

import psutil
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

def check_server_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    disk = psutil.disk_usage('/')

    issues = []

    if cpu_usage > 80:
        issues.append(f"High CPU usage: {cpu_usage}%")
    if memory.percent > 80:
        issues.append(f"High memory usage: {memory.percent}%")
    if disk.percent > 80:
        issues.append(f"Low disk space: {disk.percent}% available")

    if issues:
        send_email("Server Health Alert", "\n".join(issues))

if __name__ == "__main__":
    check_server_health()

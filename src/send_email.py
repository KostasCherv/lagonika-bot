import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from src.my_logger import log

from src.config import GOOGLE_EMAIL, GOOGLE_PASSWORD, RECIPIENTS

def send_email(items):
    log('Sending email...')
    msg = MIMEMultipart()
    timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    msg['Subject'] = f"{timestamp}: {len(items)} New items on lagonika.gr" 
    body = "<html><body>"
    for item in items:
        body += "<p>" + item['text'] + "</p>"
        body += "<p>" + item['href'] + "</p>"

    body += "</body></html>"
    msg.attach(MIMEText(body, 'html'))
        
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GOOGLE_EMAIL, GOOGLE_PASSWORD)
        text = msg.as_string()
        server.sendmail(GOOGLE_EMAIL, RECIPIENTS, text)
        server.quit()
        log("Email sent")
    except Exception as e:
        log(e)
        log("Email failed")



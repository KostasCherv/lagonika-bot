import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from src.item import Item
from src.my_logger import log

from src.config import GOOGLE_EMAIL, GOOGLE_PASSWORD, RECIPIENTS

def send_email(items: list[Item]):
    log('Sending email...')
    msg = MIMEMultipart()
    timestamp = str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    msg['Subject'] = f"{timestamp}: {len(items)} New items on lagonika.gr" 
    msg['To'] = RECIPIENTS
    body = "<html><body><div style='text-align:center'>"
    for item in items:
        body += "<div style='border:1px solid; padding-bottom: 10px'>"
        body += "<p><a href='{item.href}'>" + item.title + "</p>"
        body += f"<a href='{item.href}'><img src='{item.img_src}'>"
        body += "</div>"

    body += "</div></body></html>"

    msg.attach(MIMEText(body, 'html'))
        
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(GOOGLE_EMAIL, GOOGLE_PASSWORD)
        text = msg.as_string()
        server.sendmail(GOOGLE_EMAIL, RECIPIENTS.split(','), text)
        server.quit()
        log("Email sent")
    except Exception as e:
        log(e)
        log("Email failed")



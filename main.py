import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime
import random

email_my = "YOURE EMAIL"
addr = "RECEPIENT"
email_smtp = "SMTP_HOST"
passwordd = "PASSWORD"

def send_message(to_addr, from_addr, message):
    msg = MIMEMultipart()
    msg["From"] = from_addr
    msg["To"] = to_addr
    msg["Subject"] = "New Them"
    msg.attach(MIMEText(message, "plain"))

    connection = smtplib.SMTP(email_smtp)
    connection.starttls()
    connection.login(user=email_my, password=passwordd)
    connection.send_message(msg)
    connection.close()

with open("quotes.txt", encoding='utf-8') as file:
    motivations = file.readlines()

while True:
    now = datetime.datetime.now()
    if now.hour == 9:
        if now.weekday() == 1:
            send_message(addr, email_my, random.choice(motivations))
            time.sleep(3700)


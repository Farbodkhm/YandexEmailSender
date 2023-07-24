import smtplib
from email.mime.text import MIMEText
from email.header import Header
from random import randint


smtp_host = 'smtp.yandex.ru'
user = "Your Yandex Email Address"      # put your yandex email
password = "Your App Password"          # put your third-party yandex password
receiver = "Receiver Address "

subject = "Email Verification"
body = '<p>Your code is : ' + str(randint(10000, 99999)) + '</p>'

message = MIMEText(body, 'html', 'utf-8')
message['Subject'] = Header(subject, 'utf-8')
message['From'] = user
message['To'] = receiver

session = smtplib.SMTP(smtp_host, 587, timeout=10)

try:
    session.starttls()
    session.login(user, password)
    session.sendmail(message['From'], receiver, message.as_string())
    print("Sent")
finally:
    session.quit()

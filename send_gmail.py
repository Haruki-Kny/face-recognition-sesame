import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate
import datetime

def mail(name):
    sendAddress = 'example@gmail.com'
    password = 'your secret password'   # secret
    now = str(datetime.datetime.now())
    subject = 'Sesame'
    bodyText = name + ' is detected\n\n' + now
    fromAddress = 'example@gmail.com'
    toAddress = 'example@icloud.com'

    # SMTPサーバに接続 connet to SMTP server
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.starttls()
    smtpobj.login(sendAddress, password)

    # メール作成 write mail
    msg = MIMEText(bodyText)
    msg['Subject'] = subject
    msg['From'] = fromAddress
    msg['To'] = toAddress
    msg['Date'] = formatdate()

    # 作成したメールを送信 send mail
    smtpobj.send_message(msg)
    smtpobj.close()
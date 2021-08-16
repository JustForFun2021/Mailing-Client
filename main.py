import smtplib
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

# server = smtplib.SMTP('smtp.gmail.com', 587)
# server.ehlo()
# server.starttls()
# try:
#     server = smtplib.SMTP('smtp.mailfence.com',465)
#     server.ehlo()
#     server.starttls()
#     # ...send emails
# except Exception:
#     print('cant connecct to server')
try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
except:
    print('OPPPPSSSS SERVER not working!!!!')



with open('Mailing Client/password.txt','r') as f:
    password = f.read()


try:
    # server.login('fitness.health@mailfence.com',password)
    server.login('**@gmail.com','Ie***')
except:
    print('not work')

msg = MIMEMultipart()
#Using msg obj as dict
msg['From'] = 'Testing'
msg['To'] = "***@gmail.com"
msg['subject'] = 'Testing mailing client'

with open('Mailing Client/message.txt','r') as f:
    message = f.read()

#With attach we dont the txt file we adding this as a text

msg.attach(MIMEText(message,'plain'))

filename = 'Mailing Client/img.jpg'
attachment = open(filename,'rb')
p= MIMEBase('application','octet-stream')
p.set_payload(attachment.read())
encoders.encode_base64(p)
p.add_header('Content-Disposition',f'attachment;filename={filename}')
msg.attach(p)
text = msg.as_string()
server.sendmail('***@gmail.com','***@gmail.com',text)
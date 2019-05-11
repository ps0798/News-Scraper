from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

res = requests.get("https://www.hindustantimes.com/india-news/").text

soup = BeautifulSoup(res,'lxml')

n=1

for summary in soup.find_all('div',class_='media-heading headingfour'):
	#print(summary.text)

	with open("Today's Headlines.txt",'a') as writer:
		st='\n'+str(n)+summary.text
		writer.write(st)
		n=n+1


email_user = "sender's e-mail"
email_password = 'sender password '
email_send = 'receiver e-mail'

subject = "Today's News Headlines"
msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hi there, sending this email from Python!'
msg.attach(MIMEText(body,'plain'))

filename="Today's Headlines.txt"
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()

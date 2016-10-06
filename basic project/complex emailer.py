import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "superbleblabla@gmail.com"
toaddr = "nomnom148@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "test test"
 
body = "this is a test"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "superbleblabla")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

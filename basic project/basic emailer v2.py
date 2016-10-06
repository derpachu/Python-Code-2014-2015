import smtplib

fromaddr = 'nomnom148@gmail.com'
toaddrs  = 'superbleblabla@gmail.com'
msg = 'this is a test'


# Credentials (if needed)
username = 'nomnom148@gmail.com'
password = '15900383a q'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()

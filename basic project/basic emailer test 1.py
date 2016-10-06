import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 465)
server.starttls()
server.login("nomnom148@gmail.com", "15900383a q")
 
msg = "this is a test"
server.sendmail("nomnom148@gmail.com", "superbleblabla@gmail.com", msg)
server.quit()

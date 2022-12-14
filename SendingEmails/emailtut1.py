import smtplib

server = smtplib.SMTP('smtp.example.com', 25)
server.connect("smtp.example.com",465)
server.ehlo()
server.starttls()
server.ehlo()
server.login("dibyaranjanprm.51@gmail.com", "Pra51M@66D9")
subject = "FROM SMTP LIB PYTHON"
message = "Hello From SMTP LIB"
msg = "Subject: " + subject + '\n' + message
text = msg.as_string()
server.sendmail("dibyaranjanprm.51@gmail.com", "dibayranjan.official@gmail.com", text)
server.quit()
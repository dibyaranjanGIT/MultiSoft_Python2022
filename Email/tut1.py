'''
The smtplib module defines an SMTP client session object that can be used to send mail to any internet machine with an
SMTP
'''
import smtplib

my_email = "dibyaranjanprm.51@gmail.com"
my_pass = "fnjezfjlzwhbxxxx" #

# To connect to gmail
connection = smtplib.SMTP("smtp.gmail.com")
connection.starttls() # create a secure connection

# Now connect
connection.login(user=my_email, password=my_pass)

connection.sendmail(from_addr=my_email, to_addrs="dibyaranjan.official@gmail.com",
                    msg="Subject:Hello From Python\n\nThis is the body of image")
connection.close()
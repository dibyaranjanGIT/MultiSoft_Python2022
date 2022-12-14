'''
The smtplib library allows you to manually go through the steps of creating and sending an email in Python:
'''
import smtplib
import getpass # For hidden passwords

# password = getpass.getpass("Your hidden password here: ")

# Create an STMP object that can make the method calls to log you in to your email in order to send messages.
smtp_object = smtplib.SMTP('smtp.example.com', 25)
smtp_object.connect("smtp.example.com",465)

print(smtp_object.ehlo())

email = input("Enter your email: ")
password = getpass.getpass("Enter your password: ")
smtp_object.login(email,password)
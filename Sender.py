import smtplib, ssl
# from Location import Location
from Users import Users
# from GarbageDate import Date


port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "ourhouse589@gmail.com"  # Enter your address
receiver_email = []

# Dictionary from Users.py
Dict = Users()

for value in Dict.values():
    receiver_email.append(value)
# **********************


password = input("Type your password and press enter: ") # pasword is: H311otest


message = """\
Subject: 1695 Sheridan Isolation

Please isolate for 5 days as one of you have contacted a person with covid in the last 2 weeks."""




# Create a secure SSL context
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("ourhouse589@gmail.com", password)
    server.sendmail(sender_email, receiver_email, message)
    



import smtplib
import socket
socket.getaddrinfo('localhost',8080)
subject="Testing SMTP with python"
sender=input("enter sender's mail")
pwd=input("enter your password :")
receiver=input("enter receiver's email :")
message=input("enter the content for email")
try:
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(sender,pwd)
    print("successful you logged in ")
    server.sendmail(sender,receiver,message)
    print("Mail is successfully sent to ",receiver)
except Exception as e:
    print(e)
    print("Oops! There is a problem in sending the mail")
finally:
      print("Server closed")
      server.quit()

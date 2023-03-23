#Import necessery libraries 
#All libraries are built in libraries no need to install
from email.message import EmailMessage
import ssl
import smtplib 
#Getting user input 
x=int(input("how many times do you want to send this e mail: "))
body = input("enter the content of your email: ")
subject =input("enter your subject: ")
#Mail info for receiver and sender
email_sender ="aliozarbil1@gmail.com"
#Password hasn't been showed due to safety reasons
email_password = "add the password you get from your e mail for python"
email_receiver = "xeyavo4524@oniecan.com"
#Set the atributes for the mail
em = EmailMessage()
em["From"] = email_sender
em["To"] = email_receiver
em["SUbject"] = subject
#Detect the mail extension automatically
em.set_content(body)
#Send the mail
for i in range(x):
    context = ssl.create_default_context()
    #create an smtp connection to the gmail server
    with smtplib.SMTP_SSL("smtp.gmail.com" ,465, context = context) as smtp:
        #log in to the mail
        smtp.login(email_sender , email_password)
        #send the email
        smtp.sendmail(email_sender , email_receiver ,em.as_string()) 
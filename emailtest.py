import smtplib
lgemail="purushothamganguly0106@gmail.com"
recipient=lgemail
FROM = "numberplaterecognition01@gmail.com"
TO = recipient if isinstance(recipient, list) else [recipient]
SUBJECT = "Password email"
TEXT = "Your password is :"

# Prepare actual message
message = """From: %s\nTo: %s\nSubject: %s\n\n%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
try:
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login("numberplaterecognition01@gmail.com", "suoplausogdymlgx")
    server.sendmail(FROM, TO, message)
    server.close()
    print('successfully sent the mail')
except:
    print("failed to send mail")
'''
print('cccccccccc')
# message to be sent 
strval = "Your password is :"+str(pswd)
print(strval)
# sending the mail 
s.sendmail("numberplaterecognition01@gmail.com", lgemail, strval) 
  
# terminating the session 
s.quit()
'''




msg='Mail Sent Successfully'

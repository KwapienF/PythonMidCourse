import smtplib

mailFrom = 'Filippo'
mailTO = 'kwapienf@gmail.com'
mailSubject = "Finished"
mailBody = "Lecia kochana ma ciebia kocham z PYTHONA"

message = '''From: {}
Subject: {}

{}
'''.format(mailFrom,mailSubject,mailBody)

user = 'pankosztowy@gmail.com'
password = 'sjgpujxeufdsrmba'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.ehlo() # mowimy serwerowi kim jestesmy daje serwoerwi dane naszego kompa
    server.login(user,password)
    server.sendmail(user,mailTO,message)
    server.close()
    print('mail sent')
except :
    print('ERROR')
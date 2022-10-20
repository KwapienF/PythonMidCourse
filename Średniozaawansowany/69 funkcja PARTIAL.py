import smtplib
import functools


def sendinfoemail(user,password,mailFrom,mailTO,mailSubject,mailBody):
    message = '''From: {}
Subject: {}
    
{}
'''.format(mailFrom,mailSubject,mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com',465)
        server.ehlo() # mowimy serwerowi kim jestesmy daje serwoerwi dane naszego kompa
        server.login(user,password)
        server.sendmail(user,mailTO,message)
        server.close()
        print('mail sent')
        return True
    except :
        print('ERROR')
        return False


mailFrom = 'Filippo'
mailTO = 'kwapienf@gmail.com'
mailSubject = "Kropee"
mailBody = "Ciebia kocham me tu ne"
user = 'pankosztowy@gmail.com'
password = 'sjgpujxeufdsrmba'


Sendinfoemailfromgmail = functools.partial(sendinfoemail,user,password,mailSubject = 'Staly temat') # wymieniamyfunckje z ktroej ma korzystac i  parametry, które ta funkcja powinna juz znac
# teraz mozemy uzyc tej funkcji podajac tylko pozostale elementty
Sendinfoemailfromgmail(mailFrom = mailFrom,mailTO = mailTO,mailBody = mailBody) # musimy wszystko przekazywac nazwami bo wyzej przekazalismy mailSubject jako stalą nazwe  bez tego mozna tu dac normalnie parametry


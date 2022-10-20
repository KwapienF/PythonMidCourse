drive = 'c:\\'
folder = 'scripts\\python\\'
file = 'myscript.py'
path = drive + folder + file
print(path)
justText = 'text with \nnew line' # \n doda nam nowa linijke
justText2 = r'text with \nnew line' # r zamienilo wszystko na surowy text ROW czyli nawet \n bedzie zinterpretowane jako napis
print(justText)
print(justText2)
# 2 wersje na zapisane  MCdonald's z apostrofem
justText3 = 'MC Donald\'s'
justText4 = "MC Donald's"
print(justText3, justText4)
# jesli chce napsiac cudzyslow to tekst wpsize a apostrofach i na odwrot
print('tekst w "cudzyslowiu"')
# laby

print('0_(")(")', '( _._)', '(\\ (\\')
# cz3
number = '1000'
print(float(number) + 1) # moze tez byc int
print(number +str(1)) # konwertuje na string
print(type(number)) # type pokaże nam jaki typ ma zmienna   lub stałą string number data itd


# GDY CUDZYSLOW I APOSTROFY SA W TEKSICIE JAK UTWORZYC ZMIENNA?
t = 'Jestem (w) "szkole" i \'ucze sie\''
#lub
t2 = '''Jestem (w) "szkole" i \'ucze sie\''''
print(t,t2, sep='\n')



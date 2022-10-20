import math

def GiveGeomSeqElement(a1 = 2,factor = 2, index = 2): #a1 pierwszy element ciagu factor wsp ciagu index ktory element ciagu ma byc wyliczony

    an = pow(factor,index-1) * a1
    print(f'{index} element ciągu o ilorazie {factor} i pierwszym elemencie a1 = {a1} wynosi an = {an}')
    print('Ciąg prezentuje się następująco:')
    ciag = []
    for i in range(0,index+5):
        ciag.append(pow(factor,i)*a1)
    print(ciag)
    return

GiveGeomSeqElement(3,2,10)
# rozwiązanie Mobilo
print('---------------------------------------------------------------------------')
def GiveGeomSeqElement2(a1=2,factor=2,index=2):
    #returns n-th term of geometric sequence starting with element a1 and having
    value = a1*pow(factor,index-1)
    return value
print('element 64 =',GiveGeomSeqElement2(1,2,64))
print('------------------------------------------------')
a1=3
factor=2
maxindex=10
for i in range(1,maxindex):
    an = GiveGeomSeqElement2(a1=a1,factor=factor,index=i)
    print('Term ',i,'=',an)
print('------------------------------------------------')



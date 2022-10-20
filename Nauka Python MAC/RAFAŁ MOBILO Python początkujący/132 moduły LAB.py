inputdata = [0,1,2,3,5,8,13,21,34,55,89]
factortable = [0,0.01,0.02, 0.03,0.05,0.08,0.13,0.21,0.34,0.55,0.89]

import math
print(len(inputdata))
print(len(factortable))
if len(inputdata) == len(factortable):
    print('ok')
    for num1 in range(11):
        minvalue = inputdata[num1] - factortable[num1] * inputdata[num1]
        maxvalue = inputdata[num1] + factortable[num1] * inputdata[num1]
        print(minvalue,maxvalue)
        print('mininteger = ',math.floor(minvalue))
        print('maxinteger = ',math.ceil(maxvalue))
        print(math.floor(minvalue),math.ceil(maxvalue), maxvalue )
else:
    print("inputdata and factortable need to have equal number of elements")

import datetime
print(datetime.datetime.today())
print(datetime.datetime.now().strftime('%Y-%m-%d'))


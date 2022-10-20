# i = 1
# imax = 10
# while i  <= imax:
#     print(f'pętla {i}')
#     i +=1
# else:
#     print('zakończono')

#if w while
values = [10,43,12,48,12,11,18,98,57,28,19,27,49,19,74]
i =0

while i <= len(values)-3:
    if values[i] < values[i+1] and values[i+1] < values[i+2]:
        print(values[i], values[i+1], values[i+2])
        i += 1
    else:
        i += 1
else:
    print('KONIEC')
a = ['print', 'printer']
print(len(a[0]))


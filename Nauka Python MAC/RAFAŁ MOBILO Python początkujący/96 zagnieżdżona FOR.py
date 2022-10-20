# for x in range(1,6):
#     line = str(x)
#     for y in range(1,6):
#         line += ('\t%3d' % (x*y))
#     print(line)

i = 10
for x in range(1,i+1):
    for y in range(1,i):
        x = x*y
print(x)

i = 10
a = 1
for x in range(1,i+1):
    #a = x * a
    a *= x
print(a)
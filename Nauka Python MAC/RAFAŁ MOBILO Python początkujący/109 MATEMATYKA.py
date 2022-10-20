import math

f_smaller = 3.14159265
f_bigger = 3.8775639275

print(int(f_bigger))
print(int(f_smaller))
# WARTOSC BEZWZGLEDNA TO abs
print(abs(f_bigger), abs(-f_smaller))
print(round(f_bigger,2), round(f_smaller,2))

# MIN I MAX
print(min(f_bigger,f_smaller))

# moduły
import math
print(math.pi)
print(math.floor(math.pi))
# jezeli ziamportuje wszystko z math to nie trzeba psiac wtedy math
from math import *
print(pi)
print(floor(pi))

percent = [2.606255012, 1.222935044, 1.283079391, 3.628708901, 6.856455493, 4.911788292,
           2.886928629, 0.781876504, 0.962309543, 2.265437049, 6.816359262, 3.688853248,
           3.468323978, 5.633520449, 4.530874098, 1.984763432, 0.922213312, 3.327987169,
           4.190056135, 5.493183641, 1.864474739, 10.60545309, 2.425821973, 2.726543705,
           8.740978348, 6.174819567]

percent.sort()
print(percent)

# this ends with error
# print(median(percent))
# print(median_low(percent))
# print(median_high(percent))


# this succeeds
import statistics

print(statistics.median(percent))
print(statistics.median_low(percent))
print(statistics.median_high(percent))

# this succeedes
from statistics import *

print(median(percent))
print(median_low(percent))
print(median_high(percent))

f_smaller = 3.14159265
f_bigger = 3.8775639275
import math
print(math.ceil(f_bigger), math.ceil(f_smaller)) # ceil daje nam najmniejsza liczbe calkowita ktor ajest wieksza od argumentu
print(math.floor(f_bigger), math.floor(f_smaller)) # floor daje nam najwieksza liczbe calkowita ktora jest mniejsza od argumentu
#power
print(pow(2,8),pow(2,0.5)) # pow potegowanie
print(math.sqrt(16)) # pierwiastek
print(math.e) # liczba eulera
# trygonometria
print(math.sin((math.pi/2)))
# stopnie na radiany
print(math.radians(90))
# jak wyswietlic funkcje modulu math?
math_ls = dir(math)
print(math_ls)
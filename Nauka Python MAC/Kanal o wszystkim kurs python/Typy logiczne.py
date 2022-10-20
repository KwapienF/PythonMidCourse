x = True
y = False
print(x)
print(y)
print(5 == 5)  # czy są sobie równe
print( 4 != 3 )  # czy są różne od siebie
print( 5 > 5) # wiadomo, tak samo z < lub mniejsze lub równe <=> i >=
# mamy 6 operatorów porównania: == ; !=; >; <; <=; >=
a = 6
if 5 == a: # stawaimy dwukropek po if else
    print("spełniony pierwszy warunek")
    print("prawda")  # wszystko po 4 spacjac czyli tab  należy do funkji if
elif 5 > a:# else + if = elif oznacza koljeny warunek
    print("jest większy")
else:
    print("jest mniejszy")


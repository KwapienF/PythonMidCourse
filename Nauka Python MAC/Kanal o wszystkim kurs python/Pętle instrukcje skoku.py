i = 0 # potrzebne do zachowania pętli, aby nie stworzyć nieskończoną pętle
while i < 5:  # while = dopóki np. jakis warunek jest prawdziwy to zrób..
    print(i)
    i += 1
print("Koniec pętli nr 1")

print("Pętla nr 2: ")

f = 0
while True:
    f += 1
    if f % 2 ==1:
       continue  # kontynuje pętle  z pominięciem dolnych instrukcji
    print(f)
    if f > 10:
        break #"kończy pętle"
print("Koniec pętli nr 2")
a = True
b = True
l = not (a and b)
p = (not a) or (not b)
if l == p:
    print("Działa prawo Morgana")
else:
    print("nie działa prawo De Morgana")
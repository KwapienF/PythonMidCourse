def triangle(t):
    if t == 1:
        return 1
    else:
        return t + triangle(t-1)

def suma():
    for t in range(1,11):
        triangle(t)
        print(" dla t = ", t, "liczba trojkatna wynosi", triangle(t))
suma()

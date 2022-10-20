def dzielenie(x, y):
    assert y != 0, "Y ==0" # dajemy tu warunek false albo true i jak sie nie spelni to wywali asserterror
    if y == 0:
        raise ZeroDivisionError("...Bruh")  # wyrzucanie błedów w innych jezyakch throw
    print(x / y)

try:
    dzielenie(2,0)
except ZeroDivisionError:
    print("przez 0 ?!")
    raise

#assercja oznacza zapewnienie



#assercja oznacza zapewnienie



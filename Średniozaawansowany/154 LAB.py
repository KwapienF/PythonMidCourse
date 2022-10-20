import random

def random_with_sum(number_of_values,asserted_sum):# argmety ile losowac i suma do ktorej maja sie sumwoac
    trial = 0 # licznik losowan az do uzyskania asserted sum
    numbers = list(range(number_of_values))

    while True:
        trial +=1
        for i in range(number_of_values):
            numbers[i] = random.randint(1,101)
        if sum(numbers) == asserted_sum:
            yield((trial,numbers))
            trial = 0

# for i in range(10):
#     (number_of_trials, numbers) = next(random_with_sum(3,100))
#     print(number_of_trials, numbers)


print(next(random_with_sum(3,100)))



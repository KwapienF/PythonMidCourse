import math
import time
formulas_list = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
argument_list = []
for i in range (1000000):
    argument_list.append(i/10)

for formule in formulas_list:
    results_list = []
    print("Obecna formuła: ",formule)
    start = time.time()
    for x in argument_list:
        result = eval(formule)
        results_list.append(result)
    print('Max value = ', max(results_list))
    print('Min value = ', min(results_list))
    stop = time.time()
    print(f'Czas trwanai obliczeń wyniósł: {stop-start}')

    # to samo ale scompilowane
formulas_list1 = [
     "abs(x**3 - x**0.5)",
     "abs(math.sin(x) * x**2)"
     ]
argument_list1 = []
for i in range (1000000):
    argument_list1.append(i/10)

for formule1 in formulas_list1:
    results_list1 = []
    print("Obecna formuła: ",formule1)
    start1 = time.time()
    compiled_formula = compile(formule1,'internal variable', 'eval')
    for x in argument_list:
        result = eval(compiled_formula)
        results_list1.append(result)
    print('Max value = ', max(results_list1))
    print('Min value = ', min(results_list1))
    stop1 = time.time()
    print(f'Czas trwanai obliczeń wyniósł: {stop1-start1}')

print(f"Skompilowany program liczył się {(stop-start)/(stop1-start1)} razy szybciej")



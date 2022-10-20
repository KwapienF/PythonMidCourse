instruction = ['say hello', 'say how are You','abort','ask for money','say thank you', 'say bye']
instructionApproved = []
for instr in instruction:
    print("ADDING instruction: ",instr)
    instructionApproved.append(instr)
    if instr == 'abort':
        print('Aborting')
        instructionApproved.clear()
        break
else: # dodane do petli for instruckja ta else wykona sie tylko wtedy kiedy powyzej petla nie zostanie przerwana przez BREAK!!
    print('Following actions will be taken: ',instructionApproved)

# tak samo mozna ELSE uzyc w while zamiast for


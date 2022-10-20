import os

files_to_process = [
    r"C:\Users\Filip Kwapień\PycharmProjects\pythonProject\Mobilo Python\Średniozaawansowany\40 lab EXEC 1a.py"
    ]

print(os.path.basename(files_to_process[0]))

source = open(files_to_process[0], 'r').read()

#print(source)
result = exec(source)
print(result)

file = open("/Users/filipkwapien/Desktop/utrwalenie.txt", "a") # w aby zapisywac a append aby dodawal teksty i zachowal poprzedni
bytes = file.write(input("Write something: ") + "\n")
print(bytes)

file = open("/Users/filipkwapien/Desktop/utrwalenie.txt", "r") # r aby czytac
text = file.readlines()
print(text)
file.close()
import os
def tekst():

    view = open(path,'w')
    view.write("I see nothing cause its dark")
    view = open(path,'r')
    txt = view.read()
    print(txt)
    print(len(txt.split()))

path = r'c:\temp\view.txt'
result = os.path.isfile(path) and tekst()
# mobilo zrobil ot tak
# import os
#
#
# def CountWords(path):
#     with open(path, 'r', encoding='utf-16') as f:
#         content = f.read()
#         word_count = len(content.split())
#     return word_count
#
#
# path = r'c:\temp\test.txt'
# if os.path.isfile(path):
#     print("There are {} words in the file {}".format(CountWords(path), path))
#
# os.path.isfile(path) and print("There are {} words in the file {}".format(CountWords(path), path))
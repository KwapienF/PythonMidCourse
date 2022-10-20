list1 = ["red", "orange", "green", "violet", "blue", "yellow"]

def colors(list,n):
    list2 = list[:n].copy()
    return list2
#print(colors(list1,5))

for c1 in list1:
    c = [c1]
    for c2 in list1:
        if c1 != c2:
            c.append(c2)
            print(c)
        else:
            continue



# def get_list_of_colors(colors, n):
#     return colors[:n]
#
#
# colors = ["red", "orange", "green", "violet", "blue", "yellow"]
#
# for i in range(1, len(colors) + 1):
#     print(get_list_of_colors(colors, i))





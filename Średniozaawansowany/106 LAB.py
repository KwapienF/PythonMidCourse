class No_Duplicates:
    def __init__(self):
        self.new_list = []
    def __call__(self,item):
        for i in item:
            # if self.new_list.count(item) == 0:
            #     self.new_list.append(item)
            # else:
            #     print("Element already exist in list")
# inaczej
            if not i in self.new_list:
                self.new_list.append(i)



my_no_dup_list = No_Duplicates()
print(my_no_dup_list.new_list)
my_no_dup_list(['keyboard'])
my_no_dup_list(['mouse'])
my_no_dup_list(['mouse'])
print(my_no_dup_list.new_list)
my_no_dup_list(['keyboard','mouse','pendrive'])
print(my_no_dup_list.new_list)
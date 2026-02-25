import random
my_list = []
for i in range(4):
    my_list.append(random.randint(1, 10))
my_list_2 = my_list.copy()
for element in my_list:
    my_list_2.append(element * 2)
print(my_list)
print(my_list_2)
my_list = [5, 10, 15, 20, 25]

my_list.append(30)
print("After append:", my_list)

my_list.insert(2, 12)
print("After insert:", my_list)

my_list.remove(15)
print("After remove:", my_list)

popped_element = my_list.pop()
print("After pop:", my_list)
print("Popped element:", popped_element)

index = my_list.index(20)
print("Index of 20:", index)

count_10 = my_list.count(10)
print("Count of 10:", count_10)

my_list.sort()
print("Sorted list:", my_list)

my_list.reverse()
print("Reversed list:", my_list)

copy_list = my_list.copy()
print("Copied list:", copy_list)

extra_list = [35, 40, 45]
my_list.extend(extra_list)
print("Extended list:", my_list)

my_list.clear()
print("List after clearing:", my_list)

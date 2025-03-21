my_list = [10, 20, 30, 40, 50]

my_list.append(60)
print("After appending 60:", my_list)

my_list.insert(2, 25)
print("After inserting 25 at index 2:", my_list)

my_list.remove(40)
print("After removing 40:", my_list)

popped_element = my_list.pop()
print("After popping last element:", my_list)
print("Popped element:", popped_element)

index = my_list.index(30)
print("Index of 30:", index)

my_list.sort()
print("Sorted list:", my_list)

my_list.reverse()
print("Reversed list:", my_list)

copy_list = my_list.copy()
print("Copied list:", copy_list)

extra_list = [70, 80, 90]
my_list.extend(extra_list)
print("Extended list:", my_list)

my_list.clear()
print("List after clearing:", my_list)

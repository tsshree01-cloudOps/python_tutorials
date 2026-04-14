#we can delete items from list by using methods like remove(), pop(), del statement

item_list = ["a", "c", "a", "d"]

print(item_list)

item_list.remove("a") #removes first occurance of element

print(item_list)

element_value = item_list.pop()

print(element_value)
print(item_list)

del item_list[0]

print(item_list)


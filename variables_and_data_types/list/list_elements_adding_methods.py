#adding elements into list using methods like append(), extend(), insert(), clear()

list_of_items = []

list_of_items.append(99)

print("appending value to the list:", list_of_items)

list_of_items.insert(1, 2)
list_of_items.insert(2, 2)

print(list_of_items)

list_of_items.extend([1, 3, 5])

print(list_of_items)

list_of_items.clear()
print(list_of_items)

insert_item_in_list = [1, 2, 3, 4]

insert_item_in_list.insert(2, 1.1)
print(insert_item_in_list)
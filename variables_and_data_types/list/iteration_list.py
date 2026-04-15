#using for loop and in

list_of_numbers = [10, 20, 30, 40, 50]

for number in list_of_numbers:
    print(list_of_numbers.index(number))

#list comprehension

list_comp = [list_of_numbers.index(number) for number in list_of_numbers]
print("list created  =", list_of_numbers)
print("index of list =", list_comp)
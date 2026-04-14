#using square brackets

list_of_int = [1, 22, 33, 90]

list_of_float = [1.1, 2.2, 3.3, 4.4]

list_of_strings = ["a", "b", "c", "d"]

list_of_bool = [True, False]

'''print(list_of_int)
print(list_of_float)
print(list_of_strings)
print(list_of_bool)'''

#using list() constructor

list_ = list((1, "abcd", 2.2, True))
print(list_)

#creating list with repeated elements using multiplication (*) operator

int_list = [10] * 2
float_list = [1.1] * 4
string_list = ["python repeated elements list"] * 3

print(int_list)
print(float_list)
print(string_list)

#Internal representation of list -> python list stores reference of object and not the actual value directly
list_of_int = [1, 22, 33, 90]
print("initial list:", list_of_int)

print("element of list_of_int at index 0: ", list_of_int[0])

list_of_int[0] = 45

print("element of list_of_int at index 0 after ressigning a value: ", list_of_int[0])
print("a complete list after 0 index changes:", list_of_int)  #list in python is mutable, a list can be updated by assigning new values to list by using its index


print("last element of list:", list_of_int[-1])

print("reversing complete list by using slicing[start:end:step]:", list_of_int[::-1])
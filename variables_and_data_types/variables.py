#Python variables do not require explicit declaration of type.
#The type of variable is inferred based on the value assigned.


# Rules : 
# 1. variable names can only contain letters, digits and underscores. 
# 2. a variable name cannot start with digit. 
# 3. variable names are case-sensitive. 
# 4. avoid using python keywords as variable names.

"""
#valid variable names:
age = 27 #this variable 'age' contains only letters 
subject_1 = "python" #this variable 'subject_1' contains underscore and ends with digit
print(age)
print(subject_1)


#invalid variable names:
1_age = "Error" #variable name cannot start with digit
user-name = "user1" #variables cannot contain hypen
class = 100 #class is a keyword
print(1_age)
print(user-name)
print(class)

"""

Topic = "Python"
topic = "python_"#Topic and topic both variables are different as python variables are case sensitive.

print("Topic:", Topic)
print("topic:", topic)


# Assigning values to variables 
# 1. Basic assignment : values are assigned using assignment operator '='  
# 2. Dynamic typng : same variables can hold different values during execution. 
# 3. multiple assignment : assigning same value to multiple variables. 
# 4. assigning different values: assigning diffrenet values to multiple variables simultaneously, making the code concise and easier to read.

# 1. Basic assignment
name = "variables_topic_file"
print("Name:", name)

# 2. Dynamic typng
value = 10
value = "teen"
print("dynamic typing value:", value)

# 3. multiple assignment- concept of object reference- shared reference
value_1 = value_2 = value_3 = 100
print("value_1:", value_1)
print("value_2:", value_2)
print("value_3:", value_3)

# 4. assigning different values
value_1, value_2, value_3 = 1, 20, "one & tweenty"
print("value_1: {value_1}, vlaue_2: {value_2}, value_3: {value_3}") #observe the output for this line and below line
print(f"value_1: {value_1}, vlaue_2: {value_2}, value_3: {value_3}")

# Concept of object reference
x = 5
y = x 
x = "new" #reassigning a variable 
print(x, y)

y = "change"
print(x, y)
# The original object 5 no longer has any reference and becomes eligible for garbage collection. 
# Python variables holds reference of objects and not the actual objects itself.

# Type and casting a variable
# we can determine the type of a variable by using type() function.
# type() -> built-in function that returns the type of object which is passed to it.
determine_type = 10
determine_type_1 = "string"
determine_type_2 = [100, 1000]
determine_type_3 = (1,2)
determine_type_4 = {1,2,3,4,5}

float_value = 1.2

print(f"10 is a {type(determine_type)} type")
print(f"string is a {type(determine_type_1)} type")
print(f"[100, 1000] is a {type(determine_type_2)} type")
print(f"(1,2) is a {type(determine_type_3)} type")
print(f"1,2,3,4,5 is a {type(determine_type_4)} type")
print(f"float_value is a {type(float_value)} type")

# type() function syntax
# type(object) -> objetct is the value or variable whose type we want to determine.
# type(name, bases, dict) -> name of the class that we want to create, tuple of base classes, dictonary containing class attributes

a_type_try = type("April2026", (), {"date": 8}) 
#dynamic class creation named as April2026
# () -> represents an empty tuple of base classes 
print(a_type_try)
print(a_type_try.date)

# Type Casting in Python: implicit & Explicit

# Implicit: when python automatically converts one data type to another during an operation.
number = 10
float_value = 10.2

sum_of_both = number + float_value
multiplication_of_both = number * float_value

print(sum_of_both)
print(multiplication_of_both)

# Explicit: when programmer manually changes a value's data type using built-in type casting functions.
# Int(), float(), str() 

number = 100
change_to = float(number)
print("float:", change_to)

change_to = str(number)
print(change_to)

string_value = "10"
change_to = int(string_value)
print(change_to)

change_to = float(string_value)
print(change_to)

# Deleting a variable
x = 100
del x
#print(x)
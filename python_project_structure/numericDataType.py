#Everything is an object in python programming.
#python data types are classes and variables are instances(object) of these classes.
# Data types in python: 
# 1. Numeric: int, float, complex 
# 2. Sequence type: string, list, tuple 
# 3. Mapping type: dict 
# 4. Boolean: bool 
# 5. Set type: set, frozen set 
# 6. Binary type: byte, bytearray, memoryview

# 1. Numeric: int, float, complex 
# int() data type is a function which converts a given object to integer or if decimal(floating-point) number is passed then it truncates the fractional part.

data_variable_value = "60"
print("type of data_variable_value:", type(data_variable_value))

data_variable_value = int(data_variable_value)
print("converted to int data type:", data_variable_value)
print("type of data_variable_value after typecasting:", type(data_variable_value))

#Syntax of int() data type - function
# int(x,base) -> x is string representation of integer value, base is the actual integer value(base of number)

# octal to decimal using int()
value_with_base = int('0o12', 8)
print("int(x,base):", value_with_base)

# binary to decimal using int()
value_with_base = int('0b110', 2)
print("int(x,base):", value_with_base)

# hexa-decimal to decimal using int()
value_with_base = int('0x1A', 16)
print("int(x,base):", value_with_base)

#float() represents number with fractional component.
float_value = 2.75
print("float value type", type(float_value))

#complex() contains real and imaginary part represented in a+bj
#complex() function with int, float and string inputs

complex_number = complex(2,3)
complex_number_1 = complex(2)
complex_number_2 = complex()

print("complex_number:", complex_number)
print("complex_number_1:", complex_number_1)
print("complex_number_2:", complex_number_2)

complex_number_float = complex(2.5,3.5)

print("complex_number_float:", complex_number_float)

complex_number_string = complex("-1.1+4.3j")

print("complex_number_string:", complex_number_string)
print("non-negative:", float.__abs__(-1.2))

print("addition of complex numbers:", (complex_number + complex_number)) 
print("sub of complex numbers:", (complex_number - complex_number)) 
print("multi of complex numbers:", (complex_number * complex_number)) 
print("div of complex numbers:", (complex_number / complex_number)) 

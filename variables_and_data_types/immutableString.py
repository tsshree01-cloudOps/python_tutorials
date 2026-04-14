#String Immutability

a_string ="python lamguage"

b_string = "string in python"

#slicing 
slicing_a_string = a_string[0:1]
print("slicing the 0-1:",slicing_a_string)

slicing_a_string = a_string[0:2]
print("slicing the 0-2:",slicing_a_string)

slicing_a_string = a_string[0:-2]
print("slicing the 0 to -2:",slicing_a_string)

slicing_a_string = a_string[0:-1]
print("slicing the 0 to -1:",slicing_a_string)

#concatenation
con_string = a_string +" " + b_string
print("concatenation:", con_string)

#concatenation + slicing
print(("G"+a_string[0:2]))
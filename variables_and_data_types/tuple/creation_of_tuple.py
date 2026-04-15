#tuples are immutable unlike lists, once created cannot be changed or updated

var_tuple = ()

print(type(var_tuple))

#converting tuple to list
var_tuple = (1, 'stringintuple', True)
print(var_tuple[0])
print("convert tuple to list?: lets see..", list(var_tuple))

#converting list to tuple
list_of_string = ['astring', 'bstring1']
print("convert list to tuple?", tuple(list_of_string))
var_convert = tuple(list_of_string[1])
print(var_convert)

#list(iterable) function and tuple(iterable) function
print("length of tuple:", len(var_convert))



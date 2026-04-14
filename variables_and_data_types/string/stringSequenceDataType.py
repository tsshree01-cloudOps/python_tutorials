#string formatting 

user_name = input("enter name:")
user_age = input("enter age:")

#using f-string
#print(f"Name:{user_name}, Age:{user_age}")

#using format()

a_sentence = "name: {}, age: {}".format(user_name, user_age)

print(a_sentence)
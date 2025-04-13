# in input() any data is string


name=input("Enter your name: ")
qualification=input("enter your highest qualification:")
print("your name is ",name)
print("ypur age is ",qualification)
print(type(qualification), qualification) #input() always returns a string
print(type(name), name) #input() always returns a string


# to enter perticulat datatype data we must use type casting

val=int(input("enter any value:"))
print(type(val),val) 

marks=float(input("enter your marks:"))
print(type(marks),marks)

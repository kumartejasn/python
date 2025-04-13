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

val1=int(input("enter any integer value:"))
val2=int(input("enter any integer value:"))
sum=val1 + val2 # 12+13=25
print(type(sum),sum)

# print the area of the square with side value

side=float(input("Enter the side:"))
area=side*side # side*side=area
print(type(area),area) # area is float
print("area of squareis", side*side)


# average of two floating numbers
f1=float(input("enter first float number:"))
f2=float(input("enter second float number:"))
avg=(f1+f2)/2 # average of two float numbers
print(type(avg),avg)
print("the average of two numbers is",(f1+f2)/2) # average of two float numbers


#check first nuber greater or not
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
print(num1>=num2) # true
print(num1<=num2) # false

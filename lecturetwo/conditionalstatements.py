# conditional statements



#checking elegibility to vote
age=24

if(age>=18):
    print("can vote")
else:
    print("can not vote")


#giving rating to a movie based on user input
rating=int(input("enter the rating of the movie: " ))

if(rating>=4.5):
    print("blockbuster")
elif(rating>=3.5 and rating<4.5):
    print("good")
elif(rating>=2 and rating<3.5):
    print("average")
elif(rating<2):
    print("flop")
else:
    print("enter a valid rating number")



#giving grades based on marks

marks=int(input("enter the marks:"))

if(marks>=90):
    print("grade A")
elif(marks>=80 and marks<90):
    print("grade B")
elif(marks>=70 and marks<80):
    print("grade C")
elif(marks>=60 and marks<70):
    print("grade D")
elif(marks>=50 and marks<60):
    print("grade E")
elif(marks<50):
    print("grade F")
else:
    print("enter a valid marks number")



#nested if else statement

age1=int(input("enter your age:"))

if(age1>=18):
    if(age1>=25):
        print("you are not eligible for army")
    else:
        print("you are eligible for army")
elif(age<18):
    print("ypu are minor")





#practice

#fine wheather the entered number is even or odd

number=int(input("enter the number:"))
if(number%2==0):
    print("entered number is even")
elif(number%2==1):
    print("entered number is odd")
else:
    print("enter a integer number")


#find the greater number

n1=int(input("enter the first number:"))
n2=int(input("enter the second number:"))
n3=int(input("enter the third number:"))
if(n1>n2 and n1> n3):
    print("first number is greater")
elif(n2> n1 and n2>n3):
    print("second number is greater")
elif(n3>n1 and n3>n2):
    print("third number is greater")
else:
    print("enter integer numbers")


#find wheather number is divisible by 7 or not

n7=int(input("enter the number:"))
if(n7%7==0):
    print("number is divisible by 7")
elif(n7%7!=0):
    print("number is ot divisible by 7")
else:
    print("enter an integer number")

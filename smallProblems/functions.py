# prime numbers

for num in range(2,101):
    is_prime=True
    for i in range(2,num):
        if(num%i==0):
            is_prime=False
            break
    if is_prime==True:
        print(num)



# or


for num in range(2, 101):  
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num , end=' ')



# natural numbers

for num in range(1, 101):
    print(num)



# functions 


def multiple():
    a=2
    b=4
    mul=a*b
    print(mul)
multiple()


 
def div(a=30,b=2):
    division=a/b
    print(division)
div()



def fun(a, b):
    sum=a+b
    print(sum)
fun(4,5)    

x=int(input("enter the value of x :"))
y=int(input("enter the value of y :"))

def avg(x,y):
    average=(x+y)/2
    print(average)
    return average
average=avg(x,y)
print(average)



# WAP to find the lenth of a list using function

states=["karnataka","andhra pradesh","tamilnadu","kerala","telangana"]
player=["Dhoni","raina","rohith"]
def state1(list1):
    print(len(list1))
    print(list1)
state1(states)
state1(player)


def fun(list):
    for v in list:
        print(v,end=" ")
fun(player)



def factorial(n):
    f=1
    for o in  range(1,n+1): 
        f *= o
    print(f)
    return f
factorial(7)
x=factorial(97)


# USD TO INR

def convertor(USD):
    INR=USD * 86
    print(USD, "USD=",INR)
convertor(5)    


# even or add

y=int(input("enter the number: "))

def find_num(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")
find_num(y)


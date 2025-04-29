# functions 
def fun(a, b):
    sum=a+b
    print(sum)
fun(4,5)    

x=int(input("enter the value of x :"))
y=int(input("enter the value of y :"))

def f1(x,y):
    average=(x+y)/2
    print(average)
    return average
f12=f1(x,y)
print(f12)



# WAP to find the lenth of a list using function

states=["karnataka","andhra pradesh","tamilnadu","kerala","telangana"]
player=["Dhoni","raina","rohith"]
def st(list1):
    print(len(list1))
    print(list1)
st(states)
st(player)


def fun(list):
    for v in list:
        print(v,end=" ")
fun(player)



def fac(n):
    l=1
    for o in  range(1,n+1):
        l *= o
    print(l)
    return l
fac(7)
x=fac(97)


# USD TO INR

def convertor(USD):
    INR=USD * 86
    print(USD, "USD=",INR)
convertor(5)    


# even or add

y=int(input("enter the number: "))

def f(num):
    if(num%2==0):
        print("even")
    else:
        print("odd")
f(y)


# Recursion
import sys

print(sys.getrecursionlimit())

# i=1
# def f():
#     global i
#     i +=1
#     print("hello world", i)
#     f()
# f()


def show(n):
    if(n==0):
        return
    print(n)
    show(n-1)
show(5)


# factorial of a number

def fact(n):
    if(n==0):
        return 1
    return n*fact(n-1)
print(fact(7))


# calculating the sum of natural numbers

def sum(n):
    if(n==0):
        return 0
    return sum(n-1) + n
print(sum(7))



# print the elements of list using recursion
list=["a","b","c","d","e","f"]

def l(list1,idx=0):
    if(idx==len(list1)):
        return
    print(list[idx])
    return l(list1,idx+1)

print(l(list,0))

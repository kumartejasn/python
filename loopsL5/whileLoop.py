# while loop
# while loop is used to repeat a block of code as long as the condition is true


i=1
while i<=5:
    print("hello world",i)
    i+=1


i1=15
while i1>=10:
    print(i1)
    i1 -=1



# while loop with multiple conditions

l2=1
l3=30
while l2<=10 and l3>=20:
    print("hello world")
    print(l2)
    print(l3)
    l2+=1
    l3-=1

print("loop ended")
print(l2,l3)


x=1 
y=15

while x<=5 or y>=6:
    print("x",x)
    print("y",y)
    x+=1
    y-=1 
print("loop ended")



# print table of any number

n=3
i=1
while(i<=10):
    print(n*i)
    i+=1

i2=1
while(i2<=10):
    print(i2*8)
    i2+=1
    
# print sqaule numbers of 1 to 10

n = 1
while n <= 10:
    print(f"Square of {n} is {n * n}")
    n += 1


t=1
list=[]
while t<=10:
    list.append(t*t)
    t+=1
print(list)


# search a number in the list or tupple
list1=[1,2,3,4,5,6,7,8,9,10]
u=4
v=0
while(v<len(list1)):
    if (list1[v] == u):
        print("element found at index",v)
    v+=1



# search a number in the list or tupple
b=(1,2,3,34,64,77,887,9657,4656,456,4656)
z=4656
m=0
while m<len(b):
      if(b[m] == z):
          print("element found at index",m)
      else:print("finding")
      m+=1


#BREAK STATEMENT
# break statement is used to exit the loop when the condition is met


o=1
while o<=6:
    if o==3:
        break
    print(o)
    o+=1
r1=[1,2,3,4,5,6,7,8,9,10]
r=0
while(r<len(r1)):
    if(r1[r]==8):
        break
    print(r1[r])
    r+=1


# continue statement
# continue statement is used to skip the current iteration of the loop and move to the next iteration

c=1
while(c<=10):
    c+=1
    if(c==6):
        continue
    print(c)
     
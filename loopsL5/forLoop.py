# for loop with range function

l=[1,3,4,5,63,542]
for v in l:
    if(v==5):
        continue
    print(v)
 

list=[1,23,43,463,636,23,4,5,6,7,8,9]
for i  in list:
    if(i==8):
        break
    print(i)


l2=(1,2,3,4,5,"t","a")
for n in l2:
    print(n)
else:
    print("end")



# finding the index of an element in a list using for loop

l3=[1,2,3,4,34,31,344,41,232,42,4,5,6,7,8,9]
x=5
idx=0
for k in l3:
    if(k==x):
        print("index of the element is ", idx)
    idx +=1


# range funcction in loop

for i in range(1,10): 
    print(i)


for j in range(2,101,2): # first is starting point, second is the ending point and third is the step
    print(j)


for v in range(100, 0,-1): # first is starting point, second is the ending point and third is the step
    print(v)



# print a table

p=int(input("enter a number:"))

for o in range(1,11):
    print(p*o)




# pass satement in loop
# pass statement is used when you want to do nothing in the loop and acts as a placeholder

for u in range(8):
    pass # it will not print anything but will not give an error as well


# WAP to find the sum of numbers

l=6
sum=0
for f in range(1,l+1):
    sum += f
print(sum)    


# same using while loop

l1=6
sum1=0
f1=1
while f1<=l1:
    sum1 +=f1
    f1 +=1
print(sum1)


# find the factorial of a number using for loop

l2= int(input("enter a number:"))
fact=1
for f2 in range(1,l2+1):
    fact *=f2
print(fact)

# using while loop
l3 = int(input("enter a number:"))
fact2=1
f3=1
while f3<=l3:
    fact2 *=f3
    f3 +=1
print(fact2)

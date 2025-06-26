# find the largest element
list1=[2,3,4,1,23,42,4142,42,12]
print(max(list1))

#using loop
largest=list1[0]
for el in list1:
    if el > largest:
        largest=el
print(largest)

# usiing descending sorted
lar1=sorted(list1, reverse=True)
print(lar1[0])

# by sorted method

large=sorted(list1)[-1]
print(large)
        
# or
lar=sorted(list1)
print(lar[-1])


#find the second largest

l=list1[0]
for ele in list1:
    if(ele>l and ele<largest):
        l=ele
print(l)

# sorted method

l2=sorted(list1)
print(list[-2])

#find the smallest

l2=list1[0]
for ele in list1:
    if(ele<l2):
        l2=ele
print(l2)

# find the even numbers
for el in list1:
    if(el %2==0):
        print(el)
    #print(el)



list = [10, 23.5, "hello", 42, 3.14, True, "world", 99.9, False]
intigers=[]
string=[]
bool1=[]
float1=[]
others=[]
for ele in list:
    if(isinstance(ele,int) and not isinstance(ele,bool)):
        intigers.append(ele)
    elif(isinstance(ele,str)):
        string.append(ele)
    elif(isinstance(ele, bool)):
        bool1.append(ele)
    elif(isinstance(ele, float)):
        float1.append(ele)
    else:
        others.append(ele)

print(intigers)
print(string)
print(float1)
print(bool1)
print(others)


import numpy as np

items = [10, 23.5, "hello", 42, 3.14, True, "world", 99.9, False]
arr = np.array(items, dtype=object)

integers1 = []
strings1 = []
floats1 = []
booleans1 = []
others1 = []

for ele in arr:
    dtype = type(ele)
    if dtype == int:
        integers1.append(ele)
    elif dtype == str:
        strings1.append(ele)
    elif dtype == float:
        floats1.append(ele)
    elif dtype == bool:
        booleans1.append(ele)
    else:
        others1.append(ele)

print("Integers:", integers1)
print("Strings:", strings1)
print("Floats:", floats1)
print("Booleans:", booleans1)
print("Others:", others1)



#class methods

class Calculator:
    def add(self, a, b):  # Instance method
        return a + b

    @classmethod
    def get_info(cls):  # Class method
        return "This is a Calculator class"

    @staticmethod
    def multiply(a, b):  # Static method
        return a * b


calc = Calculator()

# Calling methods
print(calc.add(3, 4))          
print(Calculator.get_info())   
print(Calculator.multiply(3, 4))  

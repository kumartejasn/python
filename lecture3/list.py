#list 

list1=[1,2,3,4,5]
print(list1)
print(list1[1])
print(list1[0:2])
print(type(list1))
print(len(list1))
list1[0]="tejas"
print(list1)


#LIST METHOND OR FUNCTION


# 1) List slicing

l1=[1,"tejas","kumar", 4.56,True]
print(l1[2:3]) #same string slicing second value is exluded
print(l1[:3]) #from 0 to 3
print(l1[3:]) #from 3 to last

#slicing with negative index
print(l1[-3:-1]) #from -3 to -1 and -1 is excluded
print(l1[-4:]) #from -4 to last
print(l1[:]) #all elements of list
print(l1[::-1]) #reverse the list



# 2) List append method

l2=[1,25,6,76,7823,45]
l2.append(25) #append the value at last of list
print(l2)
print(l2.append(12)) #returns none
print(l2) #append the value at last of list
l1.append("kumar")
print(l1)


#3) list sort method

l3=[1,6,3,5,2,4,3,53,3]
print(l3.sort()) #returns none value
print(l3) #sort the list in ascending order

l3.sort(reverse=True) #sort the list in descending order
print(l3) #sort the list in descending order

#sort can be done to strings also

l4=["a","c","d","b","g","e","f"]
l4.sort() #sort the list in ascending order
print(l4) #sort the list in ascending order
l4.sort(reverse=True) #sort the list in descending order
print(l4) #sort the list in descending order

names=["tejas","kumar","dhoni","sachin","raina"]
names.sort() #sort the list in ascending order
print(names) #sort the list in ascending order
names.sort(reverse=True) #sort the list in descending order
print(names) #sort the list in descending order


# 4) list reverse  method

l=[1,2,3,4,5,6,7,8,9]
l.reverse()
print(l) #reverse the list
n=["tejas", "kumar", "dhoni", "sachin", "raina"]
n.reverse()
print(n) #reverse the list  


# 5) list insert method list.insert(index,value)

l0=[1,2,3,4,5,6]
print(l0.insert(4,11)) #returns none
print(l0) # 11 is inserted at index 4

n2=["tejas", "kumar", "dhoni", "sachin", "raina"]
n2.insert(3,"tribu") #insert tribu at index 3
print(n2) #insert tribu at index 3


# 6)  remove(value or element) method "removes first occurence of the value"

n2.remove("tejas") #remove first occurence of tejas
print(n2) 

list1245=[11,22,33,44,55,44]
list1245.remove(44) #remove first occurence of 44
print(list1245) #remove first occurence of 44


# 7) pop(index) method "removes the element at the index and returns it"
list12456=[12,34,56,7777,87,764,23,45]
print(list12456.pop(3)) #remove and return the element at index 3
print(list12456) #remove element at index 3 and return list12456


print(n2.pop(3)) #remove and return the element at index 3
print(n2) # remove element at index 3 and return n2







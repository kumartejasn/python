# WAP to 3 movies input names and store them in a list and print the list
movies=[]
mov1=input("enter the first movie name:")
movies.append(mov1)
mov2=input("enter the second movie name:")
movies.append(mov2)
mov3=input("enter the third movie name:")
movies.append(mov3)
print(movies)

#or

movies2=[]
movies2.append(input("enter the movie name: "))
movies2.append(input("enter the movie name:"))
movies2.append(input("enter the movie name:"))
print(movies2)



# WAP the list is palindrome or not
list1=["tejas","kumar","tejas"]
copy_list1=list1.copy()
copy_list1.reverse()

if(list1==copy_list1):
    print("list is a palindrome")
else:print("list is not a palindrome")


l1=[1,2,1]
l2=l1.copy()
l2.reverse()
if(l1==l2):
    print("list is a palindrome")
else:
    print("l1 is not a palindrome")


    #WAP to find the number of students get grade A in a tuple

grade=("A","A","D","B","E","A","B","B")
print(grade.count("A"),"stdents got grade A") #returns the number of times the element appears in tuple


#sorting a list

list1=["b","a","d","c"]
list1.sort()
print(list1) #sort the list in ascending order

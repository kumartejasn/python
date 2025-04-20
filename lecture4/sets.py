# Set in Python
# A set is a collection of unique elements.
# A set is created using curly braces {} or the set() function.
# A set is unordered, meaning the items have no index.
# A set is unchangeable, meaning you cannot change the items after creation.
# However, you can add or remove items from a set.

s1={1,2,3,2,"tejas","dhoni"}
print(s1)
print(type(s1)) #print the type of the set
print(len(s1)) #print the length of the set

s2={1,2,3,(1,2,"tejas","tejas"),"dhoni",1} #tuple is immutable
print(s2) #print the set
print(len(s2)) #print the length of the set


s3={1,2,3,(1,2,"tejas","tejas"),"dhoni",1,(1,2,"tejas","tejas")}
print(s3)

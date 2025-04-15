# TUPLE 
# Tuples are immutable sequences, typically used to store collections of heterogeneous data.
# Tuples are similar to lists, but they cannot be changed after creation.


# Creating a tuple

t1=(1,) # tuple with one element there must be a comma after the element
t2=(1,2,3,4,5) # tuple with multiple elements


#slicing a tuple

print(t2[1:3]) #from 1 to 2 and 2 is excluded

t3=("tejas","kumar","dhoni","sachin","raina")
print(t3[3:4]) #from 3 to 3 and 3 is excluded




# indexing a tuple .index(element) returns the index of the element in tuple

print(t3.index("tejas")) #returns the index of the element in tuple
print(t2.index(4)) #returns the index of the element in tuple



#.count(element) returns the number of times the element appears in tuple

tup=(1,2,3,4,5,6,1,1,2,3,3,4,4,4,5)
print(tup.count(2)) #returns the number of times the element appears in tuple
print(tup.count(1)) #returns the number of times the element appears in tuple

tup2=("tej","tej","kumar","dhoni","dhoni","dhoni")
print(tup2.count("tej")) #returns the number of times the element appears in tuple
print(tup2.count("dhoni")) #returns the number of times the element appears in tuple


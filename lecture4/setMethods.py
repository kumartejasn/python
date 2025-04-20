s={ 1,2,3,4,4,"tejas","kumar",(1,2,3,"dhoni")}


# add(el) method add new element to set

s.add(5)
print(s)
print(len(s))


# remove(el) removes the element

s.remove(4) # removes all the 4's
print(s)


#clear() empties the set

s0={1,2,3,4,5}
s0.clear()
print(s0) # set() is the syntax for empty set
print(len(s0))



# pop() removes random element from set

s2={1,2,3,4,"tejas",213,324,(1,2,3,"dhoni")}
s2.pop()
print(s2)


# union() combines both set values and returns new

s4={23,123,234,1,2}
print(s.union(s2)) # combines both set values and returns new set
print(s.union(s2,s4)) # combines both set values and returns new set
print(s) # s remains unchanged and same for s2 and s4



# intersection() # combines the common values

print(s.intersection(s2)) # combines the common values and returns new set
print(s.intersection(s2,s4)) # combines the common values  in all the 3 sets and returns new set
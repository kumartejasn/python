# dictionary methods


student={
    "name":"dhoni",
    "college":"east point",
    "education":{
        "degree":"BE",
        "branch":"cse",
        "subjects":{
            "sem1":["C","Physics","Electrical"],
            "sem2":["java","Data atructures","ADE"]
        },
        "cgpa":6,
        "year":2020
    },
    "USN":"1EP20CS099",
    "YEAR":2020
}


# keys() method
# The keys() method returns a view object that displays a list of all the keys in the dictionary.
# we must use typecasting to convert the view object to a list.

print(list(student.keys())) #print the keys of the dictionary
print(len(student.keys())) #print the number of keys in the dictionary
print(len(list(student.keys())))



# values() method
# The values() method returns a view object that displays a list of all the values in the dictionary.

print(student.values()) #print the values of the dictionary
print((list(student.values()))) #print the values of the dictionary



# items() method
# The items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.

print(student.items()) #print the items of the dictionary
print(list(student.items())) #type casting the view object to a list
pair=list(student.items())
print(pair[0]) #print the first item of the dictionary



# get() method
# The get() method returns the value for the specified key if the key is in the dictionary.
# If the key does not exist, it returns None (or a specified value).

print(student.get("education"))
print(student.get("subjects")) # none will displayed instead of error



# update()
# The update() method updates the dictionary with the specified key-value pairs.
# The specified key-value pairs will be added to the dictionary.
# If the key already exists, the existing key-value pair will be updated.

student.update({"city":"bengalore"})    #updating the dictionary with new key-value pair
print(student)
parents={"father":"narayanaswami","mother":"sathya"}
student.update(parents)
print(student)
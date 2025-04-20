#Dictionaries
# A dictionary is a collection of key-value pairs
# A dictionary is created using curly braces {} 
# A dictionary is unordered, changeable and indexed
# A dictionary can contain multiple data types
# A dictionary is mutable, meaning it can be changed after creation


information={
    "name":"tejas",
    "address":"kamalavaripalli",
    "age":24,
    "subjects":["python","javascript","java"],
    "topics":("statements","functions","datastructures"),
    3:"three"
}

print(information) #print the dictionary
print(information["name"]) #accessing the value using key
print(information["subjects"]) #accessing the value using key

information["name"]="dhoni" #updating the value using key
information["subjects"]=["c","c++","python"] #updating the value using key
print(information) #print the dictionary after updating
information["subjects"].append("java") #updating the value using key
print(information["subjects"]) #accessing the value using key]
print(type(information)) #print the type of the dictionary


# 2) example of dictionary with different data types

company={
    "name":"Microsoft",
    "location":"hyderabad",
    "field":["AL and ML","OS","hardware","software","cloud"],
    "market capital":"2.5 trillion"
}

print(company) #print the dictionary
print(company["name"]) #accessing the value using key
company["employees"]=10000000 #adding new key-value pair to the dictionary
print(company) #print the dictionary after adding new key-value pair



#nested dictionary
# A dictionary can contain another dictionary as a value

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
    }
}
print(student["education"])
print(student["education"]["subjects"])
print(student["education"]["subjects"]["sem2"])
print(student)






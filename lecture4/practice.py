# store the following words meaning in a python dictionary
# table:"a piece of furniture", "list of facts and figures"
# cat:" a small animal"

first={
    "table":("a piece of furniture", "list of facts and figures"),
    "cat":" a small animal"
}
print(first)


#you are given a list of subjects for students.Assume one classroom is required for one subject. how many classrooms are needed by all students
# "python","java","c++","python","javascript","java","python","java","c++""c"

subjects={"python","java","c++","python","javascript","java","python","java","c++""c"}
print(len(subjects),"classrooms are needed") # len of subjects is equal to class rooms needed



# WAP to enter marks of 3 subjects from the user and store them in a dictionary.start with empty dictionary and add one .Use subject name as key and marks as value


student={}
x= int(input("enter the physics marks: "))
student.update({"physics":x})
print(student)
y=int(input("enter the chemistry marks:"))
student.update({"chemistry":y})
print(student)
z=int(input("enter the marks of maths:"))
student.update({"maths":z})
print(student)



# figure out  a way to store 9 and 9.0 as separate values in the set
# you v=can use built in data types

values={"9",9.0}
print(values)

values1={

    ("int",9),
    ("float",9.0)
}
print(values1)
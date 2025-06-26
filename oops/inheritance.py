# class Animal:
#     def __init__(self,name):
#         self.name=name
    
#     def animal(self):
#         return self.name
    

# class Lion(Animal):
#     def animal(self):
#         return self.name
    
# lion=Lion("Roar")
# print(lion.animal())



# # child with multiple parents

# class Teacher1:
#     def __init__(self,name):
#         self.sub1_name=name

#     def subject(self):
#         return self.sub1_name
    

    
# class Teacher2:
#     def __init__(self,name):
#         self.sub2_name=name

#     def subject(self):
#         return self.sub2_name
    
# class Student(Teacher1,Teacher2):

#     def __init__(self,name1,name2):
#         self.sub1_name=name1
#         self.sub2_name=name2
#         Teacher1.__init__(self,name1)
#         Teacher2.__init__(self,name2)

#     def subjects(self):
#         return Teacher1.sub1_name(self), Teacher2.sub2_name(self)
    
#     def subject(self):
#         return self.sub1_name, self.sub2_name
    
# subjects=Student("physics","chemistry")
# print(subjects.subject())


class Teacher1:
    def __init__(self, name):
        self.teacher1_name = name  

    def subject(self):
        return self.teacher1_name

class Teacher2:
    def __init__(self, name):
        self.teacher2_name = name 

    def subject(self):
        return self.teacher2_name

class Student(Teacher1, Teacher2):
    def __init__(self, name1, name2):
        self.sub_name1 = name1
        self.sub_name2 = name2
        Teacher1.__init__(self, name1)  
        Teacher2.__init__(self, name2)  

    def subjects(self):
        return self.sub_name1, self.sub_name2

subjects = Student("physics", "chemistry")
print(subjects.subjects())  # Output: ('physics', 'chemistry')


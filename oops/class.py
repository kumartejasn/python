# # Methods

# #instance methods

# class Student:
#     def __init__(self,name,subject,marks):
#         self.name1=name
#         self.subject=subject
#         self.marks=marks
    
#     def name(self):
#         return self.name1
    
#     def student(self):
#         return self.name1,self.subject,self.marks
# student1=Student("Tejas","Maths","77")
# print(student1.name())
# print(student1.student())



# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
#         self.bonuses = []

#     def add_bonus(self, bonus):
#         """Add a bonus to the employee's bonus list."""
#         self.bonuses.append(bonus)

#     def calculate_total_compensation(self):
#         """Calculate total compensation including salary and bonuses."""
#         return self.salary + sum(self.bonuses)

#     def get_details(self):
#         """Return a string with employee details."""
#         return f"Employee: {self.name}, Salary: ${self.salary}"

# # Creating an instance
# emp = Employee("Alice", 50000)

# # Calling instance methods
# print(emp.get_details())              
# emp.add_bonus(5000)
# emp.add_bonus(3000)
# print(emp.calculate_total_compensation())  # Output: 58000



# # class methods

# class Library:
#     total_books = 0  # Class attribute
#     book_list = []   # Class attribute

#     def __init__(self, book_name):
#         self.book_name = book_name
#         Library.total_books += 1
#         Library.book_list.append(book_name)

#     @classmethod
#     def get_total_books(cls):
#         """Return the total number of books in the library."""
#         return cls.total_books

#     @classmethod
#     def get_book_list(cls):
#         """Return the list of all book names."""
#         return cls.book_list

#     @classmethod
#     def create_from_list(cls, book_names):
#         """Factory method to create multiple book instances from a list."""
#         return [cls(name) for name in book_names]

# # Calling class methods
# print(Library.get_total_books())  # Output: 0
# book1 = Library("Python 101")
# book2 = Library("Data Science")
# print(Library.get_total_books())  # Output: 2
# print(Library.get_book_list())   # Output: ['Python 101', 'Data Science']

# # Using factory method
# new_books = Library.create_from_list(["AI Basics", "ML Guide"])
# print(Library.get_total_books())  # Output: 4
# print(Library.get_book_list())   # Output: ['Python 101', 'Data Science', 'AI Basics', 'ML Guide']




# class Date:
#     def __init__(self,day,month,year):
#         self.day=day
#         self.month=month
#         self.year=year
    
#     @classmethod
#     def from_date(cls,date_string):
#         day , month , year =map(int, date_string.split('-'))
#         return cls(day,month,year)
    

#     def __str__(self):
#         return f"{self.day:02d}-{self.month:02d}-{self.year}"
    
# date=Date.from_date("12-12-2001")
# print(date())
        


# class  Test:
#     name="tejas"
#     age=24

#     def __init__(self,education,family_name):
#         self.education = education
#         self.family_name = family_name

#     def person(self,father):
#         return f"person name is {Test.name} and his family name is {self.family_name} and his father name is {father} "
    
# details=Test("BE","Nanjappagari")
# print(details.person("narayanswami"))


# class Student:
#     name="kumar"
#     education="BE"
#     total=[]

#     def __init__(self,sub1,sub2,sub3):
#         self.sub1=sub1
#         self.sub2=sub2
#         self.sub3=sub3
    
#     def student(self):
#          Student.total = self.sub1+self.sub2+self.sub2
#          return Student.total
    
#     @classmethod
#     def marks(cls):
#         return cls.name

# student=Student(98,77,88)
# print(Student.marks())
# print(student.student())



# # empty method

# class Example:
#     def empty(self):
#         pass


# class Tejas:
    
#     def _init__(self, name, age):
#         self.name1=name
#         self.age1=age
    
#     def person(self,familyname):
#         return self.name1,self.age1, familyname 
# tejas=Tejas("tejas", 24)
# print(tejas.person("nanjappagari"))


# class Company:
#     def __init__(self, turnover, profit, employees):
#         self.turnover1=turnover
#         self.profit1=profit
#         self.employees1=employees
#         self.salaryExpense=[]

#     def add_salary_expense(self, salary):
#         """Add a salary expense to the company's salary expense list."""
#         self.salaryExpense.append(salary)
    
#     def company_details(self):
#         return f"Turnover: {self.turnover1}, Profit: {self.profit1}, Employees: {self.employees1}"

# company=Company(10000000, 1000000, 100)
# company.add_salary_expense(4000000)
# print(company.company_details())
# print(f"Salary Expenses: {company.salaryExpense}")
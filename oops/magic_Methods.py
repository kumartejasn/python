# magical methods

# __init__ methods

# class Person:
#     def __init__(self,name,country,age):
#         self.name=name
#         self.country=country
#         self.age=age
    
#     def person(self):
#         return self.name, self.country, self.age
    
# details=Person("tejas","india",24)
# print(details.person())


# __str__ method

# class Company:
#     def __init__(self,name,origin,marketCap):
#         self.name=name
#         self.origin=origin
#         self.marketCap=marketCap

#     def company(self,employees):
#         self.current_emp=employees

#     def __str__(self):
#         # return f"{self.marketCap}"
#         cur_emp = self.current_emp
#         return f"{self.origin} , {self.marketCap},{cur_emp}"
    
#     def __repr__(self):
#         cur_emp=self.current_emp
#         return f"{cur_emp}"
    

# company=Company("Star Link","America",1000000)
# company.company(10000)
# print(company)


# __eq__ method

# class Air_force:
#     def __init__(self,name,number,country):
#         self.name=name
#         self.number=number
#         self.country=country

#     def air_force(self,gen):
#         return self.name, gen, self.number, self.country

#     def __eq__(self,other):
#         if not isinstance(other, Air_force):
#             return NotImplemented
#         return self.name==other.name and self.number==other.number and self.country==other.country

# airforce=Air_force("rafel",34,"India")
# airforce2=Air_force("rafel",34,"India")
# print(airforce==airforce2)
# print(airforce.air_force("5th"))


# class Navy:
#     def __init__(self,name,number,country):
#         self.name=name
#         self.number=number
#         self.country=country

#     def navy(self,gen):
#         return self.name, gen, self.number, self.country
    
#     def __eq__(self,other):
#         if not isinstance(other,(Air_force , Navy)):
#             return NotImplemented
#         return self.name==other.name and self.number==other.number and self.number==other.country
    
# navy=Navy("rafel",34,'India')
# print(navy.navy("5th"))

# print(airforce == navy)


# __len__ method


# class List:
#     def __init__(self, items):
#         self.items = items
    
#     def __len__(self):
#         return len(self.items)

# list = List([1, 2, 3])
# print(len(list))  




# class Stack:
#     def __init__(self):
#         self._items = []
    
#     def push(self, item):
#         self._items.append(item)
    
#     def pop(self):
#         return self._items.pop()
    
#     def __len__(self):
#         return len(self._items)

# stack = Stack()
# stack.push(1)
# stack.push(2)
# print(len(stack)) 
# stack.pop()
# print(len(stack))  


# #__getitem__ method

# class MyList:
#     def __init__(self, items):
#         self.items = items
    
#     def __getitem__(self, key):
#         return self.items[key]

# my_list = MyList([10, 20, 30, 40])
# print(my_list[0])      
# print(my_list[1:3])    


# __iter__ method

class Counter:
    def __init__(self,count, limit):
        self.count = count
        self.limit = limit

    def __iter__(self):
        return self  

    def __next__(self):
        if self.count >= self.limit:
            raise StopIteration
        self.count += 1
        return self.count

for i in Counter(0,5):
    print(i)
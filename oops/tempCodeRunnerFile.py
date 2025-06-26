s Air_force:
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

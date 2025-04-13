#str.endswith("")

string="apple"
print(string.endswith("le")) #true
stringtf=string.endswith("e")
print(stringtf) #true

s2="tejas"
print(s2.endswith("s"))
print(s2.endswith("te")) #false



#str.captitalize()   , capitalize the first letter of the string and rest of the string will be in lower case

s1="i will call u later"
print(s1.capitalize()) #I will call u later
print(s1) #i will call u later
s1=s1.capitalize()
print(s1) #I will call u later


s2="oop's cancept"
print(s2.capitalize()) #Oop's cancept
print(s2) #oop's cancept
s2=s2.capitalize()
print(s2) #Oop's cancept


#str.replace(old, new, count)  , replaces the old string with new string in the given string

s3="i will be back in tan minutes"
print(s3.replace("tan","ten")) #i will be back in ten minutes
print(s3) #i will be back in tan minutes
s3=s3.replace("tan","ten")
print(s3) #i will be back in ten minutes



s4="i will cell u "
print(s4.replace("e","a")) #i will call u
s4=s4.replace("e","a")
print(s4) #i will call u




#str.find(substring, start, end)  , returns the index of the first occurrence of the substring in the string. If not found, it returns -1.


s5="change is the only constant in life"
print(s5.find("i")) #10
print(s5.find("constant")) #20
print(s5.find("tejas")) # -1


#count(substring, start, end)  , returns the number of occurrences of the substring in the string.

s6="change is the only constant in life"
print(s6.count("a")) #2


#practice 

# WAP a program to find user first name find the length of first name

user=input("Enter your first name:")
print("your first name is ",user)
print(len(user)) #length of the string



#  WAP to find s o occurrences of a letter in a string
s7="tejas kumar"
print(s7.count("s")) #1

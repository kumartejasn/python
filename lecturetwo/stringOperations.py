# concatination

str1="tejas"
str2=" kumar"
print(str1+str2) # tejas kumar
final_str=str1+str2 # tejas kumar
print(final_str) # tejas kumar


#string length

s1="tejas"
s2="kumar"
print(len(s1)) #5
print(len(s2)) #5
len1=len(s1) #5
len2=len(s2) #5
print(len1) #5
print(len2) #5
final= len1  + len2 
print(final) #10
final_str=s1 + " " + s2 # tejas kumar
print(len(final_str)) #10




#string indexing

name="mahendra singh dhoni"
print(name[4]) #n
print(name[0])
# name[2] = "a" # not possible




#STRING SLICING

string="tejas kumar"
print(string[0:5]) #tejas here 0 and 5 are index values and 5 is excluded
print(string[ :5]) #tejas here in first index place we did not put any value so it will take 0 by default
print(string[6:11]) #kumar here 6 and 11 are index values and 11 is excluded
print(string[6:]) #kumar here in last index place we did not put any value so it will take last value by default
print(string[6:len(string)]) #kumar here 6 and len(string) is length of string and it will take last value by default
print(string[ :]) #tejas kumar here in first and last index place we did not put any value so it will take 0 and last value by default
 

 # slicing by reverse indexing
print(string[-5:-1]) #r
print(string[-11:-4])

 



 

a=7
b=2


# arithemetic operators (+,-,*,/,%,**)

sum=a+b
diff=a-b
mul=a*b
div=a/b
mod=a%b
power=a**b # a^b
print(sum) # print(a+b)
print(diff) # print(a-b)
print(mul) # print(a*b)
print(div) # print(a/b)
print(mod) # print(a%b)
print(power) #print(a^b)



# comparison operators (==,!=,>,<,>=,<=)

print(a==b) #false
print(a!=b) #true
print(a>b) #true
print(a>=b) #true
print(a<b)  #false
print(a<=b) #false



# assignment operators (=,+=,-=,*=,/=,%=,**=)
num1=7
num2=3
num3=5
num4=8
num5=7

num1 +=2 #num1= num1+2
print(num1) #num1=9

num2 -=1 #num2=num2-1
print(num2) #num2=2

num3 *=5 #num3=num3*5
print(num3) #num3=25

num4 /=2 #num4 =num4/2
print(num4) #num4=4.0

num5 **=2 #num5=num5**2 , num5^^2
print(num5) #num5=49





# logical operators (and,or,not)


a1=True
b1=False
a2=78
b2=12

# not


print(not a1) #false
print(not b1) #true
print(not (a2>b2)) #false
print(a2>b2) #true
print(not (b2>a2)) #true




# and

print(a1 and b1) #false
print((a2>b2) and (b2<a2)) #true
print(a1 and a2) #78
print(b1 and b2) #false

# or
print(a1 or b1) #true
print((a2>b2) or (a2<b2)) #true
print((a2<b2) or b1) #false


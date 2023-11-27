a=2
b=4
print("The value of 2+4 is ",a+b)
# print("the value of 3+7 is",3+7) also can be done like this.
print("The value of 2-4 is",a-b)
print("The value of 2*4 is ", a*b)
print("The value of 2/4 is",a/b)        #it will give the float value always.
print("The value of 2**4 is",a**b)       #it will give the power of the number.
print("The value of 2//4 is ",a//b)       #it will give the integer value always.
print("The value of 2%4 is",a%b)         #it will give the remainder of the division.

# Assignment operator
c=24
c+=5
c-=3
c*=6
c/=2
print(c)

# Comparision operator
# d=(22>4)
# d=(22<23)
# d=(22>=23)
# d=(22<=23)
# d=(22==23)
d=(22!=23)
print(d)

# Logical operators
bool1=True
bool2=False
print("The AND of bool1 and bool2 is",(bool1 and bool2))
print("THE OR of bool1 and bool2 is",(bool1 or bool2))
print("The NOT of bool1 is",(not bool1))
print("The NOT of bool2 is",(not bool2))
print("The NOT of bool1 and bool2 is",not(bool1 and bool2))
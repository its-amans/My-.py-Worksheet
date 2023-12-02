# // sum of two numbers

a=input("enter the first number:")
b=input("Enter the second number:")
# c= None  #input function always takes input in string format.so we have to typecast the value nbefore adding them.
# c=a+b    #Can not add two strings because in python + operator is used for concatenation of string.concvatenation meaning joining of two strings.
c=int(a)+int(b)
print("The sum of a+b is",c)
print(type(c))

# // remainder of the number divided by 2
print("The remainder of the number a is when divided by 2:",int(a)%2)

# // check the gretest number in the given values.
#max function is used to find the greatest number in the given values.
# print("The greatest number is:",max(a,b))  

if a>b:
    print("a is the largest")
else:
    print("\n b is the largest")  #\n is used to print the next line


# // average of numbers
c=10
d=12
e=3
print("The average of the number is:",(c+d+e)/5)


# // square of a number
val=(int(input("Enter the number:")))
print("The square of val is :",val**2)
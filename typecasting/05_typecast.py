b = "34343"
print(type(str))
a=int(b)                 #typecasting will change the value  of b to integer only and only if it is possible
print(type(a))
print(a+5)

#changing the value of a directly to float
c=str(33)
print(type(c))

#input function always takes input in string format
a=input("Enter a number:")
print(type(int(a)))  #converts the string to integer if possible else gives error
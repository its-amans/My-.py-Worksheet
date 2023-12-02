# WAP to input eight numbers from the user and diaplay the unique numbers.
i=0
s=set()
print("Enter the number:")
while i in range(8):      # while i < 8: #Can also be used like this. 
    s.add(int(input()))
    i=i+1
print(s)






#can we have a set of 18 int and 18 str as a value in it
i=0
s=set()
# if we add multiple inmteger values and multiple string values in set then it will print the values in ascending order and for the case of string it compares the ascii value of the string and then print the values in ascending order.
# as we know that set is unordered collection of data so it will print the values in unordered manner.

# From my observations i noticed that if we add multiple values in set then it will print the integer and float values in ascending order and for the case of string it follows unordered manner
s.update({1,2,30,31,3,32,2,10,11,1,20,33,3,3,34,2,32,4,'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',14.2223,12.22})
print(s)


# The ord is a function who returns the ascii value of the character.
print(ord('i'))
# WAP to print factorial of the given number using for loop

a =int(input("Enter the number: "))
fact=1
for i in range(1,a+1):
    fact=fact*i
print(f"The value of {a}! is",fact)
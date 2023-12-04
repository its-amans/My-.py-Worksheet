# Wrote a program to find gretest of four elements entered by the user.
# Written by : Aman Srivastava 

a = int(input("Enter the first number:\n"))
b = int(input("Enter the second number:\n"))
c = int(input("Enter the third number:\n"))
d = int(input("Enter the fourth number:\n"))

if a > b and a > c:
    if a > d:
        print(f"{a} is the greatest number")
    else:
        print(f"{d} is the greatest number")
elif b > c and b > d:
    print(f"{b} is the greatest number")
elif c > d:
    print(f"{c} is the greatest number")
else:
    print(f"{d} is the greatest number")
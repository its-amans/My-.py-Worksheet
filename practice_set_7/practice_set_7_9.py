# WAP to print the table of the number given by user in reversed order.

a=int(input("Enter the number: "))
for i in range(10,0,-1):
    print(f"{a}*{i}=",a*i)

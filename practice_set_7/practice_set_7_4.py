# // WAP to find whether a number is prime or not.

a=int(input("Enter the number"))
while a>=0 :
    if a%2==0 :
        print(f"{a} is a Prime")
        break
    else:
        print(f"{a} is a Not prime")
        break
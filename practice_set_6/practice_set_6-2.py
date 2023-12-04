# // WAP to print the result pass or fail of a student by taking marks of three subjects from the user.
#  If all subject percentage is greter then 40 and individual subject greater then 33 percentage.

a = int(input("Enter the marks of english\n"))
b = int(input("Enter the marks of maths\n"))
c = int(input("Enter the marks of bio\n"))
result=0

if a >= 33 and b >= 33 and c >= 33 :
    result = (a+b+c) / 3
    if result >= 40:
        print(f"Congratulation ! You have passed with {result} percentage the Examination.\n")
    else:
        print(f"OOPS ! You are failed by getting {result} percentage.\n")
else:
    print("Failed in subjects!\n")


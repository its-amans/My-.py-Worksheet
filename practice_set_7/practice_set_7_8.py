# WAP to print the following pattern
# for n=4
# *
# **
# ***
# ****


n=int(input("Enter the no of rows:"))
for i in range(n):
    print("*"*(i+1))
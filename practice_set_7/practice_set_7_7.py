# WAP to print the following pattern
#    *
#   ***
#  *****
# *******

n= int(input("Enter the no of rows"))
for i in range(n):  
    print(" "*(n-i-1),end="")
    print("*"*(2*i+1),end="")    # end="" enables us to skip the new line which comes after the print() by default.
    print(" "*(n-i-1))
    


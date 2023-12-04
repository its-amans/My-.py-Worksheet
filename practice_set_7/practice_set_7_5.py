# WAP to find the sum of first n natural number using a while loop

n= int(input("Enter the  number: "))
i=0 
result=0
while i<=n:
    result=result+i
    i=i+1
print(f"Result is {result}.")
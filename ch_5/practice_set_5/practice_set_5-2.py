# WAP to make your freinds to enter their fav lang and you print the fav lang of your freinds in the following manner:
#taking the name of your freind unique
i=0
d={"Aman":None,
   "Vaibhav":None,
   "Ritik":None,}
print("Enter your fav lang:")
for i in d:
    d[i]=input()
print(d)



# // Another method

# d={}
# a=input("Enter your fav lang Aman:\n")
# b=input("Enter your fav lang Vaibhav:\n")
# c=input("Enter your fav lang Ritik:\n")
# d["AMAN"]=a
# d["VAIBHAV"]=b
# d["RITIK"]=c
# print(d)


# // program when your two freinds name (keys) are same.
# ANS: There will not any big change but the last entered value to the duplicate key will taken as the value in printing.
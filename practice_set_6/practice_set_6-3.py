# // WAP to detect the spam in a text by taking the input from the user.

l=["Buy now","Make a lot of money","Subscribe this","Click This"]
i=input("Enter the phrase you want to check:\n")
if i in l:
    print("!! ALERT .. Spam Detected.!!\n")
else:
    print("NO. Problem! Enjoy\n")
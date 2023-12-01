a='''Hello, <|NAME|>
We are very proud to inform about your selection.
You have done an tremendous job in the entrance paper.
We wish you all the best for your future.
Thanks And Regards
<|DATE|>
'''
name=input("Enter your name:\n")
date=input("Enter your date:\n")
a=a.replace("<|NAME|>",name)
a=a.replace("<|DATE|>",date)   #Note:The repalced value should be stored in the parent variable
print(a)
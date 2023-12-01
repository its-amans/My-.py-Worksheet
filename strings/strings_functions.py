# //string functions
story="once upon a time there was a swimmer who swimms very well. He won several medals in swimming in his college and schoolm level and later on he won olympics also."
print(len(story))     #length of string
print(story.endswith("also."))      #it will check the end statement and returns the boolean value .    
print(story.count("al"))            #it can count either a character or a word .
print(story.capitalize())           #it will capitalize the intial letter of the string.
print(story.find("swimmer"))        #returns the index of the word .if the word is not present then it will return -1.
print(story.replace("swimmwer","very bad swimmer"))     #it will replace the word with the given word.
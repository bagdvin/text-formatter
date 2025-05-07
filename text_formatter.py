print("TEXT FORMATTER")
user_inp = input("Please enter the text")
format_action = input(""" Please select the fromat action to perform
 1)Uppercase
 2)Lowercase
 3)Titlecase 
 4)Sentence case
""")
if format_action== "1":
    print(user_inp.upper())
elif format_action=="2" :
    print(user_inp.lower())
elif format_action=="3" :
    print(user_inp.title())
else :
    print(user_inp.capitalize())
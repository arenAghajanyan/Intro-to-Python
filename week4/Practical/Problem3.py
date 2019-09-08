name="Batmana"
age=17
password="passwo&rd"
if name.count("Batman")>0:
    print("Welcome Mr. Batman!")
else:
    if age<16:
        print("Dear",name+", you are too young to register")
    elif password.count("*")==0 and password.count("&")==0:
        print("Please enter a different password")
        
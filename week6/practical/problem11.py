username=input()
try:
    if username=="Rambo":
        raise Exception
    else:
         print("Welcome,",username)
except Exception:
    print("Rambo is an invalid username")
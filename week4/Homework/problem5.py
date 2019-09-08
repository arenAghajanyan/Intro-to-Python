menu=["ice cream", "chocolate", "apple crisp", "cookies"]
desert=input()
while True:
    if desert in menu:
        print("Your desert will arrive in 10 minutes")
        break
    else:
        print("Please choose another desert")
        desert=input()
        
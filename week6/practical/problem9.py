def div(x,y):
    try:
       return x/y
    except ZeroDivisionError as e: 
        return "error:",e
       
print(div(12,0))
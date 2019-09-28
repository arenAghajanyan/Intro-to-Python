products = {"candy":10, "juice": 5, "pen": 50}
def check(product, num):
    if product in products:
        if products[product]>=num:
            return True
        else:
             return False
    else:
           return False


def calculate_discount(price, discount_percent):
    if discount_percent >= 0.2:
        #apply discount
        return f'to pay, {price * discount_percent}'
    else:
        return f'to pay, {price}'
    
print(calculate_discount(
    price = int(input("What is the price: ")),
    discount_percent = float(input("Discount percentage in decimal: "))
 ))
    
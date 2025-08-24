def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        applied_discount = (discount_percent / 100) * price
        final_price = applied_discount
        return final_price
    else:
        return price
    
try:
    price = float(input("Please enter the original price of the item: "))
    discount_percent = float(input("Enter the discount to be applied: "))

    final_price = calculate_discount(price, discount_percent)

    if discount_percent >= 20:
        print(f"The final price is: {final_price}")
    else:
        print("No discount applied")

except ValueError:
    print("Please enter a valid number for price and discount")
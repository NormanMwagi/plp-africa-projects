

def  calculate_discount(price, discount_percent):
    """
    Calculate the discounted price based on the original price and discount percentage.

    :param price: Original price of the item
    :param discount_percent: Discount percentage to apply
    :return: Discounted price
    """
    if price < 0 or discount_percent < 0:
        raise ValueError("Price and discount percent must be non-negative.")
    
    discount_amount = (discount_percent / 100) * price
    
    
    if discount_percent >= 20:
        discounted_price = price - discount_amount
        print(f"Discounted price: {discounted_price}")
        return discounted_price
    else:
        print(f"No discount applied. Original price: {price}")
        return price
   # No discount applied if less than 20%


price = int(input("Enter the original price: "))
discount_percent = int(input("Enter the discount percentage: "))


calculate_discount(price, discount_percent)
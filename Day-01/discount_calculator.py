original_price = int(input("enter the original price:"))
discount_percentage = int(input("enter the discount percentage:"))

discount_amount  = (original_price * discount_percentage)/100
final_price = original_price - discount_amount
print("Discount amount :",discount_amount)
print("final price is :", final_price)
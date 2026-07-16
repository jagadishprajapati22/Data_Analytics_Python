#1.Define a function called calculate_final_price(price, discount_rate) that returns the final price after applying the discount. Test it with price 1200 and discount_rate 0.15.
def calculate_final_price(price, discount_rate):
    calculate_final_price = price - (price*discount_rate)
    return calculate_final_price
result = calculate_final_price(1200,0.15)
print(result)    

#2.Create a function get_delivery_charge(amount, city='Ahmedabad') that returns a delivery charge: Rs. 30 for Ahmedabad, Rs. 50 for other cities. Call it with and without the city argument to see both results.
def  get_delivery_charge(amount, city='Ahmedabad'):
    if city=="Ahmedabad":
        return 30
    else:
            return 50
print(get_delivery_charge(500))
print(get_delivery_charge(500, "Surat"))            
    


#3.Build a function called format_coupon_message(username, discount=10) that returns a string like 'Hi Rahul, you get 10% off!' If no discount is given, use 10% by default. Test it for two users: one with a custom discount, one with the default.
def format_coupon_message(username, discount=10):
    return f"Hi {username}, you get {discount}% off!"

# Custom discount
print(format_coupon_message("Rahul", 20))

# Default discount
print(format_coupon_message("Priya"))

#4.Given a function apply_discount(price, rate=0.10), update it so that if the rate is not passed, it uses 0.10 by default. Then, call it with only the price argument and print the result.<br><br><em><strong>Hint:</strong> Use default arguments in your function definition.</em>
def apply_discount(price, rate=0.10):
    return price - (price * rate)

# Calling the function with only the price argument
result = apply_discount(1000)

print(result)

#5.Write a function called calculate_cashback(amount, cashback_rate=0.05) that returns the cashback amount. Then, use it to calculate cashback for a Zomato order of Rs. 500 with the default rate, and for a Flipkart order of Rs. 2000 with a 7% cashback.
def calculate_cashback(amount, cashback_rate=0.05):
    return amount * cashback_rate

# Zomato order with default cashback rate (5%)
zomato_cashback = calculate_cashback(500)

# Flipkart order with custom cashback rate (7%)
flipkart_cashback = calculate_cashback(2000, 0.07)

print("Zomato Cashback: Rs.", zomato_cashback)
print("Flipkart Cashback: Rs.", flipkart_cashback)
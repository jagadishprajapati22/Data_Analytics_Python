#1.Write a Python script that checks if a user's entered age is 18 or above and prints 'Eligible for IPL ticket booking' if true, otherwise prints 'Not eligible'.
age = int(input("enter your age ="))
if age>18:
    print("Eligible for IPL ticket booking")
else:
   print("Not eligible")  



#2.Create a Python program that takes the number of followers as input and uses if, elif, and else to print 'Micro Influencer' if followers < 10,000, 'Rising Star' if between 10,000 and 100,000, and 'Celebrity' if above 100,000.
follower = int(input("enter number of followers ="))
if follower < 10000:
    print("Micro Influencer")
elif follower <=100000:
    print("rising star")
else:
    print("celebrity")    

#3.Build a Python script that asks the user for their Zomato order total and prints 'Apply Free Delivery' if total is above 299, 'Add more items for free delivery' if between 200 and 299, else 'Delivery charges apply'.
# User se Zomato order total lena
total = float(input("Enter your Zomato order total: "))

# Order total ke hisab se message print karna
if total > 299:
    print("Apply Free Delivery")
elif total >= 200:
    print("Add more items for free delivery")
else:
    print("Delivery charges apply")

#4.Write a Python program using nested if statements: take a user's entered Flipkart cart value and payment method ('UPI', 'Card', 'Cash'). If the cart value is above 1000 and payment method is 'UPI', print 'Eligible for 10% cashback'; if above 1000 and payment is not 'UPI', print 'Eligible for 5% cashback'; else print 'No cashbck'.
# User se cart value lena
cart_value = float(input("Enter Flipkart cart value: "))

# User se payment method lena
payment_method = input("Enter payment method (UPI/Card/Cash): ")

# Nested if statement
if cart_value > 1000:
    if payment_method == "UPI":
        print("Eligible for 10% cashback")
    else:
        print("Eligible for 5% cashback")
else:
    print("No cashback")
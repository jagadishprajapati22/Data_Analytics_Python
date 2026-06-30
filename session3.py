#que 1- Declare four variables in Python: one integer (number of followers), one float (average rating), one string (your favorite app's name), and one boolean (is_premium_user). Print each variable and its type using the type() function.
followers = 1500              # Integer
average_rating = 4.7          # Float
favorite_app = "Instagram"    # String
is_premium_user = True        # Boolean

print("Followers:", followers, type(followers))
print("Average Rating:", average_rating, type(average_rating))
print("Favorite App:", favorite_app, type(favorite_app))
print("Premium User:", is_premium_user, type(is_premium_user))

#que 2-Write a Python program that takes a user's input for the price of a Zomato order as a string, converts it to a float using type casting, adds 18% GST, and prints the final bill amount.
price = input("Enter the order price: ")

price = float(price)

gst = price * 0.18
final_bill = price + gst

print("Final Bill Amount:", final_bill)

#que 3- Given a list of strings representing product prices from Flipkart, like ['199.99', '299.50', '150'], convert all to floats and calculate the total cart value.
prices = ['199.99', '299.50', '150']

float_prices = [float(price) for price in prices]

total = sum(float_prices)

print("Converted Prices:", float_prices)
print("Total Cart Value:", total)

#que 4- Build a function is_discount_applicable(order_amount) that takes a float and returns True if the amount is greater than 500, otherwise False. Print the result for order amounts 450 and 750.
def is_discount_applicable(order_amount):
    return order_amount > 500

print("450:", is_discount_applicable(450))
print("750:", is_discount_applicable(750))

#que 5- You received a dataset of ratings as strings from Spotify: ['4.5', '3.0', '5', '4.2']. Use type casting to convert these to floats, then find and print the highest rating.<br><br><em><strong>Hint:</strong> Use the float() function inside a loop or list comprehension.</em>
ratings = ['4.5', '3.0', '5', '4.2']

float_ratings = [float(rating) for rating in ratings]

highest_rating = max(float_ratings)

print("Ratings:", float_ratings)
print("Highest Rating:", highest_rating)
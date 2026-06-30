#que 1-Create three variables in Python: user_name, fav_app, and daily_usage_hours. Assign your own name, your favorite app (like Instagram or Zomato), and how many hours you use it daily.
user_name = "Jc Prajapati"
fav_app = "Instagram"
daily_usage_hours = 3

print(user_name)
print(fav_app)
print(daily_usage_hours)

#que 2-Write a Python script that declares variables for product_name, price, and is_available to represent an item on Flipkart. Print each variable and its data type using the type() function.
product_name = "iPhone 15"
price = 69999
is_available = True

print(product_name, type(product_name))
print(price, type(price))
print(is_available, type(is_available))

#que 3-Demonstrate the difference between single-line and multi-line comments in Python by writing a script that explains how a Spotify playlist recommendation system might work. Use # for single-line and triple quotes for multi-line comments.
# Spotify collects user listening history

# It checks favorite songs and artists

"""
Spotify recommendation system analyzes
listening habits, favorite artists,
and playlists to suggest new music.
"""

print("Spotify Recommendation System")

#que 4-Create variables for order_total, delivery_region, and discount_percent to represent a Zomato order. Follow Python naming conventions and print a sentence using all three variables, like 'Order from [region] totals ₹[order_total] with [discount_percent]% discount.
order_total = 450
delivery_region = "Ahmedabad"
discount_percent = 20

print(f"Order from {delivery_region} totals ₹{order_total} with {discount_percent}% discount.")

#que 5-Write a Python script that intentionally mixes tabs and spaces for indentation, then fix the script so it runs without errors.<br><br><em><strong>Hint:</strong> Use only spaces for indentation, as per Python's best practices.</em>
#Mix Tabs & Space
'''if True:
	print("Hello")
    print("Python")'''


#Only Spaces
if True:
    print("Hello")
    print("Python")
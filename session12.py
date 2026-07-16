#1-Write a lambda function that takes a price in rupees and returns the price after adding 18% GST. Test it on the prices 100, 250, and 500.
# Lambda function to add 18% GST
add_gst = lambda price: price + (price * 0.18)

# Testing the lambda function
print(add_gst(100))
print(add_gst(250))
print(add_gst(500))

#2-Given a list of song titles from Spotify with extra spaces and inconsistent casing, use map() and a lambda function to clean each title so that it is stripped of spaces and converted to title case (e.g., ' shape OF you ' → 'Shape Of You').

# List of song titles
songs = [" shape OF you ", "  belIEver ", " blINDing LIGHTS "]
clean_song = list(map(lambda song: song.strip().title(),songs))
#print result
print(clean_song)

#3-Use filter() and a lambda function to extract only those Flipkart product names from a list that start with the letter 'S' (case-insensitive).
# List of Flipkart product names
products = ["Samsung TV", "Apple iPhone", "sony Headphones", "Redmi Mobile", "Smart Watch"]

# Filter products that start with 'S' (case-insensitive)
result = list(filter(lambda product: product.lower().startswith('s'), products))

# Print the result
print(result)


#4-Given a list of order amounts from a Zomato cart [120, 340, 560, 80], use reduce() from functools to calculate the total bill amount.
from functools import reduce

# List of Zomato order amounts
orders = [120, 340, 560, 80]

# Calculate total bill
total_bill = reduce(lambda x, y: x + y, orders)

# Print the total bill
print(total_bill)

#5-Use ChatGPT or Copilot to generate a Python code snippet that uses map(), filter(), and reduce() together to process a list of numbers: first double each number, then filter to keep only numbers greater than 100, and finally sum the result. Paste and test the generated code with the list [40, 60, 80, 120].
from functools import reduce

# List of numbers
numbers = [40, 60, 80, 120]

# Step 1: Double each number using map()
doubled = list(map(lambda x: x * 2, numbers))

# Step 2: Keep only numbers greater than 100 using filter()
filtered = list(filter(lambda x: x > 100, doubled))

# Step 3: Find the total sum using reduce()
total = reduce(lambda x, y: x + y, filtered)

# Display the results
print("Original List :", numbers)
print("After map()   :", doubled)
print("After filter():", filtered)
print("Final Sum     :", total)
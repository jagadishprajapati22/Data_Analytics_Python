#1.Use the math module to calculate the square root, factorial, and value of pi for given numbers, and print each result.
import math

num = 25
fact_num = 5

print("Square Root:", math.sqrt(num))
print("Factorial:", math.factorial(fact_num))
print("Value of Pi:", math.pi)

#2.Write a script that lists all files in your current directory using the os module, and prints only those files with a .jpg or .png extension.<br><br><em><strong>Hint:</strong> Use os.listdir() and string methods to filter file names.</em>
import os

# Get the current working directory
current_directory = os.getcwd()

# List all files and folders in the current directory
items = os.listdir(current_directory)

print("Image files (.jpg and .png):\n")

# Filter and print only .jpg and .png files
for item in items:
    if item.lower().endswith(".jpg") or item.lower().endswith(".png"):
        print(item)

#3.Create a Python program that accepts a date in 'YYYY-MM-DD' format from the user and displays the day of the week using the datetime module.
from datetime import datetime

# Accept date from the user
date_input = input("Enter a date (YYYY-MM-DD): ")

# Convert string to datetime object
date_object = datetime.strptime(date_input, "%Y-%m-%d")

# Display the day of the week
day = date_object.strftime("%A")

print("Day of the week:", day)

#4.Build a simple custom module named insta_utils.py with a function format_follower_count(n) that returns '1.5K' for 1500 and '2.3M' for 2300000. Import and use this function in another script to display formatted counts for 3 sample numbers.
def format_follower_count(n):
    if n >= 1000000:
        return f"{n / 1000000:.1f}M"
    elif n >= 1000:
        return f"{n / 1000:.1f}K"
    else:
        return str(n)
#5.Create a new virtual environment using venv, activate it, and install the statistics and requests packages via pip. Then, write a script that uses statistics.mean() to calculate the average of a list of numbers.
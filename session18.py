#1.Use re.findall() to extract all valid Indian phone numbers (10 digits, starting with 7, 8, or 9) from a given text string that contains random numbers, prices, and phone numbers like those seen in OLX or WhatsApp chats.
import re

text = """
Call me at 9876543210 or 8123456789.
My old number was 6123456789.
Price is 7999.
WhatsApp: 9123456780
Random: 1234567890
"""

pattern = r"\b[789]\d{9}\b"

phone_numbers = re.findall(pattern, text)

print("Valid Phone Numbers:", phone_numbers)


#2.Write a Python function using re.search() that checks if a given string contains a valid date in the format DD/MM/YYYY (e.g., 25/06/2024), and returns True if found, otherwise False.<br><br><em><strong>Hint:</strong> Use the pattern '\b\d{2}/\d{2}/\d{4}\b'.</em>
import re

def contains_date(text):
    pattern = r"\b\d{2}/\d{2}/\d{4}\b"

    if re.search(pattern, text):
        return True
    return False

print(contains_date("Meeting on 25/06/2024"))
print(contains_date("Meeting tomorrow"))

#3.Given a messy text copied from a Zomato review containing multiple emails, use re.findall() to extract all valid email addresses and print them as a list.
import re

text = """
Contact us:
support@gmail.com
help@yahoo.in
admin123@company.co.in
Wrong email: abc@com
"""

pattern = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"

emails = re.findall(pattern, text)

print("Emails:", emails)

#4.Use re.sub() to mask all but the last 4 digits of any phone number in a string (e.g., replace 9876543210 with ******3210) like Paytm does for privacy.<br><br><em><strong>Constraint:</strong> Do not use loops; achieve this only with re.sub().</em>
import re

pattern = r"\bOD\d{18}\b"

orders = [
    "OD123456789012345000",
    "OD987654321098765432",
    "123456789",
    "OD12345"
]

for order in orders:
    if re.search(pattern, order):
        print(order, "-> Valid Order ID")
    else:
        print(order, "-> Invalid Order ID")

#5.Use ChatGPT to generate a regex pattern that matches Flipkart-style order IDs (e.g., OD123456789012345000) and test it in Python using re.search() on sample order strings.
import re

pattern = r"\bOD\d{18}\b"

orders = [
    "OD123456789012345000",
    "OD987654321098765432",
    "123456789",
    "OD12345"
]

for order in orders:
    if re.search(pattern, order):
        print(order, "-> Valid Order ID")
    else:
        print(order, "-> Invalid Order ID")
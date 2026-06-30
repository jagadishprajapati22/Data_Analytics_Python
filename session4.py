#que 1- Create a Python script that takes any product name string (e.g., 'Redmi Note 12 Pro') and prints the name in all uppercase and all lowercase using the upper() and lower() methods.
product_name = "Redmi Note 12 Pro"

print("Original:", product_name)
print("Uppercase:", product_name.upper())
print("Lowercase:", product_name.lower())


#que 2- Write a function clean_brand_name(name) that removes leading/trailing spaces and replaces any hyphens '-' with a single space in the input string. Test it with ' oneplus-Nord '.
def clean_brand_name(name):
    return name.strip().replace("-", " ")

brand = " oneplus-Nord "

print(clean_brand_name(brand))



#que 3- Given the string 'Apple iPhone 14 Pro Max', use string slicing to extract and print only the brand name and the model (i.e., 'Apple' and 'iPhone 14 Pro Max') separately.<br><br><em><strong>Hint:</strong> Use split() to help find the split point, then use slicing for the substrings.</em>
product = "Apple iPhone 14 Pro Max"

split_index = product.find(" ")

brand = product[:split_index]
model = product[split_index + 1:]

print("Brand:", brand)
print("Model:", model)


#que 4- Build a function format_product_display(name, price) that takes a product name and price (e.g., 'Boat Earbuds', 1299) and returns a formatted string like 'Boat Earbuds - ₹1299'.
def format_product_display(name, price):
    return f"{name} - ₹{price}"

print(format_product_display("Boat Earbuds", 1299))


#que 5- Suppose you have a list of messy product names: [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']. Write code to clean each name (remove spaces, replace hyphens with spaces, and make the brand title case) and print the cleaned list.<br><br><em><strong>Constraint:</strong> Use at least three string methods from this session.</em>
products = [' mi-Band 5 ', ' SAMSUNG-Galaxy ', ' realme-Book ']

cleaned_products = []

for product in products:
    clean = product.strip()          # Remove spaces
    clean = clean.replace("-", " ")  # Replace hyphen
    clean = clean.title()            # Title Case
    cleaned_products.append(clean)

print(cleaned_products)
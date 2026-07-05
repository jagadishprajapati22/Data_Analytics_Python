#1-Create a list called playlist_ids with 5 integers representing Spotify playlist IDs, then use append() to add a new playlist ID at the end and print the updated list.
playlist_ids = [101,102,103,104,105]
playlist_ids.append(106)
print(playlist_ids)

#2-Simulate a Flipkart shopping cart: start with a list cart_items containing 't-shirt', 'shoes'. Use extend() to add ['jeans', 'cap'] to the cart, then print the final list of items.
cart_items=['t-shirt', 'shoes']
cart_items.extend(['jeans','cap'])
print(cart_items)

#3-Write a function remove_last_item(order_list) that pops the last item from a Zomato order list and returns the removed item. Test it with a sample order_list.
def remove_last_item(order_list):
    return order_list.pop()

order_list = ["Pizza", "Burger", "Cold Drink", "Ice Cream"]

removed_item = remove_last_item(order_list)

print("Removed Item:", removed_item)
print("Order List:", order_list)


#4-Create a tuple called insta_filters with 4 Instagram filter names. Try to update the second filter and observe what error you get. Explain in a comment why this happens.<br><br><em><strong>Hint:</strong> Tuples are immutable, so direct assignment won't work.</em>
'''insta_filters=('Clarendon','Gingham','Juno' ,'Lark')
insta_filters[1]="Valencia"
print(insta_filters)'''
#TypeError: 'tuple' object does not support item assignment


#5-Given two scenarios — storing a user's favorite genres (which may change) and storing a fixed set of IRCTC train classes ('Sleeper', 'AC 3 Tier', 'AC 2 Tier') — choose whether to use a list or tuple for each. Write one sentence explaining your choice for both.

# User's favorite genres -> List (can change)
favorite_genres = ["Action", "Comedy", "Drama"]
# Use a list because favorite genres can be changed.

# IRCTC train classes -> Tuple (fixed)
train_classes = ("Sleeper", "AC 3 Tier", "AC 2 Tier")
# Use a tuple because train classes are fixed and cannot be changed.

print(favorite_genres)
print(train_classes)
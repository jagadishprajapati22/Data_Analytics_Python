#1.Create a Python dictionary called playlist_prices with at least 5 key-value pairs where the key is a Spotify playlist name (as a string) and the value is the playlist's price (as an integer). Print the dictionary.
playlist_prices = {
    "Top Hits India": 199,
    "Workout Beats": 149,
    "Chill Vibes": 99,
    "Party Mix": 249,
    "LoFi Study": 129

}
print(playlist_prices)

#2.Write a function update_playlist_price(playlist, new_price) that updates the price of a given playlist in the playlist_prices dictionary. Test it by updating the price of any one playlist and printing the updated dictionary.
playlist_prices = {
    "Top Hits India": 199,
    "Workout Beats": 149,
    "Chill Vibes": 99
}

def update_playlist_price(playlist, new_price):
    playlist_prices[playlist] = new_price

update_playlist_price("Chill Vibes", 150)

print(playlist_prices)

#3.Remove a playlist from the playlist_prices dictionary using the del statement. Print the dictionary after deletion to confirm the change.
playlist_prices = {
    "Top Hits India": 199,
    "Workout Beats": 149,
    "Chill Vibes": 99,
    "Party Mix": 249,
    "LoFi Study": 129
}

del playlist_prices["Party Mix"]


print(playlist_prices)


#4.Given two sets: set1 contains the names of restaurants you have ordered from on Zomato, and set2 contains the names of restaurants you have ordered from on Swiggy, find and print the union and intersection of these sets.<br><br><em><strong>Hint:</strong> Use the union() and intersection() methods of Python sets.</em>
set1 = {"Domino's", "McDonald's", "KFC", "Subway"}
set2 = {"KFC", "Subway", "Pizza Hut", "Burger King"}
print("union:", set1.union(set2))
print("intersection:", set1.intersection(set2))
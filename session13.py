#1.Write a recursive function in Python called reverse_string(s) that takes a string and returns it reversed (e.g., 'hello' becomes 'olleh').
def reverse_string(s):
    if s == "":
        return ""
    return reverse_string(s[1:]) + s[0]

print(reverse_string("hello"))

#2.Build a recursive function sum_playlist_durations(durations) that takes a list of song durations (in seconds) and returns the total duration, similar to how Spotify totals a playlist.
def sum_playlist_durations(durations):
    if len(durations) == 0:
        return 0
    return durations[0] + sum_playlist_durations(durations[1:])

songs = [180, 240, 200, 150]

print("Total Duration:", sum_playlist_durations(songs))

#3.Given the following code, identify whether the variable 'count' is local or global in each function, and explain what will be printed when run:
count = 10

def update_count():
    count = 5
    print("Inside:", count)

update_count()

print("Outside:", count)




#4.Create a recursive function count_likes(posts) that takes a nested dictionary representing Instagram posts and their replies (each with a 'likes' key), and returns the total number of likes across all posts and replies.<br><br><em><strong>Hint:</strong> Each reply can itself have more replies, so use recursion to sum likes at all levels.</em>
def count_likes(posts):
    total = posts["likes"]

    for reply in posts["replies"]:
        total = total + count_likes(reply)

    return total


post = {
    "likes": 100,
    "replies": [
        {
            "likes": 50,
            "replies": []
        },
        {
            "likes": 30,
            "replies": [
                {
                    "likes": 20,
                    "replies": []
                }
            ]
        }
    ]
}

print("Total Likes:", count_likes(post))

#5.Write a Python script that demonstrates the lifetime of a local variable inside a function versus a global variable by printing their values before, during, and after a function call. Use variable names similar to 'user_status' and 'app_status', inspired by WhatsApp online/offline status.
app_status = "Online"

def show_status():
    user_status = "Typing"

    print("Inside Function")
    print("User Status:", user_status)
    print("App Status:", app_status)

print("Before Function")
print("App Status:", app_status)

show_status()

print("After Function")
print("App Status:", app_status)
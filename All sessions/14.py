# Create a dynamic nested dictionary in Python to represent a Flipkart shopping cart where each user (by username) can have multiple items, and each item has a name, quantity, and price. Add two users with at least two items each, then print the entire cart.
shopping_cart={
    "rahul":{
        "username":"Rahul",
        "items":{
            "Shoes":{"quantity":1,"price":2499},
            "Bag":{"quantity":2,"price":899}
        }
    },
     "priya":{
        "username":"Priya",
        "items":{
            "Headphones":{"quantity":1,"price":2499},
            "Watch":{"quantity":1,"price":1299}
        }
    }
}
print(shopping_cart)

# or
# cart = {}
# cart["rahul"] = {
#     "Shoes": {"quantity": 1, "price": 1999},
#     "Bag": {"quantity": 2, "price": 899}
# }
# cart["priya"] = {
#     "Headphones": {"quantity": 1, "price": 2499},
#     "Watch": {"quantity": 1, "price": 1499}
# }
# print(cart)

# Write a function add_song_to_playlist(playlists, user, playlist_name, song_title, artist) that adds a song to a user's playlist in a nested dictionary structure like Spotify. If the user or playlist doesn't exist, create them dynamically.
def add_song_to_playlist(playlists, user, playlist_name, song_title, artist):
    if user not in playlists:
        playlists[user] = {}
    if playlist_name not in playlists[user]:
        playlists[user][playlist_name] = []
    playlists[user][playlist_name].append({
        "title": song_title,
        "artist": artist
    })
    return playlists
playlists = {}
playlists = add_song_to_playlist(playlists, "rahul", "Workout Mix", "Believer", "Imagine Dragons")
playlists = add_song_to_playlist(playlists, "rahul", "Workout Mix", "Thunder", "Imagine Dragons")
playlists = add_song_to_playlist(playlists, "priya", "Chill Vibes", "Perfect", "Ed Sheeran")
print(playlists)

# Build a dynamic nested dictionary to store IPL cricket match scores: for each team, store a dictionary of player names and their runs. Add at least two teams with three players each, then print the runs scored by a specific player of your choice.
ipl_scores = {
    "Mumbai Indians": {
        "Rohit Sharma": 65,
        "Surya Kumar Yadav": 48,
        "Ishan Kishan": 32
    },
    "Chennai Super Kings": {
        "MS Dhoni": 40,
        "Ruturaj Gaikwad": 78,
        "Ravindra Jadeja": 35
    }
}
player = "Ruturaj Gaikwad"
for team, players in ipl_scores.items():
    if player in players:
        print(f"{player} scored {players[player]} runs for {team}")

# Given a nested dictionary representing Zomato orders (order_id as key, value is another dictionary with 'restaurant', 'items' (list), and 'total'), write a function to add a new order and another function to update the total of an existing order.<br><br><em><strong>Hint:</strong> Use dict.setdefault() to handle missing keys dynamically.</em>
orders = {}
def add_order(orders, order_id, restaurant, items, total):
    orders.setdefault(order_id, {
        "restaurant": restaurant,
        "items": items,
        "total": total
    })
def update_total(orders, order_id, new_total):
    if order_id in orders:
        orders[order_id]["total"] = new_total
    else:
        print("Order ID not found.")
add_order(orders, "ORD101", "Pizza Hut", ["Pizza", "Garlic Bread"], 450)
add_order(orders, "ORD102", "Burger King", ["Burger", "Fries"], 300)
update_total(orders, "ORD101", 500)
print(orders)

# Refactor the following code to use dynamic nested dictionary creation so that it doesn't throw a KeyError when adding a new user or playlist:<br><br>playlists = {'user1': {'Favourites': ['Song1', 'Song2']}}<br>playlists['user2']['Chill'].append('Song3')<br><br><em><strong>Hint:</strong> Use collections.defaultdict or check if keys exist before accessing.</em>
from collections import defaultdict
playlists = defaultdict(lambda: defaultdict(list))
playlists['user1']['Favourites'].extend(['Song1', 'Song2'])
playlists['user2']['Chill'].append('Song3')
print(dict(playlists))

# or
playlists = {'user1': {'Favourites': ['Song1', 'Song2']}}
user = 'user2'
playlist_name = 'Chill'
if user not in playlists:
    playlists[user] = {}
if playlist_name not in playlists[user]:
    playlists[user][playlist_name] = []
playlists[user][playlist_name].append('Song3')
print(playlists)
# # Create a Python dictionary called playlist with three songs as keys and their durations (in seconds) as values. Update the duration of one song and print the updated dictionary.
playlist={'Mine':50,'Blinding lights':60,'Brown rang':150}
playlist['Brown rang']=200
print(playlist)

# Build a nested dictionary called user_profiles where each key is a username (like 'raj_07', 'ananya_xo') and the value is another dictionary with keys: 'followers', 'following', and 'posts'. Add data for at least two users and print the number of followers for 'ananya_xo'.
user_profiles = {
    "raj_07":{
        "followers": 1200,
        "following": 180,
        "posts": 45
    },
    "ananya_xo":{
        "followers": 2500,
        "following": 300,
        "posts": 78
    }
}
print("Followers of ananya is :",user_profiles["ananya_xo"]["followers"])

# Simulate a Zomato-style restaurant menu using a nested dictionary: each restaurant name as a key, and its value as another dictionary with keys 'cuisine' and 'rating'. Add two restaurants, then update the rating of one restaurant to a new value.<br><br><em><strong>Hint:</strong> Use dictionary indexing to access and update the nested 'rating' value.</em>
restaurant_profile={
    "Taj Hotel":{
        "Cuisine":"Indian Food",
        "Ratings":4.9
    },
    "Palace Hotel":{
        "Cuisine":"Fast Food",
        "Ratings":4.5
    }
}
restaurant_profile["Palace Hotel"]["Ratings"]=4.8
print(restaurant_profile)

# Given the following nested dictionary representing an IPL cricket team squad:<br><br>team = {'CSK': {'captain': 'Dhoni', 'players': 18}, 'MI': {'captain': 'Rohit', 'players': 17}}<br><br>Write code to add a new team 'GT' with captain 'Hardik' and 16 players, then print all team names and their captains.
team = {
    'CSK': {'captain': 'Dhoni', 'players': 18},
    'MI': {'captain': 'Rohit', 'players': 17}
}
team['GT'] = {'captain': 'Hardik', 'players': 16}
for t in team:
    print(t, "-", team[t]['captain'])
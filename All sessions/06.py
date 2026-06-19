# Given two lists — one of product names and one of their prices — use the zip() function to create a dictionary mapping each product to its price, then print the dictionary.
products=['T.V','Mobile','A.C']
prices=[55000,25000,45000]
product_prices=dict(zip(products,prices))
print(product_prices)

# Write a loop that takes two lists: usernames and their follower counts, and manually creates a dictionary (without using zip()) that maps each username to its follower count, similar to how Instagram tracks followers.
username=['dev07','jonh_1','sasha_xo']
followers=['520','250','425']
instagram_followers={
    username[i]:followers[i]
    for i in range(len(username))
}
print(instagram_followers)

# or
# usernames = ["raj_07", "ananya_xo", "tech_guru"]
# followers = [1200, 2500, 1800]
# instagram_followers = {}
# for index, username in enumerate(usernames):
#     instagram_followers[username] = followers[index]
# print(instagram_followers)

# usernames = ["raj_07", "ananya_xo", "tech_guru"]
# followers = [1200, 2500, 1800]
# instagram_followers = {}
# for i in range(len(usernames)):
#     instagram_followers[usernames[i]] = followers[i]
# print(instagram_followers)

# Suppose you have two lists: one with IPL team names and another with their total points this season. Use zip() to combine them into a dictionary, then print only the teams that have more than 10 points.<br><br><em><strong>Hint:</strong> After creating the dictionary, use a for loop to filter and print.</em>
# teams=['CSK','MI','RCB','KKR','RR','GT','PBKS']
# points=[20,18,19,9,7,15,5]
# result=dict(zip(teams,points))
# for teams,points in result.items():
#     if points >10:
#         print(teams,'-',points)

# Given three lists — movie titles, genres, and ratings — use zip() to create a list of dictionaries where each dictionary contains keys 'title', 'genre', and 'rating' for a movie, then print the list.<br><br><em><strong>Constraint:</strong> Do not use any external libraries.</em>
# titles=['Dhurandhar','Special-ops','Golmaal']
# genres=['Action','True story','Comedy']
# ratings=[9.8,9.7,9.6]
# movies=list(zip(titles,genres,ratings))
# for i in movies:
#     movie_dict={
#         "Title":i[0],
#         "Genre":i[1],
#         "Rating":i[2]
#     }
#     print(movie_dict)

# or
# titles = ["Inception", "Titanic", "Avengers"]
# genres = ["Sci-Fi", "Romance", "Action"]
# ratings = [8.8, 7.9, 8.4]
# movies = []
# for title, genre, rating in zip(titles, genres, ratings):
#     movies.append({
#         "title": title,
#         "genre": genre,
#         "rating": rating
#     })
# print(movies)
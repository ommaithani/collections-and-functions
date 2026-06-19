# Given a list of cricket scores: [56.7, 102.3, 88.9, 45.2, 120.8], use the round() function to create a new list with each score rounded to the nearest integer and print both the original and rounded lists.
# cricket_scores=[56.7,102.3,88.9,45.2,120.8]
# rounded_score=[]
# for i in cricket_scores:
#     rounded_score.append(round(i))
# print("Rounded score is :",rounded_score)
# print("Original score :",cricket_scores)

# or
# cricket_scores=[56.7,102.3,88.9,45.2,120.8]
# rounded_scores=[round(score) for score in cricket_scores]
# print("Rounded score is :",rounded_scores)
# print("Original score :",cricket_scores)

# Create a list of restaurant ratings (e.g., [4.2, 3.8, 4.9, 2.5, 4.0]) and use the sorted() function to display the ratings in descending order.
# restaurant_ratings=[4.2,3.8,4.9,2.5,4.0]
# sorted_ratings=sorted(restaurant_ratings,reverse=True)
# print("Original ratings :",restaurant_ratings)
# print("Sorted ratings :",sorted_ratings)

# Write a program that takes a list of Flipkart product names and sorts them alphabetically using the sort() method, then prints the sorted list.
# flipkart_products=['Smartphones','Laptop','Earbuds','Watches','Monitor']
# flipkart_products.sort()
# print("Sorted products list :",flipkart_products)

# # You have two lists: one with Zomato restaurant names ['Burger Hub', 'Pizza Point', 'Sushi House'] and another with their delivery times in minutes [30, 25, 40]. Use the zip() function to pair each restaurant with its delivery time and print each pair in the format: 'Burger Hub - 30 min'.
# Zomato_restaurant_names=['Burger Hub','Pizza Point','Sushi House']
# delivery_times_in_minutes=[30, 25, 40]
# for name,time in zip(Zomato_restaurant_names,delivery_times_in_minutes):
#     print(f'{name}-{time} min')

# Build a function that takes two lists, one of YouTube video titles and one of their view counts, and returns a list of tuples with each title and its rounded view count (to the nearest thousand using round()).<br><br><em><strong>Hint:</strong> Use zip() to pair titles and counts, and round() inside a list comprehension.</em>
# def get_video_views(titles, view_counts):
#     return [
#         (title, round(count, -3))
#         for title, count in zip(titles, view_counts)
#     ]
# titles = ["Python Tutorial", "Travel Vlog", "Cooking Tips"]
# view_counts = [12543, 98765, 456789]

# result = get_video_views(titles, view_counts)
# print(result)
# Create a Python list called playlist containing five of your favorite song names, then use a for loop to print each song with its position in the playlist (starting from 1).
# playlist=['sunflower','brown rang','mine','yellow','blue']
# for i in range(len(playlist)):
#     print(f"Song {i+1}:{playlist[i]}")

# or
# playlist=['sunflower','brown rang','mine','yellow','blue']
# for i,song in enumerate(playlist,start=1):
#     print(f"{i}.{song}")

# Given a list of food items ordered on Zomato: foods = ['Pizza', 'Burger', 'Dosa', 'Pasta', 'Fries'], use a for loop with range() to print only the first three items in the list.
# foods=['Pizza','Burger','Dosa','Pasta','fries']
# for item in range(3):
#     print(foods[item])

# Simulate a Flipkart shopping cart: prices = [299, 499, 150, 1200, 350]. Use a for loop to calculate and print the total cart value.
# prices=[299,499,150,1200,350]
# total=0
# for price in prices:
#     total+=price
# print("Total cart value is :",total)

# Build a WhatsApp-style unread messages counter: given a list unread_counts = [2, 0, 15, 120, 5], use a for loop to print '99+' if the count is greater than 99, otherwise print the actual count for each chat.
# unread_counts=[2,0,15,120,5]
# for i in unread_counts:
#     if i>99:
#         print("99+")
#     else:
#         print(i)
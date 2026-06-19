# Use the math.sqrt() function to calculate and print the square roots of the numbers 16, 49, and 81.
import math
print(math.sqrt(16))
print(math.sqrt(49))
print(math.sqrt(81))

# Build a Flipkart-style price rounder: given a list of product prices with decimals, use math.ceil() to round each price up to the nearest whole number and display the results.<br><br><em><strong>Hint:</strong> Try with prices like 199.1, 349.8, and 599.3.</em>
import math
prices = [199.1, 349.8, 599.3]
for price in prices:
    rounded_price = math.ceil(price)
    print(f"Original: {price} -> Rounded: {rounded_price}")
import math
bill_amount = 789.50
discounted_amount = bill_amount * 0.90
final_bill = math.floor(discounted_amount)
print("Original Bill:", bill_amount)
print("After 10% Discount:", discounted_amount)
print("Final Bill (Rounded Down):", final_bill)

# Create a Zomato order bill calculator that uses math.floor() to show the final bill amount after applying a 10% discount, rounding down to the nearest rupee.
import math
bill_amount = float(input("Enter the order amount (₹): "))
discounted_amount = bill_amount * 0.90
final_bill = math.floor(discounted_amount)
print(f"Original Bill: ₹{bill_amount}")
print(f"After 10% Discount: ₹{discounted_amount:.2f}")
print(f"Final Bill (Rounded Down): ₹{final_bill}")

# Simulate a dice roll for a board game app using random.randint(1, 6) and print the result each time you run the program.
import random
dice_roll = random.randint(1, 6)
print("You rolled:", dice_roll)

# Build a Spotify-style daily playlist shuffle: given a list of 8 song names, use the random module to select and print 3 random songs for today's playlist.<br><br><em><strong>Hint:</strong> Use random.sample() for this task.</em>
import random
songs = [
    "Blinding Lights",
    "Shape of You",
    "Levitating",
    "Stay",
    "Perfect",
    "Bad Habits",
    "As It Was",
    "Heat Waves"
]
todays_playlist = random.sample(songs, 3)
print("Today's Playlist:")
for song in todays_playlist:
    print("-", song)
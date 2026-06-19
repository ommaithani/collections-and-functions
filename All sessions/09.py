# Write a lambda function to calculate the square of a number and use it to print the squares of numbers from 1 to 5.
square = lambda x: x * x
for i in range(1, 6):
    print(square(i))

# Given a list of food item prices from a Zomato order: [120, 250, 99, 180, 310], use a lambda function with the map() function to add a 10% service charge to each price and print the updated list.
prices = [120, 250, 99, 180, 310]
updated_prices = list(map(lambda x: x + x * 0.10, prices))
print(updated_prices)

# Use a lambda function with the filter() function to get only the usernames with more than 1000 followers from this list: [('raj', 800), ('simran', 1500), ('veer', 1200), ('ananya', 950)]. Print the usernames that would get the 'K' badge like Instagram.
users = [('raj', 800), ('simran', 1500), ('veer', 1200), ('ananya', 950)]
top_users = filter(lambda x: x[1] > 1000, users)
usernames = list(map(lambda x: x[0], top_users))
print(usernames)

# Create a lambda function that takes two numbers and returns their sum and product as a tuple. Use it to process the pairs (3, 4), (5, 2), and (7, 8).<br><br><em><strong>Hint:</strong> You can return multiple values from a lambda by returning a tuple: (a+b, a*b).</em>
calc = lambda a, b: (a + b, a * b)
pairs = [(3, 4), (5, 2), (7, 8)]
for a, b in pairs:
    print(calc(a, b))

# or
pairs = [(3, 4), (5, 2), (7, 8)]
result = list(map(lambda x: (x[0] + x[1], x[0] * x[1]), pairs))
print(result)

# generate a lambda function that takes a string and returns True if it is a palindrome (reads the same forwards and backwards), otherwise False. Test it with 'madam', 'python', and 'noon'.
is_palindrome = lambda s: s == s[::-1]
print(is_palindrome('madam'))
print(is_palindrome('python'))
print(is_palindrome('noon'))
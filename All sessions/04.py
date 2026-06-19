# Create a tuple named my_profile that contains your name (string), age (integer), favorite food (string), and a boolean indicating if you have a pet.
my_profile=('om maithani',23,'dosa',True)
print(my_profile)

# Given the tuple playlist = ('Shape of You', 'Blinding Lights', 'Believer', 'Senorita', 'Levitating'), use slicing to print only the 2nd, 3rd, and 4th songs.
playlist = ('Shape of You', 'Blinding Lights', 'Believer', 'Senorita', 'Levitating')
print(playlist[1:4])

# Convert the tuple order = ('Burger', 'Fries', 'Coke') into a list, add 'Ice Cream' to the end, then convert it back to a tuple and print the final tuple.
order = ('Burger', 'Fries', 'Coke')
order_list=list(order)
order_list.append('Ice-Cream')
order=tuple(order_list)
print(order)

# Create a mixed tuple called insta_post containing: post_id (int), username (string), likes (int), hashtags (list of strings), and is_public (boolean). Print the tuple and the type of each element.
insta_post=(100,'john',500,['#trend','#viral'],True)
print(type(insta_post[0]))
print(type(insta_post[1]))
print(type(insta_post[2]))
print(type(insta_post[3]))
print(type(insta_post[4]))

# Take a tuple of your last 7 WhatsApp call durations in minutes (e.g., (12, 5, 0, 20, 7, 3, 15)), convert it to a list, remove all calls shorter than 5 minutes, then convert it back to a tuple and print the result.<br><br><em><strong>Hint:</strong> Use a for loop or list comprehension to filter the list before converting back to tuple.</em>
call_duration=(12,5,0,20,7,3,15)
into_list=list(call_duration)
filtered=[]
for min in into_list:
    if min>5:
        filtered.append(min)
call_duration=tuple(filtered)
print(call_duration)

# or

call_duration=(12,5,0,20,7,3,15)
call_duration=tuple([min for min in call_duration if min>5])
print(call_duration) 


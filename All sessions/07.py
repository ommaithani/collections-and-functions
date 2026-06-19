
# Write a Python script that takes a string input from the user and prints a dictionary showing how many times each character appears in the string.
text=input("Enter a string : ")
char_count={}
for ch in text:
    if ch in char_count:
        char_count[ch]+=1
    else:
        char_count[ch]=1
print(char_count)

# text = input("Enter a string: ")

# char_count = {}

# for ch in text:
#     char_count[ch] = text.count(ch)

# print(char_count)

# Create a program that reads a short review (multi-line string) about your favorite food delivery app (like Zomato or Swiggy) and counts the frequency of each word, displaying the results as a dictionary.<br><br><em><strong>Hint:</strong> Convert all words to lowercase and remove punctuation for accurate counting.</em>
review = """
Zomato is a great food delivery app.
Zomato delivers food quickly and reliably.
I like using Zomato because the app is easy to use!
"""
review = review.lower()
for ch in ".,!?":
    review = review.replace(ch, "")
words = review.split()
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
print(word_count)

# Given the following string: 'Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match', write a function word_freq_dict(text) that returns a dictionary with the frequency of each word.
def word_freq_dict(text):
    freq = {}
    for ch in ",.":
        text = text.replace(ch, "")
    words = text.split()
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1
    return freq
text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"
print(word_freq_dict(text))

# Modify your word frequency program to ignore common stopwords like 'the', 'and', 'in', 'of', 'a', 'to', 'is' when counting word frequencies.<br><br><em><strong>Constraint:</strong> Use a list of stopwords and filter them out before counting.</em>
def word_freq_dict(text):
    stopwords = ['the', 'and', 'in', 'of', 'a', 'to', 'is']
    freq = {}
    text = text.lower()
    for ch in ",.!?":
        text = text.replace(ch, "")
    for word in text.split():
        if word not in stopwords:
            freq[word] = freq.get(word, 0) + 1
    return freq
text = "Virat scored 100, Rohit scored 80, and Gill scored 50 in the IPL match"
print(word_freq_dict(text))

# Refactor your character count script to use a function named char_count_dict(text) that returns the frequency dictionary, and then print the dictionary sorted by character (A-Z or a-z).
def char_count_dict(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    return freq
text = input("Enter a string: ")
char_freq = char_count_dict(text)
for ch in sorted(char_freq):
    print(ch, ":", char_freq[ch])

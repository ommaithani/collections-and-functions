from instahelpers import format_likes

test_counts = [
    500,
    999,
    1200,
    15000,
    999999,
    1500000,
    25000000
]

for count in test_counts:
    print(f"{count} -> {format_likes(count)}")
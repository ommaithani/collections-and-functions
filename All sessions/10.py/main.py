from playlist import add_song
my_playlist = []
my_playlist = add_song('Kesariya', my_playlist)
my_playlist = add_song('Shape of You', my_playlist)
my_playlist = add_song('Believer', my_playlist)
print(my_playlist)

from playlist import add_song, remove_song
my_playlist = []
my_playlist = add_song('Kesariya', my_playlist)
my_playlist = add_song('Shape of You', my_playlist)
my_playlist = add_song('Believer', my_playlist)
print("Before removal:", my_playlist)
my_playlist = remove_song('Shape of You', my_playlist)
print("After removal:", my_playlist)

from playlist import add_song, remove_song, display_playlist
my_playlist = []
my_playlist = add_song('Kesariya', my_playlist)
my_playlist = add_song('Shape of You', my_playlist)
my_playlist = add_song('Believer', my_playlist)
print("Before removal:")
display_playlist(my_playlist)
my_playlist = remove_song('Shape of You', my_playlist)
print("\nAfter removal:")
display_playlist(my_playlist)
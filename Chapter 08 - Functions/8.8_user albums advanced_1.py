def get_make_album(artist_name, album_title):
    """ Make an album """
    album_1 = {'artist': artist_name, 'album': album_title}
    return album_1

while True:
    print("\nPlease enter an artist and album")
    print("Enter 'q' to quit.")

    artist_name = input("Artist: ")
    if artist_name == 'q':
        break

    album_title = input("Album: ")
    if album_title == 'q':
        break

    album = get_make_album(artist_name.title(), album_title.title())
    print(f"\nYour favorite artist is {artist_name.title()}, "
          f"and your favorite album is {album_title.title()}! ")

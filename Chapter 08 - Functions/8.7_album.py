def make_album(artist_name, album_title):
    """ Make an album """
    album_1 = {'artist': artist_name.title(), 'album': album_title.title()}
    return album_1

cover = make_album('jimi hendrix', 'purple haze')
cover_2 = make_album('micheal jackson', 'thriller')
cover_3 = make_album('2pac', 'dear momma')
cover_4 = make_album('jay-z', 'the blueprint')
print(cover)
print(cover_2)
print(cover_3)
print(cover_4)
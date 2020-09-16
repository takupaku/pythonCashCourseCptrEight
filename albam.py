def make_album(album_title,artist_name,track_no=''):
    if track_no:
        album = {'title': album_title, 'artist': artist_name, 'track': track_no}
        return album
    else:
        album={'title':album_title,'artist':artist_name}
        return album

album1=make_album('rokutosei no yoru','aimer')
print(album1)

album2=make_album('signal','tk')
print(album2)

album3=make_album('wherever you will go','the calling')
print(album3)

album4=make_album('clock strick','one ok rock','three')
print(album4)

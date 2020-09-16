def make_album(album_title, artist_name, track_no=''):
    #  function definition is holding the mechanism of the dictionary
    #  no need to repeat the mechanism,so not in while loop

    album = {}
    #  dictionary

    album['title'] = album_title
    #  key is defined, only the mechanism to input the value(from function call) in dictionary is mentioned
    album['artist'] = artist_name
    album['track '] = track_no

    for k, v in album.items():
        #  printing the stored item of Dictionary
        print(k + ":" + " " + v)


while True:
    #  for multiple input, while loop is declared
    print('please enter album title, artist name')
    #  the code starts here,the function defination is just a hidden machanism without function call

    title = input('album name: ')
    #  importing value
    name = input('artist name: ')
    if_track = input('do you want to add track in the album?(y/n)')
    if if_track == 'y':
        track = input('track: ')
        make_album(title, name, track)
    else:
        make_album(title, name)

    print('do u want to add more album?(y/n)')
    answer = input("your answer: ")
    if answer == 'n':
        break






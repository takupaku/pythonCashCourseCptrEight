magicians=['alice','shila','hola']
mgg=[]

def show_magicians(name):

    for mage in magicians:
        msg='hello, '+mage.title()+"!"
        print(msg)


#show_magicians(magicians)



def make_great(title):
    while magicians:
        stored_name = magicians.pop()
        new_name = stored_name + title
        magicians.append(new_name)


make_great(' the great')
for name in magicians:
     print(name)

show_magicians(magicians)


magicians=['alice','shila','hola']
def show_magicians(name):
    for mage in magicians:
        msg='hello, '+mage.title()+"!"
        print(msg)

show_magicians(magicians)
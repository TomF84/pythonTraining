class MyStuff(object):

    def __init__(self):
        self.tangerine = "And now a thousand years between"
        
    def apple(self):
        print("I AM CLASSY APPLES!")

# dict style
mystuff = {'apple': "I AM APPLES!"}
print(mystuff['apple'])

# import style
import mystuff

mystuff.apple()
print(mystuff.tangerine)

# class style
thing = MyStuff()
thing.apple()
print(thing.tangerine)
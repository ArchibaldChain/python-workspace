class Greeter(object):

    # constructor
    def __init__(self, name):
        self.name = name

    # instance method
    def greet(self, loud=False):
        if loud:
            print('HELLO, %s' % self.name.upper())
        else:
            print("hello, %s" % self.name)


g = Greeter('Freed')
g.greet()
g.greet(True)

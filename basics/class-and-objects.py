# class and object session


# creating a class
class Person:
    # behaves like constructor
    def __init__(self, name, occupation):  # self is equivalent to this
        self.name = name
        self.occupation = occupation

    # a method
    def do_worl(self):
        if self.occupation == "footballer":
            print(self.name, "plays football")
        elif self.occupation == "actor":
            print(self.name, "shoots a film")

    # another method
    def speaks(self):
        print(self.name, "says how are you?")


# creating an instance of person
timi = Person("peter parker", "actor")
# calling the first method
timi.do_worl()
# calling the second method
timi.speaks()

# creating another instance of person
timo = Person("lionel messi", "footballer")
# calling the first method
timo.do_worl()
# calling the first method
timo.speaks()

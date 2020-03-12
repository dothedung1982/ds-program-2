class FooClass:
    """my very first class: FooClass"""
    version = 0.1  # class (data) attribute

    def __init__(self, nm='The Dung'):
        """constructor"""
        self.name = nm  # class instance (data) attribute
        print("Created a class instance for " + nm)

    def showname(self):
        """display instance attribute and class name"""
        print("Your name is " + self.name)
        print("My name is: {0}".format(self.__class__))  # full class name

    def showver(self):
        """display class(static) attribute"""
        print(self.version)  # references FooClass.version

    def addMe2Me(self, x):  # does not use 'self'
        """apply + operation to argument"""
        return x + x


# Create Class Instances
foo1 = FooClass()
foo1.showname()
foo1.showver()


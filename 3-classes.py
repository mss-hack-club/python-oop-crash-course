# To represent a template in Python, we use a CLASS

# This is how the template (class) for a phone would look (according to the previous example)
class Phone:  # making a new class (template) called phone
    # NOTE: EVERY SINGLE FUNCTION in a class MUST take self as it's first argument

    # the self object refers to the CURRENT INSTANCE of a class
    # e.g. if you make an instance of this class (if you make an object of type Phone),
    # when you call functions from the class self will be the that object
    # if you call a function from ANOTHER object of the same class, the self
    # represents THAT object instead

    # This is a CONSTRUCTOR FUNCTION. This function is called  to CREATE (CONSTRUCT)
    # a new instance of the class The constructor function can take any number
    # of arguments and it RETURNS (implicitly) the instance of the class. ALL
    # CONSTRUCTOR FUNCTIONS IN PYTHON are named __init__ (special name)

    # In this case, the constructor also takes a color, size, operating system, and company
    def __init__(self, color, size, os, company):
        # ATTRIBUTES

        # This is how you set attributes. Normally, attributes are set IN THE CONSTRUCTOR FUNCTION
        # notice how all attributes are set using the self. prefix. Since attributes change from
        # instance to instance of the class, attributes are stored as INSTANCE
        # variables (hence the prefix of self.) We also use self. because self
        # is passed to all the functions, so we can access any attribute OF THE
        # CURRENT INSTANCE (e.g. the color of this particular phone is red) in any function

        # If you don't use self. to set an instance variable, but instead just use
        # the regular variable declaration syntax outside of the constructor function,
        # you will be setting the variable for ALL INSTANCES of the CLASS (all the phones,
        # not just this one)

        # for example, here, we are taking the color passed into the CONSTRUCTOR
        # and setting it as the color for THIS PARTICULAR INSTANCE OF THE CLASS
        self.color = color

        # same thing for the rest
        self.size = size
        self.os = os
        self.company = company

    # FUNCTIONS
    # You can also define any number of functions that can be called on any instance
    # of the class

    # defins a CALL function for the Phone class. Notice how it takes self as a default
    # argument, then one more which is the phone number. When you call this function,
    # you only have to pass the number (self is passed implicitly)

    def call(self, number):
        print('Calling ' + number)

    # similar thing for text
    def text(self, number):
        print('Texting ' + number)

    # or you can pass nothing
    def playYoutube(self):
        print('Playing YouTube')

# USING THE TEMPLATE


# by the way, this is a special if statement used to tell Python where exactly to
# start explicitly reading code. This is not necessary, but in some cases it's
# better for readability
if __name__ == "__main__":
    # calling the constructor function of the phone class to get back the phone object it returns

    # notice we are passing all the arguments we expected according to the constructor function
    # definition in the class

    # one instance of phone
    phone1 = Phone("red", "large", "iOS", "Apple")

    # another instance of phone
    phone2 = Phone("blue", "small", "iOS", "Apple")

    # now we can do stuff with the phone1 attributes
    # notice we access attributes by just putting the object.attribute
    # with NO BRACKETS
    print(phone1.color)

    # or, to change it on the go
    phone1.color = "blue"

    # You can also call the functions you defined on phone1
    # notice the ONE ARGUMENT we're passing here
    # self is automatically passed (and in this case self is the whole phone1 object)
    phone1.call("123456789")

    # and in this case, self is implicitly passed as the whole phone2 object
    phone2.call("123456789")

    # or you can call a function that returns nothing
    phone2.playYoutube()

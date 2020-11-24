#Construtor code to the pet game, templated from the crop simulation constructor

class Pet:

    #constructor
    def __init__(self, petName, petType):
        #setting attributes with an initial value
        self.__petName = petName
        self.__petType = petType
        self.__bored = 0
        self.__hunger = 0
        self.__intelligence = 0
        #the above attributes are prefixed with an underscore to indicate
        #that they cannot be accessed from outside the class
        #this is making them hem 'private'
        #meaning you need to use a method to access them, encapsulating them  
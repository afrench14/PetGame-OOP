class Pet:
    #constructor
    def __init__(self, petName, petType):
        #setting attributes with an initial value
        self.__petName = petName
        self.__petType = petType
        self.__bored = 0
        self.__hunger = 0
        self.__intelligence = 0
    
    def showhunger():
        return(self.__hunger)


NewPet = Pet("springy", "Tiger")

springy.showhunger()

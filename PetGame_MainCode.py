class Pet:
    #constructor
    def __init__(self, petName, petType):
        #setting attributes with an initial value
        self.petName = petName
        self.petType = petType
        self.bored = 0
        self.hunger = 0
        self.intelligence = 0
    
    def showHunger():
        print(self.hunger)
    
    def outputGreeting():
        print("hello, i am", self.petName, "i'm a", self.petType)


newPet = Pet("springy", "tiger")
newPet.showHunger()
newPet.outputGreeting()
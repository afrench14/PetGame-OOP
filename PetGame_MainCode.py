class Pet:
    #constructor
    def __init__(self, petName, petType):
        #setting attributes with an initial value
        self.petName = petName
        self.petType = petType
        self.bored = 0
        self.hunger = 50
        self.intelligence = 50

    def showHunger(self, hunger):
        if self.hunger == 100:
            print(self.petName, "has", self.hunger, "hunger points remaining and is full, good job")
        elif  70 <= self.hunger < 100:
            print(self.petName, "has", self.hunger, "hunger points remaining and is satisfied")
        elif 50 <= self.hunger < 70:
            print(self.petName, "has", self.hunger, "hunger points remaining and is getting hungry")
        elif 20 <= self.hunger < 50:
            print(self.petName, "has", self.hunger, "hunger points remaining and is a little hungry")
        elif 10 <= self.hunger < 20:
            print(self.petName, "has", self.hunger, "hunger points remaining and is extremely hungry, feed asap")
        elif 0 < self.hunger < 10:
            print(self.petName, "has", self.hunger, "hunger points remaining and will soon starve, feed immediately")
        #include 'dead' here
        else:
            print("error returning", self.petName + "'s hunger, sorry :(")

    def outputGreeting(self, petName):
        print("hello, i am", self.petName, "and i'm a", self.petType)


newPet = Pet("springy", "tiger")
newPet.showHunger(newPet.hunger)
newPet.outputGreeting(newPet.petName)
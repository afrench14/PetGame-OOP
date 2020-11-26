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
        print(self.petName, "has", self.hunger, "hunger points remaining")
        if self.hunger == 100:
            print(self.petName, "has", self.hunger, "hunger points remaining and is full, good job")
        elif  70 =< self.hunger < 100:
            print(self.petName, "has", self.hunger, "hunger points remaining and is satisfied")
        elif 50 =< self.petName < 70:
            print(self.petName, "has", self.hunger, "hunger points remaining and is getting hungry")
        elif 20 =< self.petName < 50:
            print(self.petName, "has", self.hunger, "hunger points remaining and is a little hungry")
        elif 10 =< self.petName < 20:
            print(self.petName, "has", self.hunger, "hunger points remaining and is extremely hungry, feed asap")
        elif 0 < self.petName < 10:
            print(self.petName, "has", self.hunger, "hunger points remaining and will soon starve, feed immediately")
        #include 'dead' here
        else:
            print("error returning", self.petNme + "'s hunger, sorry :(")

    def outputGreeting():
        print("hello, i am", self.petName, "i'm a", self.petType)


newPet = Pet("springy", "tiger")
newPet.showHunger()
newPet.outputGreeting()
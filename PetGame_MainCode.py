class Pet:
  #constructor
  def __init__(self, petName, petType):
    #setting attributes with an initial value
    self.petName = petName
    self.petType = petType
    self.bored = 0
    self.hunger = 50
    self.intelligence = 50
    self.alive = True
    self.entertained = True
    self.educated = True

    #show hunger values
    def showHunger(self, hunger):
      if self.hunger > 100:
        self.hunnger = 100
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
      elif self.hunger == 0:
        print("unfortunately,", self.petName + "'s hunger has reached zero, so", self.petName, "has died")
        self.alive = False
      else:
        print("error returning", self.petName + "'s hunger, sorry :(")

    #show bored values
    def showBored(self, bored):
      if self.bored == 0:
        print(self.petName, "is", self.bored, "percent bored, another good job")
      elif  0 < self.bored <= 20:
        print(self.petName, "is", self.bored, "percent bored and is not too un-entertained just yet")
      elif 20 < self.bored <= 50:
        print(self.petName, "is", self.bored, "percent bored and will probably get bored some time soon")
      elif 50 < self.bored <= 70:
        print(self.petName, "is", self.bored, "hunger points remaining and is a little hungry")
      elif 10 <= self.bored < 20:
        print(self.petName, "is", self.bored, "hunger points remaining and is extremely hungry, feed asap")
      elif 0 < self.bored < 10:
        print(self.petName, "is", self.bored, "hunger points remaining and will soon starve, feed immediately")
      elif self.bored == 0:
        print("unfortunately,", self.petName + "'s bored has reached zero")
        print("so", self.petName, "has run away to find something more interesting to do")
        self.entertained = False
      else:
        print("error returning", self.petName + "'s bored level, sorry :(")

    def outputGreeting(self, petName):
      print("hello, i am", self.petName, "and i'm a / an", self.petType)


listOfPets = []

pet1 = Pet("springy", "tiger")
pet1.outputGreeting(pet1.petName)
pet1.showHunger(pet1.hunger)
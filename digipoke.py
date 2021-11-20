import random

evolved = False

class DigiPoke ():

    def __init__ (self, name, Type):
        self.name = name
        self.Type = Type
        self.health = 100
        self.record = 0

    def fight (self):
        winLose = random.randint(0,1)
        if (winLose == 1):
            print ("You won!")
            self.health -= 10
            self.record += 1
        else:
            print ("You lost :/")
            self.health -= 25

    def heal (self):
        self.health += 10
        self.record -= 0.5
        if (self.health > 100):
            self.health = 100

    def status (self):
        information = ("DigiPoke: " + self.name + " \nType: " + self.Type + " \nHealth: " + str(self.health) + " \nRecord: " + str(self.record))
        print (information.title())

class EvolvedDigi (DigiPoke):
    def __init__(self, name, Type):
        super().__init__(name, Type)
        secondTypes = ['earth', 'water', 'fire', 'air']
        secondTypes.remove(Type)
        self.type2 = secondTypes[random.randint(0,2)]
    
    def retire(self):
        if (self.record >= 5):
            evolved = False

    def status(self):
        information = ("DigiPoke: " + self.name + " \nType: " + self.Type + " \nType2: " + self.type2 + " \nHealth: " + str(self.health) + " \nRecord: " + str(self.record))
        print (information.title())
        

n = input("Enter a Name: ")
t = input("Enter a Type [fire, water, earth, air]: ")
new_Digi = DigiPoke(n, t)

while ((new_Digi.health > 0) and (evolved == False)):
    option = int(input("Choose an action: 1)Fight 2)Heal 3)Evolve 4)Status\n")) 
    if (option == 1):
        new_Digi.fight()
    elif (option == 2):
        new_Digi.heal()
    elif (option == 3):
        new_Digi.record = 5
        if (new_Digi.record >= 5):
            evolve_Digi = EvolvedDigi(new_Digi.name, new_Digi.Type)
            evolved = True
            print ("Choose option 4 to view the status of your new DigiPoke!")
    elif (option == 4):
        new_Digi.status()
if (new_Digi.health <= 0):
    print ("GAME OVER. Your DigiPoke died!")

if (evolved):
    while ((evolve_Digi.health > 0) and (evolved == True)):
        option = int(input("Choose an action: 1)Fight 2)Heal 3)Retire 4)Status\n")) 
        if (option == 1):
            evolve_Digi.fight()
        elif (option == 2):
            evolve_Digi.heal()
        elif (option == 3):
            evolve_Digi.retire()
        elif (option == 4):
            evolve_Digi.status()
    if (evolve_Digi.health <= 0):
        print ("GAME OVER. Your Evolved DigiPoke died!")

        

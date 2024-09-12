#creating the super class item, containning name and description
class Item:
    def __init__(self, name = "N/A", description = "N/A"):
        self.__name = name
        self.__description = description
    def setName(self,newName):
        self.__name = newName
    def getName(self):
        return self.__name
    def setDescription(self,newDescription):
        self.__description = newDescription
    def getDescription(self):
        return self.__description
    def __str__(self):
        line1 = "\nName: " + self.__name
        line2 = "\nDescription: " + self.__description
        return line1 + line2
# Subclass Book inheriting from Item    
class Book(Item):
    def __init__(self, name = "N/A", description = "N/A", genre = "N/A",author= "Unknown Author", publishYear=2000):
        super().__init__(name, description)
        self.__genre = genre
        self.__author = author
        self.__publishYear = publishYear
    def setGenre(self, newGenre):
        self.__genre = newGenre
    def setAuthor(self, newAuthor):
        self.__author = newAuthor
    def setPublishYear(self, newPublishYear):
        self.__publishYear = newPublishYear
    def getGenre(self):
        return self.__genre
    def getAuthor(self):
        return self.__author
    def getPublishYear(self):
        return self.__publishYear
    def __str__(self):
        line1 = super().__str__()
        line2 = "\nGenre: " + self.__genre
        line3 = "\nAuthor: " + self.__author
        line4 = "\nPublish Year: " + str(self.__publishYear)
        return line1 + line2 + line3 + line4
# Superclass Character
class Character:
    def __init__(self, name = "N/A", health = 100):
        self.__name = name
        self.__health = health
        self.__inventory = []
    def setName(self,newName):
        self.__name = newName
    def setHealth(self,newHealth):
         self.__health = newHealth
    def getName(self):
        return self.__name
    def getHealth(self):
        return self.__health
    def addItem(self, item):
        self.__inventory.append(item)
    def dropItem(self, itemName):
        for item in self.__inventory:
            if item.getName() == itemName:
                self.__inventory.remove(item)
    # The special ability for healers, they can heal themselves or others in the party                
    def specialAbility(self):
        self.__health += 10
    def __str__(self):
        line1 = "\nName: " + self.__name
        line2 = "\nhealth: " + str(self.__health)
        line3 =  "\n', '".join([item.getName() for item in self.__inventory])
        return line1 +line2 + line3    
# Subclass Healer
class Healer(Character):
    def __init__(self, name, health=150, healingPower=50):
        super().__init__(name, health)
        self.__healingPower = healingPower
    def setHealingPower(self,newHealingPower):
        self.__healingPower = newHealingPower
    def getHealingPower(self):
        return self.__healingPower
    def specialAbility(self):
        return "%s performs a special ability: Heal themselves or others in the party." % super().getName()
    def __str__(self):
        line1 = super().__str__()
        line2 = "\nHealing Power: " + str(self.__healingPower)
        return line1 + line2

def main():
    # Create items
    sword = Item("Sword", "A sharp weapon")
    novel = Book("The Hobbit", "An adventure novel", "Fantasy")

    # Create characters
    warrior = Character("Warrior", 120)
    healer = Healer("Healing Spirit", 180, 40)

    # Test functionality
    warrior.addItem(sword)
    healer.addItem(novel)

    print(warrior)
    print(healer)

    warrior.specialAbility()
    healer.specialAbility()

    print(warrior)
    print(healer)

main()
        

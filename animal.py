class Animal(object):
    # constructor method: __init__
    # passes in all the info/attributes
    def __init__(self, hunger, happiness, health, energy, age, name, species):
        # set each attribute to corresponding inputs
        self.hunger = hunger
        self.happiness = happiness
        self.health = health
        self.energy = energy
        self.age = age
        self.name = name
        self.species = species

    # instance method: play
    # input: none
    # return: none
    # side effect: manipulates the variables
    # inc. animal's happiness by 10 and inc. the animal's hunger by 5
    def play(self):
        self.happiness = 10 + int(self.happiness)
        # value cannot be negative
        if self.happiness < 0:
            self.happiness = 0
        # value can't exceed 100
        elif self.happiness >= 100:
            self.happiness = 100

        self.hunger = 5 + int(self.hunger)
        # value cannot be negative
        if self.hunger < 0:
            self.hunger = 0
        # value can't exceed 100
        elif self.hunger >= 100:
            self.hunger = 100
        # do not need print b/c manipulating values

    # instance method: feed
    # input: none
    # return: none
    # side effect: manipulates the variables
    # dec. animal's hunger by 10
    def feed(self):
        self.hunger = int(self.hunger) - 10
        # value cannot be negative
        if self.hunger < 0:
            hunger = 0
        # value can't exceed 100
        elif self.hunger >= 100:
            hunger = 100

    # instance method: giveMedicine
    # input: none
    # return: none
    # side effect: manipulates the variables
    # dec. animal's happiness by 20 and inc. animal's health by 20
    def giveMedicine(self):
        self.happiness = int(self.happiness) - 20
        # value cannot be negative
        if self.happiness < 0:
            self.happiness = 0
        # value can't exceed 100
        elif self.happiness >= 100:
            self.happiness = 100
        self.health = int(self.health) + 20
        # value cannot be negative
        if self.health < 0:
            self.health = 0
        # value can't exceed 100
        elif self.health >= 100:
            self.health = 100

    # instance method: sleep
    # input: none
    # return: none
    # side effect: manipulates the variables
    # inc. animal energy by 20 and inc animal age by 1
    def sleep(self):
        self.energy = int(self.energy) + 20
        # value cannot be negative
        if self.energy < 0:
            self.energy = 0
        # value can't exceed 100
        elif self.energy >= 100:
            self.energy = 100

        # do not have to check range b/c only adding values and age can be > 100
        self.age = int(self.age) + 1

    # instance method: __str__
    # input: none
    # return: str
    # side effect: prints the message
    # create str containing message w/ all attributes
    def __str__(self):
        # start the message off and add values to it with \n
        msg = "Name: " + self.name + " the " + self.species + "\n"
        msg += "Health: " + self.health + "\n"
        msg += "Happiness: " + self.happiness + "\n"
        msg += "Hunger: " + self.hunger + "\n"
        msg += "Energy: " + self.energy + "\n"
        msg += "Age: " + self.age + "\n"

        # need to return the msg str
        # when class is called, the __str__ is called too
        return msg


# fxn: loadAnimals
# input: str representing name of csv file
# return: list of Animal objects
# side effect: forms a list
# store all line of data as new objects
def loadAnimals(fileName="animals.csv"):
    # not all values are str, there are also ints
    # create empty list for all animals and their attributes
    animalAttributes = []

    fileIn = open(fileName, "r")
    for line in fileIn:
        line = line.strip()
        # make the str into lists of strings with comma as separator
        info = line.split(",")
        # attributes list
        animalAttributes.append(info)
        # want only the animals therefore the 7th attribute and index of 6
        # animals.append(info[5] + " the " + info[6])

    # close the file
    fileIn.close()

    # animals = animals[2]
    # return the list
    return animalAttributes


# fxn: displayMenu
# input: none
# return: none
# side effect: prints menu of what user can do
# displays menu w/ all options to user
def displayMenu():
    # display all 7 choices with a new line for each choice
    print(
        "1) Play \n2) Feed \n3) Give Medicine \n4) Sleep \n5) Print an Animal's stats \n6) View All Animals \n7) Exit \n")


# fxn: selectAnimal
# input: list of Animals
# return: selected animal from list
# side effect: prints menu of animals
# returns animal from list based off user input
def selectAnimal(animals):
    # to number the animals
    counter = 1

    msg = ""
    # print the animals
    # there are 5 animals so only wanting it to run that many times
    while counter < 6:
        # want to start from the first animal list which is index=0
        list = animals[counter-1]
        msg += str(counter) + ") " + list[5] + " the " + list[6] + "\n"
        # inc the counter so next animal numbered correctly
        counter += 1

    # outside the while loop
    animalSelection = int(input(msg + "\n" + "Please select an animal from the list (enter the 1-5): "))

    # handle invalid inputs
    while animalSelection not in range(1, 6):
        print("Invalid input, please try again!")
        animalSelection = input("\n" + "Please select an animal from the list (enter the 1-5): ")

    # subtract one from value because indexing starts at 0
    # gives animal & attributes
    animalSelection = animals[animalSelection - 1]

    # gives only the animal name in str form
    # animalSelection = animalSelection[5] + " the " + animalSelection[6]

    # return the str
    return animalSelection


# fxn: main
# input: none
# return: none
# side effect: prints questions for user
# based on user input, there are fxns which are called
def main():
    # use a while loop and handle invalid menu selections
    # perform actions based on options called

    # create list of animal attributes
    animals = loadAnimals()

    # print welcome statement
    print("Welcome to the Animal Daycare! Here is what we can do: \n")

    # call fxn to call the menu which user will select from
    displayMenu()

    userMenu = int(input("\nPlease make a selection: "))

    # error checking
    while userMenu not in range(1, 8):
        print("*Invalid selection, please try again. \n")
        userMenu = int(input("Please make a selection: "))

    # user enters value != exit
    while userMenu != 7:
        # want to play
        if userMenu == 1:
            # pick the animal w/ attributes
            animalSelection = selectAnimal(animals)
            # call the object and instance to run
            # run all attributes through
            run = Animal(animalSelection[0], animalSelection[1], animalSelection[2], animalSelection[3], animalSelection[4], animalSelection[5], animalSelection[6])
            run.play()
            # print the end statement
            # index 5 & 6 b/c gives name the species format
            print("You played with " + animalSelection[5] + " the " + animalSelection[6] + "!")

        # want to feed
        elif userMenu == 2:
            # pick the animal w/ attributes
            animalSelection = selectAnimal(animals)
            run = Animal(animalSelection[0], animalSelection[1], animalSelection[2], animalSelection[3], animalSelection[4], animalSelection[5], animalSelection[6])
            run.feed()
            # print the end statement
            # index 5 & 6 b/c gives name the species format
            print("You fed " + animalSelection[5] + " the " + animalSelection[6] + "!")

        # giving medicine to one
        elif userMenu == 3:
            # pick the animal w/ attributes
            animalSelection = selectAnimal(animals)
            run = Animal(animalSelection[0], animalSelection[1], animalSelection[2], animalSelection[3], animalSelection[4], animalSelection[5], animalSelection[6])
            run.giveMedicine()
            # print the end statement
            # index 5 & 6 b/c gives name the species format
            print("You gave " + animalSelection[5] + " the " + animalSelection[6] + " some medicine!")

        # nap time for an animal
        elif userMenu == 4:
            # pick the animal w/ attributes
            animalSelection = selectAnimal(animals)
            run = Animal(animalSelection[0], animalSelection[1], animalSelection[2], animalSelection[3], animalSelection[4], animalSelection[5], animalSelection[6])
            run.sleep()
            # print the end statement
            # index 5 & 6 b/c gives name the species format
            print(animalSelection[5] + " the " + animalSelection[6] + " took a nap!")

        # print an animal's stats
        elif userMenu == 5:
            # pick the animal w/ attributes
            animalSelection = selectAnimal(animals)
            # calls object to run full thing on one animal
            # call the object to print
            msgStats = Animal(animalSelection[0], animalSelection[1], animalSelection[2], animalSelection[3], animalSelection[4], animalSelection[5], animalSelection[6])
            print(msgStats)

        # show all animals
        elif userMenu == 6:
            # collect all info and pass attributes in object first
            # first animal so call first list
            first = animals[0]
            firstmsg = Animal(first[0], first[1], first[2], first[3], first[4], first[5], first[6])

            # second animal
            second = animals[1]
            secondmsg = Animal(second[0], second[1], second[2], second[3], second[4], second[5], second[6])

            # third animal
            third = animals[2]
            thirdmsg = Animal(third[0], third[1], third[2], third[3], third[4], third[5], third[6])

            # fourth animal
            fourth = animals[3]
            fourthmsg = Animal(fourth[0], fourth[1], fourth[2], fourth[3], fourth[4], fourth[5], fourth[6])

            # last animal
            fifth = animals[4]
            fifthmsg = Animal(fifth[0], fifth[1], fifth[2], fifth[3], fifth[4], fifth[5], fifth[6])

            # print all msgs in format
            finalmsg = str(firstmsg) + "********************************\n"
            finalmsg += str(secondmsg) + "********************************\n"
            finalmsg += str(thirdmsg) + "********************************\n"
            finalmsg += str(fourthmsg) + "********************************\n"
            finalmsg += str(fifthmsg) + "********************************\n"
            print(finalmsg)

        # need to know if you want to exit or re-enter the loop
        displayMenu()
        userMenu = int(input("Please make a selection: "))

    # out of while loop and exit the program
    print("Goodbye!")


# call main to run the whole program
main()

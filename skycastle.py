# Author: Yuxiang Pan

# Global setting
USERNAME = 'player'
PASS = 0
MAIN = 'No main weapon'
SECONDARY = 'No secondary weapon'
HEALTH = 'No health potion'
BUFF = 'No buff potion'
SPECIAL = 'No special item'
ACHIEVEMENT = 'Achievements:\n'
ESCAPED = False
x = '=' * 100
y = '-' * 50

def inventory():
    print(y)
    print(MAIN)
    print(SECONDARY)
    print(HEALTH)
    print(BUFF)
    print(SPECIAL)
    print(y)

def achievement():
    print(y)
    print(ACHIEVEMENT)
    print(y)

def next():
    PASS1 = 0
    while PASS1 == 0:
        skip = input(">>> ")
        if skip == 'inventory':
            inventory()
        elif skip == 'achievement':
            achievement()
        elif skip == '':
            PASS1 = 1
        else:
            print("Please don't type gibberish, press enter to continue the game")

def plot():
    print("Once upon a time, the human world fall into chaos due to the appearance of the demon king. When mankind army was")
    print("on the losing point, the legendary archangel Ariel descended to the mortal plane, bestowed a divine relic")
    print("to a human soldier. The man acquired immeasurable power; powerful enough to turn the table of war. At the")
    print("end, demon king was slayed, but mankind also suffered severe consequences. The owner of the divine relic,")
    print("The Hero, as others called, exhausted every divine power of the relic to cast a blessing upon the land. As the")
    print("relic shattered to dust, the world slowly began to regenerate...\n")
    next()
    print("\nHowever, a rumor remains:\n")
    next()
    print("When the relic became a pile of dust, The Hero found a key inside the pile; a key to the divine realm!")
    print("Greed is in human nature, over decades, authorities fought each other for the ownership of the key.")
    print("Kings started war; powers unbalances thus once again world fall into chaos. Among swords and blood, the key")
    print("disappeared without any trace...")
    next()
    print(x)

def library():
    global SPECIAL, ACHIEVEMENT
    PASS1 = 0
    while PASS1 == 0:
        choice1 = input("> ")
        if choice1 == 'the apprentice librarian':
            print("You politely ask her but she doesn't even know about the legend...")
            print("You need to find another person.")
        elif choice1 == 'a shady looking person':
            print("You politely ask him and he returns you a menacing glance!\nYou feel chills down to your spine.")
            print("Better leave him and find another person.")
        elif choice1 == 'a professor':
            print("You politely ask him about the key. The professor is a history enthusiast; he gladly tells you")
            print("that the key unlocks to gate of Ariel's skycastle. The professor marks the location on your map")
            print("and wishes you a safe journey.")
            PASS1 = 1
        elif choice1 == 'inventory':
            inventory()
        elif choice1 == 'achievement':
            achievement()
        elif choice1 == 'the great sage':
            print("You respecfully ask the great sage. The old man is shocked about the appearance of the key.")
            print("He inquires you about how you obtained such a treasure for 2 hours. Then, he tells you that")
            print("the key can grant you access to the skycastle of the archangel Ariel, and marks the location")
            print("on your map.")
            next()
            print("You thank the great sage. When you are leaving the library, the old man gives you a violet crystal")
            print("emitting an ominous aura. He claims that it was found in the demon king's treasure, perhaps it can")
            print("helps you on your journey.")
            SPECIAL = 'Violet Crystal x 1'
            next()
            print("Violet Crystal +1")
            next()
            print(y)
            print("Achievement unlocked!")
            print("-= Dark Side's Calling =-")
            ACHIEVEMENT = ACHIEVEMENT + " -= Dark Side's Calling =- \n"
            print(y)
            PASS1 = 1
        else:
            print("Please enter a valid choice")

def mission():
    global PASS, ESCAPED, USERNAME, ACHIEVEMENT
    print("PREFACE:")
    USERNAME = input("Centuries passed by, a young adventurer of countryside, you (enter your name, default set to 'player':), ")
    print("came across a drunkard at the adventurer's guild. He mumbled some nonsense to you and gave you a shiny object.")
    print("After appraising, you recognize the key in legend. What do you do?")
    while PASS == 0:
        choice = input("> ")
        if choice == 'keep it a secret':
            print("This is indeed to dangerous to let people know. You decided to go to the skycastle on your own.")
            PASS = 1
        elif choice == 'recruit teammates':
            print("It might be dangerous to let others know, but a second pair of hands is always helpful! You decided")
            print("to go to the skycastle with a party.")
            PASS = 1
        elif choice == 'inventory':
            inventory()
        elif choice == 'achievement':
            achievement()
        elif choice == 'sell the key':
            print("To avoid attention, you went to the black market to sell the key. An aristocrat recognized the key")
            print("immediately and bid the highest price. You become rich over night.\n")
            next()
            print("THE END\nThank you for playing!")
            next()
            print(y)
            print("Achievement unlocked!")
            print("-= Quickest Ending =-")
            ACHIEVEMENT = ACHIEVEMENT + " -= Quickest Ending =- \n"
            print(y)
            PASS = 1
            ESCAPED = True
        elif choice == 'use the key':
            print("A brillant idea! ...If only you know what this key unlocks...")
            print("You need to think of something else.")
        elif choice == 'go to the library':
            print("You put the key inside your pocket, and head towards the library. Who would you ask about information")
            print("on the key?")
            library()
            PASS = 1
        else:
            print("Please enter a valid choice")

# Run the game
plot()
mission()
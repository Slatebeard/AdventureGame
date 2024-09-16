## VARIABLES
rooms = ["The Library", "The Grand Hall", "The Observatory", "The Inner Sanctum"]
help_list = "1.Look \n2.Go \n3.Take \n4.Use \n5.Help\n"
player_pos = rooms[1]
key1 = 0
start = 0

## INTRO ART
intro_art = r"""
  _______ _    _ ______   ______ ____  _____   _____  ____ _______ _______ ______ _   _   _______ ______ __  __ _____  _      ______ 
 |__   __| |  | |  ____| |  ____/ __ \|  __ \ / ____|/ __ \__   __|__   __|  ____| \ | | |__   __|  ____|  \/  |  __ \| |    |  ____|
    | |  | |__| | |__    | |__ | |  | | |__) | |  __| |  | | | |     | |  | |__  |  \| |    | |  | |__  | \  / | |__) | |    | |__   
    | |  |  __  |  __|   |  __|| |  | |  _  /| | |_ | |  | | | |     | |  |  __| | . ` |    | |  |  __| | |\/| |  ___/| |    |  __|  
    | |  | |  | | |____  | |   | |__| | | \ \| |__| | |__| | | |     | |  | |____| |\  |    | |  | |____| |  | | |    | |____| |____ 
    |_|  |_|  |_|______| |_|    \____/|_|  \_\\_____|\____/  |_|     |_|  |______|_| \_|    |_|  |______|_|  |_|_|    |______|______|

"""

intro_text1 = "Welcome to this simple text adventure where you will explore an ancient temple located deep in the forest."
intro_text2 = "The goal is to find the treasure hidden inside the temple.\n\n"
intro_text3 = "##HOW TO PLAY##\n\n"
intro_text4 = "In order to move around the temple simply type go and then a direction!\n"
intro_text5 = "EXAMPLE: go east\n\n"
intro_text6 = "EXAMPLE: look bookcase\n"
intro_text7 = "To start the game, simply type: start"
separator = "[---------------------------------------------<***>---------------------------------------------]\n"
cseparator = "[---------------------------------------------<***>---------------------------------------------]\n"
center_intro1 = intro_text1.center(125)
center_intro2 = intro_text2.center(125)
center_intro3 = intro_text3.center(125)
center_intro4 = intro_text4.center(125)
center_intro5 = intro_text5.center(125)
center_intro6 = intro_text6.center(125)
center_intro7 = intro_text7.center(125)
center_separator = cseparator.center(125)

## OPENING TEXT
opening = (
    "[---------------------------------------------<***>---------------------------------------------]\n"
    "The rain is poring down. \n\n"
    "The path you've been following for the past four hours seems to end abruptly \na few feet ahead of you. "
    "Tall pines surround you and you take a minute to look take in the scenery.\n\n"
    "It is then you notice a carved stone pillar, hidden by foliage and moss, breaching the soil ten feet to your left.\n"
    "After inspecting the pillar, you notice another one and five more of them further down the slope.\n\n"
    "Following the pillars leads you to a clearing and that's when you see it.\n"
    "The temple complex looms before you, ancient and forgotten.\n\n"
    "After a while you find a entrance and enter a large hall...\n\n"
    "[---------------------------------------------<***>---------------------------------------------]\n"
)

## DESCRIPTIONS
library_desc = (
    "[---------------------------------------------<***>---------------------------------------------]\n"
    "In front of you is a vast circular room, most of its walls crumbling, with rain seeping in\n"
    "through large holes in the ceiling. Scattered along the deteriorating walls are old,\n"
    "moldy books, neglected remnants of knowledge. At the center of the room, a large stone slab\n"
    "lays askew, surrounded by various rusting tools losing their metallic sheen. Along the\n"
    "periphery, a few statues stand, their features worn away, their faces forgotten by time.\n"
    "[---------------------------------------------<***>---------------------------------------------]\n"
)
grandhall_desc = (
    "[---------------------------------------------<***>---------------------------------------------]\n"
    "In front of you is a large rectangular room, its furthest face covered in vines and foliage.\n"
    "On either side of you are rows of statues, each depicting a forgotten deity, weathered by time.\n\n"
    "To your east is a crumpled doorway that leads into another room, the same to your west.\n"
    "On the furthest wall in the room, there is a large stone door, carved like a face—a humanoid face,"
    "cold and emotionless.\n\nIn its forehead, there is an empty cavity.\n"
    "[---------------------------------------------<***>---------------------------------------------]\n"
)
observatory_desc = (
    "[---------------------------------------------<***>---------------------------------------------]\n"
    "You step into chamber with a vast domed ceiling.\n"
    "Moonlight glimmers in through a hole at the center of the roof, casting a soft glow over the interior.\n\n"
    "The sounds of the forest pour in, bouncing off the sturdy stone walls and creating strange echoes.\n"
    "At the center of the room lies a massive brass structure, almost swallowed \nby a tangle of lush vegetation"
    "and blooming flowers, its shimmering gold surface barely visible in patches. \n\nEncircling the brass centerpiece, "
    "rows of tables stand in varying degrees of disrepair.\n\nIn the far eastern corner, "
    "a briny pool of water, somewhere below the surface there is a glow, illuminating the corner.\n\n"
    "[---------------------------------------------<***>---------------------------------------------]\n"
)

water_desc = (
    "[---------------------------------------------<***>---------------------------------------------]\n"
    "You walk over to the glowing pool of water in the corner of the room.\n\n"
    "Its hard to make out the depth of the water but on the bottom you can see something round that is glowing, a\n"
    "sphere. Glowing with a pulsing light blue light.\n\n"
    "You think you could reach it...\n\n"
    "[---------------------------------------------<***>---------------------------------------------]\n"
)

sanctum_desc = (
    "[---------------------------------------------<***>---------------------------------------------]\n"
    "Entering the inner sanctum you see a smaller room not touched in ages, the center of the circular room, is\n"
    "low lit and filled with still air.\n\nAs your eyes adjust to the darkness, you start to see glimmers of golden light all around\n"
    "the room.\n You've found the treasure!\n\n"
    "[---------------------------------------------<***>---------------------------------------------]\n"
)

end_screen = (
    "CONGRATULATIONS!\n"
    "Thanks for playing!"
)

# OPENING
print(intro_art)
print(center_separator)
print(center_intro1)
print(center_intro2)
print(center_intro3)
print(center_intro4)
print(center_intro5)
print(center_intro6)
print(center_intro7)
print(center_separator)

## INTRO MENU
while start == 0:
    user_menu_input = input(">").lower()
    if user_menu_input == "start":
        start = 1
        print(opening)
        print("You are currently in " + player_pos)
    if user_menu_input not in ["start", "exit"]:
        print("Sorry, I don't understand that command.")
    if user_menu_input == "exit":
        break


## GAME
while start == 1:
    user_input = input("\n\nWhat would you like to do?\n\n>").lower()

    ## HELP SYSTEM
    if user_input == "help":
        print(help_list)
        print("Here is a list of options you can do.\nFor example, you can type 'go east' to move in that direction.\n")

    ## LOOK-SYSTEM
    if user_input == "look" and player_pos == rooms[0]:
        print(library_desc)
    if user_input == "look" and player_pos == rooms[1]:
        print(grandhall_desc)
    if user_input == "look" and player_pos == rooms[2]:
        print(observatory_desc)
    if user_input == "look" and player_pos == rooms[3]:
        print(sanctum_desc)
    if user_input == "look water" and player_pos == rooms[2]:
        print(water_desc)
    if user_input == "go water" and player_pos == rooms[2]:
        print(water_desc)

    ## INTERACTION-SYSTEM
    if user_input in ["take ball", "take sphere", "take orb"] and player_pos == rooms[2]:
        key1 = 1
        print("You take the glowing sphere.\n")
    if key1 == 1:
        if user_input in ["use key", "use ball", "use sphere", "use door"] and player_pos == rooms[1]:
            print(
                "You put the sphere into the indent on the large stone door.\nThe door slowly slides open, you may enter...")

    ## MOVEMENT-SYSTEM
    ## East
    if user_input == "go east" or "e":
        if player_pos == rooms[0]:
            player_pos = rooms[1]
            print("You move east to", player_pos)
        elif player_pos == rooms[1]:
            player_pos = rooms[2]
            print("You move east to", player_pos)
        else:
            print("You cannot move further east.\n")

    ## West
    if user_input == "go west" or "w":
        if player_pos == rooms[2]:
            player_pos = rooms[1]
            print("You move west to", player_pos)
        elif player_pos == rooms[1]:
            player_pos = rooms[0]
            print("You move west to", player_pos)
        else:
            print("You cannot move further west.\n")

    ## North
    if user_input == "go north":
        if player_pos == rooms[0]:
            print("You cannot move north")
        elif player_pos == rooms[1] and key1 == 0:
            print("You need to something to open the door to your north with.")
        elif player_pos == rooms[1] and key1 == 1:
            player_pos = rooms[3]
            print("You move north to", player_pos)

        elif player_pos == rooms[2]:
            print("You cannot move north")
        # else:
        # print("You cannot move north")
    ## South
    if user_input == "go south":
        print("You cannot go south")

    ## EXIT
    if user_input == "exit":
        print("Exiting program.")
        break

    ## UNKNOWN COMMANDS
    if user_input not in ["go north", "go east", "go south", "go west", "look water", "help", "take", "look",
                          "take ball", "take sphere", "take orb", "use orb", "use ball", "use sphere", "go water"]:
        print("Sorry, I don't understand that command.")
    if key1 != 1 and user_input in ["take ball", "take sphere", "take orb", "use orb", "use ball", "use sphere"]:
        print("Sorry, I don't understand that command.")

    ## VICTORY CONDITION
    if player_pos == rooms[3] and key1 == 1:
        print(sanctum_desc)
        print(end_screen)
        break



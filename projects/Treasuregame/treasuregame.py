treasure_box = r"""
,---------------------------------------.---------.
|                                       |         |
|    ,-----------------------------.    |    .    |
|    |                             |    |    |    |
|    |    ,-------------------.    |    |    |    |
|    |    |                   |    |    |    |    |
|    |    `----     ,----     |    |    |    |    |
|    |              | X       |    |    |    |    |
|    |    ,---------"---------:    |    `----'    |
|    |    |                   |    |              |
|    `----:    ,---------.    |    `---------.    |
|         |    |         |    |              |    |
|    .    |    |    .    |    |     ---------'    |
|    |    |    |    |    |    |                   |
:----'    |    |    |    |    |    ,--------------:
|         |    |    |    |    |    |              |
|    .    |    `----'    |    |    |     ----.    |
|    |    |              |    |    |         |    |
|    `----"---------     |    |    `---------'    |
|                        |    |                   |
`------------------------'    `-------------------' """

print(treasure_box)
print("Hey Player Welcome to Treasure World! Have Some fun Here ")
print("Find Treasure By Following the below Guidelines ")

choice_1 = input("Which Side of the World Do Want to wander? Right or Left ").lower()

if choice_1 == "left":
    choice_2 = input(
        "You came to lake do you want to wait or do you want to swim? Type Swim to swim or type wait to wait\n ").lower().upper()

    if choice_2 == "wait":  # game will continue
        choice_3 = input(
            "Which Door Do You Want to choose ? Type Yellow for Yellow or Type Blue for Blue or Type Green for Green ").lower().upper()

        if choice_3 == "yellow" or "Yellow or YELLOW":
            print("You Found The Treasure , You WON!")
        else:
            print("The Game Is Over")
    else:
        print("You were attacked while swimming, Game Over")
else:
    print("You Fell into hole, Your Game is Over")



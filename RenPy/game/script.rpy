# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Mario", image="Mario")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image bg marioland = "marioland.jpg"

    scene bg marioland

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show mario happy
    # These display lines of dialogue.
    "Mario" "James senpai ur so kewl!"
    show mario dab
    "Mario" "I wish I was as cool as you!"
    show mario question
    "Bam!!" with vpunch
    show mario

    menu:
        "Beat him":
            "Mario" "Ouch Senpai that hurt"
            jump neutralend
        "Pat him":
            "Mario" "Thanks Senpai"
            jump goodend

        "Kill him":
            "Mario" "Nani!"
            jump badend

label badend:
    "Mario" "OH nos"
label neutralend:
    "Mario" "How could you senpai"
label goodend:
    "Mario" "You're the best senpai"




    # This ends the game.

    return

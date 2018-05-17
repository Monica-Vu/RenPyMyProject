# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Mario", image="Mario")
define me = Character("Me", color="#f47a42")


# The game starts here.
screen map():
     tag map
     zorder 1
     modal False

     text "This is a map"

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
    e "James senpai ur so kewl!"
    show mario dab
    e "I wish I was as cool as you!"
    show mario punch
    "Bam!!" with vpunch
    show mario

    me "I'm gonna get you back for that"
    menu:
        "Beat him":
            show mario hurt
            e "Ouch Senpai that hurt"
            jump neutralend
        "Pat him":
            e "Thanks Senpai"
            jump goodend

        "Kill him":
            show mario hurt
            "Mario" "Nani!"
            jump badend


label badend:
    e "OH nos"
    return
label neutralend:
    e "How could you senpai"
    return
label goodend:
    e "You're the best senpai"
    return




    # This ends the game.

    return

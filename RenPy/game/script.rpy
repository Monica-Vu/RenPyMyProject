# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Mario", image="Mario")
define me = Character("Me", color="#f47a42")
define peach = Character("Peach", image="Peach")
define bowserjr = Character("Bowserjr", image = "bowser")


# The game starts here.
screen example_imagemap:
    imagemap:
        auto "worldmap_%s.jpg"

        hotspot (850, 400, 400, 400) clicked Return("center")
        hotspot (150, 500, 300, 300) clicked Return("bowserjr")
        hotspot (1700, 20, 200, 300) clicked Return("peach")
        hotspot (790, 20, 200, 200) clicked Return("boo")

label peach:
    image bg peachbackground = "peachbackground.jpg"
    show bg peachbackground
    show peach
    peach "Oh hi there!"

label bowserjr:
    image bg space = "spacebg.jpg"
    show bg space
    show bowserjr

    bowserjr "Heee haaaww!"
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image bg marioland = "marioland.jpg"
    show bg marioland

    call screen example_imagemap

    $ result = _return

    if result == "center":
    elif result == "bowserjr":
        jump bowserjr
    elif result == "peach":
        jump peach
    elif result == "boo":

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    $ mario_rel = 0

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
            $ mario_rel -= 1
            jump neutralend
        "Pat him":
            e "Thanks Senpai"
            python:
                mario_rel += 1
            jump goodend

        "Kill him":
            show mario hurt
            e "Nani!"
            python:
                mario_rel -= 2
            jump badend


label finalend:
    me "End of story. Mario relationship  [mario_rel:.1]"
    return

label badend:
    e "OH nos"
    jump finalend
label neutralend:
    e "How could you senpai"
    jump finalend
label goodend:
    e "You're the best senpai"
    jump finalend




    # This ends the game.

    return

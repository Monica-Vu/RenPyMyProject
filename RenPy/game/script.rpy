#Characters
define e = Character("Mario", image="Mario")
define me = Character("Me", color="#f47a42")
define peach = Character("Peach", image="Peach")
define bowserjr = Character("Bowserjr", image = "bowser")

#Backgrounds
image bg marioland = "marioland.jpg"

# The game starts here.

init python:
    STAT_MAX = 100
    charisma = 5
    intel = 5
    strength = 5
    motivation = 5
    creativity = 5
    marioRel = 0
    peachVisited = 0

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    jump map
    return


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

label map:
    hide screen display_stats
    call screen example_imagemap
    $ result = _return
    show screen display_stats

    if result == "bowserjr":
        jump bowserjr
    elif result == "peach":
        jump peach
    elif result == "center":
        jump start

label mario:
    show bg marioland
    $ mario_rel = 0

    show mario happy
    # These display lines of dialogue.
    e "James senpai ur so kewl! [stats]"
    jump map

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
            hide bg mario
            jump neutralend
        "Pat him":
            e "Thanks Senpai"
            python:
                mario_rel += 1
            hide bg mario
            jump goodend

        "Kill him":
            show mario hurt
            e "Nani!"
            python:
                mario_rel -= 2

            hide bg mario
            jump badend




label finalend:
    me "End of story. Mario relationship  [mario_rel]"
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

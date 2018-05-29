# The script of the game goes in this file.
$ from screens.rpy import stats

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Mario", image="Mario")
define me = Character("Me", color="#f47a42")
define peach = Character("Peach", image="Peach")
define bowserjr = Character("Bowserjr", image = "bowser")

# The game starts here.

init python:
    STAT_MAX = 100
    charisma = 0
    intelligence = 10
    strength = 20

screen display_stats(name=True, bar=True, value=True, max=True):
    #   Tag menu removes everything with same tag
    #   Parsed as a name, not an expression. This specifies a tag associated with this screen. Showing a screen replaces other screens with the same tag. This can be used to ensure that only one screen of a menu is shown at a time, in the same context.

    frame:
        yalign 0.0
        xalign 0.5

        vbox:
            yalign 0.0
            xalign 0.5
            label "Statistics" xalign 0.5

            $ number_of_stats = 3
            grid 3 number_of_stats:
                xalign 0.5
                yalign 0.5
                spacing 5

                label "Charisma"
                bar value charisma range STAT_MAX xmaximum 150 xalign 0.0
                label ("%d/%d" % (charisma, STAT_MAX)) xalign 1.0

                label "intelligence"
                bar value intelligence range STAT_MAX xmaximum 150 xalign 0.0
                label ("%d/%d" % (intelligence, STAT_MAX)) xalign 1.0

                label "strength"
                bar value strength range STAT_MAX xmaximum 150 xalign 0.0
                label ("%d/%d" % (strength, STAT_MAX)) xalign 1.0


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
    peach "Oh hi there! [stats]"

    hide bg peachbackground
    hide peach
    jump map

label bowserjr:
    python:

        stats = "First"
    image bg space = "spacebg.jpg"
    show bg space
    show bowserjr

    bowserjr "Heee haaaww!"

    hide bg space
    hide bowserjr
    jump map
label map:
    call screen example_imagemap
    $ result = _return
    if result == "bowserjr":
        jump bowserjr
    elif result == "peach":
        jump peach
    elif result == "center":
        jump start
label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    image bg marioland = "marioland.jpg"
    show bg marioland
    show display_stats





    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    $ mario_rel = 0

    show mario happy
    # These display lines of dialogue.
    e "James senpai ur so kewl! "
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

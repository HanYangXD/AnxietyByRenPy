# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define salter = Character("Saber")
define mc = Character(_("Me"), color="#c8c8ff")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show salter

    # These display lines of dialogue.

    "You have anxiety disorder, and you found out that you had created your own imaginary friend."

    "So choose wisely to protect yourself from something bad. Let the story begin"

    "Tip: Choose the choices that hit your deepest and darkest fear."

    "ACT 1 ~ Lunch time"

    salter "What are you doing now?"

    menu:
        "I am..."

        "Playing phone.":
            jump playWhat

        "Eating my lunch.":

            jump eatWhat

        "doing nothing.":

            jump whyNothing

label playWhat:

    salter "What are you playing?"
    
    mc "Why are you concerning me?"

    return

label eatWhat:

    salter "What are you eating?"
    
    mc "Why are you concerning me?"

    return

label whyNothing:

    salter "Why are you doing nothing?"

    mc "Why are you concerning me?"


    # This ends the game.

    return

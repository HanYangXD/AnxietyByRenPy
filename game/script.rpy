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

    salter "Because it is lunch time, and you are not eating but instead you are playing phone."

    mc "Sure."

    salter "Do you know staring at a phone consistently will make your eyes constraint and dry eyes?"

    salter "Not just that, according to some research, there are reports showing that texting or looking on mobile phones is harmful for eyes for a long period of time."

    salter "Sometimes they may cause irritability and aggressiveness, especially among children and teenagers."    
    
    mc "K"

    salter "WHICH MEANS YOU WILL HAVE CANCER IN NO TIMEEEE."

    "You started to fear being harmful" #change colour? add sound? idk decide later

    jump A1Q2
    

label eatWhat:

    salter "What are you eating?"
    
    mc "Why are you concerning me?"

    salter "Anyway, why are you eating while talking to me? Do you know it will make you indigestion, "

    salter "and makes your body can’t absorb nutrients, WHICH WILL MAKE YOU-"

    salter "DIEEEEEEEEEEEEEEEEEEEEEEEE"

    salter "Also, why aren’t you eating with other humans and with me?"

    salter "at this rate, you will get LONELY FOREVERRRRRRRRR"

    "You started to being lonely" #change colour? add sound? idk decide later

    jump A1Q2 
    

label whyNothing:

    salter "Why are you doing nothing?"

    mc "Why are you concerning me?"

    salter "If you are not doing anything, this means you are not productive!"

    mc "So?" #added myself

    salter "Go read some book or at least do something!"

    mc "But I am not feeling to anythin-" #removed 'g' from anything

    salter "If we are not contributing to society then we are the so called..."

    salter "SOCIETY PARASITE!"

    mc "Uh huh. So?"

    salter "The society-body will go to the society-doctor for medication to kill their society-parasites then we will-"

    salter "DIEEEEEEEEEEEEEEEEEEEEEEEEE."    

    "You started to fear being a bad person" #change colour? add sound? idk decide later

    jump A1Q2

label A1Q2:
    mc "..."

    mc "You know what, I should check Facebook now."

    






    # This ends the game.

    return

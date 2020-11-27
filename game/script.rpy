# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ai = Character("AI") #ai = anxiety
define mc = Character(_("Me"), color="#c8c8ff") #mc = Main Character
define goingparty = False
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

    ai "What are you doing now?"

    menu:
        "I am..."

        "Playing phone.":
            jump playWhat

        "Eating my lunch.":
            jump eatWhat

        "doing nothing.":
            jump whyNothing

label playWhat:

    ai "What are you playing?"
    
    mc "Why are you concerning me?"

    ai "Because it is lunch time, and you are not eating but instead you are playing phone."

    mc "Sure."

    ai "Do you know staring at a phone consistently will make your eyes constraint and dry eyes?"

    ai "Not just that, according to some research, there are reports showing that texting or looking on mobile phones is harmful for eyes for a long period of time."

    ai "Sometimes they may cause irritability and aggressiveness, especially among children and teenagers."    
    
    mc "K"

    ai "WHICH MEANS YOU WILL HAVE CANCER IN NO TIMEEEE."

    "You started to fear being harmful" #change colour? add sound? idk decide later

    jump A1Q2
    

label eatWhat:

    ai "What are you eating?"
    
    mc "Why are you concerning me?"

    ai "Anyway, why are you eating while talking to me? Do you know it will make you indigestion, "

    ai "and makes your body can’t absorb nutrients, WHICH WILL MAKE YOU-"

    ai "DIEEEEEEEEEEEEEEEEEEEEEEEE"

    ai "Also, why aren’t you eating with other humans and with me?"

    ai "at this rate, you will get LONELY FOREVERRRRRRRRR"

    "You started to being lonely" #change colour? add sound? idk decide later

    jump A1Q2 
    

label whyNothing:

    ai "Why are you doing nothing?"

    mc "Why are you concerning me?"

    ai "If you are not doing anything, this means you are not productive!"

    mc "So?" #added myself

    ai "Go read some book or at least do something!"

    mc "But I am not feeling to anythin-" #removed 'g' from anything

    ai "If we are not contributing to society then we are the so called..."

    ai "SOCIETY PARASITE!"

    mc "Uh huh. So?"

    ai "The society-body will go to the society-doctor for medication to kill their society-parasites then we will-"

    ai "DIEEEEEEEEEEEEEEEEEEEEEEEEE."    

    "You started to fear being a bad person" #change colour? add sound? idk decide later

    jump A1Q2

label A1Q2:
    mc "..."

    mc "You know what, I should check Facebook now."

    ai "Please Nooooooooooooooooooo" #changed noooooooooo

    mc "Huh? Amanda is hosting a party this weekend." #changed abit

    ai "Doesn't that weirdo throw a party every weekend?"

    ai "What inner void are they trying to fill? They must be deeply messed up inside."

    mc "Wait, I got an invitation too." #added wait

    ai "Well then, What's your decision?"

    menu:
        "I am..."

        "Going":
            jump goParty
        "Not going":
            jump noParty

label goParty:
    ai "If you go you might encounter danger!"

    ai "For example there will be drugs inside the drinks."

    ai "When you are overdosed with drugs you will get nausea, drowsy, agitation, hallucination, unconsciousness and even worse you will..." #added you will

    mc "Could you sto-" #removed p

    ai "DIEEEEEEEEEEEEEEEE"

    "You started to fear being harmful" #wait what? fear of getting harm is it?

    mc "Okay fine!"

    ai "Huh?"

    mc "I will say no, just stop bothering me or I will uninstall you!" #changed popping up to bothering, can we actually change bothering to kacau?
    $goingparty=False
    jump A1Q3

label noParty:
    ai "Why not? If you don’t go you will be lonely forever!" #added why not

    ai "Researchers have found that loneliness is just as lethal as smoking 15 cigarettes per day. Lonely people are 50 percent more likely to die prematurely than those with healthy social relationships"

    "You started to fear being lonely"

    mc "Okay fine!"

    ai "Huh?"

    mc "I will say yes, just stop bothering me or I will uninstall you!" #changed popping up to bothering, can we actually change bothering to kacau?
    $goingparty=True
    jump A1Q3

label A1Q3:
    ai "But I just-"

    mc "Ughhhh, I need to make me calm and less anxiety." #changed

    mc "I will just have a look on Twitter." #changed

    "You launched Twitter" #changed

    menu:
        "Hmmm what should I check?"

        "News":
            jump lookNews

        "Looking at cat drinking milk":
            jump catDrinkMilk

label lookNews:
    mc "Oh, look at the news today!"

    ai "Yeah, it's so horrible nowadays. I feel like the world is burning and has no hope for us to live any longer anymore"

    ai "I don't know why are we here... just to suffer"

    ai "Or you're still being alive for?" #this can remove cuz ^ sentence covered liao xd

    ai "Why not retweet that? :D" #i think the expression can change gua? use sprite

    "You started to fear being harmful" #why harmful? isnt this... fear of being social parasite

    
    jump stopPhone

label catDrinkMilk:
    mc "Awww, the cat is drinking milk."

    mc "How adorable! Let's retweet this."

    "You tapped retweet."

    ai "ARE YOU SERIOUS?!" #changed !? to ?!

    ai "CAT CAN’T DIGEST MILK AND WE’RE TERRIBLE PERSON FOR ENJOYING ANIMAL ABUSE"

    "You started to feat being bad person"

    jump stopPhone

label stopPhone:
    mc "Alright, I should stop looking at my phone now."

    ai "Great! You should've did that earlier and let your mind rela-"

    "Received notification from Instagram" #dududung notification sound

    mc "Hey! I got notification from Instagram, let's check it out"

    "You launched Instagram"

#    menu:
#        ai "Wow, last week's party looks kinda nice." #changed from mc to ai
#
#        "Yea, it looks nice":
#            jump niceParty
#
#        "Nope, it doesn't seems nice to me":
#            jump notNiceParty
    
    # Here got error so i temp change 
    if goingparty: 
        jump niceparty

label niceParty:    
    mc "Everyone in the party looks so happy. Free from worry, and free from anxiety."

    mc "Maybe I shouldn't reject them after all."

label notNiceParty:
    mc "But it looks way too crowded for my anxiety"

    mc "Maybe I shouldn't say yes after all."



# Dummy variables (Need to verify at Act 2)
default jumpFromRoof = False
#testing commit

# Variables that only needed in Act 3
default count = 0
default talkFearHarmed = False
default talkFearAlone = False
default talkFearBad = False

# Act 3
# play sound "Bell rang.mp3" #Play bell rings

label startAct3:
    mc "..." #Sign sound insert
    mc "What is the moral of this story?"
    mc "What did we even learn? I was being stupid, my “friends” were using me. I almost die there."
    if jumpFromRoof:
        ai "Don’t do dumb stuff like... jumping from 3 levels building!"
    else:
        ai "Not to die…?"

    ai "But at least. We survived!"
    ai "Despite everything we went through."
    
    # Yes, no matter what user choose result will be same xd
    menu: 
        "You seems oddly calm":
            mc "You seem pretty calm considering we went through a near-death experience."
        "Why are you so calm!?":
            mc "Why are you so calm? We almost die there if I am not rational enough!"
        "...":
            mc "..."

    ai "Well at least it makes everything else less scary compared to others. This got me to think of…"
    ai "If me fighting you sucks, because it doesn’t protect you..."
    mc "But me fighting you also sucks, it just makes you more panic..." 
    ai "Then maybe..."
    mc "Maybe we don’t have to argue?"
    mc "Don’t need to…"
    ai "Don’t need to…"

    mc "Hey…"
    mc "I am sorry for not listening to you."
    
    ai "Nah, I am the one who should be sorry. I am just googling around the internet to keep you safe with facts. But not realizing it, whether they are helpful to you or not."
    ai "Then when I found something that may threaten you, I will just.."
    ai "DANGER DANGER DANGER!" # Shake the sprite
    ai "But I don’t want to just be an imagery friend. I want to be your friend."
    ai "So human… Would you like to continue to be my friend?"
    mc "I... will try..."

    mc "Okay, healthy relationship with emotions. Relationships need communication. So, let’s communicate."
    mc "The next five minutes are going to sound cheesy but let’s just fake it till we make it."
    ai "So human… how are you feeling?"

    jump startConvo

label startConvo:

    while count < 3:
        
        menu:
            "What should I talka bout?"
            
            "I feared to be harmed" if talkFearHarmed == False:
                $ count += 1
                $ talkFearHarmed = True
                jump fearHarmed
            
            "I feared to be lonely" if talkFearAlone == False:
                $ count += 1
                $ talkFearAlone = True
                jump fearAlone
            
            "I feared to be bad person" if talkFearBad == False:
                $ talkFearBad = True
                $ count += 1
                jump fearBad
            
            "Thank you...":
                $ count += 3
                jump finshFearTalk
                

        label fearHarmed:
            mc "Fear Harm route"
            jump startConvo
        
        label fearAlone:
            mc "Fear Alone route"
            jump startConvo

        label fearBad:
            mc "Fear Bad route"
            jump startConvo

            
label finshFearTalk:
    mc "Thank you I am done talking"




    # This ends the game.

    return

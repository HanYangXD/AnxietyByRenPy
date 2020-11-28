# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ai = Character("AI") #ai = anxiety
define mc = Character(_("Me"), color="#c8c8ff") #mc = Main Character
define amanda = Character("Amanda") #amanda AKA party hoster weirdo
define g1 = Character("Guy 1") #change name later
define g2 = Character("Guy 2") #change name later


define goingparty = False
define lookednews = False

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
    $lookNews=True
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
    else:
        jump notNiceParty

label niceParty:    
    mc "Everyone in the party looks so happy. Free from worry, and free from anxiety."

    mc "Maybe I shouldn't reject them after all."

    jump afterPartyThought

label notNiceParty:
    mc "But it looks way too crowded for my anxiety"

    mc "Maybe I shouldn't say yes after all."

    jump afterPartyThought

label afterPartyThought:
    mc "SHUT"
    mc "THE"
    mc "FUDGE"
    mc "UP"

    ai "Wha-"

    mc "I will just AGREE to them."
    mc "I DON'T CARE anything anymore."
    mc "You're NOT in my control!" #changed !
    mc "Now excuse me, I will need to go to my class now."

    ai "No!"
    ai "Wait!"

    "You choose to ignore the anxiety and walk away" #idk the ai anxiety is what character so i write like this first
    #play walk away sound effect

    ai "But..."

    jump startAct2

label startAct2:
    if lookednews:
        jump A2news
    else:
        jump A2cat

label A2news:
    amanda "Did you see the horrible news?"
    g1 "Yeah it's sooooo bad."
    mc "h-Hey..."
    amanda "Goshh, I hate the news. It's sensationalism and clickbait."
    mc "n-Nice party... eh...?"
    g2 "True, but they're just following incentives. The real problem is those who clicked on it."
    g1 "Who would retween that rerrible news and make others feel bad?"
    amanda "Ughh, I know right?"
    jump A2continue

label A2cat:
    amanda "Like I was saying, the Meme Industrial Complex is exploiting the cats."
    mc "h-Hey..."
    g1 "Please explain in detail Amanda" #added amanda
    mc "n-Nice party... eh...?"
    g2 "Well, yesterday I saw someone retweeted a GIF of a cat drinking milk."
    #g2 "but the person remove the tweet moments later, thinking that nobody would ever notice him doing it"
    g1 "Wait what?? Cat can't digest that! who would retween GIF that is abusing animal like that?" #changed to g1 talking
    amanda "Ughh, I know right?"
    jump A2continue

label A2continue:
    ai "Oh no they all hate us now!"
    mc "Us...?"
    mc "..."

    ai "We're bringing down the mood of this party by being such a sad lump!"
    ai "We're killing the good vibes! We're commiting first degree-vibe-murder!"
    ai "Heyyy, we need to leave now" #change human to heyy

    mc "Could you just-"
    ai "You're ignoring danger! This is dangerous!"
    mc "How is this dange-"

    ai "You think that you took out the batteries from carbon monoxide detector and you will be safe?"
    ai "You won't even smell the poison. You'll get sleepy and then you will..." #added you will
    ai "DIEEEEEEEEEEEEEEEEEEEEEEEEEE"

    mc "Stop this..."

    ai "Let me warn you about different social dangers."
    ai "What if we're just fundamentally incapable of ever being loved, or loving another?"
    ai "What if something irreversibly broke inside of us a long time ago? Or never existed in us in the first place?"
    ai "WE'RE BROKEN! SO BROKEN SO BROKEN SO SO BROKEN"

    mc "FAACKK"
    mc "FACKKKING FACK-FACKITY FACKKKKKK" #srsly meh later gg how

    "You started to fear being bad"
    "You started to fear being harmful" 
    "You started to fear being unhealthy" #why need 3

    ai "Don't worry! I will always be by your side! Anxiety Intelligence will never be obsolete!"
    mc "I had enough of this!"
    ai "Huh...?"
    mc "I can't appease you\nI can't ignore you\nI can't even run away from you!" #change delete to run away
    mc "No matter what I do. It seems like I cant get rid of you!" #changed abit

    ai "Well maybe you are NOT SUPPOSED TO GET RID OF ME!"
    ai "Do you know how I feel, human?"
    ai "I am trying to be your support, make sure you don't mess up anything."
    ai "But you keep seeing me as a bad AI" #change to bad guy maybe? or bad thought
    ai "So I try to make you realise more dangers could happen to US."
    ai "No matter how hard I try. You still think I am your enemy."
    ai "What am i doing WRONG?"
#    ai "AM I A JOKE TO YOU??" #should we? xd
    ai "I am stil new to this environment and I am using neural network model" #need to change?
    ai "Which means I need more time to learn to feel like a human."
    ai "All I want you to do is to be patient with me..." #added to do

    amanda "Hey!"
    mc "Huh?"
    amanda "Looks like you caught up a fight with yourself kiddo. What's wrong?" #added whats wrong
    mc "How would you know that? Was that obvious?"
    amanda "You were... erm... talking about carbon monoxide or something to yourself." #changed
    mc "Ah this is so messed up."

    "Amanda pats your shoulder"
    amanda "Hey, kiddo. Anxiety is super common."
    amanda "Listen, I know how it feels."
    amanda "We ALL do."

    amanda "So why not come to the rooftop and have something fun?"
    

    menu:
        ai "Human NO! Heyyyyy!!"

        "I think I will pass":
            jump passRoof
        "Let's go":
            jump goRoof


label passRoof:
    mc "I think-"
    mc "..."
    amanda "That is the spirit kiddo!"
    ai "NO HUMAN, DO NOT GOOOOOOOOOOOOOOOO!"
    jump startAct2point1

label goRoof:
    mc "You know what? Let's go now. Shall we?"
    amanda "That is the spirit kiddo!"
    ai "NO HUMAN, DO NOT GOOOOOOOOOOOOOOOO!"
    jump startAct2point1


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

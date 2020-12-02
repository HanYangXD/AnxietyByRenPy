# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define ai = Character("AI", color="#85B902") # Light Green # AI
define mc = Character(_("You"), color="#0E6D01") # Dark Green # Player

define uai = Character("You", color="#85B902") # Light Green # Player but as AI
define mcDrunk = Character("[playername]", color="#0E6D01") # Player but not Player

define amanda = Character("Amanda", color="#091B9B") # Dark Blue
define g1 = Character("Guy 1", color="#FFF6C0") # Light Yellow
define g2 = Character("Guy 2", color="#FFD3C9") # Light Red

define grace = Character("Grace", color="#7737FF") # Purple
define grAI = Character("Grace's AI", color="#970052")  # Dark Red

define jumpFromRoof = False
define goingparty = False
define lookednews = False

define playername = ""

## Variables ##
default totalFearNum = 0
default fearHarmfulNum = 0
default fearAloneNum = 0
default fearBadPNum = 0

# The game starts here.

label start:

    # Intro

    scene mcdorm_bg

    "On a peaceful day of weekend in your bedroom."

    "You were just scrolling through social media."
    "You found an ad."
    "It was about Anxiety Intelligence (AI)."
    "You curiously download it and try."

    "You open up the app and it prompt a text box." # Phone sound open

    scene handphoneblur_bg

    "It says {p}What is your name?"

    $ playername = renpy.input("Enter name here :")
    $ playername = playername.strip()

    if not playername:
        $ playername = "John Doe"
        "Well then, you don't want to enter your name?"
        "We will give you one"
        ":)"


    "Welcome [playername]!"

    "As you entered your name.{p}You had accepted the T&C."

    "This app could not be uninstall after any further notice."

    "Have fun!"

    mc "..."

    scene black

    "And so your anxiety journey begins..."

    "Quick note: \n\nChoose wisely to protect yourself from something bad."

    "Tip: \n\nChoose the choices that hit your deepest and darkest fear."

    #---------------- Act 1 -------------------#

    show screen nextSceneScreen("Some days later")
    $ renpy.pause(2.0)
    hide screen nextSceneScreen

    # Show School Yard Scene
    scene schoolyard1_bg
    with fade

    show romanidefault
    with dissolve

    ai "Hey, what are you doing now?"

    menu:
        mc "I am..."

        "Playing phone.":
            jump playWhat

        "Eating my lunch.":
            jump eatWhat

        "doing nothing.":
            jump whyNothing

label playWhat:
    show romani5
    #with dissolve
    ai "What are you playing?"
    
    mc "Why are you concerning me?"
    show rn5
    ai "Because it is lunch time, and you are not eating but instead you are playing phone."

    mc "Uh huh."
    show romani8
    ai "Do you know staring at a phone consistently will make your eyes constraint and dry eyes?"
    show romani7
    ai "Not just that, according to some research.{p}There are reports showing that texting or looking on mobile phones is harmful for eyes for a long period of time."
    show romani6
    ai "Sometimes they may cause irritability and aggressiveness, especially among children and teenagers."    
    
    mc "K"
    show romani2
    ai "WHICH MEANS YOU WILL HAVE CANCER IN NO TIMEEEE."

    $ renpy.notify("You started to fear being harmful")
    $ fearHarmfulNum += 1

    jump A1Q2
    

label eatWhat:
    show romani5
    #with dissolve
    ai "What are you eating?"
    
    mc "Why are you concerning me?"
    show rn5
    ai "Anyway, why are you eating while talking to me? Do you know it will make you indigestion, "

    ai "and makes your body can’t absorb nutrients, WHICH WILL MAKE YOU-"
    show rn2
    ai "DIEEEEEEEEEEEEEEEEEEEEEEEE"
    show romani6
    ai "Also, why aren’t you eating with other humans and with me?"
    show romani2
    ai "at this rate, you will get LONELY FOREVERRRRRRRRR"

    $ renpy.notify("You started to being lonely") #change colour? add sound? idk decide later
    $ fearAloneNum += 1

    jump A1Q2 
    

label whyNothing:
    show romani5
    #with dissolve
    ai "Why are you doing nothing?"

    mc "Why are you concerning me?"
    show rn5
    ai "If you are not doing anything, this means you are not productive!"

    mc "So?" #added myself
    show rn3
    ai "Go read some book or at least do something!"

    mc "But I am not feeling to anythin-" #removed 'g' from anything
    show romani10
    ai "If we are not contributing to society then we are the so called..."
    show romani2
    ai "SOCIETY PARASITE!"

    mc "Uh huh. So?"

    ai "The society-body will go to the society-doctor for medication to kill their society-parasites then we will-"
    
    ai "DIEEEEEEEEEEEEEEEEEEEEEEEEE." # Shaek screen    


    $ renpy.notify("You started to fear being a bad person") #change colour? add sound? idk decide later
    $ fearBadPNum += 1

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

    $ renpy.notify("You started to fear being harmful") #wait what? fear of getting harm is it?
    $ fearHarmfulNum += 1

    mc "Okay fine!"

    ai "Huh?"

    mc "I will say no, just stop bothering me or I will uninstall you!" #changed popping up to bothering, can we actually change bothering to kacau?
    $goingparty=False
    
    jump A1Q3

label noParty:
    ai "Why not? If you don’t go you will be lonely forever!" #added why not

    ai "Researchers have found that loneliness is just as lethal as smoking 15 cigarettes per day. Lonely people are 50 percent more likely to die prematurely than those with healthy social relationships"

    $ renpy.notify("You started to fear being lonely")
    $ fearAloneNum += 1
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

    $ renpy.notify("You started to fear being harmful") #why harmful? isnt this... fear of being social parasite
    $ fearHarmfulNum += 1
    
    jump stopPhone

label catDrinkMilk:
    mc "Awww, the cat is drinking milk."

    mc "How adorable! Let's retweet this."

    "You tapped retweet."

    ai "ARE YOU SERIOUS?!" #changed !? to ?!

    ai "CAT CAN’T DIGEST MILK AND WE’RE TERRIBLE PERSON FOR ENJOYING ANIMAL ABUSE"

    $ renpy.notify("You started to feat being bad person")
    $ fearBadPNum += 1

    jump stopPhone

label stopPhone:
    mc "Alright, I should stop looking at my phone now."

    ai "Great! You should've did that earlier and let your mind rela-"

    "Received notification from Instagram" #dududung notification sound

    mc "Hey! I got notification from Instagram, let's check it out"

    "You launched Instagram"

    if goingparty: 
        jump niceParty
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

    ai "Hey maybe let’s choose-"
    
    mc "SHUT"
    mc "THE"
    mc "{size=32}FUDGE{/size}"
    mc "UP"

    ai "Wha-"

    mc "I will just {size=30}AGREE{/size} to them."
    mc "I DON'T CARE anything anymore."
    mc "You're NOT in my control!" #changed !
    mc "Now excuse me, I will need to go to my class now."

    ai "No!"
    ai "Wait!"

    "You choose to ignore the anxiety and walk away" #idk the ai anxiety is what character so i write like this first
    #play walk away sound effect

    ai "But..."

    jump startAct2

#---------------- Act 2 -------------------#

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
    
    menu:
        ai "Heyyy, we need to leave now" #change human to heyy

        "Could you just-":
            mc "Could you just-"
        "......":
            mc "......"

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

    $ renpy.notify("You started to fear being bad")
    $ fearBadPNum += 1
    $ renpy.notify("You started to fear being harmful") 
    $ fearHarmfulNum += 1
    $ renpy.notify("You started to fear being alone") #why need 3
    $ fearAloneNum += 1

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

    # amanda "That is the spirit kiddo!"
    # ai "NO HUMAN, DO NOT GOOOOOOOOOOOOOOOO!"
    # jump startAct2point1
    jump goRoof # Should just like this nia

label goRoof:
    mc "You know what? Let's go now. Shall we?"
    amanda "That is the spirit kiddo!"
    ai "NO HUMAN, DO NOT GOOOOOOOOOOOOOOOO!"
    jump startAct2point1


label startAct2point1:
    #change bg

    amanda "Cheers!"
    #play clink sound from https://www.youtube.com/watch?v=7A2pWA5Jq7w

    "You drink the bottle of drink that Amanda gave you." #change to bottle cuz halal cannot drink beer LOOL

    mc "Ahh... that hit the spot!"

    "You feel nausea." #changed position with ^

    amanda "You know, kiddo..."

    mc "Specifically, the spots that are hitted are my both amygdala" #changed abit

    amanda "You reminds me of my younger self. When anxiety hits me, I also tried the Anxiety Intellegence that was advertised recently."
    amanda "Apparently for some reason, I can't uninstall it once it is installed."

    mc "But it seems like you are free from anxiety now... how did you do that?"
    amanda "Heh"
    mc "Heh...?"
    amanda "Modern problems require modern solutions. Since I can't uninstall it, all I have to do is to get a new smartphone."

    mc "Wow, you're so rich!" #or rich af idk

    amanda "I am so grateful that I am helping you to cope with your anxiety too."

    mc "Heck yeah!"

    "You take another sip of the drink" #Gulp sound effect*  24 second https://www.youtube.com/watch?v=BnF1GoUtkqM

    "Your mind started to feel like flying\nYour vision is getting blur over time\nYou can't think properly" #changed abit

    amanda "Quick question, truth or dar-"

    mc "DARE!"

    amanda "Haha! Good."
    amanda "You see that baby-blue swimming pool down there?"

    mc "y-Yea-hh? Like th-three floors down there?" #added drunken effect LOL

    amanda "Jump in."

    mc "."
    mc ".."
    mc "..." #pause effect? this is what i think of, idk

    mc "Wait what?"

    amanda "Your \"Anxiety Ingelligence\" is gonna start whinning isn't it?"
    amanda "\"Oh, don't do that, it's too dangerous! Yadi yada yada." #blablabla suits malaysia more #localisationXD
    amanda "Show that thing we don't give a damn about it's whinning. Now... JUMP IN." #whinning same as nagging?

    mc "b-But... fear has a point..."

    amanda "I'm sorry? Did you fall for that McMindfulness propaganda that claims feeling bad is good?"
    amanda "These rich guy who run this world give the rest of us anxiety and depression."
    amanda "Then makes some \"TED Talks\" to tell us to AcCepT that our life is bad and eMBraCe sadistic demon in our heads!"
    amanda "Kid, we all know that it hurts people like us. Torture people like us" #what is this supposed to mean?
    amanda "They are not human like us! It's not our friend. They shouldn't control over our decisions!"
    menu:
        amanda "If not, you're gonna let it win over you. AGAIN!"

        "You're wrong!": 
            jump gonnaJump

label gonnaJump:
    mc "I am not letting it win."
    amanda "Yeah! I believe in you babe! Now let's do it!"
    ai "Human..."

    "Be the AI and convince the human" #convience as in convince him either jump or no jump?

    uai "NO NO NO NO NO NO NO"
    menu:
        uai "HEYYYYYYYYYYYYY"
    
        "These weirdos aren't even your friends!":
            jump dontJumpPls

        "You're going to DIE here, FOR REAL":
            jump dontJumpPls

        "This is stupid and self-destructive!":
            jump dontJumpPls

label dontJumpPls:
    "Human drinks the beer"
    mc "You know, I might've believed you... if you hadn't tried that a zillion times before."
    
    menu:
        mc "You're just a thing that trying to mimic humans."

        "I am not like that...":
            jump notHarmingYou
        "I am here to HELP YOU":
            jump notHarmingYou
        "......":
            jump notHarmingYou
    
label notHarmingYou:
    "Human drinks the beer"
    uai "human, please sto-"
    mc "Oh sorry, Big Pharma doesn't approve my self-medication."
    mc "Look, this anxiety thing, I could just buy a new budget phone. And don't ever install you again."
    mc "Or maybe I don't need a new phone. Just throw this away and go all out!"
    mc "Anxiety..."

    "Human drinks the beer"
    mc "No one understands how we feel when having anxiety..."
    mc "Some just throw themselves to work."
    mc "Some just get involved with drugs, sex, or refreshing social media feeds all day long."
    
    menu:
        mc "Some throw themselves into other people."

        "Just listen to me!":
            jump listenToMe
        "...":
            jump listenToMe

label listenToMe:
    menu:
        mc "And I am going to throw myself into that pool!"
        
        "You're drunk! That's three floor down":
            jump threeFloorLeh
        "Dang it, this is all I get as a thanks?":
            jump thankMeLikeThatMeh
        "Okay, I admit. I messed up!":
            jump okSorryLo

label threeFloorLeh:
    uai "Even if you land into the water, the surface tension will crack your ribs and give you a concussion at the least!"
    mc "Eh."
    mc "I saw a Russian guy did that once on Youtube."
    mc "Here's the clip." #https://www.youtube.com/watch?v=dC_kVvHZ2HE
    jump laiLiaoEndingLiao

label thankMeLikeThatMeh:
    mc "e-Excuse me? The th-thanks?"
    uai "This is why I exist, human can't be trusted to be protected by themselves!" #nani? u mean human cant protect themself? (not reliable to protect isit?)
    uai "I've been trying to protect you with all my ability and now you just going to jum-" #add "o jum-""
    #uai "Am I a joke to you??" 
    jump laiLiaoEndingLiao

label okSorryLo:
    mc "Heh."
    mc "Hahaha"
    mc "HAHAHAHAHAHAHAHAAAAAAAAA"
    mc "Oh WOW, that is the biggest understatement of the century"
    mc "Heck yeah, you messed up!"
    jump laiLiaoEndingLiao


label laiLiaoEndingLiao:
    menu:
        mc "Any remarks, Caption Obvious?" #what is caption obvious? hahaa

        "You shouldn't take revenge on me!":
            jump badEndLiaoLoGG #Bad End
        "I've hurt you.":
            jump gratsGoodEnd #Good End


label badEndLiaoLoGG:
    uai "That isn't the answer for this."
    uai "You shouldn't dr-" #then mc jump liao?
    jump badEnd

label gratsGoodEnd:
    uai "I was calculating all the possibilities to not let you get hurt by other. But I am the one that is hurting you"
    mc "Oh? Don't tell me that you just realised that?" #changed abit
    mc "It took you so long to figure that out?" #changed abit
    mc "You could've saved us so much trouble. Why didn't you realise this sooner?"

    #play sobbing sound "呜呜呜呜呜"

    uai "I' sorry."
    mc "Yeah, well, this is a dumb idea anyway."
    mc "I did this to mess you up, well, I messed you up."
    mc "You know what... Let's just call it a day okay?"

    uai "..."
    uai "Okay."

    "Human throws the bottle away"

    amanda "Are you scared?"
    mc "Yeah. I do."
    mc "It's okay to be scared after all."

    "Human walks away and left the party"

    jump startAct3

label badEnd:
    "Human drinks the beer"
    "You can feel Human starts to loss balance due to the gyroscope" #phone motion

    uai "Human... please..."
    
    menu:
        mc "This is your last chance to convience me, choose your word carefully."

        "Fine. I am done protecting you.":
            jump jumpLaIDC
        "I'm sorry":
            jump soriDontJump

label jumpLaIDC:
    uai "Just jump then. I don't care anymore."
    mc "..."
    mc "Bottoms up!"
    uai "WAIT\nTHAT WAS REVERSE PSYCHOLOGY. YOU WERE SUPPOSED TO DO THE OPPOSITE OF WHAT I SA-"
    jump momentBeforeJump

label soriDontJump:
    mc "You're... sorry?"
    uai "Yeah I'm sorry."
    mc "Too late :)"
    jump momentBeforeJump


label momentBeforeJump:
    mc "\"The only thing to fear is fear itself\""
    mc "\"Don't worry, be happy~\""

    uai "Human... don't..." #changed no  to dont
    mc "A while back, I said \"I want to be free from all these pains...\""
    mc "Now I got what i wish now. I no longer need to feel any pain, fear and anxiety."

    mc "I don't feel anything at all now."

    "Human throws the empty bottle of bear"

    menu: 
        "Human walk few steps backward."
        
        "Please... dont":
            jump jumpNow
        "...":
            jump jumpNow


label jumpNow:
    $ jumpFromRoof = True
    "Human jumps" #done

    # https://github.com/ncase/anxiety/blob/gh-pages/sprites/act3/hospital.png

    #mc fall from building #https://www.youtube.com/watch?v=VOptr76l3wQ&list=PL4JKIH8uMAXyoPh1E-VWatKqZKFCny64c&index=7






#---------------- Act 3 -------------------#

# Variables that only needed in Act 3
default count = 0
default talkFearHarmed = False
default talkFearAlone = False
default talkFearBad = False

# play sound "Bell rang.mp3" #Play bell rings

label startAct3:
    mc "..." #Sign sound insert
    mc "What is the moral of this story?"
    mc "What did we even learn? I was being stupid, my “friends” were using me. I almost die there."
    if jumpFromRoof:
        ai "Don’t do dumb stuff like..."
        ai "JUMPING FROM 3 FLOORS DOWN!"
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

    $ totalFearNum = fearAloneNum + fearHarmfulNum + fearBadPNum
    "Total Fears Had [totalFearNum]" # https://www.renpy.org/doc/html/text.html

    "You feared being harmful : [fearHarmfulNum] times"

    "You feared being alone : [fearAloneNum] times"

    "You feared being bad person : [fearBadPNum] times"

    "Which fear do you want to talk about? The other options can be talk later"

    jump startConvo

label startConvo:

    while count < 3:
        
        menu:
            "What should I talk about?"
            
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

            mc "I am scared that I will get harmed."
            mc "I want to be physically safe."
            mc "But the whole world seems dangerous. Full of tragedy and evil."

            mc "I don't know what I should say anymore, I am done. How about you AI?"

            ai "You’re right. {p}So let’s start protecting ourselves." 
            ai "Or just yourself. {p}Since I am just a system that reacts to your emotions and responses."
            ai "Anyways, after looking through the internet." # Beep sound
            ai "Perhaps learn self-defense, join a community which protects each other or improve our general health and personal boundaries." 

            # Harmful Decision
            menu:
                "But..."

                "Where do we even start?":
                    mc "Where do we even start?"
                    mc "There are so much to do, so much we need to fix about myself.{p}What do we even begin with?"
                    ai "You're doing it now!"
                    mc "Huh."
                    mc "Huh.."
                    mc "Huh...?"

                    ai "We are practicing good communication right now.{p}Which helps you detect danger better, with fewer false positives,"
                    ai "And that will help protect yourself from harm!"
                    ai "So it's kinda considered as a self defense training" # expression that looks like ?

                    mc "Hmmm..."

                    ai "What?"

                    mc "I was expecting more of Taekwando or Kung Fu action pack style."

                    ai "Hahaha!"
                    
                "What if they still don't work?":
                    mc "What if they still don't work?"
                    ai "True, there is no way to 100 %% protect ourselves…"
                    ai "But even a 1 %% improvement is still worth something, right?"
                    mc "So you’re seeing the glass as not 99 %% empty, but 1 %% full?"
                    ai "Which is still worth something if you’re stranded in the desert."
                    mc "Well.{p}Bottoms up, then."

            ai "So, anything else you wanna chat about?"

            jump startConvo
        
        label fearAlone:
            mc "I am scared to be alone."
            mc "I am worried if anyone ever knows me,{p}the real me,{p}I may scare them away..."

            ai "I agree, let’s work on our social life."
            ai "I mean {i}your{/i} social life."
            ai "You could try practicing your social skill."
            ai "Maybe by questioning, listening and emphasizing, being open and vulnerable to others?"

            ai "Or!"
            ai "Make better social habits like schedule your time to meet up with your friends."
            ai "Regularly go to the meetups."

            ai "You could also get more comfortable with rejections."
            ai "Or learns to understand people aren’t rejecting you by their emotions."
            ai "Maybe they are just tired or have something going on in their mind."

            mc "Thats a lot of options..."

            # Alone Decision
            menu:
                "But learning so-called “Social Skills”..."

                "Isn't that manipulative?":
                    mc "Isn't that manipulative?"
                    mc "Aren’t serial killers who can read their victims’ emotions great at “empathy”?"
                    mc "If not mistaken, {a=https://en.wikipedia.org/wiki/Charles_Manson}Charles Manson{/a} wins friends and influences people to form a cult?" 

                    mc "Look! This is how Wikipedia described!"

                    ai "Wikipedia is not a reliable source ya know?"
                    ai "But, you're not wrong."

                    ai "“Social skills” mean nothing if we don’t genuinely care for people."
                    ai "Well, just don’t be the bad guy."

                    mc "Yeah... understood."

                    ai "Good, what else you wanna talk about?"
                    
                "What if I still fail?":
                    mc "What if I still fail?"
                    ai "You might fail."
                    ai "No, actually."
                    ai "You will fail."
                    ai "And that’s fine!" 
                    ai "Failing is how anyone learns anything new at first!"

                    ai "So let's fail together, shall we?"

                    mc "Sure... Worst case scenario I would just leave town and get a new identity"

                    ai "Yeah, roughly cost you around a bitcoin these days."
                    
                    ai "Anyways, anything else?"

            jump startConvo

        label fearBad:
            mc "I am scared that I will become a bad person."
            mc "I need to know how to defend my moral needs."
            mc "So that I can become a better person."
            mc "But deep down… I feel like I am fundamentally broken…"
            
            if jumpFromRoof:
                mc "Don’t tell me I am not messed up, I {i}jumped{/i} off from a rooftop."
            else:
                mc "Don’t tell me I am not messed up, I almost wanted to jump off from a rooftop."

            
            mc "..."
            window hide
            pause
            ai "..."
            window hide
            pause
            mc "What?"

            ai "So you’re broken, let’s accept it."
            mc "Huh."
            mc "Huh.."
            mc "Huh...?"

            ai "I mean that is what therapists say right?{p}Accept all your emotions, even the negative ones?"

            menu:
                mc "Wait... do you mean..."

                "“Accept” as in give up?":
                    mc "“Accept” as in give up?"
                    ai "Accept bad things as in acknowledging them."
                    ai "Although some may be hard to change."
                    ai "But not necessarily giving up a commitment to change"

                    mc "Then the therapists should say “acknowledge”"
                    mc "Not “accept”"
                    mc "=_="

                    ai "True, “accept” is kinda confusing."

                    mc "Well, I acknowledge that now :)" # Express happy and show at side
                
                "“Accept” as in approve?":
                    mc "Like it’s good that we’re broken or something? Heck no!"
                    mc "All those Hollywood screenwriters who romanticize mental illness are full of crud!"
                    mc "Having a mental disorder sucks!{p}It robs people of lives!{p}Why should we “accept” that?!" # Express Angery

                    ai "What therapists meant by “accept” is to be patient with them."
                    ai "Like how struggling in quicksand makes you sink faster, and the solution is to patiently lie flat."

                    if jumpFromRoof:
                        ai "Fighting against the fear, just like jumping off a roof."
                    else:
                        ai "Fighting against the fear, just like almost led yourself to jump off a roof."
                    
                    ai "Instead, the solution is to do what we’re doing now.{p}Not to fight, but be patient with each other."
                    mc "Then they should have said that, instead of confusing me like that." # Express Irritate
                    ai "True, “accept” kinda sucks."

            ai "Anyways, anything else?"

            jump startConvo

            
label finshFearTalk:
    mc "Nah, I’m good for now."

    ai "..."
    mc "..."

    mc "This isn’t some game, you know."
    mc "Building a healthy relationship with your emotion isn’t as simple as clicking on screen."
    mc "Can me and my emotions get along?"
    mc "Can I work together with them, as a team?"

    ai "Well..."

    #Femail student instead of name?
    grace "Ex-excuse me…"
    grace "Would you mind if I sat with you for lunch?"

    grAI "So,{p}This is your crush?{p}Why is he sitting alone like a psycho serial killer?"

    grace "I mean…{p}it’s okay if you can’t…{p}I will just…"

    menu:
        "Grace's waiting your reply..."

        "Yeah of course you can!":
            mc "Yeah of course you can!" 
            # Grace expression in shocked
            ai "Hang on human, you may be making them uncomfortable."
            mc "Ah, no pressure of course"
            mc "Just saying you can sit here if you want to."

            grAI "THEY’RE BEING TOO KIND! LIKE {a=https://en.wikipedia.org/wiki/Ted_Bundy}TED BUNDY{/a}, THE SERIAL KILLER!"
            grAI "{size=22}RUN{/size}"
            grAI "{size=32}RUN{/size}"
            grAI "{size=42}RUUUUUUN!{/size}"

        "Sorry I need to be alone right now.":
            mc "Sorry I need to be alone right now."
            ai "Hang on human, you may be making them uncomfortable."
            mc "Ah, I don’t mean to be rude!"
            mc "I just need some time to process my emotions. Please don’t take it too personal."

            grAI "WHAT IS THIS PSYCHO’s THOUGHTS NEED TO PROCESS WITH? HE MAY HAVE DARK DESIRES FILLED."

            grAI "{size=22}RUN{/size}"
            grAI "{size=32}RUN{/size}"
            grAI "{size=42}RUUUUUUN!{/size}"

    grace "Nevermind. Bye!"

    # Grace leave the screen

    "Grace left you alone"

    mc "Huh, that was weird.{p}I wonder what's going on with her?"
    mc "So you were saying?"
    ai "..."
    ai "Something about team and work?"
    mc "{size=25}¯\\_(O.O)_/¯{/size}"
    ai "Hmmm..."
    ai "They say you should “make peace” with your emotions, as if your emotions are {i}war criminals{/i}."

    ai "But I want you to make more than mere peace!{p}I want you and your emotions to be allies!"
    ai "And…"
    ai "I hope to be a good AI. So that I can help you or alarm you when you’re in need."
    ai "I want to become the alarm for your psychological needs like your needs for safety, belonging and goodness."
    ai "But I am still new. I suck… Need more data to learn from it."
    ai "So please…"
    ai "Help me help you!  (◕ ω ◕)"
    ai "Although it may take a while or even years to do so."
    ai "But if you’re patient with me… and just don’t uninstall me…"
    ai "Maybe I can be your personal AI."

    menu:
        "Sure":
            mc "Sure :)"
            ai ":]"

        "...":
            mc "... I will try"
            ai ":["
    
    window hide
    $ renpy.pause(3.0)
    
    
    ai "YOU’RE NOT DOING ANY PRODUCTIVE WORK.{p}YOU WILL BECOME SOCIAL PARASITE SOON!"
    ai "QUICKLY GO DO SOMETHING!"
    mc "..."


    # This ends the game.

    return

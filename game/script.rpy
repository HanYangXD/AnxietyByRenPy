﻿# The script of the game goes in this file.
init python:
    def callbackcontinue(ctc, **kwargs):
        if ctc == "end":
            renpy.sound.play("audio/pokemonctc.mp3",channel="sound")
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator = Character(name=None, callback=callbackcontinue)

define ai = Character("AI", color="#85B902", callback=callbackcontinue) # Light Green # AI
define mc = Character(_("You"), color="#0E6D01", callback=callbackcontinue) # Dark Green # Player

define uai = Character("You", color="#85B902", callback=callbackcontinue) # Light Green # Player but as AI
define mcDrunk = Character("[playername]", color="#0E6D01", callback=callbackcontinue) # Player but not Player

define amanda = Character("Amanda", color="#091B9B", callback=callbackcontinue) # Dark Blue
define g1 = Character("Guy 1", color="#FFF6C0", callback=callbackcontinue) # Light Yellow
define g2 = Character("Guy 2", color="#FFD3C9", callback=callbackcontinue) # Light Red

define grace = Character("Grace", color="#7737FF", callback=callbackcontinue) # Purple
define grAI = Character("Grace's AI", color="#970052", callback=callbackcontinue)  # Dark Red

define jumpFromRoof = False
define goingparty = False
define lookednews = False

define playername = "John Doe"

## Variables ##
default totalFearNum = 0
default fearHarmfulNum = 0
default fearAloneNum = 0
default fearBadPNum = 0

label splashscreen:
    scene mosaicSplash with fade
    with Pause(1)

    play sound "audio/oldtvstaticsound.wav"
    show text "{size=33}Not for {s}Made with{/s} Anxiety{/size}" with dissolve
    with Pause(2.5)

    hide text with dissolve
    scene black with fade
    with Pause(1)
    stop sound
    return


# The game starts here.

label start:

    # Intro
    stop music
    play music "audio/music/firstroom_bgm.wav" loop
    scene mcdorm_bg
    show screen locationNow("Dorm room") with dissolve

    narrator "On a peaceful day of weekend in your bedroom."

    narrator "You were just scrolling through social media."
    narrator "You found an ad."
    narrator "It was about Anxiety Intelligence (AI)."
    narrator "You curiously download it and try."

    narrator "You open up the app and it prompts a text box." # Phone sound open

    scene handphoneblur_bg

    narrator "It says {p}What is your name?"

    $ playername = renpy.input("Enter name here :")
    $ playername = playername.strip()

    if not playername:
        $ playername = "John Doe"
        narrator "Well then, you don't want to enter your name?"
        narrator "We will give you one"
        narrator ":)"


    narrator "Welcome [playername]!"

    narrator "As you entered your name.{p}You had accepted the T&C."

    narrator "This app could not be uninstalled after any further notice."

    narrator "Have fun!"

    mc  "..."
    hide screen locationNow with dissolve
    scene black

    narrator "And so your anxiety journey begins..."

    narrator "Quick note: \n\nChoose wisely to protect yourself from something bad."

    narrator "Tip: \n\nChoose the choices that hit your deepest and darkest fear."
    stop music

    #---------------- Act 1 -------------------#

    show screen nextSceneScreen("Some days later") with fade
    $ renpy.pause(2.0)
    hide screen nextSceneScreen

    # Show School Yard Scene
    play music "audio/music/act1_bgm.wav" loop
    scene schoolyard1_bg with fade
    show screen locationNow("School Yard") with dissolve

    show ai normal
    with dissolve

    ai "Hey, what are you doing now?"

    menu:
        mc "I am..."

        "Playing phone.":
            mc "Playing phone lo."
            jump playWhat

        "Eating my lunch.":
            mc "Eating lunch lo."
            jump eatWhat

        "Doing nothing.":
            mc "Nothing la."
            jump whyNothing

label playWhat:
    show ai serious
    #with dissolve
    ai "What are you playing?"
    
    mc "Why are you concerning me?"
    show ai serious neck
    ai "Because it is lunch time, and you are not eating but instead you are playing phone."

    mc "Uh huh."
    show ai serious
    ai "Do you know staring at a phone consistently will make your eyes constraint and dry eyes?"
    show ai serious
    ai "Not just that, according to some research.{p}There are reports showing that texting or looking on mobile phones is harmful for eyes for a long period of time."
    show ai worry
    ai "Sometimes they may cause irritability and aggressiveness, especially among children and teenagers."    
    
    mc "K"

    play sound "audio/shockai.wav"
    show ai shocked at x_shake with vpunch
    ai "WHICH MEANS YOU WILL HAVE CANCER IN NO TIMEEEE."

    $ renpy.notify("You started to fear being harmful")
    $ fearHarmfulNum += 1

    jump A1Q2
    

label eatWhat:
    show ai serious
    #with dissolve
    ai "What are you eating?"
    
    mc "Why are you concerning me?"
    show ai serious neck
    ai "Anyway, why are you eating while talking to me? Do you know it will make you indigestion, "

    ai "and makes your body can’t absorb nutrients, WHICH WILL MAKE YOU-"

    play sound "audio/shockai.wav"
    show ai shocked neck at x_shake with vpunch
    ai "DIEEEEEEEEEEEEEEEEEEEEEEEE"
    show ai worry
    ai "Also, why aren’t you eating with other humans and with me?"
    show ai shocked
    ai "at this rate, you will get LONELY FOREVERRRRRRRRR"

    play sound "audio/notifypopupsound.ogg"
    $ renpy.notify("You started to being lonely") 
    $ fearAloneNum += 1

    jump A1Q2 
    

label whyNothing:
    show ai serious
    #with dissolve
    ai "Why are you doing nothing?"

    mc "Why are you concerning me?"
    show ai serious neck
    ai "If you are not doing anything, this means you are not productive!"

    mc "So?" 
    show ai annoyed neck
    ai "Go read some book or at least do something!"

    mc "But I am not feeling to anythin-" 
    show ai notconfident
    ai "If we are not contributing to society then we are the so called..."
    
    play sound "audio/shockai.wav"
    show ai shocked at x_shake with vpunch
    ai "SOCIETY PARASITE!"

    mc "Uh huh. So?"

    ai "The society-body will go to the society-doctor for medication to kill their society-parasites then we will-"

    play sound "audio/shockai.wav"
    show ai shocked at x_shake with vpunch
    ai "DIEEEEEEEEEEEEEEEEEEEEEEEEE." 

    play sound "audio/notifypopupsound.ogg"
    $ renpy.notify("You started to fear being a bad person")
    $ fearBadPNum += 1

    jump A1Q2

label A1Q2:
    show ai normal
    mc "..."

    
    mc "You know what, I should check Facebook now."
    show screen fbPhone() with dissolve
    narrator "You launched Facebook"

    show ai shocked
    ai "Please Nooooooooooooooooooo"

    mc "Huh? Amanda is hosting a party this weekend." 
    show ai annoyed neck
    ai "Doesn't that weirdo throw a party every weekend?"
    show ai annoyed neck
    ai "What inner void are they trying to fill? They must be deeply messed up inside."

    mc "Wait, I got an invitation too." 
    show ai normal
    ai "Well then, What's your decision?"
    hide screen fbPhone with dissolve

    menu:
        "I am..."

        "Going":
            mc "Yea, I'm going."
            jump goParty
        "Not going":
            mc "Nah, I'm not going."
            jump noParty

label goParty:
    show ai shocked
    ai "If you go you might encounter danger!"
    show ai worry
    ai "For example there will be drugs inside the drinks."

    ai "When you are overdosed with drugs you will get nausea, drowsy, agitation, hallucination, unconsciousness and even worse you will..." #added you will

    mc "Could you sto-" 

    play sound "audio/shockai.wav"
    show ai shocked at x_shake with vpunch
    ai "DIEEEEEEEEEEEEEEEE"

    play sound "audio/notifypopupsound.ogg"
    $ renpy.notify("You started to fear being harmful") 
    $ fearHarmfulNum += 1

    mc "Okay fine!"
    show ai serious
    ai "Huh?"

    mc "I will say no, just stop bothering me or I will uninstall you!" 
    $goingparty=False
    
    jump A1Q3

label noParty:
    show ai serious
    ai "Why not? If you don’t go you will be lonely forever!" 
    ai "Based on this {a=https://www.inc.com/amy-morin/americas-loneliness-epidemic-is-more-lethal-than-smoking-heres-what-you-can-do-to-combat-isolation.html}article{/a}."
    show ai shocked at x_shake
    ai "Researchers have found that loneliness is just as lethal as smoking 15 cigarettes per day.{p}Lonely people are 50 percent more likely to die prematurely than those with healthy social relationships"

    play sound "audio/notifypopupsound.ogg"
    $ renpy.notify("You started to fear being lonely")
    $ fearAloneNum += 1
    mc "Okay fine!"
    show ai serious
    ai "Huh?"

    mc "I will say yes, just stop bothering me or I will uninstall you!"
    $goingparty=True

    jump A1Q3

label A1Q3:
    show ai smile
    ai "But you can't :)"

    mc "Ughhhh, I need to calm myself and feel less anxious." 

    mc "I will just have a look on Twitter." # Twitter

    show screen twitterPhone() with dissolve
    narrator "You launched Twitter" 
    

    menu:
        "Hmmm what should I check?"

        "News":
            jump lookNews

        "Looking at cat drinking milk":
            jump catDrinkMilk

label lookNews:
    $ lookednews = True
    mc "Oh, look at the news today!"
    show ai notconfident neck
    ai "Yeah, it's so horrible nowadays. I feel like the world is burning and has no hope for us to live any longer anymore"

    ai "I don't know why are we here... just to suffer"
    show ai serious neck
    ai "Or why you're still being alive for?" 
    
    show ai happy laugh
    ai "Why not retweet that? :D" #i think the expression can change gua? use sprite

    play sound "audio/notifypopupsound.ogg"
    $ renpy.notify("You started to fear being harmful") # Sound effect maybe
    $ fearHarmfulNum += 1
    
    jump stopPhone

label catDrinkMilk:
    mc "Awww, the cat is drinking milk."

    mc "It's so cute! Let's retweet this."

    narrator "You tapped retweet."
    show ai shocked at x_shake
    ai "ARE YOU SERIOUS?!" 

    ai "CAT CAN’T DIGEST MILK AND WE’RE TERRIBLE PERSON FOR ENJOYING ANIMAL ABUSE"

    play sound "audio/notifypopupsound.ogg"
    $ renpy.notify("You started to fear being bad person")
    $ fearBadPNum += 1

    jump stopPhone

label stopPhone:
    hide screen twitterPhone with dissolve
    mc "Alright, I should stop looking at my phone now."
    show ai happy laugh
    ai "Great! You should've did that earlier and let your mind rela-"

    play sound "audio/notificationsound.ogg"
    narrator "Received notification from Instagram" 

    mc "Eh? I got notification from Instagram, let's check it out"
    
    show screen instaPhone() with dissolve
    narrator "You launched Instagram"
    
    
    mc "Wow, this party looks kinda nice."

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
    show ai happy laugh neck
    ai "Hey maybe let’s choose-"
    
    mc "SHUT"
    mc "THE"
    mc "{size=32}FUDGE{/size}" 
    mc "UP"
    hide screen instaPhone with dissolve
    show ai shocked
    ai "Wha-"

    mc "I will just {size=30}AGREE{/size} to them."
    mc "I DON'T CARE anything anymore."
    mc "I'm NOT in your control!"
    mc "Now excuse me, I am going to my class now."
    show ai shocked neck
    ai "No!"
    ai "Wait!"

    play sound "audio/walkingsound.ogg"
    narrator "You choose to ignore the anxiety and walk away." 
    
    show ai notconfident
    ai "But..."

    hide ai
    hide screen locationNow
    stop music

    jump startAct2

#---------------- Act 2 -------------------#

label startAct2:
    
    scene black with fade
    show screen nextSceneScreen("At the party") with fade
    $ renpy.pause(2.0)
    hide screen nextSceneScreen

    play music "audio/partybeats.ogg" loop
    scene party_bg with fade
    show screen locationNow("Party Room") with dissolve

    if lookednews:
        jump A2news
    else:
        jump A2cat

label A2news:
    show amanda normal at left with dissolve
    amanda "Did you see the horrible news?"
    show g1 normal at right with dissolve
    g1 "Yeah it's sooooo bad."
    mc "h-Hey..."
    amanda "Goshh, I hate the news. It's sensationalism and clickbait."
    mc "n-Nice party... eh...?"
    show g2 normal with dissolve
    g2 "True, but they're just following incentives. The real problem is those who clicked on it."
    show g1 shout
    hide g2 with dissolve
    g1 "Who would retweet that terrible news and make others feel bad?"
    show amanda hmph
    amanda "Ughh, I know right?"
    jump A2continue

label A2cat:
    show amanda normal at left with dissolve
    amanda "Like I was saying, the Meme Industrial Complex is exploiting the cats."
    mc "h-Hey..."
    show g1 normal at right with dissolve
    g1 "Please explain in detail Amanda" 
    mc "n-Nice party... eh...?"
    show g2 normal with dissolve
    g2 "Well, yesterday I saw someone retweeted a GIF of a cat drinking milk."
    hide g2 with dissolve
    show g1 surprised
    g1 "Wait what?? Cat can't digest that! who would retween GIF that is abusing animal like that?" 
    show amanda hmph
    amanda "Ughh, I know right?"
    jump A2continue

label A2continue:
    hide amanda 
    hide g1
    hide g2

    hide screen locationNow
    # Show white scene (Like looking at phone)

    $ renpy.music.set_volume(0.3, .5, channel="music")
    scene whitebgphone with dissolve
    show screen locationNow("Phone Screen") with dissolve

    show ai shocked neck 
    ai "Oh no they all hate us now!"
    mc "Us...?"
    mc "..."
    show ai notconfident
    ai "We're bringing down the mood of this party by being such a sad lump!"
    ai "We're killing the good vibes! We're commiting first degree-vibe-murder!"
    show ai serious neck
    menu:
        
        ai "Heyyy, we need to leave now" #change human to heyy

        "Could you just-":
            mc "Could you just-" #i think we dont have to repeat our selection is it?
        "......":
            mc "......" #and this

    show ai shocked
    ai "You're ignoring danger! This is dangerous!"
    mc "How is this dange-"
    show ai worry
    ai "You think that you took out the batteries from carbon monoxide detector and you will be safe?"
    ai "You won't even smell the poison. You'll get sleepy and then you will..." #added you will
    
    play sound "audio/shockai.wav"
    show ai shocked at x_shake with vpunch
    ai "DIEEEEEEEEEEEEEEEEEEEEEEEEEE"

    mc "Stop this..."
    show ai normal
    ai "Let me warn you about different social dangers."
    show ai worry
    ai "What if we're just fundamentally incapable of ever being loved, or loving another?"
    ai "What if something irreversibly broke inside of us a long time ago? Or never existed in us in the first place?"
    show ai shocked # Chg to schocked cuz shout ma
    ai "WE'RE BROKEN! SO BROKEN SO BROKEN SO-"

    play sound "audio/shockai.wav"
    show ai shocked at x_shake with vpunch
    ai "{size=35}BROKEN{/size}"

    mc "AAAAAAAAAHHHHHHHHHHH" #changed from faq
    #mc "FACKKKING FACK-FACKITY FACKKKKKK" #srsly meh later gg how

    # Need to show 3 notify at the same time (Fix later)
    play sound "audio/notifypopupsound.ogg"
    $ renpy.notify("You started to fear being bad")
    $ fearBadPNum += 1
    $ renpy.notify("You started to fear being harmful") 
    $ fearHarmfulNum += 1
    $ renpy.notify("You started to fear being alone")
    $ fearAloneNum += 1

    show ai smile
    ai "Don't worry! I will always be by your side! Anxiety Intelligence will never be obsolete!"
    mc "I've had enough of this!" #edited I had enough of this!
    show ai worry neck
    ai "Huh...?"
    mc "I can't appease you\nI can't ignore you\nI can't even run away from you!" #change delete to run away
    mc "No matter what I do. It seems like I cant get rid of you!" #changed abit

    show ai serious
    ai "Well maybe you are NOT SUPPOSED TO GET RID OF ME!"
    ai "Do you know how I feel, [playername]?"
    show ai serious neck
    ai "I am trying to be your support, make sure you don't mess up anything."
    show ai notconfident neck
    ai "But you keep seeing me as a bad AI" #change to bad guy maybe? or bad thought
    ai "So I try to make you realise more dangers could happen to US."
    ai "No matter how hard I try. You still think I am your enemy."
    show ai notconfident
    ai "What did i do WRONG?" # edited What am i doing WRONG?
#    ai "AM I A JOKE TO YOU??" #should we? xd
    ai "I am still new to this environment and I am using neural network model" #need to change? #edited stil to still
    ai "Which means I need more time to learn to feel like a human."
    show ai serious
    ai "All I want you to do is to be patient with me..." #added to do

    hide ai with dissolve
    hide screen locationNow

    # Play music back
    # play music "audio/partybeats.ogg" loop
    $ renpy.music.set_volume(1.0, .5, channel="music")
    scene party_bg with dissolve 
    show screen locationNow("Party Room") with dissolve

    show amanda normal with dissolve#fade in

    amanda "Hey!"
    mc "Huh?"
    show amanda smile
    amanda "Looks like you caught up a fight with yourself kiddo. What's wrong?" #added whats wrong
    mc "How would you know that? Was that obvious?"
    show amanda ho
    amanda "You were... erm... talking about carbon monoxide or something to yourself." #changed
    mc "Ah this is so messed up."
    show amanda hmph
    narrator "Amanda pats your shoulder"
    show amanda normal
    amanda "Hey, kiddo. Anxiety is super common."
    amanda "Listen, I know how it feels."
    show amanda hmph
    amanda "We ALL do."
    show amanda smile
    amanda "So why not come to the rooftop and have something fun?"
    

    menu:
        ai "[playername] NO! Heyyyyy!!"

        "I think I will pass":
            mc "I think-"
            mc "..."
        "Let's go":
            jump goRoof

label goRoof:
    mc "You know what? Let's go now. Shall we?"
    show amanda smile
    amanda "That is the spirit kiddo!"
    ai "NO [playername], DO NOT GOOOOOOOOOOOOOOOO!"
    hide amanda with dissolve
    hide screen locationNow
    stop music

    # Walk to rooftop
    scene followtorooftop
    show screen locationNow("Pathway") with dissolve
    play sound "audio/walkingsound.ogg"
    narrator "You decided to join Amanda and her friends to the rooftop."
    jump startAct2point1


label startAct2point1:
    
    hide screen locationNow
    # At rooftop
    play music "audio/music/rooftopbgm.wav" loop
    scene rooftop
    show screen locationNow("Rooftop") with dissolve
    show amanda smile with dissolve
    
    amanda "Cheers!"
    play sound "audio/clinkglass.wav"
    
    narrator "You drink the glass of drink that Amanda gave you."

    mc "Ahh... that hit the spot!" 

    scene blurrooftop1 blurred
    narrator "You feel nausea." # Blurr vision

    show amanda normal
    amanda "You know, kiddo..."

    mc "Specifically, the spots that are hitted are my both amygdala" 
    show amanda smile
    amanda "You reminds me of my younger self. When anxiety hits me, I also tried the Anxiety Intellegence that was advertised recently."
    show amanda hmph
    amanda "Apparently for some reason, I can't uninstall it once it is installed."

    mc "But it seems like you are free from anxiety now... how did you do that?"
    show amanda smile
    amanda "Heh"
    mc "Heh...?"
    amanda "Modern problems require modern solutions. Since I can't uninstall it, all I have to do is to get a new smartphone."

    mc "Wow, you're so rich!" 

    amanda "I am so grateful that I am helping you to cope with your anxiety too."

    mc "Heck yeah!"

    play voice "audio/glupsip.ogg"
    narrator "You take another sip of the drink" 
    scene blurrooftop2 blurred
    narrator "Your mind started to feel like flying{p}Your vision is getting blurry over time{p}You can't think properly" # Blur vision #edited blur -> blurry
    show amanda normal
    amanda "Quick question, truth or dar-"

    mc "DARE!"
    show amanda smile
    amanda "Haha! Good."
    amanda "You see that baby-blue swimming pool down there?"

    mc "y-Yea-hh? Like th-three floors down there?"

    show amanda normal
    amanda "Jump in."

    mc "."
    mc ".."
    mc "..."

    mc "Wait what?"

    show amanda smile
    amanda "Your \"Anxiety Ingelligence\" is gonna start whinning isn't it?" #edited whinning -> whining 
    show amanda hmph
    amanda "\"Oh, don't do that, it's too dangerous! Blablablabla." 
    show amanda normal
    amanda "Show that thing we don't give a damn about its whining. Now... JUMP IN." #edited whinning -> whining #edited it's -> its

    mc "b-But... fear has a point..."

    amanda "I'm sorry? Did you fall for that McMindfulness propaganda that claims feeling bad is good?"
    amanda "These rich guy who run this world give the rest of us anxiety and depression."
    show amanda normal at round_shake
    amanda "Then makes some \"TED Talks\" to tell us to AcCepT that our life is bad and eMBraCe sadistic demon in our heads!"
    show amanda hmph
    amanda "Kid, we all know that it hurts people like us. Torture people like us" 
    show amanda shout
    amanda "They are not human like us! It's not our friend. They shouldn't control over our decisions!"
    menu:
        amanda "If not, you're gonna let it win over you. AGAIN!"

        "You're wrong!": 
            jump gonnaJump

label gonnaJump:
    mc "I am not letting it win."
    show amanda smile
    amanda "Yeah! I believe in you babe! Now let's do it!"
    hide amanda with dissolve

    stop music
    hide screen locationNow
    scene whitebgphone with fade
    show screen locationNow("Phone Screen") with dissolve
    show ai notconfident with dissolve
    ai "[playername]..."

    hide ai with dissolve
    narrator "Now YOU will become AI and convince [playername]" #convience as in convince him either jump or no jump?
    narrator "Choose wisely."
    narrator ";)"
    hide screen locationNow

    play music "audio/music/rooftopbgm.wav" loop
    scene rooftop with fade
    show screen locationNow("Rooftop") with dissolve

    uai "NO NO NO NO NO NO NO"
    menu:
        uai "HEYYYYYYYYYYYYY"
    
        "These weirdos aren't even your friends!":
            uai "These weirdos aren't even your friends!"

        "You're going to DIE here, FOR REAL":
            uai "You're going to DIE here, FOR REAL"

        "This is stupid and self-destructive!":
            uai "This is stupid and self-destructive!"
        
    jump dontJumpPls

label dontJumpPls:

    play sound "audio/gulpbeer1.ogg"
    narrator "[playername] drinks the beer"

    show mcdrunk drunk
    mcDrunk "You know, I might've believed you... if you hadn't tried that a zillion times before."
    
    menu:
        mcDrunk "You're just a thing that trying to mimic humans."

        "I am not like that...":
            uai "I am not like that..."
        "I am here to HELP YOU":
            uai "I am here to HELP YOU"
        "......":
            uai "......"

    jump notHarmingYou
    
label notHarmingYou:

    play sound "audio/gulpbeer1.ogg"
    narrator "[playername] drinks the beer"

    uai "[playername], please sto-"
    show mcdrunk drunk
    mcDrunk "Oh sorry, Big Pharma doesn't approve my self-medication."
    mcDrunk "Look, this anxiety thing, I could just buy a new budget phone.{p}And don't ever install you again.{p}Stupid T&C."
    
    show mcdrunk shout
    mcDrunk "Or maybe I don't need a new phone. Just throw this away and go all out!"

    show mcdrunk drunk
    mcDrunk "This anxiety..."

    play sound "audio/gulpbeer2.ogg"
    narrator "[playername] drinks the beer"

    mcDrunk "No one understands how we feel when having anxiety..."
    mcDrunk "Some just throw themselves to work."
    mcDrunk "Some just get involved with drugs, sex, or refreshing social media feeds all day long."
    
    menu:
        mcDrunk "Some throw themselves into other people."

        "Just listen to me!":
            uai "Just listen to me!"
            
        "...":
            uai "..."
    jump listenToMe

label listenToMe:
    show mcdrunk shout
    mcDrunk "And I am going to throw myself into that pool!"
    
    menu:
        mcDrunk "You can't stop me!"
        "You're drunk! That's three floor down":
            uai "You're drunk! That's three floor down"
            jump threeFloorLeh
        "Dang it, this is all I get as a thanks?":
            uai "Dang it, this is all I get as a thanks?"
            jump thankMeLikeThatMeh
        "Okay, I admit. I messed up!":
            uai "Okay, I admit. I messed up!"
            jump okSorryLo

label threeFloorLeh:
    uai "Even if you land into the water, the surface tension will crack your ribs and give you a concussion at the least!"
    show mcdrunk normal
    mcDrunk "Eh."
    show mcdrunk drunk
    mcDrunk "I saw a Russian guy did that once on Youtube."
    mcDrunk "Here's the {a=https://www.youtube.com/watch?v=dC_kVvHZ2HE}clip{/a}." #https://www.youtube.com/watch?v=dC_kVvHZ2HE
    jump laiLiaoEndingLiao

label thankMeLikeThatMeh:
    show mcdrunk shout
    mcDrunk "e-Excuse me? The th-thanks?"
    uai "This is why I exist, human can't be trusted to be protected by themselves!" #nani? u mean human cant protect themself? (not reliable to protect isit?)
    uai "I've been trying to protect you with all my ability and now you just going to jum-" #add "o jum-""
    #uai "Am I a joke to you??" 
    jump laiLiaoEndingLiao

label okSorryLo:
    show mcdrunk normal
    mcDrunk "Heh."
    mcDrunk "Hahaha"
    show mcdrunk shout
    mcDrunk "HAHAHAHAHAHAHAHAAAAAAAAA"
    mcDrunk "Oh WOW, that is the biggest understatement of the century"
    show mcdrunk drunk
    mcDrunk "Heck yeah, you messed up!"
    jump laiLiaoEndingLiao


label laiLiaoEndingLiao:
    menu:
        mcDrunk "Any remarks, Caption Obvious?" #what is caption obvious? hahaa

        "You shouldn't take revenge on me!":
            uai "You shouldn't take revenge on me!"
            jump badEndLiaoLoGG #Bad End
        "I've hurt you.":
            uai "I've hurt you."
            jump gratsGoodEnd #Good End


label badEndLiaoLoGG:
    uai "That isn't the answer for this."
    uai "You shouldn't dr-"
    jump badEnd

label gratsGoodEnd:
    uai "I was calculating all the possibilities to not let you get hurt by other. But I am the one that is hurting you"
    show mcdrunk shout
    mcDrunk "Oh? Don't tell me that you just realised that?" #changed abit
    mcDrunk "It took you so long to figure that out?" #changed abit
    mcDrunk "You could've saved us so much trouble. Why didn't you realise this sooner?"

    #play sobbing sound "呜呜呜呜呜"

    uai "I'm sorry."
    show mcdrunk normal
    mcDrunk "Yeah, well, this is a dumb idea anyway."
    mcDrunk "I did this to mess you up, well, I messed you up."
    mcDrunk "You know what... Let's just call it a day okay?"

    uai "..."
    uai "Okay."

    play sound "audio/beerdropsound.ogg"
    narrator "[playername] throws the bottle away"
    show mcdrunk normal at slightleft
    show amanda shout at slightright
    amanda "Are you scared?"
    show mcdrunk shout 
    mcDrunk "Yeah. I do."
    mcDrunk "It's okay to be scared after all."

    narrator "[playername] walks away and left the party"
    hide amanda with dissolve
    hide mcdrunk with dissolve
    stop music

    jump startAct3

label badEnd:

    play sound "audio/gulpbeer2.ogg"
    narrator "[playername] drinks the beer"

    show mcdrunk drunk at x_shake
    narrator "You can feel [playername] starts to loss balance due to the gyroscope" #phone motion

    uai "[playername]... please..."
    show mcdrunk drunk
    menu:
        
        mcDrunk "This is your last chance to convince me, choose your word carefully."

        "Fine. I am done protecting you.":
            uai "Fine. I am done protecting you."
            jump jumpLaIDC
        "I'm sorry":
            uai "I'm sorry"
            jump soriDontJump

label jumpLaIDC:
    uai "Just jump then. I don't care anymore."
    show mcdrunk drunk
    mcDrunk "..."

    scene toolate 
    show screen locationNow("???")
    show mcdrunk scary
    mcDrunk "Bottoms up!"
    uai "WAIT\nTHAT WAS REVERSE PSYCHOLOGY. YOU WERE SUPPOSED TO DO THE OPPOSITE OF WHAT I SA-"

    scene rooftop
    show screen locationNow("Rooftop")

    jump momentBeforeJump

label soriDontJump:
    show mcdrunk drunk
    mcDrunk "You're... sorry?"
    uai "Yeah I'm sorry."

    scene toolate 
    show screen locationNow("???")
    show mcdrunk scary
    mcDrunk "Too late :)"

    scene rooftop
    show screen locationNow("Rooftop")

    jump momentBeforeJump


label momentBeforeJump:
    show mcdrunk drunk
    mcDrunk "\"The only thing to fear is fear itself\""
    mcDrunk "\"Don't worry, be happy~\""

    uai "[playername]... don't..." 

    
    mcDrunk "A while back, I said \"I want to be free from all these pains...\""
    mcDrunk "Now I got what i wish now. I no longer need to feel any pain, fear and anxiety."
    show mcdrunk normal
    mcDrunk "I don't feel anything at all now."

    play sound "audio/beerdropsound.ogg"
    narrator "[playername] throws the empty bottle of beer"
    show mcdrunk scary
    menu: 
        
        "[playername] walk few steps backward."
        
        "Please... dont":
            uai "Please... dont"
        "...":
            uai "..."
    
    jump jumpNow


label jumpNow:


    $ jumpFromRoof = True
    narrator "[playername] jumps"
    play sound "audio/jumpdown.wav"
    stop music
    hide screen locationNow
    hide mcdrunk with dissolve

    scene black
    
    narrator "...{p}"

    play sound "audio/ambulance.wav"
    scene ambulance_bg with fade
    show screen locationNow("Ambulance") with dissolve

    narrator "[playername] hurt badly"
    narrator "..."
    stop sound

    hide screen locationNow
    # Hospital scene
    scene hospitalbed_bg with fade
    show screen locationNow("Hospital")with dissolve
    mcDrunk "..."
    show ai worry neck
    ai "..."
    hide ai with dissolve
    hide screen locationNow
    jump startAct3

#---------------- Act 3 -------------------#

# Variables that only needed in Act 3
default count = 0
default talkFearHarmed = False
default talkFearAlone = False
default talkFearBad = False

# play sound "Bell rang.mp3" #Play bell rings

label startAct3:

    scene black with dissolve
    show screen nextSceneScreen("Few days later...") 
    $ renpy.pause(2.0)
    hide screen nextSceneScreen

    play music "audio/music/act3_bgm.wav" loop
    scene schoolyard2_bg with fade
    show screen locationNow("School Yard") with dissolve

    if jumpFromRoof:
        play sound "audio/wheelchairsound.ogg"
    else:
        play sound "audio/walkingsound.ogg"


    mc "..."
    play sound "audio/signsound.wav"

    mc "What is the moral of this story?"
    mc "What did we even learn?{p}I was being stupid, my “friends” were using me. I almost die there."
    if jumpFromRoof:
        show ai annoyed neck
        ai "Don’t do dumb stuff like..."
        play sound "audio/shockai.wav"
        show ai shocked at x_shake with vpunch
        ai "JUMPING FROM 3 FLOORS DOWN!"
        show ai worry
        ai "..."
        ai "And now you end up with a wheelchair!"
        mc "Yeah..."
    else:
        ai "Not to die…?"

    ai "..."
    play sound "audio/yaysound.wav"
    show ai happy laugh
    ai "But at least. We survived!"
    show ai smile
    ai "Despite everything we went through."
    
    menu: 
        mc "Huh..."
        "You seems oddly calm":
            mc "You seem pretty calm considering we went through a near-death experience."
        "Why are you so calm!?":
            mc "Why are you so calm? We almost die there if I am not rational enough!"
        "...":
            mc "..."

    show ai worry neck
    ai "Well at least it makes everything else less scary compared to others. This got me to think of…"
    ai "If me fighting you sucks, because it doesn’t protect you..."
    mc "But me fighting you also sucks, it just makes you more panic..." 
    show ai notconfident
    ai "Then maybe..."
    mc "Maybe we don’t have to argue?"
    mc "Don’t need to…"
    show ai normal
    ai "Don’t need to…"

    mc "Hey…"
    mc "I am sorry for not listening to you."
    
    show ai smile
    ai "Nah, I am the one who should be sorry."
    ai "I am just googling around the internet to keep you safe with facts. But not realizing it, whether they are helpful to you or not."
    show ai notconfident
    ai "Then when I found something that may threaten you, I will just.."
    
    play sound "audio/shockai.wav"
    show ai shocked at x_shake with vpunch
    ai "DANGER DANGER DANGER!" # Shake the sprite 3 times maybe?

    show ai notconfident neck
    ai "But I don’t want to just be an imagery friend. I want to be your friend."
    show ai serious neck
    ai "So [playername]… Would you like to continue to be my friend?"
    mc "I... will try..."

    mc "Okay, healthy relationship with emotions.{p}Relationships need communication. So, let’s communicate!"
    show ai happy laugh
    mc "The next five minutes are going to sound cheesy but let’s just fake it till we make it."
    
    ai "So [playername]… how are you feeling?"

    hide ai with dissolve

    scene cherryblossom_bg with fade
    $ totalFearNum = fearAloneNum + fearHarmfulNum + fearBadPNum
    narrator "Total Fears Had [totalFearNum]" # https://www.renpy.org/doc/html/text.html

    narrator "You feared being harmful : [fearHarmfulNum] times"

    narrator "You feared being alone : [fearAloneNum] times"

    narrator "You feared being bad person : [fearBadPNum] times"

    narrator "Which fear do you want to talk about? The other options can be talk later"

    jump startConvo

label startConvo:

    while count < 3:
        hide ai with dissolve
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
            show ai happy laugh with dissolve
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
                    show ai smile
                    ai "You're doing it now!"
                    mc "Huh."
                    mc "Huh.."
                    mc "Huh...?"
                    show ai normal
                    ai "We are practicing good communication right now.{p}Which helps you detect danger better, with fewer false positives,"
                    ai "And that will help protect yourself from harm!"
                    show ai notconfident neck
                    ai "So it's kinda considered as a self defense training" # expression that looks like ?

                    mc "Hmmm..."
                    show ai normal
                    ai "What?"

                    mc "I was expecting more of Taekwando or Kung Fu action pack style."
                    show ai happy laugh
                    ai "Hahaha!"
                    
                "What if they still don't work?":
                    mc "What if they still don't work?"
                    show ai normal
                    ai "True, there is no way to 100 %% protect ourselves…"
                    show ai smile
                    ai "But even a 1 %% improvement is still worth something, right?"
                    mc "So you’re seeing the glass as not 99 %% empty, but 1 %% full?"
                    show ai notconfident neck
                    ai "Which is still worth something if you’re stranded in the desert."
                    mc "Well.{p}Bottoms up, then."
            
            show ai smile neck
            ai "So, anything else you wanna chat about?"

            jump startConvo
        
        label fearAlone:
            mc "I am scared to be alone."
            mc "I am worried if anyone ever knows me,{p}the real me,{p}I might scare them away..."
            show ai notconfident with dissolve
            ai "I agree, let’s work on our social life."
            show ai serious
            ai "I mean {i}your{/i} social life."
            ai "You could try practicing your social skill."
            show ai normal
            ai "Maybe by questioning, listening and emphasizing, being open and vulnerable to others?"
            show ai serious
            ai "Or!"
            show ai normal
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
                    show ai smile
                    ai "Wikipedia is not a reliable source ya know?"
                    show ai serious
                    ai "But, you're not wrong."

                    ai "“Social skills” mean nothing if we don’t genuinely care for people."
                    show ai normal
                    ai "Well, just don’t be the bad guy."

                    mc "Yeah... understood."
                    show ai smile
                    ai "Good, what else you wanna talk about?"
                    
                "What if I still fail?":
                    mc "What if I still fail?"
                    show ai serious
                    ai "You might fail."
                    ai "No, actually."
                    ai "You will fail."
                    show ai smile
                    ai "And that’s fine!"
                    show ai normal 
                    ai "Failing is how anyone learns anything new at first!"

                    ai "So let's fail together, shall we?"

                    mc "Sure... Worst case scenario I would just leave town and get a new identity"
                    show ai happy laugh
                    ai "Yeah, roughly cost you around a bitcoin these days."
                    
                    ai "Anyways, anything else?"
                    show ai normal
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
            show ai serious with dissolve
            ai "..."
            window hide
            pause
            mc "What?"

            ai "So you’re broken, let’s accept it."
            mc "Huh."
            mc "Huh.."
            mc "Huh...?"
            show ai notconfident neck
            ai "I mean that is what therapists say right?{p}Accept all your emotions, even the negative ones?"

            menu:
                mc "Wait... do you mean..."

                "“Accept” as in give up?":
                    mc "“Accept” as in give up?" #no need to say this line bah?
                    show ai serious
                    ai "Accept bad things as in acknowledging them."
                    ai "Although some may be hard to change."
                    show ai normal
                    ai "But not necessarily giving up a commitment to change"

                    mc "Then the therapists should say “acknowledge”"
                    mc "Not “accept”"
                    mc "=_="
                    show ai notconfident
                    ai "True, “accept” is kinda confusing."

                    mc "Well, I acknowledge that now :)" # Express happy and show at side
                
                "“Accept” as in approve?":
                    mc "Like it’s good that we’re broken or something? Heck no!"
                    mc "All those Hollywood screenwriters who romanticize mental illness are full of crud!"
                    mc "Having a mental disorder sucks!{p}It robs people of lives!{p}Why should we “accept” that?!" # Express Angery
                    show ai normal
                    ai "What therapists meant by “accept” is to be patient with them."
                    ai "Like how struggling in quicksand makes you sink faster, and the solution is to patiently lie flat."

                    if jumpFromRoof:
                        ai "Fighting against the fear, just like jumping off a roof."
                    else:
                        ai "Fighting against the fear, just like almost led yourself to jump off a roof."
                    show ai serious
                    ai "Instead, the solution is to do what we’re doing now.{p}Not to fight, but be patient with each other."
                    mc "Then they should have said that, instead of confusing me like that." # Express Irritate
                    show ai happy laugh
                    ai "True, “accept” kinda sucks."
            show ai normal
            ai "Anyways, anything else?"

            jump startConvo

            
label finshFearTalk:
    mc "Nah, I’m good for now."
    show ai normal
    ai "..."
    mc "..."

    mc "This isn’t some game, you know."
    mc "Building a healthy relationship with your emotion isn’t as simple as clicking on screen."
    mc "Can me and my emotions get along?"
    mc "Can I work together with them, as a team?"
    show ai notconfident neck
    ai "Well..."
    hide ai with dissolve
    
    grace "Ex-excuse me…"
    scene schoolyard2_bg with fade
    show grace scared with dissolve
    grace "Would you mind if I sat with you for lunch?"
    show grace scared at left with dissolve
    show graceai tsk at slightleft with dissolve 
    grAI "So,{p}This is your crush?{p}Why the heck is he sitting alone like a psycho serial killer?"
    show grace normal
    grace "I mean…{p}it’s okay if you can’t…{p}I will just…"

    menu:
        narrator "Grace's waiting your reply..."

        "Yeah of course you can!":
            mc "Yeah of course you can!" 
            show grace shocked
            show ai shocked at right with dissolve 
            ai "Hang on [playername], you may be making them uncomfortable."
            mc "Ah, no pressure of course"
            show graceai normal
            mc "Just saying you can sit here if you want to."
            show graceai tsk
            grAI "THEY’RE BEING TOO KIND! LIKE {a=https://en.wikipedia.org/wiki/Ted_Bundy}TED BUNDY{/a}, THE SERIAL KILLER!"
            show graceai shout
            grAI "{size=22}RUN{/size}"
            show graceai shout at x_shake
            grAI "{size=32}RUN{/size}"
            play sound "audio/shockai.wav"
            show graceai shout at x_shake with vpunch
            grAI "{size=42}RUUUUUUN!{/size}"

        "Sorry I need to be alone right now.":
            mc "Sorry I need to be alone right now."
            show ai shocked at right with dissolve
            ai "Hang on [playername], you may be making them uncomfortable."
            mc "Ah, I don’t mean to be rude!"
            mc "I just need some time to process my emotions. Please don’t take it too personal."
            show graceai tsk at x_shake
            grAI "WHAT IS THIS PSYCHO’s THOUGHTS NEED TO PROCESS WITH? HE MAY HAVE DARK DESIRES FILLED."
            show graceai shout
            grAI "{size=22}RUN{/size}"
            show graceai shout at x_shake
            grAI "{size=32}RUN{/size}"
            play sound "audio/shockai.wav"
            show graceai shout at x_shake with vpunch
            grAI "{size=42}RUUUUUUN!{/size}"

    show grace normal
    grace "Nevermind. Bye!"

    # Grace leave the screen

    narrator "Grace left you alone"
    hide grace with dissolve
    hide graceai with dissolve

    mc "Huh, that was weird.{p}I wonder what's going on with her?"
    mc "So you were saying?"
    show ai notconfident at middle with dissolve
    ai "..."
    show ai normal
    ai "Something about team and work?"
    mc "{size=25}¯\\_(O.O)_/¯{/size}"
    show ai serious
    ai "Hmmm..."
    ai "They say you should “make peace” with your emotions, as if your emotions are {i}war criminals{/i}."

    ai "But I want you to make more than mere peace!{p}I want you and your emotions to be allies!"
    ai "And…"
    show ai normal
    ai "I hope to be a good AI. So that I can help you or alarm you when you’re in need."
    show ai smile
    ai "I want to become the alarm for your psychological needs like your needs for safety, belonging and goodness."
    show ai notconfident neck
    ai "But I am still new. I suck… Need more data to learn from it."
    ai "So please…"
    show ai smile
    ai "Help me help you!  (OωO)"
    show ai notconfident
    ai "Although it may take a while or even years to do so."
    show ai happy laugh
    ai "But if you’re patient with me… and just don’t leave me…"
    show ai smile
    ai "Maybe I can be your personal AI."

    menu:
        "Sure":
            mc "Sure :)"
            show ai happy laugh
            ai ":]"

        "...":
            mc "... I will try"
            show ai notconfident neck
            ai ":["
    
    window hide
    $ renpy.pause(3.0)
    
    play sound "audio/shockai.wav"
    show ai shocked at x_shake with vpunch
    ai "YOU’RE NOT DOING ANY PRODUCTIVE WORK.{p}YOU WILL BECOME SOCIAL PARASITE SOON!"
    show ai shocked at x_shake
    ai "QUICKLY GO DO SOMETHING!"
    mc "..."

    hide ai with dissolve
    hide screen locationNow
    stop music

    jump endCredits

label endCredits:

    scene black with fade

    show text "The End" with dissolve
    $ renpy.pause(4.5)

    show text "Huge thanks to Nicky Case\nWithout him, the story cannot be made." with dissolve
    $ renpy.pause(2.5)

    show text "Also Renpy for creating this game.\nFor more information can see in About." with dissolve
    $ renpy.pause(3.5)

    show text "And last but not least." with dissolve
    $ renpy.pause(2.5)

    show text "You, [playername]." with dissolve
    $ renpy.pause(1.5)

    show text "If you ever need help, please look in our Help in main menu or {a=https://www.aia.com.my/en/what-matters/seetheotherside/mental-health-helpline-resources.html}here{/a}" with dissolve
    $ renpy.pause(4)

    show text "Good Bye!" with dissolve
    $ renpy.pause(1)

    hide text with dissolve
    $ renpy.pause(1)

    jump fakeMainMenu

label fakeMainMenu:

    play sound "audio/lastjumpscare.wav"
    scene catFaceScare with fade
    
    show text "XD"
    $ renpy.pause(0.5)
    # This ends the game.

    return

screen nextSceneScreen(word):
    add "images/bg/popupbox.png" at truecenter
    text word at truecenter

screen instaPhone():
    zorder 10
    add "sprite/act1phone/instaphone.png"

screen twitterPhone():
    zorder 10
    add "sprite/act1phone/twitterphone.png"

screen fbPhone():
    zorder 10
    add "sprite/act1phone/facebookphone.png"


screen locationNow(name):
    zorder 10
    add "gui/location.png" at topright
    hbox xalign 0.97 yalign 0.02:
        text name
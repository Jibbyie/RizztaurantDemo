# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image cr = "ChefRizz.png"
image crAwkward = "ChefRizzAwkward.png"
image d = "Daria.png"
default playerName = ""
define mc = Character("[playerName]", color="#FF0000")

image bgroom = "bgkitchen.jpg"
image bgplaceholder = "bgplaceholder.jpg"

transform speaking:
    ease 0.2 zoom 1.03
transform not_speaking:
    ease 0.2 zoom 1.0
init python:
    def daria_callback(event, interact=True, **kwargs):
        if not interact: 
            return
            ## If the character is currently shown on screen, this will search for the character 'tag'
        if renpy.showing("d"):
        
            if event == 'begin': 
                renpy.show("d", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("d", zorder=0, at_list=[not_speaking])

    def chefRizz_callback(event, interact=True, **kwargs):
        if not interact: 
            return
            ## If the character is currently shown on screen, this will search for the character 'tag'
        if renpy.showing("cr"):
        
            if event == 'begin': 
                renpy.show("cr", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("cr", zorder=0, at_list=[not_speaking])
        
        elif renpy.showing("crAwkward"):
        
            if event == 'begin': 
                renpy.show("crAwkward", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("crAwkward", zorder=0, at_list=[not_speaking])

define cr = Character("Chef Rizz", image="ChefRizz.png", callback=chefRizz_callback)
define crAwkward = Character("Chef Rizz", image="ChefRizzAwkward.png", callback=chefRizz_callback)
define d = Character("Daria", image="Daria.png", callback=daria_callback)


# The game starts here.

label start:
    label chooseName:
        $playerName = renpy.input("What is your name? (You won't be able to change this later)", length=10)
        $playerName = playerName.strip()
        if playerName == "":
            $playerName="Joe Momma"
        if playerName=="Daria".lower() or playerName=="Chef Rizz".lower():
            "Please choose a different name, not one that is already an NPC!"
            jump chooseName

    scene bgroom
    scene bgplaceholder

    show bgplaceholder 
    with dissolve
    show d at center with moveinright

    mc "Wait.. who are you?"

    play music "deathnote.mp3"
    d "{cps=50}{nw}{i}giggles{/i} I, um, couldn't resist introducing myself. I'm Daria-chan, your newest fan and self-proclaimed sidekick 
    in this captivating urban adventure! {i}adjusts glasses dramatically{/i}\nYou see, I've got an insatiable hunger for all things anim-{nw}{/cps}"
    d "{cps=30}{nw}Wait! don't leave me!{nw}{/cps}"
    play sound "running.mp3" volume 0.5

    stop music fadeout 2.0

    play music "kitchen.mp3" fadein 2.0

    show bgroom
    hide d
    with pushright

    show cr at center with moveinbottom
    cr "{cps=25}She was weird wasn't she?{/cps}"
    cr "{cps=25}A tiny bit hot though...{/cps}"

    mc "What?"

    hide cr
    show crAwkward at center
    crAwkward "{cps=25}Didn't mean to let that one slip out...{/cps}"

    mc "You're a weirdo Chef."


    return

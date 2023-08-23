# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image cr = "ChefRizz.png"
image crAwkward = "ChefRizzAwkward.png"
image crCooking = "ChefRizzCooking.png"
image d = "Daria.png"
image dHappy = "DariaHappy.png"
image dAngry = "DariaAngry.png"
image dSparkle = "DariaSparkle.png"
image rizztaurantmenu = "menu.png"

default playerName = ""
define mc = Character("[playerName]", color="#000000")

define flashbulb = Fade(0.2, 0.0, 0.4, color='#fff') 

define audio.background = "rizztaurantambience.mp3"

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
        
        elif renpy.showing("dHappy"):
        
            if event == 'begin': 
                renpy.show("dHappy", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dHappy", zorder=0, at_list=[not_speaking])

        elif renpy.showing("dAngry"):
        
            if event == 'begin': 
                renpy.show("dAngry", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dAngry", zorder=0, at_list=[not_speaking])
        elif renpy.showing("dSparkle"):
        
            if event == 'begin': 
                renpy.show("dSparkle", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dSparkle", zorder=0, at_list=[not_speaking])

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

        elif renpy.showing("crCooking"):
        
            if event == 'begin': 
                renpy.show("crCooking", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("crCooking", zorder=0, at_list=[not_speaking])

define cr = Character("Chef Rizz", image="ChefRizz.png", callback=chefRizz_callback)
define crAwkward = Character("Chef Rizz", image="ChefRizzAwkward.png", callback=chefRizz_callback)
define crCooking = Character("Chef Rizz", image="ChefRizzCooking.png", callback=chefRizz_callback)
define d = Character("Daria", image="Daria.png", callback=daria_callback)
define dHappy = Character("Daria", image="DariaHappy.png", callback=daria_callback)
define dAngry = Character("Daria", image="DariaAngry.png", callback=daria_callback)
define dSparkle = Character("Daria", image="DariaSparkle.png", callback=daria_callback)


# The game starts here.

label start:
    label chooseName:
        $playerName = renpy.input("What is your name?", length=10)
        $playerName = playerName.strip()
        if playerName == "":
            $playerName="Joe Momma"
        if playerName=="Daria".lower() or playerName=="Chef Rizz".lower():
            "Please choose a different name, not one that is already an NPC!"
            jump chooseName

    stop music fadeout 2.0

    play music rizztaurantambience volume 0.2

    scene bgroom
    scene bgplaceholder

    show bgkitchen
    with Dissolve(2.0)

    "{cps=30}{i}(Another quiet day at work. Feels like I'm serving ghosts more than customers.){/i}{/cps}"
    "{cps=30}{i}(Serving imaginary friends might be easier than these empty seats. And less lonely.){/i}{/cps}"
    "{cps=30}{i}(I wonder if I should just close up shop and go home. Seriously, it's like I'm the only one who cares about these tables.){/i}"
    mc "{cps=30}{i}([playerName], the expert in serving.. invisible customers. If only they left invisible tips, right? Who am I kidding, at this rate, I'd be happy to see a ghost show up and ask for water.){/i}{/cps}"

    stop music fadeout 0.5
    play sound dooropening fadein 0.1
    show bgkitchen with vpunch
    $renpy.pause(4.5)
    play music heartbeat1 volume 0.75 fadein 1.0
    mc "{cps=30}{i}(Wait... wh-what? What was that? Am I hearing things?!){/i}{/cps}"

    play sound walking
    mc "{cps=30}{i}(I think I hear footsteps... Wait, do I? Is it just my imagination?){/i}{/cps}"
    play sound walking
    mc "{cps=30}{i}(A customer?! It can't be, it's been damn near.. I don't know...- 10 years since we've last had one? What should I do, oh god, I can't remember the la-){/i}{/cps}{nw}"

    show bgkitchen with hpunch
    stop music
    show d at center with easeinright
    play music dariamainbgm volume 0.5 fadein 1.0 
    "{cps=50}Konnichiwa. Does this establishment currently harbor any occupants?{/cps}"

    mc "{cps=30}{i}(Oh my god, it's a real person! I'm not crazy!){/i}{/cps}"
    mc "{cps=30}{i}(Stick to the script, stick to the script.. y-you know what to do man!){/i}{/cps}"

    mc "{cps=30}Welcome to Rizztaurant, how may I help yo-{/cps}{nw}"

    "{cps=50}Salutations, diligent restaurant employee.{/cps}"
    "{cps=50}I extend my sincere apologies if my unexpected entrance caused you disarray. My intent was merely to locate an establishment to appease the incessant demands of my ever-expansive hunger.{/cps}"
    "{cps=50}Upon observation, your establishment's signage beckoned to me from the exterior.{/cps}"
    d "{cps=50}You may address my humble self as Daria.{/cps}"
    hide d
    show dSparkle at center
    play sound shing
    show bgkitchen with flashbulb
    d "{cps=50}{i} Yoroshiku Onegaishimasu!{/i}{/cps}"
    show d at center
    hide dSparkle
    d "{cps=50}Pray, reassure me, have I unwittingly intruded upon an ongoing engagement?{/cps}"

    mc "{cps=30}Oh, no, not at all! I was just.. cleaning up. Yeah, cleaning up.{/cps}"
    mc "{cps=30}{i}(That was a bit weird..){/i}{/cps}"
    play sound chairpullout
    mc "{cps=30}I'm [playerName]. I'll be your waiter today. May you please take a seat just infront of me here?{/cps}"

    play sound chairpullin
    d "{cps=50}Indubitably. I shall engage in partaking without reservation.{/cps}"

    d "{cps=50}Perchance, [playerName], would you be so kind as to elucidate upon the culinary highlights of this fine establishment?{/cps}"

    mc "{cps=30}Oh, uh, sure!{/cps}"
    mc "{cps=30}Let me just go get a menu for you really quick!{/cps}"

    stop music fadeout 1.0
    play music rizztaurantambience volume 0.2 fadein 2.0

    play sound walking
    hide d with Dissolve(2.0)

    mc "{cps=30}{i}(I can't believe it! A real customer!){/i}{/cps}"
    mc "{cps=30}{i}(Alright, stay calm, stay calm. It's just a menu.){/i}{/cps}"
    mc "{cps=30}{i}(All I've got to do is bring it back. Like nothing's unusual.){/i}{/cps}"
    mc "{cps=30}{i}(Just gotta walk back there and then they'll decide what they want, and I'll go tell the chef, and everything will be normal!){/i}{/cps}"

    show rizztaurantmenu at truecenter 
    play sound paperflip
    mc "{cps=30}{i}Ta-da!{/i}{/cps}"

    mc "{cps=30}{i}(Oh who am I kidding, she's not going to want to eat any of this garbage..){/i}{/cps}"
    play sound paperdown
    hide rizztaurantmenu
    mc "{cps=30}{i}(Think man think, we can't let this opportunity go to waste.){/i}{/cps}"
    mc "{cps=50}{i}....{/i}{/cps}"
    mc "{cps=50}{i}.......{/i}{/cps}"
    mc "{cps=50}{i}..................{/i}{/cps}"
    mc "{cps=50}{i}.................................................{/i}{/cps}"
    mc "{cps=50}{i}..........................................................................................................................................{/i}{/cps}"

    play sound brightidea
    $ renpy.pause(1.5)
    mc "{cps=30}{i}(I've got it!){/i}{/cps}"
    mc "{cps=30}{i}(I'll just tell her that we're out of everything on the menu, and that we're only serving one thing today!){/i}{/cps}"
    mc "{cps=30}{i}(No you idiot that doesn't even make sense, how would we be out of everything without a single other customer?){/i}{/cps}"
    window hide
    show text "{color=#FFFF00}{size=+10}{b}A few minutes later...{/b}{/color}" with Dissolve(0.5)
    $ renpy.pause(1.5)
    hide text
    mc "{cps=30}{i}(Hmm, what if...){/i}{/cps}" with Dissolve(0.5)
    mc "{cps=30}{i}(Ah, I've got an idea!){/i}{/cps}"
    mc "{cps=30}{i}(Why not offer something unique? Something that'll grab her attention. Like...){/i}{/cps}"

    mc "{cps=30}{i}(I'll ask her if she's up for a culinary adventure. You know, something different from the usual fare.){/i}{/cps}"
    mc "{cps=30}{i}(A chance to savor the unexpected. After all, who wants predictable when you can have... surprise?){/i}{/cps}"
    mc "{cps=30}{i}(Yeah, that sounds good!){/i}{/cps}"

    mc "{cps=30}{i}(Alright, I've got this. I'll tell her: 'Excuse me, we have a rather special offering today.'){/i}{/cps}"
    mc "{cps=30}{i}(I'll tell her about the opportunity to have a meal tailored precisely to her tastes. You know, a chance to create her own culinary masterpiece.){/i}{/cps}"
    mc "{cps=30}{i}(And then, the pièce de résistance, our Michelin-starred chef will personally craft her culinary desires into reality. It's a symphony of flavors, a melody of imagination!){/i}{/cps}"
    mc "{cps=30}{i}(I'll exclaim 'Miss, it's only available for a limited time, you should act now before it's too late!'){/i}{/cps}"
    mc "{cps=30}{i}(Yep, I'm screwed.){/i}{/cps}"

    play sound walking
    stop music fadeout 1.0
    show dAngry at center with Dissolve(2.0)

    play sound stomachgrowl
    $ renpy.pause(4.0)
    play music dariamainbgm volume 0.5 fadein 1.5
    mc "{cps=10}Oh, uh, miss are you alrigh-{/cps}{nw}"
    d "{cps=50}I apologize for my impatience, but I am in dire need of sustenance.{/cps}"

    return
 
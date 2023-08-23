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
        $playerName = renpy.input("What is your name? (You won't be able to change this later)", length=10)
        $playerName = playerName.strip()
        if playerName == "":
            $playerName="Joe Momma"
        if playerName=="Daria".lower() or playerName=="Chef Rizz".lower():
            "Please choose a different name, not one that is already an NPC!"
            jump chooseName

    stop music fadeout 2.0

    play music rizztaurantambience loop

    scene bgroom
    scene bgplaceholder

    show bgkitchen
    with Dissolve(2.0)

    "{cps=30}{i}(Another quiet day at work. Feels like I'm serving ghosts more than customers.){/i}{/cps}"
    "{cps=30}{i}(Serving imaginary friends might be easier than these empty seats. And less lonely.){/i}{/cps}"
    "{cps=30}{i}(I wonder if I should just close up shop and go home. Seriously, it's like I'm the only one who cares about these tables.){/i}"
    mc "{cps=20}{i}([playerName], the expert in serving.. invisible guests. If only they left invisible tips, right? Who am I kidding, at this rate, I'd be happy to see a ghost show up and ask for water.){/i}{/cps}"

    stop music fadeout 0.5
    play sound dooropening fadein 0.1
    show bgkitchen with vpunch
    $renpy.pause(4.5)
    play music heartbeat1 volume 0.75 fadein 1.0
    mc "{cps=15}{i}(Wait... wh-what? What was that? Am I hearing things?!){/i}{/cps}"

    play sound walking
    mc "{cps=30}{i}(I think I hear footsteps... Wait, do I? Is it just my imagination?){/i}{/cps}"
    play sound walking
    mc "{cps=30}{i}(A customer?! It can't be, it's been damn near.. I don't know...- 10 years since we've last had one? What should I do, oh god, I can't remember the la-){/i}{/cps}{nw}"

    show bgkitchen with hpunch
    stop music
    show d at center with easeinright
    play music deathnote volume 0.2 fadein 1.0 
    "{cps=40}Konnichiwa. Does this establishment currently harbor any occupants?{/cps}"

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
    stop music fadeout 0.5
    play music dariamainbgm volume 0.5 fadein 1.0
    show d at center
    hide dSparkle
    d "{cps=50}Pray, reassure me, have I unwittingly intruded upon an ongoing engagement?{/cps}"

    mc "{cps=30}Oh, no, not at all! I was just.. cleaning up. Yeah, cleaning up.{/cps}"
    mc "{cps=30}{i}(That was a bit weird..){/i}{/cps}"
    play sound chairpullout
    mc "{cps=30}I'm [playerName]. I'll be your waiter today. May you please take a seat just infront of me here?{/cps}"

    play sound chairpullin
    d "{cps=50}Indubitably! I shall engage in partaking without reservation!{/cps}"

    d "{cps=50}Perchance, [playerName], would you be so kind as to elucidate upon the culinary highlights of this fine establishment?{/cps}"


    return

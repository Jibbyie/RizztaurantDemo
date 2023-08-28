# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image irritatedAura = "irritatedAura.png"
image cr = "ChefRizz.png"
image crAwkward = "ChefRizzAwkward.png"
image crCooking = "ChefRizzCooking.png"
image d = "Daria.png"
image dHappy = "DariaHappy.png"
image dAngry = "DariaAngry.png"
image dSparkle = "DariaSparkle.png"
image dGlare = "DariaGlare.png"
image dGlassesShine = "DariaGlassesShine.png"
image dThinking = "DariaThinking.png"
image rizztaurantmenu = "menu.png"
image halfblack = "#00000088"

default playerName = ""
define mc = Character("[playerName]", color="#000000", what_slow_cps=30)

define flashbulb = Fade(0.2, 0.0, 0.4, color='#fff') 

define audio.background = "rizztaurantambience.mp3"

image bgroom = "bgkitchen.jpg"
image doombackground = "doombackground.png"

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

        elif renpy.showing("dGlare"):
        
            if event == 'begin': 
                renpy.show("dGlare", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dGlare", zorder=0, at_list=[not_speaking])

        elif renpy.showing("dGlassesShine"):
        
            if event == 'begin': 
                renpy.show("dGlassesShine", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dGlassesShine", zorder=0, at_list=[not_speaking])

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
define d = Character("Daria", image="Daria.png", what_slow_cps=50, callback=daria_callback)
define dHappy = Character("Daria", image="DariaHappy.png", callback=daria_callback)
define dAngry = Character("Daria", image="DariaAngry.png", callback=daria_callback)
define dSparkle = Character("Daria", image="DariaSparkle.png", callback=daria_callback)
define dGlare = Character("Daria", image="DariaGlare.png", callback=daria_callback)
define dGlassesShine = Character("Daria", image="DariaGlassesShine.png", callback=daria_callback)


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
    
    show bgkitchen
    with Dissolve(2.0)

    # Introducing MC's distaste for his job
    "{cps=30}{i}(Another quiet day at work. Feels like I'm serving ghosts more than customers.){/cps}{/i}"
    "{cps=30}{i}(Serving imaginary friends might be easier than these empty seats. And less lonely.){/cps}{/i}"
    "{cps=30}{i}(I wonder if I should just close up shop and go home. Seriously, it's like I'm the only one who cares about these tables.){/cps}{/i}"
    mc "{i}([playerName], the expert in serving.. invisible customers. If only they left invisible tips, right? Who am I kidding, at this rate, I'd be happy to see a ghost show up and ask for water.){/i}"

    # New customer comes into the scene
    stop music fadeout 0.5
    play music dooropening volume 0.2 fadein 0.1
    play sound shopbelldoor fadein 0.1
    show bgkitchen with vpunch
    $renpy.pause(4.5)
    play music heartbeat1 volume 0.75 fadein 1.0
    mc "{i}(Wait... wh-what? What was that? Am I hearing things?!){/i}"

    play sound walking
    mc "{i}(I think I hear footsteps... Wait, do I? Is it just my imagination?){/i}"
    play sound walking
    mc "{i}(A customer?! It can't be, it's been damn near.. I don't know...- 10 years since we've last had one? What should I do, oh god, I can't remember the la-){/i}{nw}"

    # Daria introduction
    show bgkitchen with hpunch
    stop music
    show d at center with easeinright
    play music dariamainbgm volume 0.5 fadein 1.0 
    "{cps=50}Konnichiwa. Does this establishment currently harbor any occupants?{/cps}"

    mc "{i}(Oh my god, it's a real person! I'm not crazy!){/i}"
    mc "{i}(Stick to the script, stick to the script.. y-you know what to do man!){/i}"

    menu respond_in_japanese:
        "Respond in Japanese":
            $ initialResponse = "Japanese"
            mc "{font=japanese.otf}いらっしゃいませ！{/font}"
            jump response_in_japanese
        "Respond in English":
            $ initialResponse = "English"
            mc "Welcome to Rizztaurant, how may I help yo-{nw}"
            jump main_core_loop

    label response_in_japanese:
        stop music
        "{cps=50}P-p-pardon me?{/cps}"
        mc "I'm sorry, you speak Japanese don't you?"
        "{cps=50}I uh, uh-{/cps}"
        "{cps=50}Yes, mochiron, you just, caught me off guard... sumimasen..{/cps}"
        "{cps=50}I'm sorry, I'm just... simply, uh.. not used to being greeted in the language of the homeland. That is all. Yes of course.{/cps}"
        "{cps=50}Ahem.{/cps}"
        play music dariamainbgm volume 0.5

    label main_core_loop:
        "{cps=50}Salutations, diligent restaurant employee.{/cps}"
    "{cps=50}I extend my sincere apologies if my unexpected entrance caused you disarray. My intent was merely to locate an establishment to appease the incessant demands of my ever-expansive hunger.{/cps}"
    "{cps=50}Upon observation, your establishment's signage beckoned to me from the exterior.{/cps}"
    d "You may address my humble self as Daria."
    hide d
    show dGlare at center
    play sound shing
    show bgkitchen with flashbulb
    if initialResponse == "English":
        d "{i} Yoroshiku Onegaishimasu!{/i}"
    if initialResponse == "Japanese":
        d "{i} Nice to meet you!{/i}"
    hide dGlare
    show d at center
    d "Pray, reassure me, have I unwittingly intruded upon an ongoing engagement?"

    mc "Oh, no, not at all! I was just.. cleaning up. Yeah, cleaning up."
    mc "{i}(That was a bit weird..){/i}"
    play sound chairpullout
    mc "I'm [playerName]. I'll be your waiter today. May you please take a seat just infront of me here?"

    play sound chairpullin
    d "Indubitably. I shall engage in partaking without reservation."

    d "Perchance, [playerName], would you be so kind as to elucidate upon the culinary highlights of this fine establishment?"
    
    # MC goes to get Daria a menu
    mc "Oh, uh, sure!"
    mc "Let me just go get a menu for you really quick!"

    stop music fadeout 1.0
    play music rizztaurantambience volume 0.2 fadein 2.0

    play sound walking
    hide d with Dissolve(2.0)

    mc "{i}(I can't believe it! A real customer!){/i}"
    mc "{i}(Alright, stay calm, stay calm. It's just a menu.){/i}"
    mc "{i}(All I've got to do is bring it back. Like nothing's unusual.){/i}"
    mc "{i}(Just gotta walk back there and then they'll decide what they want, and I'll go tell the chef, and everything will be normal!){/i}"

    # Menu appears on screen
    show rizztaurantmenu at truecenter 
    play sound paperflip
    mc "{i}Ta-da!{/i}"

    mc "{i}(Oh who am I kidding, she's not going to want to eat any of this garbage..){/i}"
    play sound paperdown
    hide rizztaurantmenu
    mc "{i}(Think man think, we can't let this opportunity go to waste.){/i}"
    mc "{i}....{/i}"
    mc "{i}.......{/i}"
    mc "{i}..................{/i}"
    mc "{i}.................................................{/i}"
    mc "{i}..........................................................................................................................................{/i}"

    play sound brightidea
    $ renpy.pause(1.5)
    mc "{i}(I've got it!){/i}"
    mc "{i}(I'll just tell her that we're out of everything on the menu, and that we're only serving one thing today!){/i}"
    mc "{i}(No you idiot that doesn't even make sense, how would we be out of everything without a single other customer?){/i}"

    # Intermission, MC introduces main idea (core gameplay loop)
    window hide
    show text "{color=#FFFF00}{size=+10}{b}A few minutes later...{/b}{/color}" with Dissolve(1.5)
    $ renpy.pause(3)
    hide text
    mc "{i}(Hmm, what if...){/i}" with Dissolve(1)
    mc "{i}(Ah, I've got an idea!){/i}"
    mc "{i}(Why not offer something unique? Something that'll grab her attention. Like...){/i}"

    mc "{i}(I'll ask her if she's up for a culinary adventure. You know, something different from the usual fare.){/i}"
    mc "{i}(A chance to savor the unexpected. After all, who wants predictable when you can have... surprise?){/i}"
    mc "{i}(Yeah, that sounds good!){/i}"

    mc "{i}(Alright, I've got this. I'll tell her: 'Excuse me, we have a rather special offering today.'){/i}"
    mc "{i}(I'll tell her about the opportunity to have a meal tailored precisely to her tastes. You know, a chance to create her own culinary masterpiece.){/i}"
    mc "{i}(I'll exclaim 'Miss, it's only available for a limited time, you should act now before it's too late!'){/i}"
    mc "{i}(And then, the pièce de résistance, our Michelin-starred chef will personally craft her culinary desires into reality. It's a symphony of flavors, a melody of imagination!){/i}"
    mc "{i}(Yep, I'm screwed.){/i}"
    
    # MC returns to Daria to introduce main idea
    play sound walking
    stop music fadeout 1.0

    scene doombackground
    show dThinking at center 
    show halfblack
    with Dissolve(4.0)

    # Daria Stomach growl
    play sound stomachgrowl
    $ renpy.pause(3.2)
    mc "{cps=10}Oh, uh, miss are you alrigh-{nw}"
    d "{cps=5}I apologize for my impatience, but I am in dire need of sustenance."

    mc "My sincere apologies for the wait!"
    menu:
        "Show her the menu":
            $ ideaOrMenu = "menuShown"
            mc "Here's our.. menu. Please take a look and let me know if you have any questions."
            jump backtodSparkle
        "Present your fabulous idea":
            $ ideaOrMenu = "ideaPresented"
            mc "We actually have a rather special offering today."
            jump backtodSparkle

    label backtodSparkle:
        hide dThinking
        hide doombackground
        show bgkitchen
        show dSparkle at center
        play music dariamainbgm volume 0.5
        if ideaOrMenu == "menuShown":
            jump showing_menu
        if ideaOrMenu == "ideaPresented":
            jump presenting_idea

    label showing_menu:
        d "Oh?"
        hide dSparkle
        show d at center
        d "Allow me to take a gander."
        play sound paperflip
        d "Hm."
        stop music
        d "I see."
        play music dariamainbgm volume 0.5
        d "You know, these choices are... quite unusual. Is this some sort of avant-garde selection?"
        d "I must say, I wasn't expecting such.. creativity in the realm of taste combinations."
        d "But alas, I regret to inform you these.. {i}meals,{/i} presented here are not to my liking."
        d "I am most apologetic."
        d "Thank you for your courteous hospitality. I shall be taking my leav-.{nw}"
        mc "Wait!"
        d "Pardon me?"
        mc "I mean, uh, I'm sorry to hear that."
        mc "But, uh, we have a rather special offering today."
        jump presenting_idea

    label presenting_idea:
        hide dSparkle
        show d at center
        d "{i}Hmmmmm..?{/i}"
        hide d
        show dGlare at center
        play sound shing
        show bgkitchen with flashbulb
        d "Sugoi! Do tell."
        d "I am most intrigued."

    hide dGlare
    show d at center
    mc "{i}(She really needs to stop doing that..){/i}"
    mc "It's a chance to have a meal tailored precisely to your tastes."
    mc "Our Michelin-starred chef will personally craft your culinary desires into reality."
    mc "It's a symphony of flavors, a melody of imagination!"
    mc "Miss, it's only available for a limited time, you should act now before it's too late!"
    mc "{i}(I am so totally screwed){/i}"

    # Daria accepts the notion of the idea
    hide d
    show dGlassesShine at center
    d "Oh-ho-ho-ho-ho-ho." # Introduce laughing animation in future
    hide dGlassesShine
    show d at center
    d "You have quite the way with words fine gentleman. I am most impressed."
    d "To think of a culinary adventure tailored to my own preferences, it's positively thrilling!"
    d "The prospect of this Michelin-starred chef weaving a symphony of flavors for my palate fills me with delight."
    d "And only for a limited time? How could I possibly resist?"
    d "I wholeheartedly embrace this opportunity!"

    mc "{i}(Wait, what?){/i}"
    mc "{i}(She actually wants to try it?){/i}"
    mc "{i}(Wait a minute... This could be more trouble than I thought. Chef Rizz isn't exactly a culinary genius...){/i}"
    mc "I'm truly glad you're enthusiastic! Our chef has a... uh.. unique approach to his creations."
    mc "But don't worry, it's bound to be an unforgettable experience in its own right."

    d "Oh, how marvelous it sounds! An opportunity to tantalize my taste buds and embrace the unexpected."
    d "The very notion of a chef's unique approach intrigues me even further. After all, artistry often emerges from the unexpected."
    d "Fear not, kind sir, for I am prepared to embark on this culinary adventure with an open heart and an adventurous spirit."

    # MC brings up mention of Chef Rizz
    mc "Uh, sure!"
    mc "{i}(Wow, she's really into this huh...){/i}"
    mc "Just... be prepared for the unexpected, alright? Chef Rizz has a knack for surprising even myself."
    mc "{i}(I hope you know what you're getting into, Daria...){/i}"

    d "Oh but of course, I live for the suspense."
    d "I shall await the chef's creation with bated breath."
    d "Apprise, how do we commence such an immense undertaking?"
    d "I'm testing some text speed right now though!"

    return
 
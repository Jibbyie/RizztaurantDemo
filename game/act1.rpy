label act1:
    
    show black
    scene black
    stop music fadeout 2.0

    play music rizztaurantambience volume 0.2
    
    show bgkitchen
    with Dissolve(2.0)

    # Introducing MC's distaste for his job
    hide screen nt_button
    
    "{cps=30}{i}(Another quiet day at work. Feels like I'm serving ghosts.){/cps}{/i}"
    "{cps=30}{i}(Serving imaginary friends might be easier than these empty seats. And less lonely.){/cps}{/i}"
    "{cps=30}{i}(I wonder if I should just close up shop and go home.){/cps}{/i}"
    mc "{i}([playerName], the expert in serving.. invisible customers. If only they left invisible tips, right? Who am I kidding, at this rate, I'd be happy to see a ghost show up and ask for water.){/i}"
    
    # New customer comes into the scene
    window hide
    
    stop music fadeout 0.5
    play music dooropening volume 0.2 fadein 0.1
    play sound shopbelldoor fadein 0.1
    show bgkitchen with vpunch
    $ renpy.pause(4.5, hard=True)
    play music heartbeat1 volume 0.75 fadein 1.0
    
    mc "{i}(Wait... wh-what? What was that? Am I hearing things?!){/i}"

    play sound walking
    mc "{i}(I think I hear footsteps... Wait, do I? Is it just my imagination?){/i}"
    play sound walking
    mc "{i}(A customer?! It can't be, it's been damn near.. I don't know...- 10 years since we've last had one? What should I do, oh god, I can't remember the last time we had one.){/i}"
    mc "{i}Ever since that incident with Chef Rizz and that guy's girlfriend I-{/i}"
    
    window hide
    
    # Daria(HiraganaLover95) introduction
    show bgkitchen with hpunch
    stop music
    show d at center with easeinright
    play music dariamainbgm volume 0.5 fadein 1.0 
    
    window show
    "{cps=50}Konnichiwa. Does this establishment currently harbour any occupants?{/cps}"

    mc "{i}(Oh my god, it's a real person! I'm not crazy!){/i}"
    mc "{i}(Stick to the script, stick to the script.. y-you know what to do man!){/i}"

    
    window hide
    

    menu respond_in_japanese:
        "Respond in Japanese":
            $ initialResponse = "Japanese"
            $ renpy.fix_rollback()
            
            mc "{font=japanese.otf}いらっしゃいませ！{/font}"
            jump response_in_japanese
        "Respond in English":
            $ initialResponse = "English"
            $ renpy.fix_rollback()
            
            mc "Welcome to Rizztaurant, how may I help yo-"
            jump main_core_loop

    label response_in_japanese:
        
        $ renpy.fix_rollback()
        stop music
        hide d
        show dThinking
        "{cps=50}P-p-pardon me?{/cps}"
        window hide
        show sweat
        show flushed
        with Dissolve(2.0)
        window show
        mc "I'm sorry, you speak Japanese don't you?"
        "{cps=50}I uh, uh-{/cps}"
        "{cps=50}Yes, mochiron, you just, caught me off guard... sumimasen..{/cps}"
        "{cps=50}I'm sorry, I'm just... simply, uh.. not used to being greeted in the language of the homeland. That is all. Yes of course.{/cps}"
        "{cps=50}Ahem.{/cps}"
        hide sweat
        hide flushed
        hide dThinking
        show d
        play music dariamainbgm volume 0.5

    label main_core_loop:
        $ renpy.fix_rollback()
        
        "{cps=50}Salutations, diligent restaurant employee.{/cps}"
    "{cps=50}I extend my sincere apologies if my unexpected entrance caused you disarray. My intent was merely to locate an establishment to appease the incessant demands of my ever-expansive hunger.{/cps}"
    "{cps=50}Upon observation, your establishment's signage beckoned to me from the exterior.{/cps}"
    d "You may address my humble self as my Reddit pseudonym - HiraganaLover95."
    
    hide d
    show dGlare at center
    play sound shing volume 0.5 if_changed
    show bgkitchen with flashbulb
    if initialResponse == "English":
        
        d "{i} Yoroshiku Onegaishimasu!{/i}"
    if initialResponse == "Japanese":
        
        d "{i} Nice to meet you!{/i}"
    hide dGlare
    show d at center
    d "Pray, reassure me, have I unwittingly intruded upon an ongoing engagement?"

    mc "Oh, no, not at all! I was just uh...."
    hide d
    
    
    show bgkitchen:
        # Start at full image
        crop (0,0, 1920, 1080) size (1920, 1080)
        subpixel True
        # Over 1.0 seconds move to focus on the cropped area and rescale up to size
        linear 1.0 crop (510, 290, 160, 90) size (1920, 1080) # Flies
        pause 1.0
        linear 0.5 crop (50, 630, 200, 130) size (1920, 1080) # Cobwebs
        pause 1.0
        linear 0.5 crop (30, 270, 160, 90) size (1920, 1080) # Cockroach
        pause 1.0
        linear 0.5 crop (1410, 600, 220, 150) size (1920, 1080) # Silverfish
        pause 1.0
        linear 0.5 crop (935, 610, 160, 90) size (1920, 1080) # Rat
        pause 1.0
        linear 0.5 crop (280, 670, 220, 150) size (1920, 1080) # Chalk outline
 
    window hide
    $ renpy.pause(9.4, hard = True)
    
    mc "Uhm.."

    show bgkitchen:
        crop (0,0, 1920, 1080) size (1920, 1080)
        subpixel True
        crop (0,0, 1920, 1080) size (1920, 1080)
    show d
    mc "Cleaning up! Yeah.. cleaning up."
    #

    mc "{i}(That was a bit weird...){/i}"
    mc "{i}(Wait what.. a Reddit pseudonym? I-I don't think I should even question that..)"
    play sound chairpullout
    mc "I'm [playerName]. I'll be your waiter today. May you please take a seat just infront of me here?"

    play sound chairpullin
    d "Indubitably. I shall engage without reservation."

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
    mc "{i}(Just gotta walk back there and then she'll decide what she wants, and I'll go tell the chef, and everything will be okay!){/i}"

    mc "{i}Ta-da!{/i}"
    
    window hide 
    # Menu appears on screen
    show rizztaurantmenu at center 
    play sound paperflip
    pause 30.0
    

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
    $ renpy.pause(1.5, hard=True)
    
    mc "{i}(I've got it!){/i}"
    mc "{i}(I'll just tell her that we're out of everything on the menu, and that we're only serving one thing today!){/i}"
    mc "{i}(No you idiot that doesn't even make sense, how would we be out of everything without a single other customer?){/i}"
    

    # Intermission, MC introduces main idea (core gameplay loop)
    show text "{color=#80400B}{size=+10}{b}A few minutes later...{/b}{/color}" with Dissolve(1.5)
    $ renpy.pause(3, hard=True)
    
    hide text
    mc "{i}(Hmm, what if...){/i}" with Dissolve(1)
    mc "{i}(Ah, I've got an idea!){/i}"
    mc "{i}(Why not offer something unique? Something that'll grab her attention. Like...){/i}"

    mc "{i}(I'll ask her if she's up for a culinary adventure. You know, something different from the usual fare.){/i}"
    mc "{i}(A chance to savour the unexpected. After all, who wants predictable when you can have... surprise?){/i}"
    mc "{i}(Yeah, that sounds good!){/i}"
    mc "{i}(I'm so screwed....){/i}"
    
    hide dThinking

    # MC returns to Daria to introduce main idea
    play sound walking
    stop music fadeout 1.0

    scene doombackground
    show dThinking at center 
    show daria angry zorder 1000
    show halfblack
    with Dissolve(4.0)

    # Daria Stomach growl
    play sound stomachgrowl
    $ renpy.pause(3.2, hard=True)
    
    mc "{cps=10}Oh, uh, miss are you alrigh-"
    d "{cps=5}I apologise for my impatience, but I am in dire need of sustenance."

    mc "My sincere apologies for the wait!"
    
    menu:
        "Show her the menu":
            $ ideaOrMenu = "menuShown"
            $ renpy.fix_rollback()
            
            mc "Here's our.. menu. Please take a look and let me know if you have any questions."
            jump backtodGlare
        "Present your fabulous idea":
            $ ideaOrMenu = "ideaPresented"
            $ renpy.fix_rollback()
            
            mc "We actually have a rather special offering today."
            jump backtodGlare

    label backtodGlare:
        hide dThinking
        hide doombackground
        hide daria angry
        show bgkitchen
        show dGlare at center
        play music dariamainbgm volume 0.5
        if ideaOrMenu == "menuShown":
            jump showing_menu
        if ideaOrMenu == "ideaPresented":
            jump presenting_idea

    label showing_menu:
        $ renpy.fix_rollback()
        d "Oh?"
        hide dGlare
        hide daria angry
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
        d "Thank you for your courteous hospitality. But i'm going to have to-."
        mc "Wait!"
        d "Pardon me?"
        mc "I mean, uh, I'm sorry to hear that."
        mc "But, uh, we have a rather special offering today."
        jump presenting_idea

    label presenting_idea:
        $ renpy.fix_rollback()
        hide dGlare
        show d at center
        d "{i}Hmmmmm..?{/i}"
        hide d
        show dGlare at center
        play sound shing
        show bgkitchen with flashbulb
        d "{b}Sugoi!{/b} Do tell."
        d "I am most intrigued."

    hide dGlare
    show d at center
    mc "{i}(She really needs to stop doing that..){/i}"
    mc "It's a chance to have a meal tailored precisely to your tastes."
    mc "Our Michelin-starred chef will personally craft your culinary desires into reality."
    mc "It's a symphony of flavours, a melody of imagination!"
    mc "Miss, it's only available for a limited time, you should act now before it's too late!"
    mc "{i}(I am so totally screwed.){/i}"

    # Daria accepts the notion of the idea
    hide d
    show d2 at laugh, center
    d "Oh-ho-ho-ho-ho-ho." 
    hide d2
    show d at center
    d "You have quite the way with words fine gentleman. I am most impressed."
    d "To think of a culinary adventure tailored to my own preferences, it's positively thrilling!"
    d "The prospect of this Michelin-starred chef weaving a symphony of flavours for my palate fills me with delight."
    d "And only for a limited time? How could I possibly resist?"
    d "I wholeheartedly embrace this opportunity!"

    mc "{i}(Wait, what?){/i}"
    show daria glasses shine zorder 1000
    mc "{i}(She actually wants to try it?){/i}"
    mc "{i}(Wait a minute... This could be more trouble than I thought. Chef Rizz isn't exactly a culinary genius...){/i}"
    mc "I'm truly glad you're enthusiastic! Our chef has a... uh.. unique approach to his creations."
    mc "But don't worry, it's bound to be an unforgettable experience in its own right."

    hide daria glasses shine
    d "Oh, how marvelous it sounds! An opportunity to tantalise my taste buds."
    d "After all, artistry often emerges from the unexpected."
    d "Fear not, kind sir, for I am prepared to embark with an open heart and an adventurous spirit."

    # MC brings up mention of Chef Rizz
    mc "Uh, sure!"
    mc "{i}(Wow, she's really into this huh...){/i}"
    mc "Just... be prepared for.. something unique, alright? Chef Rizz has a knack for surprising even myself."
    mc "{i}(I hope you know what you're getting into...){/i}"

    hide d
    show dGlassesShine at running, center 
    show d at offscreenleft 
    d "Oh-ho-ho-ho but of course! I live for the suspense!" # d at offscreenleft is a workaround to apply laughing animation during speech
    hide dGlassesShine
    hide d 
    show d at center
    d "Apprise, how do we commence such an immense undertaking?"
    
    mc "Um, well, let me know when you're ready and I'll explain the process."
    d "I am prepared to begin at your behest."
    mc "O-okay.. {i}(what the heck does behest mean?){/i}"
    mc "So, first, I will ask you four culinary related questions."
    mc "Each one of them will determine certain aspects of your meal."
    mc "You can be as specific or as vague as you want."
    mc "Then I'll relay it to the chef."
    mc "The chef will do his best to create something that closely matches your answers."
    mc "The sky's the limit, as long as what you propose is within reason."
    d "I see, I see."
    d "I shall endeavour to be as specific as possible."
    d "How delightful! I am most eager to begin."

    mc "Alright, let's get started then!"
    mc "So, what are some of your favourite cuisines?"
    stop music fadeout 2.0
    play music rizztaurantambience volume 0.5 fadein 3.0
    hide d with Dissolve(1.0)

    "HiraganaLover95 will now talk about her preferences. As you might have noticed, she's a bit chatty."
    "Do your best to memorise her answers and take note of what she loves, likes, dislikes or is neutral about."
    "This will be important later for when you relay it to the chef."
    "Don't worry, there'll be a point where you can write down what you think is best."
    "One more thing!"
    "Just a little hint, you can't write down everything!"

    stop music fadeout 2.5
    play music dariamainbgm volume 0.5 fadein 3.0
    show d with Dissolve(0.5)

    d "Cuisines, oh what a labryinth of sensory experiences they offer!"
    d "If you wish to probe the depths of my culinary inclinations, you may. For I grant you passage."
    hide d
    show dHappy at center
    dHappy "You would discern a certain affinity for the comforting embrace of Italian cuisine, its familiar aromas evoking memories long dormant."
    hide dHappy
    show dThinking
    dThinking "Even so, admist the whispers of marina and basil and hearty carbonara pasta, there lies a subtle intrigue."
    dThinking "An intrigue in the subtle complexities of Greek cuisine, its delicate balance of flavours a puzzle waiting to be unraveled."
    dThinking "While many may revel in bold spices and zesty salsas, it has yet to capture my palate in the same way."
    mc "You speak Japanese right? Excuse me for prying but what about Japanese food?"
    show sweat zorder 1000 with Dissolve(1.0)
    dThinking "Ah, Japanese cuisine, once it captivated my senses, though its allure now wanes in comparison to the passions stirred by the aforementioned."
    hide dThinking
    hide sweat
    show d
    d "Thus concludes my exploration of cuisine preferences!"
    mc "Thank you very much! Let me just write that down."
    menu:
        "Write down 'Greek Cuisine' as her preference":
            $ cuisine_preferences.append("Greek Cuisine")
            play sound writing volume 0.5
            $ renpy.fix_rollback()
            jump dialogue1
        "Write down 'Italian Cuisine' as her preference":
            $ cuisine_preferences.append("Italian Cuisine")
            play sound writing volume 0.5
            $ renpy.fix_rollback()
            jump dialogue1
        "Write down 'Japanese Cuisine' as her preference":
            $ cuisine_preferences.append("Japanese Cuisine")
            play sound writing volume 0.5
            $ renpy.fix_rollback()
            jump dialogue1
        "Write down 'Mexican Cuisine' as her preference":
            $ cuisine_preferences.append("Mexican Cuisine")
            play sound writing volume 0.5
            $ renpy.fix_rollback()
            jump dialogue1
        
    label dialogue1:
        mc "Thank you again."
        mc "Ready for the next question?"
    
    hide d
    show dGlare
    dGlare "Ready as I'll ever be good sir!"
    mc "Perfect!"
    mc "So, what would be your ideal flavour combination?"
    hide dGlare
    show dThinking
    dThinking "Ah.. deep within the recesses of my culinary consciousness, there exists within me a certain fascination for sensations that linger, inviting contemplation long after the last bite."
    dThinking "The kind of flavour that beckons with a depth that leaves an indelible impression upon the senses, an intriguing bitterness that hints at complexity yet undiscovered."
    dThinking "Unfolding like the pages of a well-worn novel waiting to be explored."
    dThinking "I too yearn for a subtle brininess, a touch of sea-swept allure that transports me to distant shores, summoning up memories of salt-kissed breezes and sun-drenched afternoons."
    dThinking "Yet... admist the vast array of flavours that grace my soul, there are many that fail to spark interest. Fail to conjure the joyous symphony of sensations that I seek."
    dThinking "A blandness that lingers like a shadow, leaving me indifferent to their presence comparable to a mere whisper."
    dThinking "For those tastes that stir neither passion nor aversion, they remain elusive, their significance veiled in ambiguity."
    dThinking "Sourness.. holding a curious neutrality. Neither captivating nor repelling, but existing as a fleeting murmur in this ensemble."
    dThinking "On the other hand, there are many that elicit a distate that cannot be ignored."
    show d at offscreenleft
    show daria angry zorder 1000
    hide dThinking
    show dThinking at shake, center:
        zoom 1.03
    dThinking "Lest I be met with a saccharine embrace again, I will respond with a vile recoil of the senses."
    dThinking "As if repelled by the very essence of disgust itself, an embrace akin to tasting the forbidden fruit of excess."
    hide d
    hide dThinking
    hide daria angry
    stop music fadeout 1.0
    hide bgroom

    show bgroomdark
    show dThinkingDark 
    with Dissolve(3.0)
    dThinking "{cps=20}And thus.{/cps}"
    mcthinking "Wait... who turned off the lights?"
    dThinking "{cps=18}The tangled web unfolds, each flavour a thread in the intricate tapestry of gastronomic exploration.{/cps}" 
    dThinking "{cps=15}Each weaving together a mosaic of experiences waiting to be deciphered.{/cps}" 
    dThinking "{cps=12}A puzzle whose solution lies hidden within the harmony of a grand orchestration of epicurean delight.{/cps}"
    dThinking "{cps=9}.......{/cps}"
    hide dThinkingDark
    show dThinking at offscreenleft
    show dThinkingGlassesShineDark at center:
        zoom 1.03
    dThinking "{cps=5}.......{/cps}"
    mc "Everything... alright?"
    dThinking "{cps=2}......{/cps}"
    mc "I take it that that you're done answering?"
    hide dThinking
    hide dThinkingGlassesShineDark
    show dThinkingGlassesShineDark
    dThinking "{cps=18}Oh yes.. of course.. apologies.. I was just ensnared in deep thought.{/cps}"
    play music dariamainbgm volume 0.5 fadein 0.5
    hide dThinkingGlassesShineDark
    show dThinkingGlassesShining
    hide bgroomdark
    show bgkitchen
    mc "Okay.. thank you! I will just write that down again."
    menu:
        "Write down 'Sweet & Savoury' as her preference.":
            $ flavour_preferences.append("Sweet")
            $ flavour_preferences.append("Savoury")
            play sound writing volume 0.5
            $ renpy.fix_rollback()
            jump dialogue2
        "Write down 'Bitter & Salty' as her preference.":
            $ flavour_preferences.append("Bitter")
            $ flavour_preferences.append("Salty")
            play sound writing volume 0.5
            $ renpy.fix_rollback()
            jump dialogue2
        "Write down 'Sour & Salty' as her preference.":
            $ flavour_preferences.append("Sour")
            $ flavour_preferences.append("Salty")
            play sound writing volume 0.5
            $ renpy.fix_rollback()
            jump dialogue2
        "Write down 'Sour & Sweet' as her preference.":
            $ flavour_preferences.append("Sour")
            $ flavour_preferences.append("Sweet")
            play sound writing volume 0.5
            $ renpy.fix_rollback()
            jump dialogue2

    label dialogue2:
        mc "Okay! Ready for question 3?"
        hide bgroom
        show bgroomdark
        hide dThinkingGlassesShining
        show dThinkingGlassesShineDark
        stop music
        dThinking "{cps=1}.....{/cps}"
        play music dariamainbgm volume 0.5 
        hide bgroomdark 
        hide dThinkingGlassesShineDark
        show dThinkingGlassesShining
        show bgkitchen
        mc "Okay!"


    mc "Do you have any specific dietary requirements?"
    hide dThinkingGlassesShineDark
    show dThinking at center



    


    



    d "I hope this is sufficient for the chef to work with."
    mc "Wh- Uhh-, yeah! That's perfect!... I think."

    call act2
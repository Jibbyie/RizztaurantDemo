# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# Chef Rizz drawings
image cr = "ChefRizz.png"
image cr2 = "ChefRizz.png"
image crNoCallback = "CheffRizz.png"
image crDark = "CheffRizzDark.png"
image crAwkward = "ChefRizzAwkward.png"
image crCooking = "ChefRizzCooking.png"
image crEyeClosed = "ChefRizzEyeClosed.png"
image crEyebrowRaise = "ChefRizzEyebrowRaise.png"

# Chef Emotions
image chefSweat = "ChefRizzSweat.png"
image chefKiss = "ChefRizzKiss"
image chefKissSmudged = "ChefRizzKissSmudged"

# Daria drawings
image d = "Daria.png"
image d2 = "DariaHappy.png"
image d3 = "DariaAngryLarge.png"
image dHappy = "DariaHappy.png"
image dHorny = "DariaHorny.png"
image dAngry = "DariaAngryLarge.png"
image dFlushed = "DariaFlushed.png"
image dDetective = "DetectiveDaria.png"
image dDetectiveGlare = "DetectiveDariaGlare.png"
image dAngryLarge = "DariaAngryLarge.png"
image dAngrySmall = "DariaAngrySmall.png"
image dSweat = "DariaSweat.png"
image dGlare = "DariaGlare.png"
image dGlassesShine = "DariaGlassesShine.png"
image dThinking = "DariaThinking.png"
image dThinkingDark = "DariaThinkingDark.png"
image dThinkingGlassesShining = "DariaThinkingGlassesShine.png"
image dThinkingGlassesShineDark = "DariaThinkingGlassesShineDark.png"


# Daria's emotions
image flushed = "Flushed.png"
image horny = "Horny.png"
image sweat = "Sweat.png"
image glare = "Glare.png"
image angrylarge = "AngryLarge.png"
image angrysmall = "AngrySmall.png"
image glasshesShine = "GlassesShine.png"
image dfb = "DetectiveFedoraBadge.png"
image dThinkingGlassesShine = "ThinkingGlassesShine.png"

# Misc
image rizztaurantmenu = "menu.png"
image halfblack = "#00000088"
image black = "#000000ff"

# Backgrounds
image bgroom = "bgkitchen.jpg"
image bgroomdark = "bgkitchendark.png"
image bgkitchen1dark = "bgkitchen1dark.png"
image doombackground = "doombackground.png"

# Animations
image daria angry:
    "AngryLarge.png"
    pause 0.3
    "AngrySmall.png"
    pause 0.3
    repeat

image daria glasses shine:
    "Daria.png" with Dissolve(0.2)
    "GlassesShine.png" with Dissolve(0.6)
    pause 1.0
    "Daria.png" with Dissolve(0.2)
    pause 0.5 
    repeat

image chef wink:
    "ChefRizz.png"
    pause 0.2
    "ChefRizzEyeClosed.png"
    pause 0.4
    "ChefRizz.png"

# Defaults
default playerName = ""
default likes = ""
default dislikes = ""
default current_input = "likes"
default show_quick_menu = True

# Preferences Defaults
default cuisine_preferences = []
default flavour_preferences = []
default dietary_preferences = []
default consistency_preferences = []
default points = 0

# MC and effects definitions
define mc = Character("[playerName]", what_slow_cps=30)
define mcthinking = Character("[playerName]", what_slow_cps=30, what_prefix="{i}(", what_suffix="){/i}")
define flashbulb = Fade(0.2, 0.0, 0.4, color='#fff') 
define audio.background = "rizztaurantambience.mp3"

# Transforms/transform animations
transform half_size:
    zoom 0.5
transform speaking:
    ease 0.2 zoom 1.03
transform not_speaking:
    ease 0.2 zoom 1.0
transform bounce:
    pause .05
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat
transform shake:
    pause .001
    xoffset 0
    easein .175 xoffset -1
    easeout .175 xoffset 1
    easein .175 xoffset -1
    easeout .175 xoffset 1
    xoffset 0
    repeat
transform laugh:
    pause .01
    yoffset 0
    easein .175 yoffset -10
    easeout .175 yoffset 0
    easein .175 yoffset -4
    easeout .175 yoffset 0
    yoffset 0
    repeat
transform walking:
    pause .01
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    easein .175 yoffset -8
    easeout .175 yoffset 0
    yoffset 0
transform running:
    yoffset 0
    easein .175 yoffset -20
    easeout .175 yoffset 0
    easein .175 yoffset -8
    easeout .175 yoffset 0
    yoffset 0
    repeat
    
transform leftoffscreen:
    xalign -3.0

# Text callbacks for speaking
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

        elif renpy.showing("dHorny"):
        
            if event == 'begin': 
                renpy.show("dHorny", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dHorny", zorder=0, at_list=[not_speaking])
        
        
        elif renpy.showing("dAngry"):
        
            if event == 'begin': 
                renpy.show("dAngry", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dAngry", zorder=0, at_list=[not_speaking])

        elif renpy.showing("dFlushed"):
        
            if event == 'begin': 
                renpy.show("dFlushed", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dFlushed", zorder=0, at_list=[not_speaking])

        elif renpy.showing("dDetective"):
        
            if event == 'begin': 
                renpy.show("dDetective", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dDetective", zorder=0, at_list=[not_speaking])

        elif renpy.showing("dDetectiveGlare"):
        
            if event == 'begin': 
                renpy.show("dDetectiveGlare", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dDetectiveGlare", zorder=0, at_list=[not_speaking])

        elif renpy.showing("dAngryLarge"):
        
            if event == 'begin': 
                renpy.show("dAngryLarge", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dAngryLarge", zorder=0, at_list=[not_speaking])

        elif renpy.showing("dAngrySmall"):
        
            if event == 'begin': 
                renpy.show("dAngrySmall", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dAngrySmall", zorder=0, at_list=[not_speaking])

        elif renpy.showing("dThinking"):
        
            if event == 'begin': 
                renpy.show("dThinking", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dThinking", zorder=0, at_list=[not_speaking])

        elif renpy.showing("dSweat"):
        
            if event == 'begin': 
                renpy.show("dSweat", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dSweat", zorder=0, at_list=[not_speaking])

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

        elif renpy.showing("dThinkingDark"):
        
            if event == 'begin': 
                renpy.show("dThinkingDark", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dThinkingDark", zorder=0, at_list=[not_speaking])

        elif renpy.showing("dThinkingGlassesShine"):
        
            if event == 'begin': 
                renpy.show("dThinkingGlassesShine", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dThinkingGlassesShine", zorder=0, at_list=[not_speaking])
        
        elif renpy.showing("dThinkingGlassesShineDark"):
        
            if event == 'begin': 
                renpy.show("dThinkingGlassesShineDark", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("dThinkingGlassesShineDark", zorder=0, at_list=[not_speaking])

    def chefRizz_callback(event, interact=True, **kwargs):
        if not interact: 
            return
            ## If the character is currently shown on screen, this will search for the character 'tag'
        if renpy.showing("cr"):
        
            if event == 'begin': 
                renpy.show("cr", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("cr", zorder=0, at_list=[not_speaking])

        elif renpy.showing("cr2"):
        
            if event == 'begin': 
                renpy.show("cr2", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("cr2", zorder=0, at_list=[not_speaking])
        
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
        
        elif renpy.showing("crEyeClosed"):
        
            if event == 'begin': 
                renpy.show("crEyeClosed", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("crEyeClosed", zorder=0, at_list=[not_speaking])

        elif renpy.showing("crEyebrowRaise"):
        
            if event == 'begin': 
                renpy.show("crEyebrowRaise", zorder=10, at_list=[speaking])
                
            elif event == 'end': 
                renpy.show("crEyebrowRaise", zorder=0, at_list=[not_speaking])

# Chef Rizz
define cr = Character("Chef Rizz", image="ChefRizz.png", what_slow_cps=30, callback=chefRizz_callback)
define cr2 = Character("Chef Rizz", image="ChefRizz.png", what_font="Tangerine_Bold.ttf", what_size=60, what_slow_cps = 20, callback=chefRizz_callback, what_prefix="{i}", what_suffix="{/i}")
define crAwkward = Character("Chef Rizz", image="ChefRizzAwkward.png",  what_slow_cps=30, callback=chefRizz_callback)
define crEyeClosed = Character("Chef Rizz", image="ChefRizzEyeClosed.png",  what_slow_cps=30, callback=chefRizz_callback)
define crEyebrowRaise = Character("Chef Rizz", image="ChefRizzEyeClosed.png",  what_slow_cps=30, callback=chefRizz_callback)
define crCooking = Character("Chef Rizz", image="ChefRizzCooking.png",  what_slow_cps=30, callback=chefRizz_callback)

# Daria
define d = Character("HiraganaLover95", image="Daria.png", what_slow_cps=50, callback=daria_callback)
define dHappy = Character("HiraganaLover95", image="DariaHappy.png", what_slow_cps=50, callback=daria_callback)
define dHorny = Character("HiraganaLover95", image="DariaHorny.png", what_slow_cps=50, callback=daria_callback)
define dAngry = Character("HiraganaLover95", image="DariaAngryLarge.png", what_slow_cps=50, callback=daria_callback)
define dThinking = Character("HiraganaLover95", image="DariaThinking.png", what_slow_cps=40, callback=daria_callback)
define dFlushed = Character("HiraganaLover95", image="DariaFlushed.png", what_slow_cps=50, callback=daria_callback)
define dDetective = Character("HiraganaLover95", image="DetectiveDaria.png", what_slow_cps=50, callback=daria_callback)
define dDetectiveGlare = Character("HiraganaLover95", image="DetectiveDariaGlare.png", what_slow_cps=50, callback=daria_callback)
define dAngryLarge = Character("HiraganaLover95", image="DariaAngryLarge.png", what_slow_cps=50, callback=daria_callback)
define dAngrySmall = Character("HiraganaLover95", image="DariaAngrySmall.png", what_slow_cps=50, callback=daria_callback)
define dSweat = Character("HiraganaLover95", image="DariaSweat.png", what_slow_cps=50, callback=daria_callback)
define dGlare = Character("HiraganaLover95", image="DariaGlare.png", what_slow_cps=50, callback=daria_callback)
define dGlassesShine = Character("HiraganaLover95", image="DariaGlassesShine.png", what_slow_cps=50, callback=daria_callback)
define dThinkingDark = Character("HiraganaLover95", image="DariaThinkingDark.png", what_slow_cps=50, callback=daria_callback)
define dThinkingGlassesShine = Character("HiraganaLover95", image="DariaThinkingGlassesShine.png", what_slow_cps=50, callback=daria_callback)
define dThinkingGlassesShineDark = Character("HiraganaLover95", image="DariaThinkingGlassesShineDark.png", what_slow_cps=50, callback=daria_callback)

# The game starts here.
label start:
    scene black
    label chooseName:
        $playerName = renpy.input("What is your name?", length=10)
        $playerName = playerName.strip()
        $playerName = playerName.lower()
        if playerName == "": 
            $playerName="Joe Momma"
        if playerName =="HiraganaLover95".lower() or playerName=="Chef Rizz".lower():
            "Please choose a different name, not one that is already an NPC!"
            jump chooseName
    call act1
    call act2

    return
 
# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image irritatedAura = "irritatedAura.png"
image cr = "ChefRizz.png"
image crNoCallback = "CheffRizz.png"
image crDark = "CheffRizzDark.png"
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
image black = "#00000000"

default playerName = ""
define mc = Character("[playerName]", color="#000000", what_slow_cps=30)
define cr2 = Character("Chef Rizz", image="CheffRizz.png")

default likes = ""
default dislikes = ""
default current_input = "likes"

# Notebook Screen
screen notepad_screen():
    frame:
        xsize 1400
        ysize 275
        has vbox
        vbox:
            spacing 10
            textbutton "Likes" action SetVariable("current_input", "likes")
            textbutton "Dislikes" action SetVariable("current_input", "dislikes")

            if current_input == "likes":
                input:
                    default likes
                    value VariableInputValue('likes')
                    length 75 # Adjust the length as needed
            else:
                input:
                    default dislikes
                    value VariableInputValue('dislikes')
                    length 75  # Adjust the length as needed

            textbutton "Close Notepad" action Return()


screen nt_button:
    textbutton "Notepad" action ShowMenu('notepad_screen')

define flashbulb = Fade(0.2, 0.0, 0.4, color='#fff') 

define audio.background = "rizztaurantambience.mp3"

image bgroom = "bgkitchen.jpg"
image bgkitchen1 = "bgkitchen1.png"
image bgkitchen1dark = "bgkitchen1dark.png"
image doombackground = "doombackground.png"

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
image d1 = "Daria.png"
image d2 = "DariaHappy.png"
image d3 = "DariaAngry.png"
define dHappy = Character("Daria", image="DariaHappy.png", callback=daria_callback)
define dAngry = Character("Daria", image="DariaAngry.png", callback=daria_callback)
define dSparkle = Character("Daria", image="DariaSparkle.png", callback=daria_callback)
define dGlare = Character("Daria", image="DariaGlare.png", callback=daria_callback)
define dGlassesShine = Character("Daria", image="DariaGlassesShine.png", callback=daria_callback)


# The game starts here.
label start:
    scene black
    label chooseName:
        $playerName = renpy.input("What is your name?", length=10)
        $playerName = playerName.strip()
        if playerName == "":
            $playerName="Joe Momma"
        if playerName=="Daria".lower() or playerName=="Chef Rizz".lower():
            "Please choose a different name, not one that is already an NPC!"
            jump chooseName
    call act1
    call act2

    return
 
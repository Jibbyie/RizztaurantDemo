# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

image cr = "ChefRizz.png"
image d = "Daria.png"

image bgroom = "bgkitchen.jpg"

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

define cr = Character("Chef Rizz", image="ChefRizz.png", callback=chefRizz_callback)
define d = Character("Daria", image="Daria.png", callback=daria_callback)

# The game starts here.

label start:

    scene bgroom
    show bgroom

    show cr at center
    show d at left

    "Wait.. who are you guys again?"

    d "I'm Daria!"
    cr "And I'm Chef Rizz!"
    d "We're here to help you with your cooking!"
    cr "We're going to teach you how to make a delicious meal!"

    "You guys are weird..."


    return

# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define CR = Character("Chef Rizz")
image ChefRizz neutral = "ChefRizz.png"
image bgroom = "bgkitchen.jpg"

# The game starts here.

label start:

    scene bgroom
    show bgroom
    show ChefRizz neutral


    CR "Hey Gurl"


    return

label act2:
   # Act 2, Chef Rizz intro and kitchen scene
   stop music fadeout 1.0

   play sound walking
   hide d with Dissolve(1.0)

   hide bgroom with Dissolve(0.5)
   show bgkitchen1dark with Dissolve(4.0)
   show crDark:
      xalign 2.0

   mc "Chef! We've got a customer!"
   mc "{i}Where are those damned lights..{/i}"
   play sound chefdoor volume 0.2
   $ renpy.pause(7.2)
   "{cps=10}{i}A customer you say?...{/i}{/cps}"

   play music cheffintromusic volume 1.0 fadein 0.5

   show crDark at center
   with MoveTransition(11.0)

   scene bgkitchens 
   show crNoCallback at center
   with flashbulb
   cr2 "{cps=15}{i}How can I be of service?{/i}{/cps}"
   hide crNoCallback

   show cr at center behind Sparkle

   cr "I love you"
   show Sparkle zorder 2000:
      ypos -0.15
      xalign 0.589
   cr "Meow"
   # mc "She says she likes [likes], and dislikes [dislikes]."
   
    
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
   mc "Chef??"
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
   cr "{cps=18}{i}How can I be of service?{/i}{/cps}"
   hide crNoCallback
   show cr at center
   mc "Did you time your entry with the music and the lights Chef?"
   cr "{cps=18}{i}What music?{/i}{/cps}"
   mc "The music blaring over the kitchen speakers, Chef."
   cr "{cps=18}{i}Oh, aha, how quaint, I didn't even notice such an alluring melody had begun to play.{/i}{/cps}"
   mc "Of course you didn't Chef."
   stop music

   cr "*Ahem*"
   play music chefambience fadein 1.5 volume 0.5
   cr "A customer?"
   cr "Are you sure it's not another youtuber thinking this place is haunted?"
   mc "I'm very sure Chef, she's an... eccentric young woman."
   cr "{cps=18}{i}A young woman you say?..{/i}{/cps}"
   cr "{cps=18}{i}My oh my.. I better go introduce myself..{/i}{/cps}"
   play sound running volume 0.5
   show cr at running, leftoffscreen
   with MoveTransition(2.0)
      
   mc "Hold your horses there Chef!"
   play sound rewind volume 0.5
   show cr at laugh, center
   with MoveTransition(1.0)
   show cr at center
   mc "Remember what happened last time?"
   cr "What do you mean?"
   mc "You stole a good customers' girlfriend from him on the spot."
   cr "Oh.. how forgetful I can be. She deserved someone better anyways."
   mc "How could you possibly know that, we had just catered to them for not even a good 10 minutes."
   cr "When you've spent enough time around women as I have [playerName], you'll know."
   mc "That doesn't even make sens-, anyways that's besides the point. She is a real customer, human as far as I can tell and I know she is starving."
   mc "We haven't had business in forever, this is important for us to keep this place running."
   cr "Don't even worry about it sweetheart. Daddy's loaded."
   cr "I can keep this place afloat for years to come."
   mc "That's not the point i'm trying to make Chef. Not the finances. We are going to need to maintain the image of a functioning restaurant here."
   mc "We need to keep your.. benefactors happy."
   cr "Oh don't worry sugarplum, my bosses love me."
   mc "{i}(His bosses huh? If only Chef really knew about the people he was working under.){/i}"
   show cr at walking:
      linear 0.5 xalign 0.3
   mc "{i}(Or the fact this whole restaurant is a money laundering business for a cartel.){/i}"
   show cr at walking:
      linear 0.5 xalign 0.7
   mc "{i}(I wonder how he'd react if he knew, heck, I'm surprised he doesn't know considering he worked as a bodyguard for them for so many years.){/i}"
   show cr at center:   
      parallel:
         ease 4.0 zoom 2.8
      parallel:
         yalign 0.0 xalign 0.7
         linear 0.5 yalign 0.18  #or whatever fit.
   mc "{i}(What did they even make him do?){/i}"
   mc "{i}(I've never met someone so charismatic that they just throw money at him like nothing.)"
   "{i}You okay there kitten whiskers? You seem a little lost in thought..{/i}"
   mc "Jesus Chef when did you get so close!"
   hide cr
   show cr:
      xalign 0.5
      yalign 0.5
   show cr at center:
      ease 0.5
   cr "Just making sure you're alright sugar."
   mc "Anyways, don't you remember what you told me?"
   mc "You wanted to be the greatest chef in the world?"
 

   # show cr at center behind Sparkle

   # cr "I love you"
   # show Sparkle zorder 2000:
   #    ypos -0.18
   #    xalign 0.589
   # cr "Meow"
   # mc "She says she likes [likes], and dislikes [dislikes]."
   
    
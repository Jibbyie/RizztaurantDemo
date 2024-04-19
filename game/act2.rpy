label act2:
   # Act 2, Chef Rizz intro and kitchen scene
   
   stop music fadeout 1.0

   play sound walking noloop
   hide d with Dissolve(1.0)

   hide bgroom with Dissolve(0.5)
   show bgkitchen1dark with Dissolve(4.0)
   show crDark:
      xalign 2.0

   #Chef's intro
   
   mc "Chef! We've got a customer!"
   mc "Chef??"
   mc "{i}Where are those damned lights..{/i}"
   
   play sound chefdoor volume 0.2 noloop
   $ renpy.pause(7.2, hard=True)
   
   "{cps=20}{i}{font=Tangerine_Bold.ttf}{size=60}A customer you say?...{/font}{/size}{/i}{/cps}"
   

   play music cheffintromusic if_changed volume 1.0 fadein 0.5
   show crDark at center
   with MoveTransition(11.0)
   scene bgkitchens 
   show crNoCallback at center
   with flashbulb
   
   cr2 "How can I be of service?"
   hide crNoCallback
   
   # Chef introduced
   show cr at center
   mc "Did you time your entry with the music and the lights Chef?"
   hide cr
   show cr2 at center
   cr2 "What music?"
   mc "The music blaring over the kitchen speakers, Chef."
   cr2 "Oh, aha, how quaint, I didn't even notice such an alluring melody had begun to play."
   mc "Of course you didn't Chef."
   stop music
   hide cr2
   show cr

   cr "*Ahem*"
   play music chefambience fadein 1.5 volume 0.5
   cr "A customer?"
   cr "Are you sure it's not another youtuber thinking this place is haunted?"
   mc "I'm very sure Chef, she's an... eccentric young woman."
   hide cr
   show crEyebrowRaise at center
   cr2 "A young woman you say?.."
   hide crEyebrowRaise
   show cr2
   hide cr2
   show cr
   cr2 "My oh my.. I better go introduce myself.."
   
   play sound running volume 0.5
   
   show cr at running, leftoffscreen
   with MoveTransition(2.0)
   
   
   mc "Hold your horses there Chef!"
   
   play sound rewind volume 0.5
   show cr at laugh, center
   with MoveTransition(1.0)
   show cr at center
   
   mc "Remember what happened last time?"
   cr "What could you possibly be referring to?"
   mc "You stole a good customers' girlfriend from him on the spot."
   cr "Oh.. how forgetful I can be. She deserved someone better anyways."
   mc "How could you possibly know that? We only catered to them for not even a good 10 minutes."
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
   show cr at walking, center:   
      parallel:
         ease 4.0 zoom 2.8
      parallel:
         yalign 0.0 xalign 0.7
         linear 0.5 yalign 0.18  #or whatever fit.
   mc "{i}(What did they even make him do?){/i}"
   mc "{i}(I've never met someone so charismatic that they just throw money at him like nothing.)"
   "{i}{font=Tangerine_Bold.ttf}{cps=20}{size=60}You okay there kitten whiskers? You seem a little lost in thought..{/size}{/font}{/cps}{/i}"
   
   show bgkitchens with hpunch
   
   mc "Jesus Chef when did you get so close!"
   hide cr
   show cr:
      xalign 0.5
      yalign 0.5
   show cr at center:
      ease 1.5
   hide cr
   show chef wink
   cr "Just making sure you're alright sugar."
   mc "Jesus- anyways, don't you remember what you told me?"
   hide chef wink
   show cr
   mc "You wanted to be the greatest chef in the world?"
   mc "This is your chance to prove it!-"
   
   play sound phoneringing volume 0.2
   show bgkitchens with vpunch
   $ renpy.pause(3.0, hard=True)
   
   
   cr "Pardon me sugar, I think that's my phone, would you be a doll and pick it up and put it on speaker for me?"
   play sound iphoneunlock volume 0.5
   mc "*Sigh*, make it quick Chef."
   hide cr
   show cr2

   cr2 "Hey babygirl, is this who I think it is?"
   
   play sound call1 
   $ renpy.pause(1.0, hard=True)
   
   cr2 "I'd never forget you baby, you know you're important to me."
   play sound call2
   
   $ renpy.pause(1.0, hard=True)
   
   cr2 "Alright, alright, dinner this Friday at 9, wear that nice dress and the lacey underwear that I love."
   play sound call3
   
   $ renpy.pause(2.0, hard=True)
   
   cr2 "You know Daddy's got you kitten. Anything you want and it's yours."
   play sound call4
   
   $ renpy.pause(3.0, hard=True)
   
   cr2 "Till we meet again Princess. Mwah~♡"
   hide cr2
   show cr

   mcthinking "I think I just threw up a little."
   

   # show cr at center behind Sparkle

   # cr "I love you"
   # show Sparkle zorder 2000:
   #    ypos -0.18
   #    xalign 0.589
   # cr "Meow"
   # mc "She says she likes [likes], and dislikes [dislikes]."
   
    
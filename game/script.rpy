# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"
 
    
    

define urname = 'You'

image letter = "letter.jpeg"
image bg classroom = "classroom.jpg"
image bg hallway = "hallway.jpg"

image ms-joy = im.FactorScale("mitsuki-joy.png", 0.15)
image ms-ang = im.FactorScale("mitsuki-angry.png", 0.8)
image ms-con = im.FactorScale("mitsuki-concerned.png", 0.8)
image ms-neu = im.FactorScale("mitsuki-neutral.png", 0.8)
image ms-sup = im.FactorScale("mitsuki-surprised.png", 0.8)


# Declare characters used by this game.
define n  = Character('' , color ="#36d1cb")
define mc = Character("[urname]", color="#c8ffc8")
define ms = Character("Mitsuki", color="#c8ffc8")
define l = Character("???", color="#efb41f")

define emotions = ["angry","joy","","",""]
define temp =""
define broad = False
    

# The game starts here.
label start:
    scene bg classroom
    $ urname =renpy.input("What is your name?") or "Dat Boi"
    
    n "You’re in a classroom and the bell is about to ring. You’re anxious and really want to leave."
    n "Bell rings."
    
    l "[urname]-chan! Wait Up!"

    n "It's Mitsuki, your best friend since grade school."

    n  "Mitsuki runs up to greet you."
    
    show ms-joy
    ms "[urname]! How are you?"
    

    menu:
        "I'm good!":
            
            python:
               import response
               temp = response.Reaction().get_mood()
               
            if temp == "anger" or temp == "sorrow":
               show ms-con
               ms "Really? You don’t look so good."
               jump first
            elif temp == "joy":
               show ms-joy
               ms "That’s great to hear! When you’re happy, I’m happy!"
               jump second
            elif temp == "surprise":
               show ms-sup
               ms "Tell me about it. You look like you’ve seen a ghost."
               jump first
            else:
               show ms-joy
               ms "That’s great to hear! When you’re happy, I’m happy!"
               jump second
            
        "I've been better.":
        
            python:
               import response
               temp = response.Reaction().get_mood()
               
            if temp == "sorrow":
               show ms-con
               ms "What’s the matter? You seem upset."
               jump first
            elif temp =="anger":
               show ms-sup
               ms "Whoa, chill out! What’s wrong?"
               jump first
            elif temp == "joy":
               show ms-joy
               ms "Too real."
               jump second
            elif temp == "surprise":
               show ms-con
               ms "Tell me about it. You look like you’ve seen a ghost."
               jump first
            else:
               show ms-joy
               ms "Too real."
               jump second
        
    label first:
    
       menu:
           "I'm fine!":
              jump third
           "You know that one girl that always sits next to me?":
              jump fourth
    
    label second:
       mc "Well..."
       mc "You know that one girl that always sits next to me?"
       jump fourth
    
    label third:
       python:
          import response
          temp = response.Reaction().get_mood()
       
       if temp == "joy":
          show ms-ang
          ms "You’re a terrible liar. What’s really going on?"
          mc "You know that one girl that always sits next to me?"
       elif temp == "anger" or temp == "surprise":
          show ms-ang
          ms "Man, what is up with you?"
          mc "You know that one girl that always sits next to me?"
       elif temp == "sorrow":
          show ms-con
          ms "Hey, cheer up! I’m sure you’ll get through this… You sure you don’t want to talk about it?"
          mc "You know that one girl that always sits next to me?"
       else:
          show ms-ang
          ms "You’re a terrible liar. What’s really going on?"
          mc "You know that one girl that always sits next to me?"

    label fourth:
       ms "You mean Sayako? Yeah, I do. Why?"
       menu:
          "She's a total broad.":
             $ broad = True
             ms "What’d she do this time?"
             mc "She tried to cheat off my quiz."
          "She tried to cheat off my quiz.":
             jump fifth
                 
    label fifth:
       show ms-ang
       ms "That's horrible! But I'm not surprised."
       menu:
          "Yeah... I should talk to her.":
             jump sixth
          "it's fine, I didn't do that well anyway.":
             jump seventh
    label sixth:
        python:
          import response
          temp = response.Reaction().get_mood()
    
    if temp == "joy":
        show ms-ang
        ms "Why do I get the feeling you’re about to say something stupid to her?"
        mc "Too late. She’ll get what’s coming to her"
        jump eighth
    elif temp == "anger":
        show ms-con
        ms "I think you should take some time to clear your head first."
        mc "Yeah, you're probably right."
        jump ninth
    elif temp == "sorrow":
        show ms-con
        ms "You sure? You don’t look so good."
        mc "Yeah, I’m gonna go home."
        jump ninth                       
    elif temp == "surprise":
        show ms-neu
        ms "Yeah… you should."
        mc "I have a bad feeling bad about this..."
        jump eighth
    else:
        show ms-ang
        ms "Why do I get the feeling you’re about to say something stupid to her?"
        mc "Too late. She’ll get what’s coming to her"
        jump eighth
        
    label seventh:
        python:
           import response
           temp = response.Reaction().get_mood()
           
        if temp == "joy":
           show ms-joy
           ms "You're such a jerk lmao."
           mc "I know. ;)"
           jump eighth
        else:
           show ms-joy
           ms "You don’t need to be that hard on yourself. I’m sure you did fine."
           mc "Yeah, I’m fine. {i}Everything’s fine.{/i}"
           jump ninth
    
    # Part 2          
           
    label eighth:
       scene bg hallway
       with dissolve
       
       l "Hey, watch where you're going, jerk!"
       
       n "You bump into Sayako, standing outside the door."
       
          menu:
             "Oh, hey Sayako! I'm really sorry!":
                jump tenth
             "Wait... were... you spying on me? O_o":
                jump eleventh
                
    label ninth:
       scene bg hallway
       with dissolve
       
       n "You start walking down the hallway when you hear Sayako."
       
       if broad == True:
          show ms-ang
          

    return
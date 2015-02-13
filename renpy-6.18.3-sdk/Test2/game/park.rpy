# PARK


label park:
    
    scene bg park
    with fade
    
    label park_menu:
        with dissolve
        
        $ updateSound("park")
        
        
        $ av = checkAvailable(park_sched)
        
            
        if av != True:
            "The park seems to be closed.. You'll have to come back some other time.."
            jump map
        else:
        
        
            if time_of_day >= 5:
                "It's getting late, so you should probably head back to your dorm room."
                jump dorm
            
            menu:
                with dissolve
                
                "Relax \n {size=-8} +sta":
                    "You sit down on an empty nearby bench to take a short break and take your mind off things."
                    
                    scene black
                    with dissolve
                    "..."
                    "....."
                    "......."
                    $ success = checkSuccess(.9)
                    
                    
                    scene bg park
                    with dissolve
                    
                    if success:
                        "After almost falling asleep, you stand up and stretch, realizing how much tension that was previously affecting your body has now faded away."
                        $ amt = getStatValue(10,20)
                        $ p.sta += amt
                        "[amt] of you stamina points have been recovered!"
                    else:
                        ".. You couldn't relax, as noisy people seemed to swarm the park today.."
                        "You almost feel as though you're more stressed out now that you were before.."
                        
                    $ time_of_day += 1
                    jump park_menu
                    
                    
                    
                "Talk with people \n {size=-8} -Sta +Cou {/size}":
                    "You decided to muster up the courage to talk to the person sitting on the bench next to you."
                    scene black
                    with dissolve
                    "..."
                    "....."
                    "......."
                    $ success = checkSuccess(.6)
                    
                    scene bg park
                    with dissolve
                    
                    if success:
                        python:
                            
                            kno_success = checkSuccess(.75)
                            cha_success = checkSuccess(.75)
                            
                            cou_amt = getStatValue(1,2)
                            kno_amt = getStatValue(1,2)
                            cha_amt = getStatValue(1,2)
                        "Despite your initial fear, you were able to have a pleasant conversation with the stranger."
                        if kno_success:
                            "you learned a lot of new interesting things talking to them!"
                        if cha_success:
                            "You also feel that you have learned how to communicate your thoughts and feelings more effectively."
                        
                            
                        $ p.cou += cou_amt
                        "Your courage has increased by [cou_amt]!"
                        if kno_success:
                            $ p.kno += kno_amt
                            "Your knowledge has incresed by [kno_amt]!"
                        if cha_success:
                            $ p.cha += cha_amt
                            "your charm has increased by [cha_amt]!"
                            
                    
                    
                    else:
                        ".. You ended up fumbling over your words and accidentally saying things you didn't mean to..."
                        "Eventually, the stranger just moved to another bench to get away from you.."
                        
                    $ amt = getStatValue(8,12)
                    $ subtractSta(-amt)
                    
                    
                    
                    
                    $ time_of_day += 1
                    jump park_menu
                    
                    
                    
                "More stuff...":
                    "You did more stuff."
                    jump park_menu
                "Return to Town":
                    "You decide to head back into town.."
                    jump map
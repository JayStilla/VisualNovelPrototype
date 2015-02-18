label dorm:
    scene bg dorm
    with fade
    
    
    label dorm_menu:
        
        $ updateMusic("dorm")
        
        menu: 
            with dissolve
            
            "Read \n {size=-8} +Sta +Cha {/size}":
                
                if checkTime(1):
                    "You decide to relax a bit and read a book."
                    scene black
                    with dissolve
                    "..."
                    "....."
                    "......."
                    $ success = checkSuccess(0.75)
                    
                    $ renpy.pause(1.0)
                    
                    scene bg dorm
                    with dissolve
                    
                    if success:
                        "You were able to engage in the story and relate to the characters portrayed on an emotional level."
                        $ amt = getStatValue(1,3)
                        $ p.cha += amt
                        "Your charm has increased by [amt]!"
                        $ amt = getStatValue(1,5)
                        $ p.sta += amt
                        "[amt] of your stamina points have been recovered!"
                        
                    else:
                        "It just isn't your day... You can't seem to focus and ended up spacing out for half the time.."
                        
                        $ amt = getStatValue(1,5)
                        $ p.sta += amt
                        "[amt] of your stamina points have been recovered!"
                        
                    $ time_of_day += 1
                    
                else:
                    
                    $ result = allNighter("{size=-8} --Sta ++Cha {/size}")
                    
                    if result:
                        scene black
                        with dissolve
                        "You decide to spend the entire night reading.."
                        $ advDay()
                        $ renpy.pause(0.5)
                        scene bg dorm
                        with dissolve
                        "You're exhausted, but it was definitely worth it. You managed to finish the entire novel!"
                        
                        $ amt = getStatValue(3,5)
                        $ p.cha += amt
                        
                        "Your charm has increased by [amt]!"
                        
                        $ amt = getStatValue(8,15)
                        $ subtractSta(-amt)
                    else:
                        jump dorm_menu
                            
                            
                            
                jump dorm_menu
                
                
                
                
        
            "Watch TV \n {size=-8} +Sta {/size}":
                
                if checkTime(1):
                    "You decided to take a break and watch some TV."
                    scene black
                    with dissolve
                    "..."
                    "....."
                    "......."
                    $ success = checkSuccess(0.65)
                    
                    $ renpy.pause(1.0)
                    
                    scene bg dorm
                    with dissolve
                    
                    if success:
                        "You feel some of your stress and anxiety melt away as you lose yourself in the plot of some of your favorite TV shows."
                        $ amt = getStatValue(5,10)
                        $ p.sta += amt
                        "[amt] of your stamina points have been recovered!"
                        
                    else:
                        ".. Nothing good seemed to be on, so you ended up aimlessly channel surfing for most of the time. But I guess that beats actually doing anything productive.."
                        $ amt = getStatValue(2,5)
                        $ p.sta += amt
                        "[amt] of your stamina points have been recovered!"
                        
                    $ time_of_day += 1
                    
                else:
                    "It's a little too late for that..."
                jump dorm_menu
                
                
                
            "Study \n {size=-8} -Sta +Kno {/size}":
                if checkTime(1):
                    "You decided to do some studying."
                    scene black
                    with dissolve
                    "..."
                    "....."
                    "......."
                    $ success = checkSuccess(0.8)
                    
                    $ renpy.pause(1.0)
                    
                    scene bg dorm
                    with dissolve
                    
                    if success:
                        "You flew through the chapters with ease, getting more done than you were even orinally planning to."
                        $ amt = getStatValue(1,5)
                        $ p.kno += amt
                        "You knowledge has increased by [amt]!"
                    else:
                        ".. Things aren't making sense to you.. You keep reading over the chapter, but these concepts are just so foreign.. Maybe your luck will be better next time.."
                    
                    
                    $ time_of_day += 1
                    
                    $ amt = getStatValue(5,8)
                    $ subtractSta(-amt)
                    
                    
                else:
                    #"You don't feel like you'll have enough time to get much done at this point.."
                    $ result = allNighter("{size=-8} --Sta ++Cha {/size}")
                    if result:
                        scene black
                        with dissolve
                        "You decide to spend the entire night studying.."
                        $ advDay()
                        $ renpy.pause(0.5)
                        scene bg dorm
                        with dissolve
                        "5 cups of coffee later, you see the sun rising."
                        "You managed to get a lot done!"
                        
                        $ amt = getStatValue(3,5)
                        $ p.cha += amt
                        
                        "Your knowledge has increased by [amt]!"
                        
                        $ amt = getStatValue(8,15)
                        $ subtractSta(-amt)
                        
                    else:
                        jump dorm_menu
                
                jump dorm_menu
                
                
            "Sleep \n {size=-8} +++Sta {/size}":
                
                if time_of_day < 5:
                    "There is still time left in the day."
                    menu:
                        "Go to bed early?"
                        "Yes \n ++++Sta":
                            "You decide to turn in early today.. Some extra sleep could do you good.."
                            
                            stop music fadeout 1.0
                            
                            scene black
                            with dissolve
                            
                            
                            $ renpy.pause(2)
                            
                            $ advDay()
                            
                            $ updateMusic("dorm")
                            
                            scene bg dorm
                            with dissolve
                            
                            "You wake up feeling great! You can feel the effect of the extra sleep kicking in"
                            $ amt = getStatValue(25,35)
                            $ p.sta += amt
                            "[amt] of your stamina points have been recovered!"
                            
                        "No":
                            jump dorm_menu
                    
                else:
                    menu:
                        "Turn in for the day?"
                        
                        "Yes":
                            "You decide to turn in for the day.. You can get an early start on things tomorrow.."
                            scene black
                            with dissolve
                            
                            $ success = checkSuccess(0.6)
                            
                            $ renpy.pause(2)
                            
                            $ advDay()
                            
                            scene bg dorm
                            with dissolve
                            
                            if success:
                                "You wake up feeling refreshed and ready to start the day."
                                $ amt = getStatValue(20,30)
                                $ p.sta += amt
                                "[amt] of your stamina points have been recovered!"
                            else:
                                ".. You wake up feeling a little strange after having a really weird dream... I hope this isn't a bad omen for how the rest of the day is going to go.."
                                $ amt = getStatValue(10,20)
                                $ p.sta += amt
                                "[amt] of your stamina points have been recovered!"
                        "No":
                            jump dorm_menu
                
                
                
                jump dorm_menu
            "Return to Town":
                "You decide to head back into town.."
                jump map
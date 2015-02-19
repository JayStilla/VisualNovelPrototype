label school:
    scene bg school
    with fade
    
    label school_menu:
        
        $ av = checkAvailable(school_sched)
        
        if av != True:
            if time_of_day <= 0:
                "It looks like the school isn't open yet.. You should come back at a later time"
            else:
                "It looks like the school is closed for today.. You'll have to come back tomorrow.."
            jump map
            
        else:
            
            $ updateSound("school")
            
            menu:
                with dissolve
                "temporary menu"
                
                "pass time":
                    $ time_of_day += 1
                    jump school_menu

                "talk to teacher?":
                    menu:
                        "yes":
                            jump teachers_office
                        "no":
                            jump school_menu
                    
                "Return to Town":
                    "You decide to head back into town.."
                    jump map
            jump map

    label teachers_office:
        scene bg teacher
        menu:
            with dissolve
            "still developing"
            
            "Still working on this...":
                jump map
        jump map
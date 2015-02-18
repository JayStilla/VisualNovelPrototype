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
            
            play music amb_school fadein 1 fadeout 1
        
            "put stuff here"
            jump map
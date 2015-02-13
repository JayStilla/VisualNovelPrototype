###################
# OVERWORLD
###################

label overworld:
    
    scene bg city
    with fade
    
    
    menu:
        with dissolve
        "Where should I go..?"
        
        "Intro":
            "You decided to go to the intro.."
            jump main
            with fade
        
        "Go to Dorm":
            "You went back to your dorm room.."
            jump dorm
            
        "Go to Map":
            jump map
    
    
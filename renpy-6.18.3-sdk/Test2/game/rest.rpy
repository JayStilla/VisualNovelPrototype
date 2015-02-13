#RESTAURANT

label rest:
    
    scene bg rest
    with fade
    
    label rest_menu:
        
        $ updateSound("rest")

        $ av = checkAvailable(rest_sched)

        if av != True:
            "The restaurant is Closed right now... Come back later."
            jump map

        else:
            if time_of_day >= 5:
                "It's starting to get late. I should probably head back soon."
                jump dorm

            menu:
                with dissolve

                "Eat \n {size=-8} +sta -money {/size}":
                    "You order the first thing on the menu that sounds appetizing to you."

                    scene black
                    with dissolve
                    "..."
                    "....."
                    "......."
                    $ success = checkSuccess(.9)
                    
                    scene bg rest
                    with dissolve

                    if success:
                        "You weren't even aware of how hungry you were and cleared your plate completely"
                        $ amt = getStatValue(1,5)
                        $ p.sta += amt
                        "[amt] of your stamina was recovered!"

                    else: 
                        "It Didn't taste the way you thought it would..."
                        "You almost wish you never chose to eat here..."

                    $ time_of_day += 1
                    $ amt = getStatValue(2,4)
                    "[amt] dollars were spent on this meal."
                    $ subtractMoney(-amt)
                    jump rest_menu
                
                "Get some Desert \n {size=-8} +sta -money {/size}":
                    "You order some of your favorite ice cream."
                    
                    scene black 
                    with dissolve
                    "..."
                    "....."
                    "......."
                    $ success = checkSuccess(.9)
                    
                    scene bg rest
                    with dissolve
                    
                    if success:
                        "That ice cream was delicious!!!"
                        $ amt = getStatValue(1,5)
                        $ p.sta += amt
                        "[amt] of your stamina was recovered!"
                        
                    else: 
                        "IT WAS ALL MELTED!"
                    
                    $ time_of_day += 1
                    $ amt = getStatValue(2,4)
                    "[amt] dollars were spent on this meal."
                    $ subtractMoney(-amt)
                    jump rest_menu
                    
                "Return to Town":
                    "You decide to head back into town.."
                    jump map
                
                    
        
        "Put stuff here..."
        jump map
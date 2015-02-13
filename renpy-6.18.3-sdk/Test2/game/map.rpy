# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define d = Character('Darth', color="#c8ffc8")

# The game starts here.
label map:
    scene bg map
    with fade
    
    $ updateSound("map")
    $ renpy.music.set_volume(amb_volume, delay=0, channel='amb')
    
    label map_menu:
        $ result = renpy.imagemap("images/hotspot.png","images/hotspot_selected.png",[(125, 480, 800, 600, "school"),
                                                                                    (375, 500, 800, 600, "dorm"),
                                                                                    (325, 300, 800, 600, "park"),
                                                                                    (500, 200, 800, 600, "rest")]) 
        with dissolve
        if result == "school":
            menu:
                with dissolve
                "Go to school?"
                "Yes":
                    jump school
                "No":
                    jump map_menu
            jump main
        if result == "dorm":
            menu:
                with dissolve
                "Go to dorm?"
                "Yes":
                    jump dorm
                "No":
                    jump map_menu
        if result == "park":
            menu:
                with dissolve
                "Go to Park?"
                "Yes":
                    jump park
                "No":
                    jump map_menu
                    
        if result == "rest":
            menu:
                with dissolve
                "Go to Restaurant?"
                "Yes":
                    jump rest
                "No":
                    jump map_menu

# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"


# '$' is used when creating Python statements

# Declare characters used by this game.




# The game starts here.
label main:
    
    
    scene bg club
    with fade
    
    show Player normal at left with dissolve
    $ player_name = renpy.input("Enter a Name")
    $ player_name = player_name.strip()
    $ player = Character(player_name, color=player_color)
    
    show screen stats
    with dissolve
    
    show Bob normal at right with dissolve
    
    show Player surprised
    bob.c "%(player_name)s.. Got it!" with weak_shake
    
    show Player sad
    player "Geez, man. Don't scare me like that.."
    
    show Player normal
    bob.c happy "Here are some stat bonus!" #with dissolve
    
    
    python:
        renpy.pause(1)
        
        p.kno += 10
        renpy.pause(1)
        
        p.cou += 10
        renpy.pause(1)
        
        p.cha += 10
        renpy.pause(1)
    
    player "Oh, um.. Ok... Thanks?"
    
    
    bob.c "Seeya!"
    hide Bob with dissolve
    
    $ renpy.pause(1)
    
    "You decide to return to the overworld.."
    jump map
    
    #return

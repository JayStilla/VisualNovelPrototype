#############
# CHARACTERS
#############
    
init python:
    class actor:
            
            def __init__(self, name, col, tag):
                self.c = Character(name, color=col, image=tag)
                
                self.disp = 5
                
                
                
                
                
                
init python:
    
    
    dir = "images/"

# CHARACTERS
    
    #bob = actor("Bob", "#FFFFFF", ["images/Bob_Normal.png", "images/Bob_Happy.png"])
    
init:
    
    # PLAYER
    image Player normal =      dir+"player/player_normal.png"
    image Player happy =       dir+"player/player_happy.png"
    image Player sad =         dir+"player/player_sad.png"
    image Player surprised =   dir+"player/player_surprised.png"
    
    $ player = Character('default', color="#AA0000", image="Player")
    
    # BOB
    image Bob normal =      dir+"Bob_Normal.png"
    image Bob happy =       dir+"Bob_Happy.png"
    image Bob sad =         dir+"Bob_Sad.png"
    image Bob angry =       dir+"Bob_Angry.png"


    $ bob = actor("Bob", "#FFFFFF", "Bob")
    #define bob = Character("Bob", color="#FFFFFF", image="Bob")
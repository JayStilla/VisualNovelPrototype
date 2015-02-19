# INITIALISE GLOBAL AND PLAYER DATA HERE

# '$' is used when creating Python statements
    
  
            

            
init python:
    

    # disables rollback
    config.rollback_enabled = False
    #define e = Character('Eileen', color="#AA0000")
    player_name = None
    player_color = "#7777BB"
    
    #guy = Actor("Guy", "images/club.jpg", "#AA0000")
    
    class player_stats:
        stat_max = 100
        #hp  = 50
        sta = 50
        kno = 10
        cou = 10
        cha = 10
        money = 100
      
      
        
    p = player_stats
    
    
    
    # Schedules
    park_sched =        [1,5, 0,3]
    school_sched =      [0,6, 1,3]
    rest_sched =        [1,5, 0,3]
    
    
    # 0 = early morning, 
    # 1 = late morning, 
    # 2 = early afternoon, 
    # 3 = late afternoon, 
    # 4 = early evening, 
    # 5 = late evening
    day_of_week = 5
    time_of_day = 3
    
    
    
# BACKROUND IMAGES
    
image bg club =         "images/club.jpg"
image bg city =         "images/overworld.jpg"
image bg dorm =         "images/dorm.jpg"
image bg map =          "images/map_text.jpg"
image bg classroom =    "images/classroom.jpg"
image bg park =         "images/park.jpg"
image bg rest =         "images/restaurant.jpg"
image bg school =       "images/classroom.jpg"
image bg teacher =      "images/teacheroffice.jpg"


# SOUNDS

init python:
    amb_park =          "sounds/amb_park.wav"
    amb_night =         "sounds/amb_night.wav"
    amb_school =         "sounds/amb_classroom.wav"
    amb_rest =          "sounds/amb_restaurant.wav"
    
    sfx_surprise =      "sounds/sfx_surprise.wav"
    sfx_flash =         "sounds/flashback.wav"
    
    
    renpy.music.register_channel("amb", "sfx", True)
    amb_volume = 0.3
    
    
    

 

   
    
screen stats:
    ###############
    # STAT SCREEN #
    ############### 
    frame:
        xalign 0.0
        yalign 0.0
    
        vbox:           # verical box
            #hbox:       # horixontal box
                #text "Health"
            hbox:
                text "Stamina"
            hbox:
                text "Knowledge"
            hbox:
                text "Courage" 
            hbox:
                text "Charm"
            hbox:
                text "Money"
    frame:
        $ xsize = 75
        xalign 0.18
        vbox:           
           # hbox:       
                #$ ui.bar(p.stat_max, p.hp,
                    #xmaximum=xsize,
                    #thumb=None,
                    #thumb_shadow=None)
            hbox:
                $ ui.bar(p.stat_max, p.sta,
                    xmaximum=xsize,
                    thumb=None,
                    thumb_shadow=None)
            hbox:
                $ ui.bar(p.stat_max, p.kno,
                    xmaximum=xsize,
                    thumb=None,
                    thumb_shadow=None)
            hbox:
                $ ui.bar(p.stat_max, p.cou,
                    xmaximum=xsize,
                    thumb=None,
                    thumb_shadow=None)
            hbox:
                $ ui.bar(p.stat_max, p.cha,
                    xmaximum=xsize,
                    thumb=None,
                    thumb_shadow=None)
            hbox:
                $ ui.bar(p.stat_max, p.money,
                    xmaximum=xsize,
                    thumb=None,
                    thumb_shadow=None)
                
    frame:
        xalign 0.27
        vbox:           
            #hbox:       
                #text ("%d" % p.hp)
            hbox:
                text ("%d" % p.sta)
            hbox:
                text ("%d" % p.kno)
            hbox:
                text ("%d" % p.cou)
            hbox:
                text ("%d" % p.cha)
            hbox:
                text ("%d" % p.money)
    frame:
        xalign 0.95
        vbox:
            hbox:
                if day_of_week ==   0:
                    text ("Sunday")
                elif day_of_week == 1:
                    text ("Monday")
                elif day_of_week == 2:
                    text ("Tuesday")
                elif day_of_week == 3:
                    text ("Wednesday")
                elif day_of_week == 4:
                    text ("Thursday")
                elif day_of_week == 5:
                    text ("Friday")
                elif day_of_week == 6:
                    text ("Saturday")
            hbox:
                if time_of_day ==   0:
                    text ("Early Morning")
                elif  time_of_day == 1:
                    text ("Late Morning")
                elif time_of_day == 2:
                    text ("Early Afternoon")
                elif time_of_day == 3:
                    text ("Late Afternoon")
                elif time_of_day == 4:
                    text ("Early Evening")
                elif time_of_day == 5:
                    text ("Late Evening")
                




# The game starts here.
label start:
    show screen stats
    jump map
        
    return
    
    
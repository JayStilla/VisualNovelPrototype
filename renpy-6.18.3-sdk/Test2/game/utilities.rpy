init python:
    
    import random
        
        
    # CHECKS IF ACTIVITY WAS SUCCESSFUL
    def checkSuccess(percent_chance):
        
        if random.random() < percent_chance:
            return True
        else:
            return False
            
    # GET AMOUNT OF STAT INCREASE
    def getStatValue(value_min, value_max):
        return random.randint(value_min, value_max)
        
        


# SHAKE EFFECT
init:

    python:
    
        import math

        class Shaker(object):
        
            anchors = {
                'top' : 0.0,
                'center' : 0.5,
                'bottom' : 1.0,
                'left' : 0.0,
                'right' : 1.0,
                }
        
            def __init__(self, start, child, dist):
                if start is None:
                    start = child.get_placement()
                #
                self.start = [ self.anchors.get(i, i) for i in start ]  # central position
                self.dist = dist    # maximum distance, in pixels, from the starting point
                self.child = child
                
            def __call__(self, t, sizes):
                # Float to integer... turns floating point numbers to
                # integers.                
                def fti(x, r):
                    if x is None:
                        x = 0
                    if isinstance(x, float):
                        return int(x * r)
                    else:
                        return x

                xpos, ypos, xanchor, yanchor = [ fti(a, b) for a, b in zip(self.start, sizes) ]

                xpos = xpos - xanchor
                ypos = ypos - yanchor
                
                nx = xpos + (1.0-t) * self.dist * (renpy.random.random()*2-1)
                ny = ypos + (1.0-t) * self.dist * (renpy.random.random()*2-1)

                return (int(nx), int(ny), 0, 0)
        
        def _Shake(start, time, child=None, dist=100.0, **properties):

            move = Shaker(start, child, dist=dist)
        
            return renpy.display.layout.Motion(move,
                          time,
                          child,
                          add_sizes=True,
                          **properties)

        Shake = renpy.curry(_Shake)
    #

#  

init python:
    
    # shake prefabs
    weak_shake = Shake((0, 0, 0, 0), 0.5, dist=15)
    strong_shake  = Shake((0, 0, 0, 0), 0.75, dist=25)
    
    
    
    def checkTime(amt):
        if time_of_day + amt <= 5:
            return True
        else:
            return False
            
    def advDay():
        # make sure the scope is right
        global day_of_week
        global time_of_day
        
        time_of_day = 0
        
        if day_of_week == 6:
            day_of_week = 0
        else:
            day_of_week += 1
            
            
    def subtractSta(amt):
        global p
        p.sta += amt
        if p.sta < 0:
            p.sta = 0
            renpy.jump("exhaustion")
        else:
            return
            

    def subtractMoney(amt):
        global p
        p.money += amt
        if p.money < 0:
            p.money = 0
            renpy.jump("You're out of money")
            
            
    def allNighter(stat):
        renpy.say (None, "It's already very late.. You could stay up, but..")
        
        renpy.say(None, "Pull an all-nighter?", interact=False)
        result = renpy.display_menu([('Yes \n '+ stat, 'result1'), ('No', 'result2')])
        
        if result == 'result1':
            return True
        else:
            return False
            
            
    def checkAvailable(sched):
        global time_of_day
        
        if time_of_day < sched[2] or time_of_day > sched[3]:
            return False
        else:
            return True
            
    def updateSound(location):
        
        global time_of_day
        
        if renpy.music.is_playing(channel='amb'):
            current = renpy.music.get_playing(channel='amb')
        else:
            current = None
                
            
        if location == "park" or location == "dorm" or location == "map":
            
            if time_of_day <= 3:
                switch = amb_park
            else:
                switch = amb_night
                
            if current != switch:
                renpy.music.play(switch, channel='amb', fadein=0.25, fadeout=0.25)
                
                
                
        elif location == "school":
            
            switch = amb_school
            
            if current != switch:
                renpy.music.play(switch, channel='amb', fadein=0.25, fadeout=0.25)
                
        elif location == "rest":
            
            switch = amb_rest
            
            if current != switch:
                renpy.music.play(switch, channel='amb', fadein=0.25, fadeout=0.25)
                
            
        
        
        
        
        
        
        
 
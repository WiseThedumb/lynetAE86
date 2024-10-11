from sshkeyboard import listen_keyboard
def Goforward():
    print("going forward")
    set_motor('h_front', 'forward', 75) 
    set_motor('v_b', 'forward', 75)
    set_motor('h_b', 'forward', 75)
    set_motor('v_f', 'forward', 75)

def Gobackward():
    print ("Going Backwards")
    set_motor('h_front', 'backward', 75)
    set_motor('v_b', 'backward', 75)
    set_motor('h_b', 'backward', 75)
    set_motor('v_f', 'backward', 75)
def Goleft():
    print ("Going Left")
    set_motor('h_front', 'forward', 60)
    set_motor('v_b', 'backward', 20)
    set_motor('h_b', 'forward', 60)
    set_motor('v_f', 'backward', 20)
def Goright():
    print ("Going Right")
    set_motor('h_front', 'backward', 20) 
    set_motor('v_b', 'forward', 60)
    set_motor('h_b', 'backward', 20)
    set_motor('v_f', 'forward', 60)

def press(key):
    switch = {
        'w': Goforward,
        's': Gobackward,
        'a': Goleft,
        'd': Goright
    }
    if key in switch:
        switch[key]()
    elif key == 'esc':  # press esc to stop
        return False

listen_keyboard(on_press=press)








#while True:
#    listen_keyboard(on_press = press)
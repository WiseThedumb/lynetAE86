from sshkeyboard import listen_keyboard
def Goforward():
    print("going forward")

def Gobackward():
    print ("Going Backwards")

def Goleft():
    print ("Going Left")

def Goright():
    print ("Going Right")

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
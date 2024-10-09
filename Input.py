from sshkeyboard import listen_keyboard


def press(w):
    print(f"'{w}' pressed")
def press(s):
    print(f"'{s}' pressed")
def press(a):
    print(f"'{a}' pressed")
def press(d):
    print(f"'{d}' pressed")





while true:
    listen_keyboard(on_press = press)
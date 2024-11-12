
class Ret(object):
    def __init__(self, navn, pris, vegetarisk):
        self.navn = navn
        self.pris = pris
        self.vegetarisk = vegetarisk
    def info(self):
        return("Ret:" + str(self.navn) + " pris er " + str(self.pris) + " vegetarisk: " + str(self.vegetarisk))
class Menu(Ret):
    def tilMenu(self, menu):
        self.menu = menu
        menu = []
        
        for i in menu:
            menu.append(Ret.info)
            return(menu)
while True:        
    My_menu = Ret("burger", 12, False)
    
    print(My_menu.info())
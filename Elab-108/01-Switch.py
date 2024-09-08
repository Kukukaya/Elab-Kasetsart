class Switch:
    def __init__(self,name,status = False):
        self.name = name
        self.status = status

    def turn(self):
        self.status =  not self.status

    def clone(self):
        return Switch(self.name + '.copy',self.status)
    def __str__(self):
        if self.status == True:
            l = 'on'
        else: l='off'
        return f"switch({self.name}) is {l}"


class Light:
    def __init__(self,name,switch = Switch):
        self.name = name
        self.switch = switch

    def turn(self):
        self.switch.turn()
    def get_status(self):
        return self.switch
    def set_switch(self,new_switch):
        self.switch = new_switch
    def clone(self):
        return Light(self.name + '.copy',self.switch.clone())
    def __str__(self):
        return f"light({self.name}) with {self.switch}"

l = Light("l1", Switch("s1"))
print(l.get_status())
l.set_switch(Switch("s2"))
print(l.get_status())
print()
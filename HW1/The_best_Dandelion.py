import turtle as t

def rectangle(a,b):
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    t.forward(a)
    t.right(90)
    t.forward(b)
    t.right(90)
    
def endpollen(angle,size):
    t.right(angle+2)
    t.forward(size)
    t.right(180)
    t.forward(size)
    t.left(angle+2)
    t.right(180)
    
def pollen(size):
    t.width(2)
    t.forward(size)
    t.width(0.5)    
    ps = size//2.5
    for i in range(6):
        an = (i-2.5)*15
        endpollen(i,ps)
        
    
t.speed(0)
t.Screen().bgcolor("darkslategrey") 
#set up code
t.color("bisque3")
t.width(8)
rectangle(8,250)
t.forward(4)
#body of the Dandelion

for i in range(30):
    t.color("ghostwhite")
    a = i*12
    t.right(a)
    pollen(105)
    t.right(180)
    t.forward(105)
    t.right(180)
for i in range(60):
    t.color("papayawhip")
    a = i*6
    t.right(a)
    pollen(75)
    t.right(180)
    t.forward(75)
    t.right(180)
    t.left(a)
for i in range(80):
    t.color("navajowhite4")
    a = i*5
    t.right(a)
    pollen(35)
    t.right(180)
    t.forward(35)
    t.right(180)
    t.left(a)
    
    





    

class Line:
    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
    def contains(self,x,y):
        m = (self.y2 - self.y1) / (self.x2 - self.x1)
        # m = slope
        c = self.y2 - (m*self.x2)
        check_1 = x < self.x1 and y < self.y1 and x < self.x2 and x < self.y2
        check_2 = x > self.x2 and y > self.y2 and x > self.x1 and y > self.y1
        if y-(m*x) == c and not check_1 and not check_2:
            return True
        else:
            return False
        
    def get_distance(self):
        return ((self.y2-self.y1)**2 + (self.x2-self.x1)**2)**0.5
        
    def get_x1(self):
        return self.x1
    def get_y1(self):
        return self.y1	
    def get_x2(self):	
        return self.x2
    def get_y2(self):
        return self.y2	
    def get_y(self, x):
        m = (self.y2 - self.y1) / (self.x2 - self.x1)
        # m = slope
        c = self.y2 - (m*self.x2)
        y = (m*x)+c
        if self.contains(x,y):
            return y
        else:
            return -999.999


"""
////
///
//
/
This is end of assignment section
/
//
///
////
"""

class Point:
    # Constuctor
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def is_on_x_axis(self):
        if self.__y == 0: return True
        else: return False

    def is_on_y_axis(self):
        if self.__x == 0: return True
        else: return False

    def translate(self, dist_x, dist_y):
        self.__x = self.__x + dist_x
        self.__y = self.__y + dist_y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, new_x):
        self.__x = new_x

    def set_y(self, new_y):
        self.__y = new_y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

n = Line(1, 1, 4, 4)

print(f"{n.get_x1()} {n.get_y1()} {n.get_x2()} {n.get_y2()}")
print(n.contains(0.0, 0.0))
print(n.contains(1.0, 1.0))
print(n.contains(1.0, 0.0))
print(n.contains(0.0, 1.0))
print(n.contains(2.0, 0.0))
print(n.contains(0.0, 3.0))
print(n.get_distance())
print(n.get_y(3))
print(n.get_y(0))
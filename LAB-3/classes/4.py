import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f'Point({self.x}, {self.y})')

    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x)**2 + (self.y - other_point.y)**2)

p1 = Point(1, 2)
p2 = Point(4, 6)

p1.show() 
p2.show()

p1.move(2, 2)
p2.move(-1, -1)

p1.show() 
p2.show() 

distance = p1.dist(p2)
print(f'Distance between the points: {distance}') 

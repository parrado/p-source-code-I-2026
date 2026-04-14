from math import pi

class Shape:
    def __init__(self,centerXi,centerYi):
        self.centerX=centerXi
        self.centerY=centerYi
    
    def area(self):
        pass

    def showCoordinates(self):
        print(f'My coordinates are ({self.centerX},{self.centerY})')

class Triangle(Shape):
    def __init__(self,centerXi,centerYi,basei,heighti):
        super().__init__(centerXi,centerYi)
        self.height=heighti
        self.base=basei
    
    def area(self):
        return (self.base*self.height)/2
    

class Circle(Shape):
    def __init__(self,centerXi,centerYi,radiusi):
        super().__init__(centerXi,centerYi)
        self.radius=radiusi
    
    def area(self):
        return pi*self.radius**2


t0=Triangle(-1,-1,10,20)
print(t0.area())

t0.showCoordinates()

c0=Circle(0,0,1.0)
print(c0.area())
c0.showCoordinates()
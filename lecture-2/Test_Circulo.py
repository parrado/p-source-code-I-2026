from math import pi

class Circulo:
    def __init__(self,iradio,icentroX,icentroY):
        self.radio=iradio
        self.centroX=icentroX
        self.centroY=icentroY
    
    def area(this):
        a=pi*this.radio**2
        return a
    
    def perimetro(me):
        p=2*pi*me.radio
        return p

    

circulo0=Circulo(1.0,0.0,0.0)
circulo1=Circulo(8,5.0,-8.0)

print(f'El área de circulo0 es {circulo0.area()} UA')
print(f'El área de circulo1 es {circulo1.area()} UA')

p0=circulo0.perimetro()
print(f'El perímetro de circulo0 es {p0}')

p1=circulo1.perimetro()
print(f'El perímetro de circulo1 es {p1}')
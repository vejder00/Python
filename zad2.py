class Punkt2D(object):
  def __init__(self):
    self.punt = [0,0]
  def x(self,zmiennaX):
    self.punt[0]=zmiennaX
  def y(self,zmiennaY):
    self.punt[1]=zmiennaY
  def odleglosc(self,other):
    return (((other.punt[0]-self.punt[0])*(other.punt[0]-self.punt[0]))+((other.punt[1]-self.punt[1])*(other.punt[1]-self.punt[1])))**0.5
  def __str__(self):
    return ("(%d,%d)" % (self.punt[0] , self.punt[1]))
    
class Punkt3D(Punkt2D):
  def __init__(self):
    super(Punkt3D,self).__init__()
    self.punt.append(0)
  def x(self,zmiennaX):
    super(Punkt3D,self).x(zmiennaX)
  def y(self,zmiennaY):
    super(Punkt3D,self).y(zmiennaY)
  def z(self,zmiennaZ):
    self.punt[2]=zmiennaZ
  def odleglosc(self,other):
    #DOKONCZ
  def __str__(self):
    return ("(%d,%d,%d)" % (self.punt[0] , self.punt[1] , self.punt[2]))

p1 = Punkt2D()
p1.x(1)
p1.y(1)
p2 = Punkt2D()
p2.x(1)
p2.y(1)

print(p1.odleglosc(p2))

p13 = Punkt3D()
p23 = Punkt3D()

p13.x(1)
p13.y(1)
p13.z(1)   

p23.x(1)
p23.y(1)
p23.z(1)

print(p13.odleglosc(p23))
    
    

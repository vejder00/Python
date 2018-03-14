class liczbaZespolona(object):
  def __init__(self):
    self.tab = [0,0]
    #self.zmiennaIm=0
    #self.zmiennaRe=0
  def im(self,zmiennaIm):
    self.tab[1]=zmiennaIm
  def re(self,zmiennaRe):
    self.tab[0]=zmiennaRe
  def __add__(self,other):
    c=liczbaZespolona()
    c.re(self.tab[0]+other.tab[0])
    c.im(self.tab[1]+other.tab[1])
    return c
  def __sub__(self,other):
    c=liczbaZespolona()
    c.re(self.tab[0]-other.tab[0])
    c.im(self.tab[1]-other.tab[1])
    return c
  def __mul__(self,other):
    c=liczbaZespolona()
    c.re(self.tab[0]*other.tab[0])
    c.im(self.tab[1]*other.tab[1])
    return c
  def __floordiv__(self,other):
    c=liczbaZespolona()
    c.re(self.tab[0]/other.tab[0])
    c.im(self.tab[1]/other.tab[1])
    return c
  def modul(self):
    return (self.tab[0]*self.tab[0])+(self.tab[1]*self.tab[1])**0.5
  def __str__(self):
    return ("%d + %di" % (self.tab[0], self.tab[1]))
  def __lt__(self,other):
    if(self.modul()<other.modul()):
      return True
    else:
      return False
  def __le__(self,other):
    if(self.modul()<=other.modul()):
      return True
    else:
      return False
  def __eq__(self,other):
    if(self.modul()==other.modul()):
      return True
    else:
      return False
  def __ne__(self,other):
    if(self.modul()!=other.modul()):
      return True
    else:
      return False
  def __gt__(self,other):
    if(self.modul()>other.modul()):
      return True
    else:
      return False
  def __ge__(self,other):
    if(self.modul()<other.modul()):
      return True
    else:
      return False

l1=liczbaZespolona()
l1.re(1)
l1.im(1)

l2=liczbaZespolona()

l2.re(2)
l2.im(2)


print (l1.modul())
print (l1)

print (l1+l2)
print (l1>l2)
print (l1*l2)
print (l1//l2)
print (l1<=l2)

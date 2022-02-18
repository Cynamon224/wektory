import math

class Wektor:
    def __init__(self,x=0,y=0):
        self.__x=x
        self.__y=y
        
    def dlugosc(self):
        return math.sqrt(self.__x**2+self.__y**2)
    def normalizuj(self):
        a=self.__x/self.dlugosc()
        b=self.__y/self.dlugosc()
        return Wektor(a,b)
    def wyswietl(self):
        wek=[]
        wek.append(self.__x)
        wek.append(self.__y)
        print ("Wektor {} o długosci {}".format(wek,self.dlugosc()))
    def __add__(self,w):
        x=(self.__x+w.__x)
        y=(self.__y+w.__y)
        return Wektor(x,y)
    def __sub__(self,w):
        x=(self.__x-w.__x)
        y=(self.__y-w.__y)
        return Wektor(x,y)
    def __iadd__(self,w):
        self.__x=(self.__x+w.__x)
        self.__y=(self.__y+w.__y)
        return Wektor(self.__x,self.__y)    
    def __isub__(self,w):
        self.__x=(self.__x-w.__x)
        self.__y=(self.__y-w.__y)
        return Wektor(self.__x,self.__y)
    def __str__(self):
        tab=[]
        tab.append(self.__x)
        tab.append(self.__y)
        return str(tab)
    def __mul__ (self,a):
        x=self.__x*a
        y=self.__y*a
        return Wektor(x,y)
    def __rmul__ (self,a):
        x=a*self.__x
        y=a*self.__y
        return Wektor(x,y)    

w1 = Wektor(2,4)
w2 = Wektor(1.5)
print("Wektor w1:", w1, "wektor w2:", w2)
print("Dł. w1 =", w1.dlugosc(), "dł. w2 =", w2.dlugosc())
print("w1+w2 =", w1+w2)
print("w1-w2 =", w1-w2)
print("w1*2 =", w1*2)
print("-3*w2 =", -3*w2)
print("w1*2-w2 =", w1*2-w2)
print("w1 po normalizacji =", w1.normalizuj())
print("w2 po normalizacji =", w2.normalizuj())
w1.wyswietl()
w2.wyswietl()
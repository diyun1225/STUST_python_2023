# -*- coding: utf-8 -*-

class Myclass:
    x=10
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    #def __str__(self):
        #return f"{self.name}({self.age})"
    def myfunc(self):
        print("Hello my name is " + self.name)

class Calculate: #length:長,weigth:寬,radius:半徑
    def __init__(self,square_side=0,length=0,weigth=0,radius=0):
        self.square_side = square_side
        self.length = length
        self.weigth = weigth
        self.radius = radius
    
    #getSquareArea():計算正方形面積
    def getSquareArea(self):
        return int(self.square_side)*int(self.square_side)
    
    #getRectangleArea():計算長方形面積
    def getRectangleArea(self):
        return int(self.length)*int(self.weigth)
    
    #getCircleArea():計算圓形面積
    def getCircleArea(self):
        ans = 3.14*int(self.radius)**2
        return ans
        


a = Calculate(square_side=1,length=2,weigth=3,radius=4)
print(a.length)
print(a.getCircleArea())
print(a.getRectangleArea())
print(a.getSquareArea())


#p1 = Person(age = 36,name = "John") 
#print(p1.age) 
#print(p1.name)  
#print(p1.age)  
#print(p1.myfunc())


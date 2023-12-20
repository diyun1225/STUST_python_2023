class Sports:
    def __init_subclass__(cls) -> None:
        pass
    def __init__(self,name):
        self.name = name
    @property
    def sports_name(self):
        return self.name
    @sports_name.setter
    def sports_name(self,value):
        self.name = value
        print(f'已修改為"{self.name}"')
    def practice(self):
        print("Doing Sports pratice.")

class WaterSports(Sports):
    #field :場地
    def __init__(self,name,field):
        super().__init__(name)
        self.field = field
class LandSports(Sports):
    def __init__(self,name,field):
        super().__init__(name)
        self.field = field
    def practice(self):
        print("Doing Land Sports pratice.")
if __name__ == '__main__':
    sportA = LandSports("排球", "室外")
    print(sportA.sports_name)
    sportA.practice()

    
"""
class ball(LandSports):
    def __init__(self,name):
class no_ball(LandSports):
    def __init__(self,name):
class ocean(WaterSports):
    def __init__(self,name):
class swimming_pool(WaterSports):
    def __init__(self,name):
"""
"""
    # 汽車類別
    class Car:
        # 駕駛方法
        def drive(self):
            print("drive method is called.")
        # 加速方法
        def accelerate(self):
            print("accelerate method is called.")
    # 飛機類別
    class Airplane:
        # 駕駛方法
        def drive(self):
            print("drive method is called.")
        # 飛行方法
        def fly(self):
            print("fly method is called.")
"""
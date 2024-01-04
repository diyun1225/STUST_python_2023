# -*- coding: utf-8 -*-

#南台資工飲料店：
#Beverage:飲料
class Beverage:
    def __init__(self, price, sweetness,ice):
        self.price = price
        self.sweetness = sweetness
        self.ice = ice
#冷飲
class ColdBeverage(Beverage):
    def __init__(self, name, sweetness):
        super().__init__(name, sweetness)
#熱飲
class HotBeverage(Beverage):
    def __init__(self, name, sweetness):
        super().__init__(name, sweetness)

class Employee:
    #name:員工姓名,seniority:資歷,work_hours:工時
    def __init__(self, name, seniority, work_hours):
        self.name = name
        self.seniority = seniority
        self.work_hours = work_hours
    #搜尋員工姓名
    def search_name(self):
        print(f"此員工姓名為：{self.name}")
    #搜尋年資
    def search_seniority(self):
        print(f"員工{self.name}的年資為{self.seniority}")
    #搜尋工時
    def search_work_hours(self):
        print(f"員工{self.name}的當月工時為{self.work_hours}")
    #計算月薪
    def calculate_monthly_salary(self):
        total_month_salary = self.work_hours * 180
        print(f"員工{self.name}的當月工時{self.work_hours}，月薪為{total_month_salary}")
    #增加工時
    def Add_work_hours(self,new_hours):
        old_work_hours = self.work_hours
        if((self.work_hours + new_hours)>744):
            print(f"錯誤！員工{self.name}的當月工時{old_work_hours}新增{new_hours}後超過法定之每月工時744小時")
        else:
            self.work_hours = self.work_hours + new_hours
            print(f"員工{self.name}的原當月工時{old_work_hours}新增{new_hours}後變成{self.work_hours}")
    #增加年資
    def Add_seniority(self,new_seniority): 
        old_seniority = self.seniority
        self.seniority = self.seniority + new_seniority
        print(f"員工{self.name}的年資{old_seniority}年新增{new_seniority}年後變成{self.seniority}年")

if __name__ == '__main__':
    
    person1 = Employee("小明",2,100)
    person1.search_name()
    person1.search_seniority()
    person1.search_work_hours()
    person1.calculate_monthly_salary()
    person1.Add_work_hours(100)
    person1.Add_seniority(2)
    print("")
    person2 = Employee("小美",5,250)
    person2.search_name()
    person2.search_seniority()
    person2.search_work_hours()
    person2.calculate_monthly_salary()
    person2.Add_work_hours(700)
    person2.Add_seniority(1)
    print("")
    person3 = Employee("小華",1,13)
    person3.search_name()
    person3.search_seniority()
    person3.search_work_hours()
    person3.calculate_monthly_salary()
    person3.Add_work_hours(400)
    person3.Add_seniority(2)
# -*- coding: utf-8 -*-

#南台資工飲料店：
#Beverage:飲料
class Beverage:
    def __init__(self, price, sweetness, ice):
        self.price = price
        self.sweetness = sweetness
        self.ice = ice

    #更改飲料名稱
    def revise_name(self,new_name):
        old_name = self.name
        self.name = new_name
        print(f"更改成功！{old_name}的名稱改為{self.name}")
    #調整甜度
    def revise_sweetness(self,new_sweetness):
        old_sweetness = self.sweetness
        self.sweetness = new_sweetness
        print(f"更改成功！{self.name}的甜度從{old_sweetness}改為{self.sweetness}")    
    #調整價錢
    def revise_price(self,new_price):
        old_price = self.price
        self.price = new_price
        print(f"更改成功！{self.name}的價格從{old_price}元改為{self.price}元")    

# 冷飲
class ColdBeverage(Beverage):
    def __init__(self, name, price, sweetness, ice):
        super().__init__(price, sweetness, ice)
        self.name = name
    def search_coldbeverage(self):
        print(f"冷飲區：{self.name}的價格為{self.price}元_甜度為{self.sweetness}_冰塊為{self.ice} ")
    
# 熱飲
class HotBeverage(Beverage):
    def __init__(self, name, price, sweetness):
        super().__init__(price, sweetness, 0)
        self.name = name
    def search_hotbeverage(self):
        print(f"熱飲區：{self.name}的價格為{self.price}元_甜度為{self.sweetness} ")


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
        print(f"員工{self.name}的年資為{self.seniority}年")
    #搜尋工時
    def search_work_hours(self):
        print(f"員工{self.name}的當月工時為{self.work_hours}小時")
    #計算月薪
    def calculate_monthly_salary(self):
        #月薪 = 工時 * 時薪(180元)
        total_month_salary = self.work_hours * 180
        print(f"員工{self.name}的當月工時{self.work_hours}小時，月薪為{total_month_salary}元")
    #增加工時
    def Add_work_hours(self,new_hours):
        old_work_hours = self.work_hours
        if((self.work_hours + new_hours)>744):
            #假如超過法定月工時744小時，就會出現錯誤且不計算。
            print(f"新增錯誤！員工{self.name}的當月工時{old_work_hours}新增{new_hours}後超過法定之每月工時744小時，請重新輸入")
        else:
            self.work_hours = self.work_hours + new_hours
            print(f"新增成功！員工{self.name}的原當月工時{old_work_hours}小時新增{new_hours}小時後變成{self.work_hours}小時")
    #增加年資
    def Add_seniority(self,new_seniority): 
        old_seniority = self.seniority
        self.seniority = self.seniority + new_seniority
        print(f"新增成功！員工{self.name}的年資{old_seniority}年新增{new_seniority}年後變成{self.seniority}年")

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
    print("")
    milktea = ColdBeverage("奶茶",40,"微糖","多冰")
    greentea = ColdBeverage("綠茶",25,"無糖","少冰")
    hotcoco = HotBeverage("熱可可",60,"半糖")
    #search_coldbeverage為測試 冷熱飲是否分開 用
    milktea.search_coldbeverage()
    hotcoco.search_hotbeverage()

    print("")
    milktea.revise_name("紅茶")
    milktea.revise_sweetness("無糖")
    milktea.revise_price(20)

    print("")
    hotcoco.revise_name("美式咖啡")
    hotcoco.revise_sweetness("無糖")
    hotcoco.revise_price(60)

    print("")
    greentea.revise_name("烏龍茶")
    greentea.revise_sweetness("無糖")
    greentea.revise_price(30)
    
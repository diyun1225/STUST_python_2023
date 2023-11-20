#第一題
#符串的反轉
#寫一個Python函數，該函數以字符串作為輸
#入並返回該字符串的反轉。例如，如果輸入
#是"hello"，該函數應返回"olleh"。

def reverse_string(str):
    r_str = str[::-1]
    return r_str

input_str = input()
print(reverse_string(input_str))

#第二題遞歸函式: 正整數的階乘
#創建一個Python程序，使用遞歸函數計算給
#定正整數的階乘。例如，如果輸入是5，程序
#應返回階乘值，即120
#num = 輸入要階乘的數字
#5!=5*4*3*2*1
def factorial(num,ans = 1):
    if num >= 1:
        ans=ans*num
        return factorial(num-1,ans)
    else:
        return ans
    
input_number= int(input())
print(factorial(input_number))

#第三題刪除重複元素
#實現一個Python函數，該函數接受整數LIST作
#為輸入，並返回僅包含唯一元素且刪除任何重
#複元素的新LIST。

def delete_repeat_element(list):
    return set(list)

input_list = list(input().split())
print(delete_repeat_element(input_list))

    
#Python讀取CSV
#編寫一個Python程序，讀取包含學生信息
#（姓名，年齡和成績）的CSV文件，並顯示
#成績高於某個閾值的學生的名字。

import csv 

#with open('students.csv', newline='') as csvfile:
    #rows = csv.reader(csvfile)
#for row in rows:
    #print(row) 
       
#第五題類別和物件的建立
#定義一個名為“Person”的Python類別，具有名
#稱、年齡和地址等屬性。然後，創建一個名
#為“Student”的子類別，該子類別繼承自
#"Person"，並具有學生ID和專業等附加屬性。

#創建Person類別，有名字、年齡、家
class Person():
    def __init__(self,name,age,home):
        self.name = name
        self.age = age
        self.home = home
    def printall1(self):
        print(self.name,self.age,self.home)
#student_id = 學號 , major = 專業
#創建學生類別，繼承Person類別，還有學號、專業
class Student(Person):
    def __init__(self,name,age,home,student_id,major):
        super().__init__(name,age,home)
        self.student_id = student_id
        self.major = major
    def printall2(self):
        print(self.name,self.age,self.home,self.student_id,self.major)    
#student = Student("anna",15,"Tainan","4B0G0033","CSIE")
#print(student)
#創建Person類別
emma_profile = Person("emma","18","Tainan")
#創建student子類別
john_student_profile = Student("john","15","Yunlin","4B0G0033","CSIE")

emma_profile.printall1()
john_student_profile.printall2()
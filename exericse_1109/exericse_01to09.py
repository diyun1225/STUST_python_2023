# -*- coding: utf-8 -*-

#1.input name and age , and print it
def print_name_and_age(name,age):
    print(name,age)

#2.input 多少 numbers 就 print 多少 numbers
def fun1(*numbers):
        print(numbers)

#3.input a,b ,print add and mius
def calculation1(a,b):
    print(int(a+b),int(a-b))

#3.input int a,b , return add and mius
def calculation2(a,b):
    add = a+b
    mius = a-b
    return add,mius

#4.input employee and money,if don't input money it will print default argument(9000)
def show_employee(name,money = 9000):
     print("name: {} money: {}".format(name, money))

#5.add a and b and 5
def fun2(a,b):
        return a+b+5 

#6.1+2+3+...+N
def sumMtoN(M,N,ans=0):
      if M<=N:
        return sumMtoN(M+1,N,ans+M)
      else:
        return ans
      
#7.display student's name and age
def display_student(name,age):
     return name,age

#8.find even in range
def find_even_in_M(m):
    even_number = [ i for i in range(0,m,2)]
    return even_number

#9.find biggest number
def find_biggest_number(numbers):
     biggest_number=numbers[0]
     for number in numbers:
          if number > biggest_number:
               biggest_number = number
          else:
               continue
     return biggest_number

print_name_and_age("penny",22)

fun1(1,342,14)
fun1(4,53)

calculation1(40, 10)

print(calculation2(40,10))
show_employee("Ben",12000)

print(fun2(3,4))
print(sumMtoN(1,10,ans=0))

show_Student = display_student("emma",36)
print(show_Student)

print(find_even_in_M(10))

numbers = [10,3,5,6,43,200]
print(find_biggest_number(numbers))
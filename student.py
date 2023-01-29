



# class Student:
#    col=0 #атрибут класса
#    def __init__(self, height=160, name=None, age=12):
#        self.height=height
#        self.name=name
#        self.age=age
#        Student.col+=1
#
#    def grow(self,height=5):
#        self.height+=height
#
#    def __str__(self):
#        return f"Меня зовут {self.name}. Мне {self.age} лет"
#
# student1=Student(name="Vanya", age=16)
# print(student1.__str__())
# print("Cредний рост студентa №1:", student1.height)
# print("Кол. студентов:", student1.col)
# print()
# student2=Student(height=5)
#
#
# def __str__(self):
#     return f"Меня зовут {self.name}. Мне {self.age} лет"
#
# student2=Student(name="Ivan", age=17)
# print(student2.__str__())
# print("Средний рост студента №2:", student2.height)
# print("Кол. студентов:", Student.col)
# student2.grow(height=15)



#Симулятор студента
from random import randint
class Student:
    def __init__(self, name):
        self.name=name
        self.happy=50
        self.progress=0
        self.life=True
        self.money=2000

    def study(self):
        print("Time to study")
        self.happy-=10
        self.progress+=4

    def work(self):
        print("Time to work")
        self.money+=155
        self.happy-=13

    def sleep(self):
        print("Time to sleep")
        self.happy+=5

    def rest(self):
        print("Time to rest")
        self.happy+=8
        self.progress-=4
        self.money-=150

    def isLive(self):
        if self.happy<=0:
            print("Depression")
            self.life=False
        if self.progress>=10:
            print("Session is passed, have a rest")
            self.happy+=10
            self.life=True
        if self.progress<10 and self.money>0:
            print("Session is not passed. You are out of here!!!")
            self.life=False
        if self.money<=0 and self.progress>10:
            print("You are out of money!!!")
            self.life=False
        elif self.progress<10 and self.money<=0:
            print("Session is not passed. You are expelled!!!")
            print("You are out of money too!!!")
            self.life=False


    def day(self):
        print("Happyness: ", self.happy)
        print("Efficiency in school: ", self.progress)
        print("money: ", self.money)

    def choice(self, numDay):
        numDay="Day #"+str(numDay)+" from the life of student"+ self.name
        print(f"{numDay:=^50}")
        rnd=randint(1,4)
        if self.progress < 10 and self.money>0:
            self.study()
        elif self.money<=0 and self.progress>10:
            self.work()
        elif rnd==1: self.study()
        elif rnd==2: self.sleep()
        elif rnd==3: self.work()
        else: self.rest()
        self.day()
        self.isLive()

stodent1=Student(name=" Nikita")
for i in range(1,366):
    stodent1.choice(i)












# OOP เป็นวิธีการเขียนโปรแกรมรูปแบบหนึ่ง โดยมองสิ่งต่างๆในระบบเป็นวัตถุ (Object)
# ชิ้นหนึ่งที่มีหน้าที่และความหมายในตัว โดยวัตถุๆนั้น ก็มี คุณสมบัติ (Attributes) และ
# พฤติกรรม (Method,Behavior) หรือการกระทำของมัน เป็นการมองบนพื้นฐานความเป็นจริงมากขึ้น เช่น
class Robot:
    def __init__(self,wight,high):
        self.wight= wight
        self.high= high
    
    def move(self,direct):
        print("moveee"+str(direct))
# Inheritance
# การสืบทอดคลาสเพิื่อใช้คลาสเก่าแบบที่มีการพัฒนา

class evolotion_bot(Robot):
    def __init__(self,color,wight,high):
        super().__init__(wight,high)
        self.color= color
# ในภาษา Python หากแอททริบิวต์ถูกประกาศด้วยเครื่องหมาย Underscore (__) สองตัวที่หน้าชื่อของตัวแปรจะทำให้ระดับการเข้าถึงของมันเป็นแบบ Private
# Encapsulation ปกปิดข้อมูลภายนอก
        self.__controlPass="1234"
    def show(self):
        print(""+self.__controlPass)
        
# @staticmethod นำหน้าก่อนหนึ่งบรรทัด เมธอดนี้ไม่ได้มีส่วนเกี่ยวข้องกับข้อมูลภายในคลาส สังเกตว่ามันไม่มีพารามิเตอร์ self ถูกส่งเข้ามา สำหรับการเรียกใช้งาน static variables 
# หรือ static method นั้นจะไม่ขึ้นกับออบเจ็คเข้ามาเกี่ยว เพียงแต่มีการเรียกใช้ผ่าน  classนั้นๆ
    @staticmethod
    def compare(a,b):
        if a > b:
            return 'greater than'
        elif a == b:
            return 'equal'
        else:
            return 'less than'


box1 = evolotion_bot("red",3, 4)
box1.move("right")

# Encapsulation ปกปิดข้อมูลภายนอก
# ตอนนี้โชว์ว่าถ้าเป็นค่าปกติสามารถโชว์ได้    แต่ค่า.__controlPassเพราะถูกป้องกันการเข้าถึงจาก "__"  
print(box1.high)
try:
    print(box1.__controlPass)
except:
    print("cann't print ")
box1.show()

print(box1.compare(1,2))



# class Ocean:
    
#     def __init__(self, sea_creature_name, sea_creature_age):
#         self.name = sea_creature_name
#         self.age = sea_creature_age
    
#     def __str__(self):
#         return f'The creature type is {self.name} and the age is {self.age}'

#     def __repr__(self):
#         return f'Ocean(\'{self.name}\', {self.age})'

# c = Ocean('Jellyfish', 5)

# print(str(c))
# print(repr(c))

# Output
# The creature type is Jellyfish and the age is 5
# Ocean('Jellyfish', 5)
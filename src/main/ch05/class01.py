# python의 class 정의
class Student:
    # python은 클래스 메서드와 스태틱 메서드를 구분해둠
    # 클래스 변수(Java의 static 변수)
    name = "김준일(클래스 변수)"
    age = "32(클래스 변수)"
    # # 멤버 변수
    # name = "김준일"
    # age = 32
    def __init__(self):
        # 인스턴스 변수
        self.name = "김준일"
        self.age = 32

    def toString(self):
        return f"Student(name: {self.name}, age:{self.age}, clsName: {self.__class__.name})"
    # 객체의 값이 있어야 하는데 없을 경우 디폴드 값에서 가져옴

    @classmethod
    def toString2(cls):
        return f"Student(name: {cls.name}, age:{cls.age})"

    @staticmethod
    def toString3(name, age):
        return f"Student(name: {name}, age:{age})"

# s1 = Student()
# print(s1.name)
# print(s1.age)
# print(s1.toString())
# Student.name = "김준이"
# s1.name = "김준삼"
# print(Student.toString2())

print(Student.name)
print(Student.age)
s1 = Student()
print(s1.name)
print(s1.age)
print(s1.toString())


#a = int(input("a입력: "))
#b = int(input("b입력: "))

#print(a, b)
#print(type(a))
#print(type(b))

# 10 20
number = input("두 수 입력: ").split()
print (number)

def parseInt(n):
    return int(n)

parseInt = lambda n: int(n)

r1 = parseInt("10")
r2 = int("10")
fx1 = parseInt
fx2 = int
r3 = fx1("10")
r4 = fx2("10")

map(parseInt, ["10", "20"])

number1, number2 = list(map(int, input("두 수 입력: ").split()))
print (type(number1))
print (number2)

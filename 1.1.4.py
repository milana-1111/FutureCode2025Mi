x = 15
result = (x > 10) and (x < 20)
print(result)

coins = -35
if coins <= 20:
    status = "гоблин"
elif coins <= 50:
    status = "орк"
elif coins <= 75:
    status = "эльф"
else:
    status = "гном"

text = input("введите строку для проверки палиндрома ")
text = text.lower()
text = text.replace(" ", "")
reversed_text = text[::-1]
if reversed_text == text:
    print('палиндром')
else:
    print('не палиндром')

a = int(input("введите значение стороны a = "))
b = int(input("введите значение стороны b = "))
c = int(input("введите значение стороны c = "))
if a**2 + b**2 == c**2:
    print("прямоугольник")

elif a**2 + b**2 > c**2:
    print("остроульник")

elif a**2 + c**2 < b**2:
    print("тупоугольник")

elif a+b**2 < c**2:
    print("не существует")


    number = 36
    if number % 2 == 0 and number % 3 == 0:
        if number > 30:
            result = number // 6
        else:
            result = number * 2
    else:
        if number % 2 == 0:
            result = number + 10
        else:
            result = number - 5
print(result)

score = 85
if score < 60 or score > 90:
    if score < 60:
        grade = "F"
    else:
        grade = "A"
else:
    if score >= 80:
        grade = "B"
    else:
        grade = "C"
if grade == "A" or grade == "B":
    status = "Pass"
else:
    status = "Fail"

print(grade, status)

a = int(input())
k = 4
s = a * k
print(s)

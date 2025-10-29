x = -10
y = -5
result = x > y
print(result)

age = 15
if age >= 16:
    print("Можно получить права")
else:
    print("Нужно подождать")

    a = 14
    n = a // 4
    print(n)

    a = 43
    b = 96
    a = a % 3 + b // 4
    z = a + b // 10 % 3
    print(z)

    n = int(input())
    print(n / 200)

    x = 12
    y = 8
    if x > y:
        result = x - y
    else:
        result = y - x
    if result > 0:
        result = result + 10
    else:
        result = result - 10

        name1 = "Anna"
        name2 = "Anna"
        if name1 == name2:
            check = True
        else:
            check = False
        if check:
            answer = "Yes"
        else:
            answer = "No"

            n = int(input())
            if n >= 5:
                print("Добряк!")
            elif 5 > n > 2:
                print("Помогатор!")
            else:
                print("Безразличник!")
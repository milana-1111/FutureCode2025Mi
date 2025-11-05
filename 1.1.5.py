count1 = 0
while count1 < 5:
    count1 = count1 + 1
print(count1)

a = 4
b = 10
while a <= b:
    a = a + 2
print(a)

n = 0
s = 0
while s <= 30:
    n += 2
    s += 6
print(n)

n = 129
s = 0
while n > 0:
   p = n % 10
   s += p
   n = n // 10
print(s)

n = int(input())
total = n * (1.1 ** 5)
print (int(total))

count = 0
total = 0
while total < 20:
    count = count + 1
    total = total + count
result = count
print(result)

number = 1
flag = True
sum_numbers = 0
while flag:
    sum_numbers = sum_numbers + number
    number = number + 2

    if sum_numbers > 15:
        flag = False
    if number > 10:
        break
result = sum_numbers
print(result)

for i in range(3):
    print(i, end=" ")
    print()

total = 1
for number in range(1, 4):
    total = total + total
    print(total)

    for i in range(1, 22):
        print('*')

        s = 0
        for i in range(30):
            if ((i % 2 != 1) and (i % 3 == 0)) or (i // 10 == 2):
                s += i
print(s)

c = 0
for n in range(10,100):
    if n % 6 == 0 and(n % 10 == 8 or n % 10 == 2):
        c += 1
print(c)

n = int(input())
count = 0
for num in range (12, min(n, 100), 2):
  if num % 10 == 4 or num % 10 ==8:
    count += 1
print(count)

total = 0
for i in range(1, 10, 2):
    total = total + i
result = total
print(result)

number = 384
sum_digits = 0
for digit in str(number):
    sum_digits = sum_digits + int(digit)
if sum_digits % 2 == 0:
    result = sum_digits * 2
else:
    result = sum_digits + 1
    print(result)


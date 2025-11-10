# 0-30 -без сознания 31-70 ранен 71-90 - легкое недомогание 91 здоров
from multiprocessing.connection import answer_challenge

health = int(input("Ведите уровень здоровья "))
if health >=90:
    print('персонаж здоров')
elif 70 <= health < 90:
    print('нужно выпить зелеье, согласны? (Y/N)')
    answer = input()
    if answer.lower() == 'y':
        health += 10
        print('')

elif 30 <= health < 70:
    print('вы ранены. использовать аптечку? (Y/N) ')
    answer = input()
    if answer.lower() == 'y':
        health += 30
        print('здоровье увеличено до ' , health)
    else:
        health -= 30
        print('')

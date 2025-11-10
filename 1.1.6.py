from multiprocessing.connection import answer_challenge
from random import randint

hp = 100
rooms = 3
rooms_content = ['лава' , 'пустая' , 'орк']

while hp > 0 and rooms > 0:
    print('(перед вами три двери. в какую войдете? (1/2/3) )')
    answer = int(input())
    if 0 < answer <= 3:
        content = rooms_content[randint(0, len(rooms_content) - 1)]
        print('вам открылась комната - ')
        if content !='пустая комната':
            damage = randint(10, 31)
            hp -= damage
        print("вам нанесен урон" , damage, "осталось" , hp, "здоровье")

    if hp > 0:
        print('вы победили!')
    else:
        print('вы проиграли!')

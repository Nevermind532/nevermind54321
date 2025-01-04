import random


def get_random_year():
    return random.randint(1930, 1950)

print("ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?")


schetchik_poka = 0

while True:
    user_input = input().strip()

    if user_input.upper() == "ПОКА":
        schetchik_poka += 1
        if schetchik_poka < 3:
            print(f"НЕТ, НИ РАЗУ С {get_random_year()} ГОДА!")
        else:
            print("ДО СВИДАНИЯ, МИЛЫЙ!")
            break
    else:
        schetchik_poka = 0
        if user_input.isupper():
            print(f"НЕТ, НИ РАЗУ С {get_random_year()} ГОДА!")
        else:
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
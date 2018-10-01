"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html
"""
import random

g_stroka = 3
g_stolbsy = 9
g_instroka = 5
g_start = 1
g_end = 90


class Player():
    # если *lcard - то передается в фунция два объекта (print (self.lcard)=([10, 7, 2, 5, 5, 5, 3, 10, 5, 7, 5, 3, 2, 10, 13],)),
    # а без * передается только список ((print (self.lcard)=[10, 7, 2, 5, 5, 5, 3, 10, 5, 7, 5, 3, 2, 10, 13])

    def __init__(self, name, lcard):
        self.name = name
        self.lcard = lcard
        # print("Self_card = ", self.lcard)  # нужно удалить, для проверки

    def choice(self, number, stroka=g_stroka, stolbsy=g_stolbsy):
        for i in range(stroka):
            for ii in range(stolbsy):
                if number == self.lcard[i][ii]:
                    self.lcard[i][ii] = "-"
                    return True
        return False

    def pr_lcard(self, stroka=g_stroka, stolbsy=g_stolbsy):
        s = 2
        ls = 0
        a = "Карточка " + self.name
        print(a.center((stolbsy * s + (stolbsy - 1)), '-'))
        for i in range(stroka):
            for ii in range(stolbsy):
                print(str(self.lcard[i][ii]).rjust(s), end=" ")
                if self.lcard[i][ii] == "-":
                    ls += 1
            print('\n', end='')
        print("".center((stolbsy * s + (stolbsy - 1)), '-'))
        return ls


# возвращает список из stroka списков, каждая длиной в stolbsy, состоящих из случайных чисел в диапазоне от start по end в количестве instroka,
# остальные не заполненные числами элементы списка будут заполнены symb
def rand_unical(start=g_start, end=g_end, stroka=g_stroka, stolbsy=g_stolbsy, instroka=g_instroka, symb=" "):
    list_r = list(set([random.randint(start, end) for _ in range(instroka * stroka)]))

    while len(list_r) < (stroka * instroka):
        list_r.append(random.randint(start, end))
        list_r = list(set(list_r))
    print(list_r)  # нужно удалить, для проверки
    p = []
    pp = []
    if instroka < stolbsy:
        for i in range(stroka):
            p = list_r[(i * instroka):(i * instroka + instroka)]
            # l = list(" " * stolbsy)
            # for n in range(instroka):
            #     if l[p[n] // 10] == symb:
            #         l[p[n] // 10] = p[n]
            #     else:
            #         k = p[n] // 10
            #         l[k - 1:k + 1].sort()
            # pp.append(l)
            # print(l)
            for ii in range(stolbsy - instroka):
                p.append(symb)
                random.shuffle(p)
            pp.append(p)

        list_r = pp
    else:
        print("Введите корректно кол-во чисел в строке и кол-во столбцов")

    return list_r


player1 = Player("player", rand_unical())
orig_player1 = player1  # для сохранения карточки player1

computer1 = Player("computer", rand_unical())
orig_computer1 = computer1  # для сохранения карточки computer1

o_list = list(range(1, (g_end + 1)))

while True:
    print(o_list)  # нужно удалить, для проверки
    o = random.choice(o_list)
    o_list.remove(o)
    print("Выпал бочонок под номером: ", o)
    if player1.pr_lcard() == g_stroka * g_instroka:
        print("Выиграл ", player1.name)
        break
    if computer1.pr_lcard() == g_stroka * g_instroka:
        print("Выиграл ", computer1.name)
        break
    b_p = player1.choice(o)
    b_c = computer1.choice(o)
    x = input("Зачеркнуть цифру? (y/n)")
    while x != "Y" and x != "y" and x != "N" and x != "n":
        x = input("Введите коректно. Зачеркнуть цифру? (y/n)")
    if x == "Y" or x == "y":
        if b_p:
            print("Цифра ", o, "зачеркнута. Игра продолжается.")
            continue
        else:
            print("Вы проиграли. Игра окончена.")
            break
    elif x == "N" or x == "n":
        if b_p:
            print("Вы проиграли. Игра окончена.")
            break
        else:
            print("Игра продолжается.")
            continue

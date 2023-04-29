## Проверка правильности ввода целого числа

try:
    x = int(input())
except ValueError as e:
    print('Введено неправильное число')
else:
    print('Всё ок. Введено целое число')
finally:
    print('Выход из программы')

## Ось координат. Определение четверти в которой находится точка.
x, y = float(input()), float(input())

if x > 0 and y > 0:
    print("Первая четверть")
if x > 0 and y < 0:                        # x > 0, y < 0
    print("Четвертая четверть")
if x < 0 and y > 0:                        # x < 0, y > 0
    print("Вторая четверть")
if x < 0 and y < 0:                        # x < 0, y < 0
    print("Третья четверть")

## A, B, C - переменные. True когда одна из этих переменных меньше 45
A, B, C = int(input()), int(input()), int(input())
if ((A < 45) and (B >= 45) and (C >= 45)) or \
    ((A >= 45) and (B < 45) and (C >= 45)) or \
    ((A >= 45) and (B >= 45) and (C < 45)):
    print('Есть число меньше 45 и только одно')
else:
    print('Числа меньше 45 нет или их несколько')

## Проверка того, что А не в заданных интервалах
A = int(input())
if not (-10 <= A <= -1 or 2 <= A <= 15):
    print("А не в заданных интервалах")
else:
    print("A в заданных интервалах")

## Входит ли 5 в двухзначное число. Решить с помощью // и %
n = int(input())
if (n // 10 == 5 or n % 10 == 5) and (10 <= n <= 99):
    print("5 входит в двухзначное число")
else:
    print("5 НЕ входит в двухзначное число или число больше 99")

## Все ли элементы списка уникальны?
list1 = [1, 2, 3, 4, 5, -1, -10, -5, 2]
print(len(list1) == len(set(list1)))

## Число восьмизначное палиндром?

number = 12345678
print(str(number) == str(number)[::-1])

## Звёздочки
n = 5
for i in range(1, n + 1):
    i *= '*'
    print(i)


## My 9nd to be run.
list_ = [-5, 2, 4, 8, 12, -7, 5]
# Объявим переменную, в которой будем хранить индекс отрицательного элемента
index_negative = None

for i, value in enumerate(len(list_)):
    if value < 0:
        print("Отрицательное число: ", value)
        index_negative = i  # перезаписываем значение индекса
        print("Новый индекс отрицательного числа: ", index_negative)
    else:
        print("Положительное число: ", value)
    print("---")
print("Конец цикла")
print()
print("Ответ: индекс последнего отрицательного элемента = ", index_negative)

## Гипотеза Сиракуз. Если произвести необходимые вычисления рано или поздно значение будет == 1.
n = int(input("Введите число"))

while True:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3 + 1) // 2
    print(n)

    if n == 1:
        print("Done")
        break


## Число удовлетворяет условиям. Решить через if.
a = None
if type(a) == int:
    if 100 <= a and a <= 999:
        if a % 2 == 0:
            if a % 3 == 0:
                print("Число удовлетворяет условиям")
    else:
        pass

## Число удовлетворяет условиям. Через if в одну строку.

if type(a) == int and 100 <= a <= 999 and a % 2 == 0 and a % 3 == 0:
    print("Число удовлетворяет условиям")

## My 13nd to be run. False если одно из значений == 0, True != 0 все.

L = list(map(int, input().split()))
print(all(L))

## My 14nd to be run. False если одно из значений != 0. True если все == 0.

L = list(map(int, input().split()))
print(not any(L))


## My 15nd to be run. Таблица умножения от 1 до 10.

T = [[i*j for j in range(1, 11) for i in range(1, 11)]]
print(T, sep="\n")

## My 16nd to be run. True - чётные числа, Fale - нечётные числа.

L = [int(input()) % 2 == 0 for i in range(5)]
print(L)
## Result будет истинным только тогда, когда в списке есть хотя бы один четный и хотя бы один нечетный элемент.

L = [int(input()) % 2 == 0 for i in range(5)]
print(any(L) and not all(L))

## Поэлементные значения произведений списков L и M
L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
M = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
N = [a*b for a,b in zip(L,M)]
print(N)

## Сжатие последовательности символов на входе. 'aaa' == 'a3'

text = input()  # получаем строку

first = text[0]  # сохраняем первый символ
count = 0  # заводим счетчик
result = ''  # и результирующую строку

for c in text:
    if c == first:  # если символ совпадает с сохраненным,
        count += 1  # то увеличиваем счетчик
    else:
        result += first + str(count)  # иначе - записываем в результат
        first = c  # и обновляем сохраненный символ с его счетчиком
        count = 1

result += first + str(count)  # и добавляем в результат последний символ
print(result)


## Вывод текста песни "Трава у дома"

with open("C:/Users/DartWeder/Desktop/filename.txt", "rt", encoding="utf=8") as My_song:
    print(My_song.read())

## Чтение файла построчно в цикле for

for line in My_song:
    print(line)


## Элементы - строки выводит по очереди

print(My_song.readline())

## Запись в файл .write

with open("C:/Users/DartWeder/Desktop/filename.txt", "a", encoding="utf=8") as My_song:
    My_song.write('This song is cool!!!')

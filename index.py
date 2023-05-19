numbers = list(map(int, input().split()))
element = int(input())
numbers.append(element)

# Необходимо проверить, является ли введенное число element больше минимального и меньше максимального
# Если нет, то проводить поиск не нужно. Достаточно вывести сообщение, что условия не удовлетворяются
# Если условие выполняется, то нужно провести поиск и найти индекс числа, которое меньше введенного
# пользователем числа, а следующий за ним больше или равен этому числу
def binary_search(array, element, left, right):
    if element < min(array) or element > max(array):
        return "Условия задачи не удовлетворяются"
    else:
        return array.index(element) - 1


def qsort(array):
    for i in range(len(array)):
        for j in range(len(array) - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


qsort(numbers)

# запускаем алгоритм на левой и правой границе

print(binary_search(numbers, element, 0, len(numbers) - 1))

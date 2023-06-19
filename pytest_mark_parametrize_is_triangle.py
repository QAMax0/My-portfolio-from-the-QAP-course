import pytest

#  Напишите функцию, которая определяет, можно ли составить треугольник из трёх отрезков,
#  длины которых передаются в функцию.

#  Например, вызов функции is_triangle(3, 4, 5) возвращает True, а вызов is_triangle(1, 4, 5) возвращает False.
#  Напишите параметризованный тест на эту функцию, используя фикстуру @pytest.mark.parametrize,
#  который рассматривает все возможные варианты параметров:

#  Позитивные тесты - положительные длины, из которых можно составить треугольник.
#  Негативные тесты - отрицательные длины отрезков;
#  Длины, равные 0;
#  Положительные длины отрезков, из которых невозможно составить треугольник.

def is_triangle(a, b, c):
    if (a + b > c and
        b + c > a and
        c + a > b):
        return True
    else:
        return False


@pytest.mark.parametrize("a, b, c", [(1, 1, 1), (0, 0, 0), (-1, -3, -2), (2, 4, 1)],
                         ids=['is positive', 'is zero', 'is negative', 'is invalid values'])
def test_is_triangle(a, b, c):
    result = is_triangle(a, b, c)
    assert result == True

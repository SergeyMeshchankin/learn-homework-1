"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    def string_comparison(str1, str2):
        if type(str1) != str or type(str2) != str:
            return 0
        elif str1 == str2:
            return 1
        elif str1 != str2 and len(str1) > len(str2):
            return 2
        elif str1 != str2 and str2 == 'learn':
            return 3

    print(string_comparison('hello', 1))
    print(string_comparison('hello', 'hello'))
    print(string_comparison('hello', 'help'))
    print(string_comparison('hello', 'learn'))


if __name__ == "__main__":
    main()

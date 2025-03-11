"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    sold_phones = [
        {'product': 'iPhone 12', 'items_sold': [
            363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]},
        {'product': 'Xiaomi Mi11', 'items_sold': [
            317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
        {'product': 'Samsung Galaxy 21', 'items_sold': [
            343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    total_sales_per_item = {}
    average_sales_per_item = {}

    for item in sold_phones:
        name_phone = item['product']
        sum_of_sales = sum(item['items_sold'])
        average_of_sales = sum(item['items_sold']) / len(item['items_sold'])

        total_sales_per_item[name_phone] = sum_of_sales
        average_sales_per_item[name_phone] = average_of_sales

    print(
        f'Суммарное количество продаж для каждого товара:\n{total_sales_per_item}')
    print(
        f'Среднее количество продаж для каждого товара:\n{average_sales_per_item}')

    all_sales = sum(total_sales_per_item.values())
    print(f'Суммарное количество продаж всех товаров: {all_sales}')

    average_all_sales = []
    for item in sold_phones:
        average_all_sales.extend(item['items_sold'])
        average_sales = sum(average_all_sales) / len(average_all_sales)

    print(f'Среднее количество продаж всех товаров: {average_sales}')


if __name__ == "__main__":
    main()

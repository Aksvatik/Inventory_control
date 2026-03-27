import inventory_tools
import json_tools
import utilities
from decimal import Decimal, InvalidOperation


MENU_TEXT = (
    "1 — Показать все товары\n"
    "2 — Добавить новый товар\n"
    "3 — Добавить количество товара\n"
    "4 — Удалить товар\n"
    "5 — Найти товар\n"
    "6 — Показать общую стоимость склада\n"
    "0 — Выход\n"
)

# Выгрузка данных из json
products = json_tools.load_inventory("products")
view = json_tools.load_inventory("view_config")

print(MENU_TEXT)

while True:
    cmd = input("Выберите действие: ").strip()

    match cmd:
        case "1":
            if products:
                for value in products:
                    print(inventory_tools.print_product(value, products[value]))
                print("")

                if not utilities.ask_continue("Хотите изменить фильтр сортировки?"):
                    pass  # Просто продолжаем цикл главного меню
                else:
                    print("ЕЩЕ НЕ РАБОТАЕТ\n")
            else:
                print("Склад пуст.\n")

        case "2":
            while True:
                while True:
                    product = input("Введите название продукта: ").strip().lower()
                    if utilities.is_empty_string(product):
                        print("Ошибка. Имя пустое, попробуйте еще раз.")
                        continue
                    if product in products:
                        print("Ошибка. Такой продукт уже существует.")
                        continue
                    break

                while True:
                    quantity = input("Введите количество продукта: ")
                    if not utilities.is_positive_number(quantity):
                        print("Ошибка. Вы ввели некорректное количество, попробуйте еще раз.")
                        continue
                    break

                while True:
                    price = input("Введите стоимость продукта: ")
                    if not utilities.is_positive_number(price):
                        print("Ошибка. Вы ввели некорректную цену, попробуйте еще раз.")
                        continue
                    break

                while True:
                    unit = input("Введите в чем измеряется товар (кг, шт): ").strip().lower()
                    if unit not in ["кг", "шт"]:
                        print("Вы ввели некорректную единицу измерения, попробуйте еще раз.")
                        continue
                    break

                inventory_tools.add_product(products, product, quantity, price, unit)
                print("Добавлено.\n")

                if not utilities.ask_continue("Хотите добавить еще один продукт?"):
                    break

        case "3":
            while True:
                while True:
                    product = input("Введите название продукта: ").strip().lower()
                    if utilities.is_empty_string(product):
                        print("Ошибка. Имя пустое, попробуйте еще раз.")
                        continue
                    if product not in products:
                        print("Ошибка. Такого продукта не существует.")
                        continue
                    break

                current_qty = Decimal("0")
                new_qty = Decimal("0")
                d_delta = Decimal("0")

                while True:
                    delta_str = input("Введите изменение в количестве (для уменьшения используйте минус): ").strip()
                    if not utilities.is_number(delta_str):
                        print("Ошибка. Некорректный ввод, попробуйте еще раз.")
                        continue

                    # Перевод в Decimal
                    try:
                        d_delta = Decimal(delta_str)
                    except InvalidOperation:
                        print("Ошибка. Некорректный формат числа.")
                        continue

                    current_qty = Decimal(str(products[product]["quantity"]))
                    new_qty = current_qty + d_delta

                    # Проверка не уходит ли количество в минус
                    if new_qty < 0:
                        print("Ошибка. Вы пытаетесь уменьшить больше, чем у вас есть.")
                        continue
                    # Проверка для штучного товара
                    if products[product]["unit"] == "шт":
                        if d_delta % 1 != 0:
                            print("Ошибка. Для штучного товара изменение должно быть целым числом.")
                            continue
                    break

                inventory_tools.update_quantity(products, product, delta_str)
                print(f'Количество продукта "{product.capitalize()}" изменено: {current_qty} -> {new_qty}.\n')

                if not utilities.ask_continue("Хотите изменить еще один продукт?"):
                    break
        case "4":
            print("ЕЩЕ НЕ РАБОТАЕТ")
        case "5":
            print("ЕЩЕ НЕ РАБОТАЕТ")
        case "6":
            print("ЕЩЕ НЕ РАБОТАЕТ")
        case "0":
            json_tools.save_inventory(products ,"products")
            break
        case _:
            print("Ошибка. Такого действия нет, введите повторно.\n")
products_dict = {
    "яблоко": (50, 10),  # (цена за 1 штуку, количество на складе)
    "банан": (30, 5),
}


def print_product(key, value):
    total = value[0] * value[1]
    print(f"{key.capitalize()} — цена: {value[0]}, количество: {value[1]}, общая стоимость: {total}")


def show_products(products):
    for key, value in sorted(products.items()):
        print_product(key, value)
    print("")


def input_validation(number):
    try:
        return int(number)
    except ValueError:
        return None


def add_product(products):
    key = input("Введите название: ").lower().strip()
    if key in products:
        print(f'Товар - "{key.capitalize()}" уже есть на складе.\n')
    else:
        value_0 = input_validation(input("Введите цену за штуку: "))
        value_1 = input_validation(input("Введите количество: "))
        if None in (value_0, value_1) or min(value_0, value_1) < 0:
            print("Ввод некорректен. Попробуйте еще раз.\n")
        else:
            products[key] = (value_0, value_1)
            print("Сохранено.\n")


def update_quantity(products):
    key = input("Введите название товара для изменения его количества: ").lower().strip()
    if key not in products:
        print("Такого товара нет. Попробуйте еще раз.\n")
    else:
        value_1 = input_validation(input("Введите изменение количества: "))
        if value_1 is None:
            print("Ввод некорректен. Попробуйте еще раз.\n")
        else:
            tmp = list(products[key])
            tmp[1] += value_1
            if tmp[1] >= 0:
                products[key] = tuple(tmp)
                print("Сохранено.\n")
            else:
                print("Нельзя уменьшить количество ниже 0.\n")


def delete_product(products):
    key = input("Введите название товара для удаления: ").lower().strip()
    if key not in products:
        print("Такого товара нет. Попробуйте еще раз.\n")
    else:
        products.pop(key)
        print(f'Товар - "{key.capitalize()}" удален.\n')
    return products


def find_product(products):
    key = input("Введите название товара: ").lower().strip()
    if key not in products:
        print("Такого товара нет. Попробуйте еще раз.\n")
    else:
        print(f"{key.capitalize()} — цена: {products[key][0]}, количество: {products[key][1]}\n")


def sorted_product(products):
    print("0 - Сортировка по алфавиту\n"
          "1 - Сортировка по общей стоимости\n"
          "2 - Сортировка по цене за единицу\n"
          "3 - Сортировка по остатку на складе\n")
    choice = input("Выберите действие: ").strip()
    if choice == "0":
        show_products(products)
    elif choice == "1":
        sorted_total_cost = sorted(
            products.keys(),
            key=lambda k: products[k][0] * products[k][1],
            reverse=True)
        for total_cost in sorted_total_cost:
            print_product(total_cost, products[total_cost])
        print("")
    elif choice == "2":
        sorted_total_cost = sorted(
            products.keys(),
            key=lambda k: products[k][0],
            reverse=True)
        for total_cost in sorted_total_cost:
            print_product(total_cost, products[total_cost])
        print("")
    elif choice == "3":
        sorted_total_cost = sorted(
            products.keys(),
            key=lambda k: products[k][1],
            reverse=True)
        for total_cost in sorted_total_cost:
            print_product(total_cost, products[total_cost])
        print("")
    else:
        print("Ошибка. Такого действия нет, введите повторно.\n")


def total_value(products):
    total = 0
    for value in products.values():
        total += value[0] * value[1]
    print(f"Общая стоимость всех товаров на складе: {total}\n")


def main(products):
    print("1 — Показать все товары\n"
          "2 — Добавить новый товар\n"
          "3 — Изменить количество товара\n"
          "4 — Удалить товар\n"
          "5 — Найти товар\n"
          "6 — Показать общую стоимость склада\n"
          "0 — Выход\n")
    while True:
        choice = input("Выберите действие: ").strip()
        if choice == "0":
            break
        elif choice == "1":
            if products:
                show_products(products)
                while True:
                    choice = input("Хотите изменить фильтр сортировки?\n"
                                   "Выберите действие (0 - нет, 1 - да): ").strip()
                    if choice == "0":
                        break
                    elif choice == "1":
                        sorted_product(products)
                    else:
                        print("Ошибка. Такого действия нет, введите повторно.\n")
            else:
                print("Склад пуст.\n")
        elif choice == "2":
            add_product(products)
            while True:
                choice = input("Хотите еще добавить товар?\n"
                               "Выберите действие (0 - нет, 1 - да): ").strip()
                print("")
                if choice == "0":
                    break
                elif choice == "1":
                    add_product(products)
                else:
                    print("Ошибка. Такого действия нет, введите повторно.\n")
        elif choice == "3":
            update_quantity(products)
            while True:
                choice = input("Хотите еще изменить количество товара? \n"
                               "Выберите действие (0 - нет, 1 - да): ").strip()
                print("")
                if choice == "0":
                    break
                elif choice == "1":
                    update_quantity(products)
                else:
                    print("Ошибка. Такого действия нет, введите повторно.\n")
        elif choice == "4":
            delete_product(products)
            while True:
                choice = input("Хотите еще удалить товар?\n"
                               "Выберите действие (0 - нет, 1 - да): ").strip()
                print("")
                if choice == "0":
                    break
                elif choice == "1":
                    delete_product(products)
                else:
                    print("Ошибка. Такого действия нет, введите повторно.\n")
        elif choice == "5":
            find_product(products)
            while True:
                choice = input("Хотите еще найти товар?\n"
                               "Выберите действие (0 - нет, 1 - да): ").strip()
                print("")
                if choice == "0":
                    break
                elif choice == "1":
                    find_product(products)
                else:
                    print("Ошибка. Такого действия нет, введите повторно.\n")
        elif choice == "6":
            total_value(products)
        elif choice == "7007":
            print(products)
        else:
            print("Ошибка. Такого действия нет, введите повторно.\n")


main(products_dict)
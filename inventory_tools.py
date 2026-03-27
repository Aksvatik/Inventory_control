from decimal import Decimal, InvalidOperation


# Вывод продукта
def print_product(product: str, value: dict) -> str:
    quantity = Decimal(str(value["quantity"]))
    price = Decimal(str(value["price"]))
    total_cost = quantity * price

    return (
        f"{product.capitalize()} — цена: {format(price, '.2f')}₽, "
        f"количество: {format(quantity, '.2f')} {value['unit']}, "
        f"общая стоимость: {format(total_cost, '.2f')}₽"
    )


# Добавление нового продукта
def add_product(products: dict, product: str, quantity: str, price: str, unit: str) -> None:
    products[product] = {
        "quantity": float(quantity),
        "price": float(price),
        "unit": unit
    }


# Изменение количества продукта
def update_quantity(products: dict, product: str, delta: str) -> None:
    # Перевод в Decimal
    d_delta = Decimal(delta)
    current_quantity = Decimal(str(products[product]["quantity"]))

    products[product]["quantity"] = float(current_quantity + d_delta)


# Удаление продукта
def delete_product(products: dict, product: str) -> bool:
    # Проверка на существование продукта
    if product not in products:
        return False

    # Удаление продукта
    products.pop(product)
    return True


# Поиск продукта
def find_product(products: dict, product: str) -> dict | None:
    # Проверка на существование продукта
    if product not in products:
        return None

    return products[product]


# Общая стоимость всех продуктов
def total_value(products: dict) -> Decimal:
    total_cost = Decimal("0")

    for product, value in products.items():
        quantity = Decimal(str(value["quantity"]))
        price = Decimal(str(value["price"]))
        total_cost += quantity * price

    return total_cost


def sorted_inventory(products):
    pass
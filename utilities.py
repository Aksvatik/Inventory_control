def is_empty_string(string: str) -> bool:
    if not string:
        return True
    return False


def is_number(string: str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False


def is_positive_number(string: str) -> bool:
    if is_number(string) and float(string) > 0:
            return True
    return False


def ask_continue(question: str) -> bool:
    while True:
        cmd = input(f"{question}\nВыберите действие (0 - нет, 1 - да): ").strip()
        match cmd:
            case "0":
                return False
            case "1":
                return True
            case _:
                print("Ошибка. Такого действия нет, введите повторно.\n")
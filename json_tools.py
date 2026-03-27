import json


# Выгрузка из json
def load_inventory(name) -> dict:
    try:
        with open(f"data/{name}.json", "r", encoding="utf-8") as file:
            data = json.load(file)

        return data
    # Если файл не существует
    except (FileNotFoundError, json.decoder.JSONDecodeError):
        data = {}

        return data


# Сохранение в json
def save_inventory(data, name):
    with open(f"data/{name}.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
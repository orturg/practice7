def write_to_console(text):
    """Функція для виводу тексту у консоль,"""
    print(text)


def write_to_file(filename, text):
    """Функція для запису до файлу за допомогою вбудованих можливостей python"""
    with open(filename, "a", encoding="utf-8") as file:
        file.write(text + "\n")

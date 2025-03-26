import pandas as panda

def read_from_console():
    """Функція для вводу тексту з консолі,"""
    return input("введіть текст ")


def read_from_file(filename):
    """Функція для зчитування з файлу за допомогою вбудованих можливостей python,"""
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return "такого файлу не існує"


def read_from_file_pandas(filename):
    """Функція для зчитування з файлу за допомогою бібліотеки pandas."""

    try:
        df = panda.read_csv(filename, header=None)
        return df.to_string(index=False, header=False)
    except FileNotFoundError:
        return "такого файлу не існує"
    except panda.errors.EmptyDataError:
        return "файл пустий"
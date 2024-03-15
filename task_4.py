import csv
import random

def read_csv_file(file_path):
    """
    Читает CSV-файл и возвращает его содержимое в виде списка строк.

    Args:
        file_path (str): Путь к CSV-файлу.

    Returns:
        list: Список, содержащий строки CSV-файла.
    """
    with open(file_path, encoding='UTF-8') as file:
        lines = file.read().split('\n')
        return [line.split(',') for line in lines]

def generation_login(full_name):
    """
    Генерирует логин на основе полного имени.

    Args:
        full_name (str): Полное имя студента.

    Returns:
        str: Сгенерированный логин.
    """
    name = full_name.split(' ')

    if len(name) == 1:
        return 'Name'

    login = f'{name[0]}_{str(name[1])[0]}{str(name[2])[0]}'
    return login

def generate_password(length=8):
    """
    Генерирует случайный пароль заданной длины.

    Args:
        length (int): Длина пароля (по умолчанию 8 символов).

    Returns:
        str: Сгенерированный пароль.
    """
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    return ''.join(random.choice(alphabet) for _ in range(length))

def main():
    """
    Основная функция для обработки данных студентов из CSV-файла.
    """
    file_path = "C:/Users/oppoe/Downloads/students (1).csv"
    data = read_csv_file(file_path)[:-1]
    with open('students_password.csv ', 'a+', newline='', encoding='Utf-8') as file:
        writer = csv.writer(file)
        sp_for_new = []
        for i in range(len(data)):
            sp_for_new.append(data[i][0])
            sp_for_new.append(data[i][1])
            sp_for_new.append(data[i][2])
            sp_for_new.append(data[i][3])
            sp_for_new.append(generation_login(data[i][1]))
            sp_for_new.append(generate_password())

            # Записываем данные в файл
            writer.writerow(sp_for_new)
            sp_for_new = []

if __name__ == "__main__":
    main()

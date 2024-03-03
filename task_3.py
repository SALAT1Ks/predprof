import csv

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
        return [line.split('\t') for line in lines]

def linear_search(arr, target):
    """
    Выполняет линейный поиск в списке данных студентов.

    Args:
        arr (list): Список данных студентов в формате CSV.
        target (str): Фамилия студента, которую нужно найти.

    Returns:
        None
    """
    for i in range(len(arr)):
        if arr[i][0] == target:
            print(f'{arr[i][0]} {str(arr[i][1])[0]} {arr[i][3]} {arr[i][2]} {arr[i][4]}')

def main():
    """
    Основная функция для обработки данных студентов из CSV-файла.
    """
    file_path = "C:/Users/oppoe/Downloads/9.csv"
    data = read_csv_file(file_path)

    while True:
        surname = input()
        if surname == 'СТОП':
            break
        else:
            linear_search(data, surname)

if __name__ == "__main__":
    main()

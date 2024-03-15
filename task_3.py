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
        return [line.split(',') for line in lines]

def linear_search(arr, target):
    """
    Выполняет линейный поиск в списке данных студентов.

    Args:
        arr (list): Список данных студентов в формате CSV.
        target (str): Фамилия студента, которую нужно найти.

    Returns:
        None
    """
    c = 0
    for i in range(len(arr)):
        if arr[i][2] == target:
            name = arr[i][1].split(' ')
            print(f'Проект № {arr[i][0]} делал: {name[1][0]}. {name[0]} он(а) получил(а) оценку - {arr[i][4]}.')
            c+=1
    if c == 0:
        print('Ничего не найдено.')


def main():
    """
    Основная функция для обработки данных студентов из CSV-файла.
    """
    file_path = "C:/Users/oppoe/Downloads/students (1).csv"
    data = read_csv_file(file_path)[:-1]

    while True:
        id_project = input()
        if id_project == 'СТОП':
            break
        else:
            linear_search(data, id_project)

if __name__ == "__main__":
    main()

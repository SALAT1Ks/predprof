import csv


def read_csv_file(file_path):
    """
    Читает CSV-файл и возвращает его содержимое в виде списка строк.

    Аргументы:
        file_path (str): Путь к CSV-файлу.

    Возвращается:
        list: Список, содержащий строки CSV-файла.
    """
    with open(file_path, encoding='UTF-8') as file:
        lines = file.read().split('\n')
        return [line.split(',') for line in lines]

def insertion_sort(arr):
    """
    Сортировка вставками по последнему элементу внутренних списков.

    Args:
        arr (list): Список списков длиной в 5 элементов, который нужно отсортировать.

    Returns:
        list: Отсортированный список.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key[-1] < arr[j][-1]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

    return arr[::-1]

def main():
    """
    Основная функция для обработки данных студентов из CSV-файла.
    """
    file_path = "C:/Users/oppoe/Downloads/students (1).csv"
    data = read_csv_file(file_path)
    print(data)
    data = insertion_sort(data)
    print(data)
    number_winner = 1
    for i in range(len(data)):
        if '10' in data[i][3]:
            print(f'{number_winner} место {data[i][1]} {data[i][0]}')
            number_winner += 1
        elif number_winner == 4:
            break

if __name__ == "__main__":
    main()

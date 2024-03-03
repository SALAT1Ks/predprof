import csv

# Функция для чтения CSV-файла и возвращения его содержимого в виде списка строк
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

# Функция для хэширования имени
def hash(name):
    """
    Вычисляет хэш-код для строки.

    Args:
        name (str): Строка, для которой нужно вычислить хэш-код.

    Returns:
        int: Хэш-код строки.
    """
    m = 10**9 + 9
    degree = 0

    z = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67]
    q = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я', 'А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я', ' ']

    hash_score = 0
    for i in range(len(name)):
        hash_score += (z[q.index(str(name[i]))] + 68**degree)

    return hash_score % m

# Основная функция для обработки данных студентов из CSV-файла
def main():
    """
    Основная функция для обработки данных студентов из CSV-файла.
    """
    file_path = "C:/Users/oppoe/Downloads/students (1).csv"
    data = read_csv_file(file_path)

    with open('students_with_hash.csv', 'a+', newline='') as file:
        writer = csv.writer(file)
        sp_for_new = []
        for i in range(len(data)):
            # Если текущая строка - заголовок, записываем новый заголовок
            if data[i] == ['id', 'Name', 'titleProject_id', 'class', 'score']:
                first_row = ['name_hash', 'Name', 'titleProject_id', 'class', 'score']
                writer.writerow(first_row)
                continue
            # Если текущая строка пустая, пропускаем её
            if data[i] == ['']:
                continue
            # Получаем хэш для имени и записываем данные во временный список
            sp_for_new.append(hash(data[i][1]))
            sp_for_new.append(data[i][1])
            sp_for_new.append(data[i][2])
            sp_for_new.append(data[i][3])
            # Записываем данные из временного списка в файл
            writer.writerow(sp_for_new)
            sp_for_new = []

# Проверяем, что код выполняется как отдельный скрипт
if __name__ == "__main__":
    main()

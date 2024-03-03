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


def main():
    """
    Основная функция для обработки данных студентов из CSV-файла.
    """
    file_path = "C:/Users/oppoe/Downloads/students (1).csv"
    data = read_csv_file(file_path)
    print(data)

    student_scores = []
    subject = ''
    grade = ''

    # Поиск оценок студента Колесниковой Ксении
    for row in range(len(data)):
        if 'Хадаров Владимир' in data[row][1]:
            print(f'Ты получил: {data[row][-1]}, за проект {data[row][2]}')

            clas = data[row][3]
            break

    final_scores = []
    proverka_na_pystoe_znachenye = ['']
    # Подсчет средней оценки по указанному предмету и классу
    for row in range(len(data)):
        if data[row] == proverka_na_pystoe_znachenye:
            break
        elif data[row][3] == clas:
            print(data[row][4])
            final_scores.append(int(data[row][4]))

    average_score = round(sum(final_scores) / len(final_scores), 3)

    # Запись средней оценки в новый CSV-файл
    with open('student_new.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([average_score])


if __name__ == "__main__":
    main()

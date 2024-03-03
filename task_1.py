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
        return [line.split('\t') for line in lines]


def main():
    """
    Основная функция для обработки данных студентов из CSV-файла.
    """
    file_path = "C:/Users/oppoe/Downloads/9.csv"
    data = read_csv_file(file_path)

    student_scores = []
    subject = ''
    grade = ''

    # Поиск оценок студента Колесниковой Ксении
    for row in data:
        if row[0] == 'Колесникова' and row[1] == 'Ксения':
            print(f'Ты получил: {row[4]}, за предмет {row[3]}')
            subject = row[3]
            grade = row[2]

    final_scores = []
    proverka_na_pystoe_znachenye = ['']
    # Подсчет средней оценки по указанному предмету и классу
    for row in data:
        if row == proverka_na_pystoe_znachenye:
            break
        elif row[2] == grade and row[3] == subject:
            final_scores.append(int(row[4]))

    average_score = round(sum(final_scores) / len(final_scores), 3)

    # Запись средней оценки в новый CSV-файл
    with open('student_new.csv', 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([average_score])


if __name__ == "__main__":
    main()

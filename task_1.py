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
    data = read_csv_file(file_path)[:-1]



    for row in range(len(data)):
        if 'Хадаров Владимир' in data[row][1]:
            print(f'Ты получил: {data[row][-1]}, за проект {data[row][2]}')
            break

    class_none = []
    for i in range(len(data)):
        if data[i][-1] == 'None':
            class_none.append(data[i][3])

    class_none_update = []
    trash_for_all_none = []
    trash_without_none = []
    for i in range(len(class_none)):
        for ii in range(len(data)):
            if data[ii][3] == class_none[i]:
                trash_for_all_none.append(data[ii][-1])
            if ii+1 == len(data):
                if 'None' in trash_for_all_none:
                    trash_for_all_none.remove('None')
                trash_without_none.append(trash_for_all_none)
                trash_for_all_none = []
    trash_for_int = []
    nakonecto = []
    for i in range(len(trash_without_none)):
        for ii in range(len(trash_without_none[i])):
            trash_for_int.append(int(trash_without_none[i][ii]))
        nakonecto.append(trash_for_int)
        trash_for_int = []

    for i in range(len(trash_without_none)):
        class_none_update.append(round((sum(nakonecto[i])/len(nakonecto[i])), 3))

    c = 0
    for i in range(len(data)):
        if data[i][-1] == 'None':

            data[i][-1] = class_none_update[c]
            c+= 1

    with open('students_pass.csv ', 'a+', newline='', encoding='UTF-8') as file:
        writer = csv.writer(file)
        for i in range(len(data)):
            writer.writerow(data[i])

if __name__ == "__main__":
    main()

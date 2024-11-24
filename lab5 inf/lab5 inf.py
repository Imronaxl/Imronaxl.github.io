import pandas as pd

def filter_multiple_dates(input_file, output_file, target_dates):
    # Читаем исходный CSV-файл
    try:
        data = pd.read_csv(input_file)
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
        return

    # Создаём пустой DataFrame для хранения результата
    result_data = pd.DataFrame()

    # Фильтруем данные для каждой указанной даты
    for date in target_dates:
        try:
            filtered_data = data[data['<DATE>'] == date]
            if filtered_data.empty:
                print(f"Данные для даты {date} не найдены.")
            else:
                print(f"Добавлены данные для даты {date}.")
                result_data = pd.concat([result_data, filtered_data], ignore_index=True)
        except KeyError:
            print("Колонка <DATE> не найдена в файле. Проверьте формат.")
            return

    # Сохраняем объединённые данные в итоговый CSV
    if not result_data.empty:
        try:
            result_data.to_csv(output_file, index=False)
            print(f"Файл успешно сохранён: {output_file}")
        except Exception as e:
            print(f"Ошибка при сохранении файла: {e}")
    else:
        print("Нет данных для указанных дат. Файл не был создан.")

# Пример использования

input_file = 'SPFB.RTS-12.18_180901_181231.csv'  # Укажите путь к исходному файлу
output_file = 'data.csv'  # Итоговый CSV-файл
target_dates = ['25/09/18', '23/10/18', '23/11/18', '03/12/18']  # Список дат

filter_multiple_dates(input_file, output_file, target_dates)

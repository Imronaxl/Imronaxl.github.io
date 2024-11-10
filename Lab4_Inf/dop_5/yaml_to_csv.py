import yaml
import csv

# Преобразуем данные YAML в CSV
def yaml_to_csv(yaml_file = "./in_yaml.yaml", csv_file ="./out_csv.csv"):
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    
    # Предполагаем, что данные в формате словаря верхнего уровня
    root_key = list(data.keys())[0]
    records = data[root_key]  # Получаем список записей
    
    # Определяем заголовки CSV на основе ключей первого элемента
    headers = set()
    for record in records:
        headers.update(record.keys())
    headers = list(headers)

    # Запись в CSV файл
    with open(csv_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=headers)
        writer.writeheader()
        for record in records:
            writer.writerow(record)

# Вызов функции для конвертации
yaml_to_csv()

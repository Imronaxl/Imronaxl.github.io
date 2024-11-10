import yaml
import xml.etree.ElementTree as ET
from xml.dom import minidom

def dict_to_xml(tag, data):
    """Конвертирует данные из словаря в XML."""
    # Создаем элемент с указанным тегом
    elem = ET.Element(tag)
    
    # Если значение является словарем, рекурсивно обрабатываем каждый элемент
    if isinstance(data, dict):
        for key, value in data.items():
            child = dict_to_xml(key, value)
            elem.append(child)
    # Если значение является списком, обрабатываем каждый элемент списка
    elif isinstance(data, list):
        for item in data:
            child = dict_to_xml(tag, item)  # Используем текущий тег для каждого элемента списка
            elem.append(child)
    else:
        # Для простых значений добавляем текстовое содержимое
        elem.text = str(data)
    
    return elem


def convert_yaml_to_xml(yaml_file = "./in_yaml.yaml", xml_file = "./out_xml.xml"):
    """Конвертирует YAML в XML и записывает результат в файл."""
    # Чтение данных из YAML
    with open(yaml_file, 'r', encoding='utf-8') as f:
        data_dict = yaml.safe_load(f)

    # Получаем корневой тег из словаря и создаем соответствующий XML
    for root_tag, data in data_dict.items():
        root_element = dict_to_xml(root_tag, data)
    
    # Создаем дерево XML
    tree = ET.ElementTree(root_element)

    # Форматируем XML, добавляя отступы и новые строки
    rough_string = ET.tostring(root_element, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")

    # Записываем в XML файл с форматированием
    with open(xml_file, 'w', encoding='utf-8') as f:
        f.write(pretty_xml)


# Пример использования
convert_yaml_to_xml()

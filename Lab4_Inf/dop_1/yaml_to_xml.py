import yaml
import xml.etree.ElementTree as ET
from xml.dom import minidom

def process(yaml_path = "./in_yaml.yaml", xml_path = "./out_xml.xml"):
    # Чтение YAML файла
    with open(yaml_path, 'r', encoding='utf-8') as yaml_file:
        data = yaml.safe_load(yaml_file)

    # Создание XML структуры
    root = ET.Element("schedule")

    for entry in data["schedule"]:
        para = ET.SubElement(root, "para")
        for key, value in entry.items():
            element = ET.SubElement(para, key)
            element.text = str(value)

    # Преобразование XML с форматированием
    rough_string = ET.tostring(root, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    pretty_xml = reparsed.toprettyxml(indent="  ")

    # Запись отформатированного XML в файл
    with open(xml_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(pretty_xml)

process()

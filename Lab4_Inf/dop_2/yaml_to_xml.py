import re

def yaml_to_xml(yaml_content, indent=2):
    xml_str = ""
    item_pattern = re.compile(r"^(\s*)([a-zA-Z0-9_]+):\s*'?([^\n']*)'?")
    list_item_pattern = re.compile(r"^\s*-\s+'?(.+?)'?")

    lines = yaml_content.splitlines()
    i = 0

    while i < len(lines):
        line = lines[i]
        
        # Проверка на ключ-значение
        match = item_pattern.match(line)
        if match:
            space, key, value = match.groups()
            if value:
                xml_str += " " * indent + f"<{key}>{value}</{key}>\n"
            else:
                xml_str += " " * indent + f"<{key}>\n"
                nested_content = ""
                i += 1
                while i < len(lines) and lines[i].startswith(" " * (len(space) + 2)):
                    nested_content += lines[i] + "\n"
                    i += 1
                xml_str += yaml_to_xml(nested_content, indent + 2)
                xml_str += " " * indent + f"</{key}>\n"
            i += 1

        # Проверка на элементы списка
        elif list_item_pattern.match(line):
            list_key = lines[i - 1].split(":")[0].strip()
            xml_str = xml_str.rstrip(f"</{list_key}>\n") + "\n"
            while i < len(lines) and list_item_pattern.match(lines[i]):
                item_value = list_item_pattern.match(lines[i]).group(1)
                xml_str += " " * indent + f"  <{list_key[:-1]}>{item_value}</{list_key[:-1]}>\n"
                i += 1
            xml_str += " " * indent + f"</{list_key}>\n"
            
        else:
            i += 1
    return xml_str

def process(yaml_path="in_yaml.yaml", xml_path="out_xml.xml"):
    with open(yaml_path, 'r', encoding='utf-8') as yaml_file:
        yaml_content = yaml_file.read()
    
    xml_content = "<schedule>\n" + yaml_to_xml(yaml_content, indent=2) + "</schedule>"

    with open(xml_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_content)
    print(f"XML content written to {xml_path}")

process()

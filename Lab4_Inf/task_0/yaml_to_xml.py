import yaml

def yaml_to_xml(data, indent=0):
    xml_str = ""
    for key, value in data.items():
        xml_str += " " * indent + f"<{key}>"
        
        if isinstance(value, dict):  # Nested dictionary
            xml_str += "\n" + yaml_to_xml(value, indent + 2) + " " * indent
        elif isinstance(value, list):  # List of items
            xml_str += "\n"
            for item in value:
                if isinstance(item, dict):
                    xml_str += " " * (indent + 2) + f"<{key[:-1]}>\n" + yaml_to_xml(item, indent + 4)
                    xml_str += " " * (indent + 2) + f"</{key[:-1]}>\n"
                else:
                    xml_str += " " * (indent + 2) + f"<{key[:-1]}>{item}</{key[:-1]}>\n"
            xml_str += " " * indent
        else:
            xml_str += f"{value}"
        
        xml_str += f"</{key}>\n"
    return xml_str

def process(yaml_path="in_yaml.yaml", xml_path="out_xml.xml"):
    with open(yaml_path, 'r', encoding='utf-8') as yaml_file:
        data = yaml.safe_load(yaml_file)
    
    xml_content = yaml_to_xml(data)
    
    with open(xml_path, 'w', encoding='utf-8') as xml_file:
        xml_file.write(xml_content)
    print(f"XML content written to {xml_path}")

if __name__ == "__main__":
    process()

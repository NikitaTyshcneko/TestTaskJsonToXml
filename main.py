import json
import xml.etree.ElementTree as ElementTree
from xml.dom import minidom


def dict_to_xml(root_name: str, data: dict, indent: int = 0):
    root = ElementTree.Element(root_name)
    for key, value in sorted(data.items()):
        elements_conditions(root, key, value, indent)
    return root


def elements_conditions(root, key, value, indent):
    if isinstance(value, dict):
        root.append(dict_to_xml(key, value, indent + 1))
    elif isinstance(value, list):
        add_list_value(root, key, value, indent)
    else:
        root.append(create_element(key, value))


def add_list_value(root: ElementTree.Element, key, value, indent: int):
    elements_tag = ElementTree.Element(key)
    for val in value:
        elements_conditions(elements_tag, 'element', val, indent)
    root.append(elements_tag)


def create_element(element_name, value) -> ElementTree.Element:
    element = ElementTree.Element(element_name)
    element.text = str(value)
    return element


def prettify_xml(elem, indent="   "):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent=indent)


def main():
    with open('data.json') as json_file:
        data = json.load(json_file)

    root_element = dict_to_xml("root", data)
    xml_string = prettify_xml(root_element, indent="   ")

    print(xml_string)


if __name__ == '__main__':
    main()

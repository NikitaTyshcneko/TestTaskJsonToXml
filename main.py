import argparse
import json
import xml.etree.ElementTree as ElementTree
from xml.dom import minidom


def dict_to_xml(root_name: str, data: dict):
    root = ElementTree.Element(root_name)
    for key, value in sorted(data.items()):
        elements_conditions(root, key, value)
    return root


def elements_conditions(root, key, value):
    if isinstance(value, dict):
        root.append(dict_to_xml(key, value))
    elif isinstance(value, list):
        add_list_value(root, key, value)
    else:
        root.append(create_element(key, value))


def add_list_value(root: ElementTree.Element, key, value):
    elements_tag = ElementTree.Element(key)
    for val in value:
        elements_conditions(elements_tag, 'element', val)
    root.append(elements_tag)


def create_element(element_name, value) -> ElementTree.Element:
    element = ElementTree.Element(element_name)
    element.text = str(value)
    return element


def prettify_xml(elem):
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml()


def main():
    parser = argparse.ArgumentParser(description='Convert JSON to XML')
    parser.add_argument('filename', help='JSON file to convert')
    parser.add_argument('--rootname', help='Name for the root element', default='root')
    args = parser.parse_args()

    with open(args.filename) as json_file:
        json_data = json.load(json_file)

    root_element = dict_to_xml(args.rootname, json_data)
    xml_string = prettify_xml(root_element)

    print(xml_string)


if __name__ == '__main__':
    main()

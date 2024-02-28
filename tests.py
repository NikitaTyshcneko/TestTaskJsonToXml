import unittest
import json

from main import dict_to_xml, prettify_xml


class TestJsonToXmlConversion(unittest.TestCase):

    def test_basic_elements(self):
        json_data = {'name': 'John', 'age': 30}
        expected_xml = '<?xml version="1.0" ?>\n<root>\n   <age>30</age>\n   <name>John</name>\n</root>\n'

        xml_root = dict_to_xml('root', json_data)
        xml_string = prettify_xml(xml_root)

        self.assertEqual(xml_string, expected_xml)

    def test_nested_elements(self):
        json_data = {'person': {'name': 'Alice', 'age': 25, 'address': {'city': 'New York', 'zip': 10001}}}
        expected_xml = ('<?xml version="1.0" ?>\n<root>\n   <person>\n      <address>\n         <city>New '
                        'York</city>\n         <zip>10001</zip>\n      </address>\n      <age>25</age>\n      '
                        '<name>Alice</name>\n   </person>\n</root>\n')

        xml_root = dict_to_xml('root', json_data)
        xml_string = prettify_xml(xml_root)

        self.assertEqual(xml_string, expected_xml)

    def test_array_elements(self):
        json_data = {'numbers': [1, 2, 3, 4, 5]}
        expected_xml = ('<?xml version="1.0" ?>\n<root>\n   <numbers>\n      <element>1</element>\n      '
                        '<element>2</element>\n      <element>3</element>\n      <element>4</element>\n      '
                        '<element>5</element>\n   </numbers>\n</root>\n')

        xml_root = dict_to_xml('root', json_data)
        xml_string = prettify_xml(xml_root)

        self.assertEqual(xml_string, expected_xml)

    def test_empty_json_input(self):
        json_data = {}
        expected_xml = '<?xml version="1.0" ?>\n<root/>\n'

        xml_root = dict_to_xml('root', json_data)
        xml_string = prettify_xml(xml_root)

        self.assertEqual(xml_string, expected_xml)

    def test_invalid_json_input(self):
        invalid_json_data = '{"name": "John", "age": }'  # Invalid JSON with syntax error
        with self.assertRaises(json.JSONDecodeError):
            json.loads(invalid_json_data)


if __name__ == '__main__':
    unittest.main()

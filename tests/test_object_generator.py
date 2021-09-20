from states_generator.object_generator import ObjectGenerator
from unittest import TestCase
from unittest.mock import Mock


class ObjectGeneratorTest(TestCase):
    def test_add_object(self):
        object_generator = ObjectGenerator("python", "testInterface")
        object_generator._write_file = Mock(side_effect=self.assert_write_interface)
        object_dict = {
            "initialState": "testState1",
            "attributes": {"testAttribute": "int", "testAttribute2": "str"},
            "functions": {
                "testFunction": {"arg1": "int", "arg2": "str"},
                "testFunction2": {"arg1": "int"},
            },
            "interface": {
                "attributes": {
                    "testAttributeState1": "int",
                    "testAttributeState2": None,
                },
                "functions": {
                    "testFunctionState1": {"arg1": "int", "arg2": "dict"},
                    "testFunctionState2": {"arg1": "str"},
                },
            },
            "states": {
                "testState1": {"testFunctionState1": "testState2"},
                "testState2": {"testFunctionState2": "testState1"},
            },
        }
        object_generator.add_object("objectTest", object_dict)

    def assert_write_interface(self, file_path, parsed_template):
        self.assertEqual(file_path, "states/models/objectTest.py")
        with open("./tests/files/expected/objectTest.py") as f:
            self.assertEqual(f.read(), parsed_template)

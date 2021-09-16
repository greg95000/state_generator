from states_generator.interface_generator import InterfaceGenerator
from unittest import TestCase
from unittest.mock import Mock
from states_generator.interface_generator import InterfaceGenerator


class InterfaceGeneratorTest(TestCase):
    def test_add_interface(self):
        state_generator = InterfaceGenerator("python", "testInterface")
        state_generator._write_file = Mock(side_effect=self.assert_write_interface)
        states = {
            "attributes": {"testAttributeState1": "int", "testAttributeState2": None},
            "functions": {
                "testFunctionState1": {"arg1": "int", "arg2": "dict"},
                "testFunctionState2": {"arg1": "str"},
            },
        }
        state_generator.add_interface("interfaceTest", states)

    def assert_write_interface(self, file_path, parsed_template):
        self.assertEqual(file_path, "states/interfaces/interfaceTestInteface.py")
        with open("./tests/files/expected/interfaceTestInteface.py") as f:
            self.assertEqual(f.read(), parsed_template)

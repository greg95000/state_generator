from unittest import TestCase
import unittest
from unittest.mock import Mock, mock_open, patch
from jinja2.exceptions import TemplateNotFound
from states_generator.states_generator import (
    StateGenerator,
    ExtensionNotFound,
)


class StatesGeneratorTest(TestCase):
    def test_get_template(self):
        state_generator = StateGenerator("python", "blop")
        template = state_generator._get_template("interface")
        self.assertIsNotNone(template)
        self.assertEqual(template.name, "interface_template.py")

    def test_get_template_fail(self):
        state_generator = StateGenerator("blop", "not the root path")
        with self.assertRaises(ExtensionNotFound):
            state_generator._get_template("objectName")

        state_generator = StateGenerator("python", "root_path")
        with self.assertRaises(TemplateNotFound):
            state_generator._get_template("blop")

    def test_add_interface(self):
        state_generator = StateGenerator("python", "testInterface")
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

from states_generator.abstract_generator import AbstractGenerator
from unittest.case import TestCase
from states_generator.interface_generator import InterfaceGenerator
from states_generator.abstract_generator import ExtensionNotFound
from jinja2.exceptions import TemplateNotFound


class AbstractGeneratorTest(TestCase):
    def test_get_template(self):
        abstract_generator = AbstractGenerator("python", "blop")
        template = abstract_generator._get_template("interface")
        self.assertIsNotNone(template)
        self.assertEqual(template.name, "interface_template.j2")

    def test_get_template_fail(self):
        state_generator = InterfaceGenerator("blop", "not the root path")
        with self.assertRaises(ExtensionNotFound):
            state_generator._get_template("objectName")

        state_generator = InterfaceGenerator("python", "root_path")
        with self.assertRaises(TemplateNotFound):
            state_generator._get_template("blop")

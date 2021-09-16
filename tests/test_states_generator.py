from unittest import TestCase
from states_generator.states_generator import (
    StateGenerator,
)


class StatesGeneratorTest(TestCase):
    def assert_write_interface(self, file_path, parsed_template):
        self.assertEqual(file_path, "states/interfaces/interfaceTestInteface.py")
        with open("./tests/files/expected/interfaceTestInteface.py") as f:
            self.assertEqual(f.read(), parsed_template)

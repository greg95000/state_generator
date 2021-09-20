from unittest import TestCase
from unittest.mock import Mock
from states_generator.states_generator import (
    StateGenerator,
)


class StatesGeneratorTest(TestCase):
    def assert_write_state(self, file_path, parsed_template):
        self.assertIn(
            file_path,
            ["states/states/testState1State.py", "states/states/testState2State.py"],
        )
        if file_path == "states/states/testState1State.py":
            with open("./tests/files/expected/testState1.py") as f:
                self.assertEqual(f.read(), parsed_template)
        elif file_path == "states/states/testState2State.py":
            with open("./tests/files/expected/testState2.py") as f:
                self.assertEqual(f.read(), parsed_template)

    def test_add_state(self):
        state_generator = StateGenerator("python", "testInterface")
        state_generator._write_file = Mock(side_effect=self.assert_write_state)
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
                "testState1": {
                    "testFunctionState1": "testState2",
                    "testFunctionState2": "testState1",
                },
                "testState2": {"testFunctionState2": "testState1"},
            },
        }
        state_generator.interface_functions = [
            "testFunctionState1",
            "testFunctionState2",
        ]
        state_generator.add_states(
            "statesTest",
            object_dict.get("interface"),
            object_dict.get("states"),
        )

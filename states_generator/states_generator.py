from states_generator.constants import STATES_DIR, TEMPLATE_EXTENSION
from states_generator.abstract_generator import (
    AbstractGenerator,
    StateNotFound,
)
from states_generator.utils import beautify_template_from_language


class InterfaceMethodNotFound(Exception):
    pass


class StateGenerator(AbstractGenerator):
    def __init__(self, template_type: str, root_path: str) -> None:
        super().__init__(template_type, root_path)
        self.interface_functions = []
        self.states_names = []

    def _does_state_name_exists(self, state_name):
        if state_name not in self.states_names:
            raise StateNotFound(
                "State {state_name} not found".format(state_name=state_name)
            )

    def _get_states_name(self, states):
        self.states_names = [state for state in states]

    def _does_interface_function_exists(self, state_name, function_name):
        if function_name not in self.interface_functions:
            raise InterfaceMethodNotFound(
                "Method {function_name} used in state {state_name} not found".format(
                    function_name=function_name, state_name=state_name
                )
            )

    def _validate_states(self, states):
        self._get_states_name(states)
        for state, action_dict in states.items():
            self._does_state_name_exists(state)
            function_call, state_call = list(action_dict.items())[0]
            self._does_interface_function_exists(state, function_call)
            self._does_state_name_exists(state_call)

    def add_states(self, object_name, interface: dict, states: dict) -> None:
        self._validate_states(states)
        template = self._get_template("state")
        for state, action_dict in states.items():
            parsed_template = template.render(
                attributes=interface.get("attributes", []) or [],
                functions=interface.get("functions", []) or [],
                state_name=state,
                functions_call=action_dict,
                object_name=object_name,
                root_path=self.root_path,
            )
            file_path = "{state_dir}/{state_name}State.{extension}".format(
                state_dir=STATES_DIR,
                state_name=state,
                extension=TEMPLATE_EXTENSION[self.template_type],
            )
            self._write_file(
                file_path,
                beautify_template_from_language(self.template_type, parsed_template),
            )

    def update_states(self, states: dict) -> None:
        pass

    def _reverse_read_file(self, path: str) -> None:
        pass

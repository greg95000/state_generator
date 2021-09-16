from states_generator.abstract_generator import AbstractGenerator


class ObjectGenerator(AbstractGenerator):
    def __init__(self, template_type: str, root_path: str) -> None:
        super().__init__(template_type, root_path)

    def _does_state_name_exists(self, state_name):
        pass

    def add_object(self, object):
        pass

    def update_object(self):
        pass

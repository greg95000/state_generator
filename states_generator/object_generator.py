from states_generator.abstract_generator import AbstractGenerator
from states_generator.constants import MODELS_DIR, TEMPLATE_EXTENSION
from states_generator.utils import from_camel_to_snake, beautify_template_from_language


class ObjectGenerator(AbstractGenerator):
    def __init__(self, template_type: str, root_path: str) -> None:
        super().__init__(template_type, root_path)

    def _does_state_name_exists(self, state_name):
        pass

    def add_object(self, object_name, object):
        template = self._get_template("object")
        parsed_template = template.render(
            attributes=object.get("attributes", []) or [],
            functions=object.get("functions", []) or [],
            object_name=object_name,
            snake_object_name=from_camel_to_snake(object_name),
            root_path=self.root_path,
        )
        file_path = "{model_dir}/{object_name}.{extension}".format(
            model_dir=MODELS_DIR,
            extension=TEMPLATE_EXTENSION[self.template_type],
            object_name=object_name,
        )
        self._write_file(
            file_path,
            beautify_template_from_language(self.template_type, parsed_template),
        )

    def update_object(self):
        pass

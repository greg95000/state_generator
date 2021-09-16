from states_generator.abstract_generator import AbstractGenerator
from states_generator.constants import INTERFACE_DIR, TEMPLATE_EXTENSION
from states_generator.utils import beautify_template_from_language


class InterfaceGenerator(AbstractGenerator):
    def __init__(self, template_type: str, root_path: str) -> None:
        super().__init__(template_type, root_path)

    def add_interface(self, object_name: str, interface: dict) -> None:
        """Add interface file

        Args:
            object_name (str): the name of the object when we want to create the interface
            states (dict): the states used for this object
        """
        template = self._get_template("interface")

        self.interface_functions = [
            function_name for function_name in interface.get("functions", []) or []
        ]
        parsed_template = template.render(
            object_name=object_name,
            attributes=interface.get("attributes", []) or [],
            functions=interface.get("functions", []) or [],
        )
        file_path = "{interface_dir}/{object_name}Inteface.{extension}".format(
            interface_dir=INTERFACE_DIR,
            object_name=object_name,
            extension=TEMPLATE_EXTENSION[self.template_type],
        )
        self._write_file(
            file_path,
            beautify_template_from_language(self.template_type, parsed_template),
        )

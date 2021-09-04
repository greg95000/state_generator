from jinja2 import Environment, select_autoescape
from jinja2.environment import Template
from jinja2.loaders import FileSystemLoader
from states_generator.constants import INTERFACE_DIR, STATES_DIR

TEMPLATE_EXTENSION = {
    "python": "py",
    "javascript": "js",
    "typescript": "ts",
    "golang": "go",
    "C": "c",
    "java": "java",
}


class StateGenerator:
    def __init__(self, template_type: str, root_path: str) -> None:
        self.env = Environment(
            autoescape=select_autoescape(),
            loader=FileSystemLoader("templates/{}".format(template_type)),
        )
        self.template_type = template_type
        self.root_path = root_path

    def _get_template(self, object_name: str) -> Template:
        if self.template_type not in TEMPLATE_EXTENSION:
            raise Exception(
                "Extension does not exists, the available extensions are {}".format(
                    [extension_type[0] for extension_type in TEMPLATE_EXTENSION.items()]
                )
            )
        return self.env.get_template(
            "{object_name}_template.{template_extension}".format(
                object_name=object_name,
                template_extension=TEMPLATE_EXTENSION.get(self.template_type),
            )
        )

    def add_interface(self, object_name: str, states: dict) -> None:
        """[summary]

        Args:
            states (dict): [description]
        """
        interface = states.get("interface", {}) or {}
        template = self._get_template("interface")

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
        with open(file_path, "w") as f:
            f.write(parsed_template)

    def add_state(self, states: dict) -> None:
        pass

    def update_state(self, states: dict) -> None:
        pass

    def reverse_read_file(self, path: str) -> None:
        pass

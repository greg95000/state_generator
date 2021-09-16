from jinja2.environment import Template
from jinja2 import Environment, select_autoescape
from jinja2.loaders import FileSystemLoader


TEMPLATE_EXTENSION = {
    "python": "py",
    "javascript": "js",
    "typescript": "ts",
    "golang": "go",
    "C": "c",
    "java": "java",
}


class ExtensionNotFound(Exception):
    pass


class StateNotFound(Exception):
    pass


class AbstractGenerator:
    def __init__(self, template_type: str, root_path: str) -> None:
        self.template_type = template_type
        self.root_path = root_path
        self.env = Environment(
            autoescape=select_autoescape(),
            loader=FileSystemLoader("templates/{}".format(template_type)),
        )

    def _get_template(self, object_name: str) -> Template:
        if self.template_type not in TEMPLATE_EXTENSION:
            raise ExtensionNotFound(
                "Extension does not exists, the available extensions are {}".format(
                    [extension_type[0] for extension_type in TEMPLATE_EXTENSION.items()]
                )
            )
        return self.env.get_template(
            "{object_name}_template.j2".format(
                object_name=object_name,
            )
        )

    def _write_file(self, file_path, parsed_template):
        with open(file_path, "w") as f:
            f.write(parsed_template)

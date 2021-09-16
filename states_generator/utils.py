import re
from black import format_str, FileMode


def from_camel_to_snake(camel_case):
    name = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", camel_case)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", name).lower()


def beautify_template_from_language(language, template_to_format):
    if language == "python":
        return format_str(template_to_format, mode=FileMode())

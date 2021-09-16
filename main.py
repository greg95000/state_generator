from states_generator import object_generator
import yaml
import os
import argparse

from states_generator.states_generator import StateGenerator
from states_generator.interface_generator import InterfaceGenerator
from states_generator.constants import ROOT_DIR, INTERFACE_DIR, MODELS_DIR, STATES_DIR


def get_project_name() -> str:
    return ROOT_DIR.split(os.path.sep)[-1]


parser = argparse.ArgumentParser()
parser.add_argument(
    "--language",
    required=True,
    help="The language that we will use for generating the states",
)
parser.add_argument(
    "--project_name",
    default=get_project_name(),
    help="The project name we want to use for the imports",
)
parser.add_argument(
    "--yaml_file",
    default="./states_config.yml",
    help="The yaml path for generate the states",
)
parser.add_argument("--overwrite", default=False, help="Overwrite all the files")


def create_directories() -> None:
    sub_directories = (INTERFACE_DIR, MODELS_DIR, STATES_DIR)
    if not os.path.exists("states"):
        os.mkdir("states")
    with open("./states/__init__.py", "w"):
        pass
    for sub_directory in sub_directories:
        if not os.path.exists(sub_directory):
            os.mkdir(sub_directory)
        with open(
            "./{sub_directory}/__init__.py".format(sub_directory=sub_directory), "w"
        ):
            pass


if __name__ == "__main__":
    args = parser.parse_args()
    create_directories()
    object_generator = object_generator.ObjectGenerator(
        args.language, args.project_name
    )
    # interface_generator = InterfaceGenerator(args.language, args.project_name)
    # state_generator = StateGenerator(args.language, args.project_name)
    with open(args.yaml_file) as f:
        result = yaml.load(f)
    object_generator.add_object("documentTest", result.get("objects")["documentTest"])
"""     print(result.get("objects").get("documentTest").get("interface"))
    interface_generator.add_interface(
        "documentTest",
        result.get("objects").get("documentTest").get("interface"),
    )
    state_generator.interface_functions = interface_generator.interface_functions
    state_generator.add_states(
        "documentTest",
        result.get("objects").get("documentTest").get("interface"),
        result.get("objects").get("documentTest").get("states"),
    ) """

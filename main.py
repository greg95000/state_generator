import yaml
import os
from states_generator.states_generator import StateGenerator
from states_generator.constants import ROOT_DIR, INTERFACE_DIR, MODELS_DIR, STATES_DIR


def get_project_name() -> str:
    return ROOT_DIR.split(os.path.sep)[-1]


def create_directories() -> None:
    sub_directories = (INTERFACE_DIR, MODELS_DIR, STATES_DIR)
    if not os.path.exists("states"):
        os.mkdir("states")
    for sub_directory in sub_directories:
        if not os.path.exists(sub_directory):
            os.mkdir(sub_directory)


if __name__ == "__main__":
    project_name = get_project_name()
    create_directories()
    state_generator = StateGenerator("python", project_name)
    with open("./tests/files/fixtures/success.yml") as f:
        result = yaml.load(f)
    print(result.get("objects").get("documentTest").get("states").get("interface"))
    state_generator.add_interface(
        "documentTest",
        result.get("objects").get("documentTest").get("states").get("interface"),
    )

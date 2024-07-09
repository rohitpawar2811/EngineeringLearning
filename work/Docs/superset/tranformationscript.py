from zipfile import ZipFile
import jinja2
from pathlib import Path, PurePosixPath
from typing import Any
import yaml
from datetime import datetime
from io import BytesIO


# try:
#     import jinja2
# except ModuleNotFoundError:
#     exit("Jinja2 is a required dependency for this script")


# def render_template(template_file: str, **kwargs: dict) -> str:
#     """
#     Simple render template based on named parameters

#     :param template_file: The template file location
#     :param kwargs: Named parameters to use when rendering the template
#     :return: Rendered template
#     """
#     template = jinja2.Template(template_file)
#     return template.render(**kwargs)

instance_name = "ADOC GN -"

def remove_root(file_path: str) -> str:
    """Remove the first directory of a path"""
    full_path = PurePosixPath(file_path)
    relative_path = PurePosixPath(*full_path.parts[1:])
    return str(relative_path)

def is_valid_config(file_name: str) -> bool:
    path = Path(file_name)

    # ignore system files that might've been added to the bundle
    if path.name.startswith(".") or path.name.startswith("_"):
        return False

    # ensure extension is YAML
    if path.suffix.lower() not in {".yaml", ".yml"}:
        return False

    return True

def get_contents_from_bundle(bundle: ZipFile) -> dict[str, str]:
    return {
        remove_root(file_name): bundle.read(file_name).decode()
        for file_name in bundle.namelist()
        if is_valid_config(file_name)
    }


import uuid
def replace_variables_in_yaml(zip_file_path: str):
    with ZipFile(zip_file_path) as bundle:
        contents = get_contents_from_bundle(bundle)
        configs = load_configs(contents)
        old_to_new_uuid = {}
        
        for file_name, content in configs.items():
            if file_name.startswith("databases/"):
                random_uuid = generate_uuid()
                old_to_new_uuid[content["uuid"]] = random_uuid

                content["database_name"] = update_instance_name(content["database_name"])
                content["uuid"] = random_uuid
                
        for file_name, content in configs.items():
            if file_name.startswith("datasets/"):
                random_uuid = generate_uuid()
                old_to_new_uuid[content["uuid"]] = random_uuid
                content["uuid"] = random_uuid

                content["table_name"] = update_instance_name(content["table_name"])
                content["database_uuid"] = old_to_new_uuid.get(content["database_uuid"], generate_uuid())
       
        for file_name, content in configs.items():
            if file_name.startswith("charts/"):
                random_uuid = generate_uuid()
                old_to_new_uuid[content["uuid"]] = random_uuid
                content["uuid"] = random_uuid
                
                content["slice_name"] = update_instance_name(content["slice_name"])
                content["dataset_uuid"] = old_to_new_uuid.get(content["dataset_uuid"], generate_uuid())
                

        for file_name, content in configs.items():
            if file_name.startswith("dashboards/"):
                content["uuid"] = generate_uuid()
                content["dashboard_title"] = update_instance_name(content["dashboard_title"])
                position = content["position"]
                for child in position.values():
                    if (
                        isinstance(child, dict)
                        and child["type"] == "CHART"
                        and "uuid" in child["meta"]
                    ):
                        child["meta"]["uuid"] = old_to_new_uuid.get(child["meta"]["uuid"], generate_uuid())
                        child["meta"]["sliceName"] = update_instance_name(child["meta"]["sliceName"])
        
        yamlContent = {}
        for file_name, content in configs.items():
            yamlContent[file_name] = yaml.safe_dump(content, sort_keys=False)

        timestamp = datetime.now().strftime("%Y%m%dT%H%M%S")
        root = f"assets_export_{timestamp}"
        filename = f"{root}.zip"

        buf = BytesIO()
        with ZipFile(buf, "w") as bundle:
            for file_name, file_content in yamlContent.items():
                with bundle.open(f"{root}/{file_name}", "w") as fp:
                    fp.write(file_content.encode())
        buf.seek(0)

        # Save the content of the ZIP archive to a local file
        with open(filename, "wb") as zip_file:
            zip_file.write(buf.read())

        print("ZIP file saved successfully:", filename)

        print(configs);



def generate_uuid() -> str:
    return str(uuid.uuid4())

def update_instance_name(file_name) -> str:
    first_hyphen_index = file_name.find("-")
    if first_hyphen_index != -1:
        replaced_string = file_name[first_hyphen_index + 1:]
    else:
        replaced_string = file_name
    return instance_name + replaced_string.strip()
    
             

def load_yaml(file_name: str, content: str) -> dict[str, Any]:
    """Try to load a YAML file"""
    try:
        return yaml.safe_load(content)
    except yaml.parser.ParserError as ex:
        logger.exception("Invalid YAML in %s", file_name)
        raise ValidationError({file_name: "Not a valid YAML file"}) from ex


# pylint: disable=too-many-locals,too-many-arguments
def load_configs(
    contents: dict[str, str]
) -> dict[str, Any]:
    configs: dict[str, Any] = {}

    for file_name, content in contents.items():
        # skip directories
        if not content:
            continue

        prefix = file_name.split("/")[0]

        try:
            config = load_yaml(file_name, content)
            configs[file_name] = config
        except ValidationError as exc:
            exc.messages = {file_name: exc.messages}
            exceptions.append(exc)

    return configs


def find_chart_uuids(position: dict[str, Any]) -> set[str]:
    return set(build_uuid_to_id_map(position))

def build_uuid_to_id_map(position: dict[str, Any]) -> dict[str, int]:
    return {
        child["meta"]["uuid"]: child["meta"]["chartId"]
        for child in position.values()
        if (
            isinstance(child, dict)
            and child["type"] == "CHART"
            and "uuid" in child["meta"]
        )
    }


# Example usage:
zip_file_path = "/home/rohit/Downloads/dashboard_export_20240318T063627.zip"
replace_variables_in_yaml(zip_file_path)

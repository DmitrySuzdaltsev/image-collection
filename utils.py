import yaml
from dot_dict import DotDict


def get_config(pathname):
    with open(pathname) as f:
        yaml_config = yaml.safe_load(f)
    return DotDict(yaml_config)

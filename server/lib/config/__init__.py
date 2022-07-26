from .config_utils import get_from_default, get_from_env, get_from_cli
import json


class Config:
    def __init__(self, args, env):
        self.args = args
        self.env = env

        config_file_path = args.get('config') or env.get('test_app_config')

        default_config = get_from_default()
        env_config = get_from_env(env)
        cli_config = get_from_cli(args)

        all = {**default_config, **env_config, **cli_config}

        for key in all:
            value = all[key]
            if type(value) == str:
                if value.strip().lower() == 'true':
                    all[key] = True
                elif value.strip().lower() == 'false':
                    all[key] = False

        self.config_file_path = config_file_path
        self.env_config = env_config
        self.cli_config = cli_config
        self.all = all

    def get(self, key=None):
        rest = {
            k:v for k,v in self.all.items() if k != 'connections'
        }

        if not key:
            return rest

        if not self.all.get(key):
            raise Exception(f"config item '{key}' not defined in config_items.js")

        return self.all[key]

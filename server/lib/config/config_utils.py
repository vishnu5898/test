from .config_items import config_items as definitions
from functools import reduce


def get_from_default():
    default_map = {}
    for doc in definitions:
        default_map[doc['key']] = doc['default']
    return default_map


def get_from_env(env):
    def func1(doc):
        if doc.get('env_var'):
            return True
        return False

    def func2(env_map, doc):
        if env.get(doc['env_var']):
            env_map[doc['key']] = env[doc['env_var']]
        return env_map

    filtered = filter(func1, definitions)
    reduced = reduce(func2, filtered, {})
    return reduced


def get_from_cli(args):
    def func1(conf_map, doc):
        key = doc['key']
        if args.get(key):
            conf_map[key] = args[key]
        return conf_map
    reduced = reduce(func1, definitions, {})
    return reduced
from email.policy import default
from server.lib.config import Config
import click
import os
from dotenv import load_dotenv


load_dotenv('config.env')


@click.command()
@click.option('--log_level')
@click.option('--test_app_config')
def cli_parser(**kwargs):
    return kwargs

args = cli_parser(standalone_mode=False)
env = os.environ
config = Config(args, env)
print(config.get())
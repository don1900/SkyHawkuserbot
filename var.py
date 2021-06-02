import os

ENV = bool(os.environ.get("ENV", False))
if ENV:
    from heroku_config import Var as ExampleConfig
else:
    from config.py import Development as ExampleConfig


Var = ExampleConfig

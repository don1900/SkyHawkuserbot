import os

ENV = bool(os.environ.get("ENV", False))

if ENV:
    from sample_config import Var as Config
else:
    if os.path.exists("config.py"):
        from local_config import Development as Config
        
        
Var = Config

import os


class Configuration:
    ENV = os.getenv("env")

    @classmethod
    def get_config(cls):
        from config.environments import DEV
        from config.environments import QA
        from config.environments import STAGE
        from config.environments import PROD

        config_by_env = {
            "qa": QA,
            "dev": DEV,
            "stage": STAGE,
            "prod": PROD
        }

        return config_by_env[cls.ENV]()

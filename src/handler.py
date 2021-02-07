from src.config import config


def foo(event, context):
    print(f"Yup, config works: {config.other_settings.foo}")


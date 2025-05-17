from __future__ import annotations

from ckanext.selftools import utils, config


def selftools_categories():
    return utils.get_selftools_categories()


def selftools_get_db_model_options():
    models = utils.get_db_models()
    return [{"value": i["label"], "text": i["label"]} for i in models]


def selftools_get_db_row_values(row, columns):
    values = []
    whitelist_fields = ["password", "apikey"]
    for col in columns:
        if col in whitelist_fields:
            value = "SECURE"
        else:
            value = getattr(row, col, None)

        if value is not None:
            values.append(value)
        else:
            values.append("")

    return values


def get_operations_limit():
    return config.selftools_get_operations_limit()


def check_operations_pwd_set():
    return True if config.selftools_get_operations_pwd() else False

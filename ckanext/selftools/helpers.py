from __future__ import annotations

import ckan.plugins.toolkit as tk

import ckanext.selftools.utils as utils


def selftools_tools():
    return utils.SELFTOOLS_TOOLS


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

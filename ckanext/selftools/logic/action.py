from __future__ import annotations

import requests
import logging

import ckan.model as model
import ckan.plugins.toolkit as tk
from ckan.lib.search.common import (
    is_available as solr_available,
    make_connection as solr_connection,
)
from ckan.lib.search import clear, rebuild

import ckanext.selftools.utils as utils

log = logging.getLogger(__name__)


def selftools_solr_query(context, data_dict):
    tk.check_access("sysadmin", context, data_dict)

    if solr_available():
        solr = solr_connection()
        solr_url = solr.url

        q_response = requests.get(
            solr_url.rstrip("/") + "/query?" + data_dict.get("q", "q=*:*")
        )
        q_response.raise_for_status()

        query = q_response.json()

        return query
    return False


def selftools_solr_delete(context, data_dict):
    tk.check_access("sysadmin", context, data_dict)
    pkg = model.Package.get(data_dict.get("id"))
    if not pkg:
        return {"success": False}

    clear(pkg.id)
    return {"success": True}


def selftools_solr_index(context, data_dict):
    tk.check_access("sysadmin", context, data_dict)
    pkg = model.Package.get(data_dict.get("id"))
    if not pkg:
        return {"success": False}
    try:
        rebuild(
            package_id=pkg.id,
            force=tk.asbool(data_dict.get("force", "False")),
        )
    except Exception:
        return {"success": False, "message": "An Error appeared while indexing."}
    return {"success": True}


def selftools_db_query(context, data_dict):
    tk.check_access("sysadmin", context, data_dict)

    q_model = data_dict.get("model")
    limit = data_dict.get("limit")
    field = data_dict.get("field")
    value = data_dict.get("value")
    if q_model:
        models = utils.get_db_models()
        curr_model = [m for m in models if m["label"] == q_model]

        if curr_model:
            try:
                model_class = curr_model[0]["model"]
                q = model.Session.query(model_class)

                if field and value:
                    q = q.filter(getattr(model_class, field) == value)

                if limit:
                    q = q.limit(int(limit))

                return {
                    "success": True,
                    "results": q.all(),
                    "fields": [col.name for col in model_class.__table__.columns],
                }
            except AttributeError:
                return {
                    "success": False,
                    "message": f"There no attribute '{field}' in '{curr_model[0]['label']}'",
                }

    return False


def selftools_db_update(context, data_dict):
    tk.check_access("sysadmin", context, data_dict)

    q_model = data_dict.get("model")
    limit = data_dict.get("limit")
    field = data_dict.get("field")
    value = data_dict.get("value")
    where_field = data_dict.get("where_field")
    where_value = data_dict.get("where_value")
    if q_model:
        models = utils.get_db_models()
        curr_model = [m for m in models if m["label"] == q_model]

        if curr_model:
            try:
                model_class = curr_model[0]["model"]

                primary_key = None
                mapper = model_class.__mapper__
                pk_prop = list(mapper.iterate_properties)
                for prop in pk_prop:
                    if hasattr(prop, "columns") and prop.columns[0].primary_key:
                        primary_key = getattr(model_class, prop.key)
                if not primary_key:
                    return {
                        "success": False,
                        "message": "Cannot extract Primary key for the Model.",
                    }

                # First filter and limit results
                q = model.Session.query(primary_key)

                if field and value:
                    q = q.filter(getattr(model_class, where_field) == where_value)

                if limit:
                    q = q.limit(int(limit))

                if where_field and where_value:
                    ids = [i[0] for i in q.all()]
                    # Update already limited results
                    upd = (
                        model.Session.query(model_class)
                        .filter(primary_key.in_(ids))
                        .update({field: value})
                    )

                    model.Session.commit()

                    return {"success": True, "updated": upd, "effected": ids}
                else:
                    return {"success": False, "message": "Provide the WHERE condition"}
            except AttributeError:
                return {
                    "success": False,
                    "message": f"There no attribute '{field}' in '{curr_model[0]['label']}'",
                }

    return {"success": False}

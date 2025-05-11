from __future__ import annotations

import ckan.plugins.toolkit as tk

import pprint
import json
from typing import Any, cast
from flask import Blueprint

import ckan.lib.navl.dictization_functions as dict_fns
import ckan.logic as logic
from ckan import types
import ckan.model as model
import ckan.plugins.toolkit as tk
from ckan.common import _, request


selftools_htmx = Blueprint("selftools_htmx", __name__)


@selftools_htmx.route("/selftools/solr-query", methods=["POST"])
def selftools_solr_query():
    try:
        context: types.Context = cast(
            types.Context,
            {
                "model": model,
                "user": tk.current_user.name,
                "auth_user_obj": tk.current_user,
            },
        )

        tk.check_access("sysadmin", context)
    except tk.NotAuthorized:
        tk.abort(404)

    try:
        data_dict = logic.clean_dict(
            dict_fns.unflatten(logic.tuplize_dict(logic.parse_params(request.form)))
        )
    except dict_fns.DataError:
        return tk.base.abort(400, _("Integrity Error"))

    resp = tk.get_action("selftools_solr_query")(context, data_dict)

    pretty_json = json.dumps(resp, indent=2)

    return tk.render(
        "/selftools/snippets/pretty_json.html", extra_vars={"json": pretty_json}
    )


@selftools_htmx.route("/selftools/solr-delete", methods=["POST"])
def selftools_solr_delete():
    try:
        context: types.Context = cast(
            types.Context,
            {
                "model": model,
                "user": tk.current_user.name,
                "auth_user_obj": tk.current_user,
            },
        )

        tk.check_access("sysadmin", context)
    except tk.NotAuthorized:
        tk.abort(404)

    try:
        data_dict = logic.clean_dict(
            dict_fns.unflatten(logic.tuplize_dict(logic.parse_params(request.form)))
        )
    except dict_fns.DataError:
        return tk.base.abort(400, _("Integrity Error"))

    resp = tk.get_action("selftools_solr_delete")(context, data_dict)

    if not resp.get("success"):
        return _("Couldn't delete index. No such Dataset.")
    else:
        return _("Deleted.")


@selftools_htmx.route("/selftools/solr-index", methods=["POST"])
def selftools_solr_index():
    try:
        context: types.Context = cast(
            types.Context,
            {
                "model": model,
                "user": tk.current_user.name,
                "auth_user_obj": tk.current_user,
            },
        )

        tk.check_access("sysadmin", context)
    except tk.NotAuthorized:
        tk.abort(404)

    try:
        data_dict = logic.clean_dict(
            dict_fns.unflatten(logic.tuplize_dict(logic.parse_params(request.form)))
        )
    except dict_fns.DataError:
        return tk.base.abort(400, _("Integrity Error"))

    resp = tk.get_action("selftools_solr_index")(context, data_dict)

    if not resp.get("success"):
        return (
            resp["message"]
            if resp.get("message")
            else _("Couldn't index dataset. No such Dataset.")
        )
    else:
        return _("Indexed.")


@selftools_htmx.route("/selftools/db-query", methods=["POST"])
def selftools_db_query():
    try:
        context: types.Context = cast(
            types.Context,
            {
                "model": model,
                "user": tk.current_user.name,
                "auth_user_obj": tk.current_user,
            },
        )

        tk.check_access("sysadmin", context)
    except tk.NotAuthorized:
        tk.abort(404)

    try:
        data_dict = logic.clean_dict(
            dict_fns.unflatten(logic.tuplize_dict(logic.parse_params(request.form)))
        )
    except dict_fns.DataError:
        return tk.base.abort(400, _("Integrity Error"))

    resp = tk.get_action("selftools_db_query")(context, data_dict)

    if not resp.get("success"):
        return resp["message"] if resp.get("message") else _("Something went wrong...")
    else:
        return tk.render(
            "/selftools/snippets/db_results.html", extra_vars={"data": resp}
        )


@selftools_htmx.route("/selftools/db-update", methods=["POST"])
def selftools_db_update():
    try:
        context: types.Context = cast(
            types.Context,
            {
                "model": model,
                "user": tk.current_user.name,
                "auth_user_obj": tk.current_user,
            },
        )

        tk.check_access("sysadmin", context)
    except tk.NotAuthorized:
        tk.abort(404)

    try:
        data_dict = logic.clean_dict(
            dict_fns.unflatten(logic.tuplize_dict(logic.parse_params(request.form)))
        )
    except dict_fns.DataError:
        return tk.base.abort(400, _("Integrity Error"))

    resp = tk.get_action("selftools_db_update")(context, data_dict)

    if not resp.get("success"):
        return resp["message"] if resp.get("message") else _("Something went wrong...")
    else:
        if resp.get("effected"):
            resp["effected"] = pprint.pformat(resp["effected"])
        return tk.render(
            "/selftools/snippets/db_effected.html", extra_vars={"data": resp}
        )

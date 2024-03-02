from __future__ import annotations

from typing import Any, cast
from flask import Blueprint
from flask.views import MethodView

from ckan import types
import ckan.model as model
import ckan.plugins.toolkit as tk
from ckan.logic import parse_params


selfinfo = Blueprint("selfinfo", __name__, url_prefix="/ckan-admin")


class SelfinfoView(MethodView):
    def get(self):
        context: types.Context = cast(types.Context, {
            "model": model,
            "user": tk.current_user.name,
            "auth_user_obj": tk.current_user
        })
        tk.check_access(u'sysadmin', context)
        
        data: dict[str, Any] = tk.get_action("get_selfinfo")({}, {})
        status_show: dict[str, Any] = tk.get_action("status_show")({}, {})

        return tk.render("selfinfo/index.html", {
            "data": data,
            "status_show": status_show,
            }
        )
    
    def post(self):
        form_data = parse_params(tk.request.form)

        tk.get_action("update_all_modules_check")({"ignore_auth": True}, {
            "force-reset": tk.asbool(form_data.get('force-reset', False)),
            })
        
        return tk.redirect_to("selfinfo.index")


selfinfo.add_url_rule(
    "/selfinfo",
    view_func=SelfinfoView.as_view("index"),
)

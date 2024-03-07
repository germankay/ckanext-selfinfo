from __future__ import annotations

from typing import Any
import pytest
import platform

from ckan import model
import ckan.plugins.toolkit as tk
from ckan.tests.helpers import call_action
import ckan.tests.factories as factories

@pytest.mark.ckan_config("ckan.plugins", "selfinfo")
@pytest.mark.usefixtures("with_plugins", "clean_db")
class TestGET:
    def test_get_selfinfo(self):
        user = factories.User()
        sysadmin = factories.Sysadmin()
        context: dict[str, Any] = {
            "model": model,
            "user": user["name"],
            "ignore_auth": False,
        }

        with pytest.raises(tk.NotAuthorized):
            call_action("get_selfinfo", context=context)

        context["user"] = sysadmin['name']
        
        selfinfo: dict[str, Any] = tk.get_action("get_selfinfo")(context, {})
        
        assert type(selfinfo) == dict
        
        assert len(selfinfo.keys()) == 3
        
        assert selfinfo["platform_info"]["python_version"] == platform.python_version()

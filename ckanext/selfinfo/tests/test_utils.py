from __future__ import annotations

from typing import Any

from ckanext.selfinfo import utils as utils


class TestUTILS:
    def test_get_python_modules_info(self):
        python_moduls_info: dict[str, Any] = utils.get_python_modules_info()

        assert isinstance(python_moduls_info, dict)

        assert len(python_moduls_info.keys()) == 3, python_moduls_info.keys()

    def test_get_lib_data(self):
        lib_data: dict[str, Any] | None = utils.get_lib_data("ckan")

        assert isinstance(lib_data, dict)

        assert lib_data["info"]["name"] == "ckan"

    def test_get_lib_latest_version(self):
        lib_data_latest_version: str | None = utils.get_lib_latest_version(
            "ckan"
        )

        assert isinstance(lib_data_latest_version, str)

    def test_get_ram_usage(self):
        ram_usage: dict[str, Any] = utils.get_ram_usage()

        assert isinstance(ram_usage, dict)

        assert len(ram_usage.keys()) >= 2, ram_usage.keys()

    def test_get_platform_info(self):
        platform_info: dict[str, Any] = utils.get_platform_info()

        assert isinstance(platform_info, dict)

        assert len(platform_info.keys()) >= 2, platform_info.keys()

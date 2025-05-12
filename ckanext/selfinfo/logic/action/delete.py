from __future__ import annotations

import logging
from typing import Any

from ckanext.selfinfo import utils

from ckan import types

log = logging.getLogger(__name__)


def selfinfo_delete_profile(context: types.Context, data_dict: dict[str, Any]) -> bool:
    return utils.selfinfo_delete_redis_key(data_dict.get("profile", ""))

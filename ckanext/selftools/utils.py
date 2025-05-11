from __future__ import annotations

import logging

import ckan.model as model

log = logging.getLogger(__name__)

SELFTOOLS_TOOLS = [
    {
        "key": "solr",
        "label": "Solr",
        "tools": [
            {
                "key": "solr_query",
                "label": "Query",
                "snippet": "/selftools/tools/solr/solr_query.html",
            },
            {
                "key": "solr_index",
                "label": "Index",
                "snippet": "/selftools/tools/solr/solr_index.html",
            },
            {
                "key": "solr_delete",
                "label": "Delete",
                "snippet": "/selftools/tools/solr/solr_delete.html",
            },
        ],
    },
    {
        "key": "db",
        "label": "DB",
        "tools": [
            {
                "key": "db_query",
                "label": "Query",
                "snippet": "/selftools/tools/db/db_query.html",
            },
            {
                "key": "db_update",
                "label": "Update",
                "snippet": "/selftools/tools/db/db_update.html",
            },
        ],
    },
]


def get_db_models():
    try:
        models = [
            model.Package,
            model.PackageExtra,
            model.Resource,
            model.ResourceView,
            model.User,
            model.Group,
            model.Member,
            model.PackageMember,
            model.Vocabulary,
        ]
        return [{"label": model.__name__, "model": model} for model in models]
    except Exception:
        log.error("Cannot retrieve DB Models.")

    return []

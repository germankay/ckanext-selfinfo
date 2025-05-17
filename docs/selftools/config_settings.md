**`ckan.selftools.opetations_pwd`** - (Recommended) Provides an additional security layer for operations like update/delete/create for the Categoires.

**`ckan.selftools.operations_limit`** - Sets an limit to most of the operations like query/update. By default the limit is set to `100`.

**`ckan.selftools.categories`** - You can specify the categories you want to see on Selftools, for example you can remove DB category or leave only Config category. By default if not set, Selftools will show all possbile Categories. Current list looks this `solr db redis config`.

**`ckan.selftools.tools_blacklist`** - This is needed, when you don't want to remove for example DB Category, but want to disable the Update tools for security reasons, this config params allows you do to this. Here is an example of how it will look like if you want to disable DB Update and Redis Delete tools. In CKAN config we need to provide it like this `db.db_update redis.redis_delete`.

**`ckan.selftools.config_blacklist`** - In this configuration, you can add CKAN config that you don't want to expose while doing the query as an additional security layer, for example DB conection or Tokens. By default there already an predefined list of CKAN configuations that won't be shown like `sqlalchemy.url` and more. To provide an additional list set it like this `ckan.site_url ckan.site_id` and so on.

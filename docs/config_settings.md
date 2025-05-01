**`ckan.selfinfo.redis_prefix_key`** - This configuration is needed, when you use Redis with multiple CKAN apps. In order to have a unique key per portal, this configuration can be used. Example `ckan_test` will be used as `ckan_test_errors_selinfo`.

**`ckan.selfinfo.page_url`** - (Recommended to use) Used to provide alternative URL to Selfinfo Admin Page. By default it is set to `/ckan-admin/selfinfo`.

**`ckan.selfinfo.main_action_name`** - (Recommended to use) Used to provide an alternative name for the main action of selfinfo. By default it is set to `get_selfinfo`.

**`ckan.selfinfo.partitions`** - Used for representing disk space. The value is comma separated paths. By default the value is `/`, which is usually the root.

Example: `/path/to/partition /path/to/partition2 /path/to/partition3`

**`ckan.selfinfo.errors_limit`** - Limit used to specify how much errors will be stored in Redis. By default this value is `40`.

**`ckan.selfinfo.ckan_repos_path`** - Path to the src folder where CKAN and CKAN Extensions stored at the environment. While provided, additional GIT Infromation will be granted. Make sure that there no other folders and files that are not related to CKAN are stored there. Example: `/usr/lib/ckan/default/src`

**`ckan.selfinfo.ckan_repos`** - List of CKAN Extension folders separated by space (ckanext-scheming ckanext-spatial ckanext-xloader). By default, if `ckan.selfinfo.ckan_repos_path` is provided, it will look into the directory and gather the extensions from there.

#### NOTE!
For Linux, keep in mind that the added folder in `ckan.selfinfo.ckan_repos_path` should have the same owner as the one that runs the application (e.g. if the application runs from `ckan` User in the system, then ckanext-scheming folder owner should be `ckan`), otherwise there will be an error related to ownership of the repository.

Errors for GIT now being stored below the original Table on GIT Info tab.

**`ckan.selfinfo.solr_schema_filenamet`** - (Optional) Used to specify the filename that Solr uses for CKAN schema. Mentioned in [Enable Solr Schema](configuration/solr_schema.md).

**`ckan.selfinfo.additional_profiles_using_redis_keys`** - Retrieves selfinfo data on page from external sources that store selfinfo data using `write-selfinfo` cli command under unique Redis key. The stored data should be under same Redis connection as per the "default" profile.

Example: `unique_redis_key_1 unique_redis_key_2`

**`ckan.selfinfo.categories_list`** - (Optional) List of categories that should be shown on Selfinfo Page or Returned using API. Example of usage `ckan.selfinfo.categories_list = errors ram_usage disk_usage`.
By default shows all configured categories.

**`ckan.selfinfo.duplicated_envs.mode`** - (Optional) By enabling, removes `default` profile and replaces it by duplicated Envs mentioned in [Selfinfo under Redis internal env IP key](profiles/duplicated_env.md) section. By default set to `False`.

**`ckan.selfinfo.categories_list`** - (Optional) Used in combination with ckan.selfinfo.duplicated_envs.mode to specify, which categories are going to be shared between the duplicated Envs. Mentioned in [Shared categories](profiles/shared_categories.md).

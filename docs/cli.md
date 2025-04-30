**`selfinfo write-selfinfo`** - Stores Selfinfo data under unique Redis key. This data can be retrieved by selfinfo page if `ckan.selfinfo.additional_profiles_using_redis_keys` is set with the stored keys.

Arguments:

* **key** - Unique Redis key. Example `CKAN_Additional_Selfinfo_Source`
* **label** - (Optional) Label to be displayed on selfinfo page. Example `"Additional Selfinfo Source"`. If not provided, `key` will be used as label instead.

**`selfinfo delete-selfinfo-redis-key`** - Deletes Redis key if such exists specifically created for selfinfo as it adds an prefix to the unique under the hood.

Arguments:

* **key** - Unique Redis key. Example `CKAN_Additional_Selfinfo_Source`

**`selfinfo write-selfinfo-duplicated-env`** - Stores Selfinfo information in Redis under internal IP address of the Env. In order to show them, `ckan.selfinfo.duplicated_envs.mode` should be turned on in CKAN config, this replaces `default` profile with those Profile Keys.

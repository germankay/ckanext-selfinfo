**`selfinfo write-selfinfo`** - Stores selfinfo data under unique Redis key. This data can be retrieved by selfinfo page if `ckan.selfinfo.additional_profiles_using_redis_keys` is set with the stored keys.

Arguments:

* **key** - Unique Redis key. Example `CKAN_Additional_Selfinfo_Source`
* **label** - (Optional) Label to be displayed on selfinfo page. Example `"Additional Selfinfo Source"`. If not provided, `key` will be used as label instead.

**`selfinfo delete_selfinfo_redis_key`** - Deletes Redis key if such exists specifically created for selfinfo as it adds an prefix to the unique under the hood.

Arguments:

* **key** - Unique Redis key. Example `CKAN_Additional_Selfinfo_Source`
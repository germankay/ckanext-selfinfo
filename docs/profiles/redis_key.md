## Store Selfinfo under Redis unique key

Using `ckan selfinfo write-selfinfo` cli command, you can store Selfinfo information about the CKAN APP under an unique Redis key, additionally adding label to it.

The additional evironment should use same Redis connection, as the default profile in this example.

Example of Cron job, running every 10 minutes:

    */10 * * * * /usr/lib/ckan/VIRTUAL_ENV/bin/ckan -c CONFIG_PATH selfinfo write-selfinfo UNIQUE_REDIS_KEY "CUSTOM LABEL" > /dev/null 2>&1

Then you need to add this custom key to Selnfinfo config param `ckan.selfinfo.additional_profiles_using_redis_keys`, after reload the additional profile will be displayed.

![Additional Profile using Cron](../assets/cron_redis_unique_key.png)
## Shared Caregories between Envs

While completing the steps from [previous section](duplicated_env.md), you'll be able to see new profiles per each duplicated Env.

But because each Env stores its data, the storage can be increased `x` times per each duplicated Env, this is mostly related to Errors storage or Python Packages.
Also Errors are going to be updated only after the cron job is completed (e.g. each 10 minutes for example).

We can improve this by providing `ckan.selfinfo.duplicated_envs.shared_categories`, which are categories that will be shared between all duplicated Envs on fly.

As an example I will take `errors`, as they are being stored in Redis and usually you want to have an access to them as soon as possible.

Adding `errors` to `ckan.selfinfo.duplicated_envs.shared_categories`:

* While running the `ckan selfinfo write-selfinfo-duplicated-env` cronjob, it wont save the `errors` key in the Data, which free the storage for Redis.
* While opening the Selfinfo page, it will load the Env profiles and will attach the `errors` key to them on fly from the global `errors` key instead (e.g. wont store them per Env profile).
* Those Errors will be provided in real time on each page load, no matter what Env profile you are looking at, meaning that if one of Envs encountered an Error, it will be present on all profiles.

``` py
ckan.selfinfo.duplicated_envs.shared_categories =
    errors
```


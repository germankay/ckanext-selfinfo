Make sure to re-install Selfinfo extension mentioned in [Installation](../installation.md) step.

To enable Selftools, you'll need to add `selftools` plugin to plugins list, but make sure that it is added before `selfinfo` plugin.

Recommended step is to provide an password that will be required each time you want to do an Update/Delete operations using CKAN param `ckan.selftools.opetations_pwd` and this password will be required by the Action as an additional security layer. This configuration param is by default added to Config blacklist, so won't be exposed.

You can check other CKAN config params that can be configured for Selftools and its Categories [here](config_settings.md).
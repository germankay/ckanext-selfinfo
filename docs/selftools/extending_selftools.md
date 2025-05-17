
## Extending DB Models list

To extend Selftools DB Models list, you can use CKAN hooks.

### CKAN Hooks

There is an interface `ISelftools` that has an method `selftools_db_models`, which provides you an ability to extend or modify Models list that will appear in DB Category.

Example of how it might look in your `plugin.py` file:

``` py
from ckanext.selftools.interfaces import ISelftools

class MyPlugin(plugins.SingletonPlugin):
    plugins.implements(ISelftools, inherit=True)

    def selftools_db_models(self, models_list):
        # Modifications done to models_list here

        return models_list
```

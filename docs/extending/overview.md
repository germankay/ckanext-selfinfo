Selfinfo provides a different types of information about CKAN, but sometimes you need some custom information or manipulate with existing Data that Selfinfo provides.

To extend Selfinfo, you can use CKAN hooks + template overwrite.

### CKAN Hooks

There is an interface ISelfinfo that has an method selfinfo_after_prepared, which provides you an ability to extend or modify the data before main Selfinfo action provides you.

Example of how it might look in your `plugin.py` file:

``` py
from ckanext.selfinfo.interfaces import ISelfinfo

class MyPlugin(plugins.SingletonPlugin):
    plugins.implements(ISelfinfo, inherit=True)

    def selfinfo_after_prepared(self, data):
        # Modifications done to data here

        return data
```

### Template overwrite

You can add additional Tabs navigation and Tabs content by overwriting `additional_content_tabs.html` and `additional_navigation_tabs.html` templates. Those templates were specifically created to be overwritten.

Example of how it might look for example overwriting `additional_navigation_tabs.html`:

In your templates folder that structure should be like this:

``` py
/templates
    /selfinfo
        /snippets
            /additional_navigation_tabs.html
```

Content example

``` py
<a href="#nav-custom-{{ profile }}" class="nav-link" id="nav-custom-{{ profile }}-tab" data-bs-toggle="tab" data-bs-target="#nav-custom-{{ profile }}" role="tab" aria-controls="nav-custom-{{ profile }}" aria-selected="false">Custom Tab</a>
```

Why `snippets` instead of `{% block custom_block %}`, because of variables transferring after you extend an block, which are missing variables from the original template, while in overwriting snippet you can use the provided variables like `profile` and `data`.

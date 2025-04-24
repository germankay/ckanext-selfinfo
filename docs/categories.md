## Categories

Out of the box, Selfinfo will try to load all the possible information that currently available, but you can reduce those by adding `ckan.selfinfo.categories_list`, where you provide an list of categories you want to see on the page and API endpoint.

This is really needed, when you have an instance that doesn't use UI, like CKAN Jobs worker, so for example the Blueprints are not needed, as CKAN won't provide them or Python Modules, which can be spacing consuming for big projects.

See [Config Settings](config_settings.md) for an example of this CKAN Config.

Here are the current list of categories to choose:

* python_modules
* platform_info
* ram_usage
* disk_usage
* git_info
* freeze
* errors
* actions
* auth_actions
* blueprints
* helpers
* status_show
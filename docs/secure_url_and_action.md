## Setup secure URL and Action name

Out of the box, Selfinfo page registered under `/ckan-admin/selfinfo` URL, which can is only protected by Sysadmin access check.

To add an additional layer of protection, provide an custom path that will modify the original path, so other wont know under what URL it is actually registered. This can be done by adding `ckan.selfinfo.page_url` to CKAN config, where that value is your custom URL.

Same goes for main Selfinfo endpoint that provides same information, but in API format. By default it uses `get_selfinfo` endpoint and to modify it using `ckan.selfinfo.main_action_name` CKAN config, where that value is the new action name.

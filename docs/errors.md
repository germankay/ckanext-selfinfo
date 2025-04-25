## Enable Errors Saving

![Enabled Errors storing](assets/errors.png)

In CKAN INI file, need to add and modify few lines.

After `handler_console` section add:

    [handler_selfinfoErrorHanlder]
    class = ckanext.selfinfo.handlers.SelfinfoErrorHandler
    level = ERROR
    formatter = generic

In `handlers` modify the `keys`, example:

    [handlers]
    keys = console, selfinfoErrorHanlder

In `logger_ckan` modify `handlers`, example:

    [logger_ckan]
    level = INFO
    handlers = console, selfinfoErrorHanlder
    qualname = ckan
    propagate = 0
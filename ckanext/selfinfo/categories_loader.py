from ckanext.selfinfo import utils

def get_categories():
    return {
        "python_modules": utils.get_python_modules_info,
        "platform_info": utils.get_platform_info,
        "ram_usage": utils.get_ram_usage,
        "disk_usage": utils.get_disk_usage,
        "git_info": utils.gather_git_info,
        "freeze": utils.get_freeze,
        "errors": utils.retrieve_errors,
        "actions": utils.ckan_actions,
        "auth_actions": utils.ckan_auth_actions,
        "blueprints": utils.ckan_bluprints,
        "helpers": utils.ckan_helpers,
        "status_show": utils.get_status_show,
        "ckan_queues": utils.get_ckan_queues,
        "ckan_solr_schema": utils.get_solr_schema,
    }

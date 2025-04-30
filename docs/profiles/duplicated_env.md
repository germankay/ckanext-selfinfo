## Store Selfinfo under Redis internal env IP key

Using `ckan selfinfo write-selfinfo-duplicated-env` cli command, you can store Selfinfo information about the CKAN APP under an internal Env IP Redis key.

This option is needed, when your infostructure is build using Load Balancer from AWS for example, that generates duplicated Envs to distribute incoming traffic between Envs.

By default Selfinfo stores and returns only infromation for 1 active Env that you got response from within the Client Browser or by making an request to it from another source, while having multiple duplicated Envs and opening the page, it will randomly load information from the Env that reponseded, with its current information.

In order to see all Active duplicated Envs, you can store the information of each under an unique key using their internal IP that is assigned to them.

To do so, you need to setup and cronjob for the Env image, from which new ENVs will be created that will run for example every 10 minutes and store its information under their IP address key.

Then enable `ckan.selfinfo.duplicated_envs.mode` by setting it to `true` value.

Now while opening the Selfinfo page, instead of `default` profile, there will be one or multiple profiles per each Env that is currently active.

![Duplicated Env Profile](../assets/duplicated_env.png)

Example of Cron job, running every 10 minutes:

    */10 * * * * /usr/lib/ckan/VIRTUAL_ENV/bin/ckan -c CONFIG_PATH selfinfo write-selfinfo-duplicated-env" > /dev/null 2>&1

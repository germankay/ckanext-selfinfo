## Pypi Publishing

For ``publish.yml`` to work, you need to set the following configuration in pypi.org

Once the following steps have been completed, When a version is pushed to
GitHub and project.toml verson matches the version in the tag, a new release will be created on pypi.org
if all tests pass.

### Add a new pending publisher
If you have not already got a package on pypi, you need to add a new pending publisher.
1. Go to https://pypi.org/manage/account/publishing/
2. At bottom ``Add a new pending publisher``
3. Fill in the form with the following information
   - **Name**: ``#PACKAGE NAME#`` (e.g. ``ckanext-selfinfo``)
   - **Owner**: ``#GITHUB ORG/USERNAME#`` (e.g. ``DataShades``)
   - **Repository name**: ``#Repo Name#`` (e.g. ``ckanext-selfinfo``)
   - **Workflow name**: ``publish.yml``
   - **Environment name**: ``pypi``
5. Click ``Add``


### Existing publisher
If you have already got a package on pypi, you need to add a new **Trusted** publisher.
1. Go to https://pypi.org/manage/account/publishing/
2. Find project and click ``Manage``

    It should take to you to something like https://pypi.org/manage/project/ckanext-selfinfo/settings/publishing/
3. At bottom ``Add a new publisher``
4. Fill in the form with the following information
   - **GitHub Tab**
   - **Owner**: ``#GITHUB ORG/USERNAME#`` (e.g. ``DataShades``)
   - **Repository name**: ``#Repo Name#`` (e.g. ``ckanext-selfinfo``)
   - **Workflow name**: ``publish.yml``
   - **Environment name**: ``pypi``
5. Click ``Add``


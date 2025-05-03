## Doc build and deployment

This workflow will build the documentation and conditional deploy it to GitHub Pages.

For auto deployment to work, you need to set the following configuration in GitHub.

### GitHub Pages
Ensure that 
https://github.com/#USER_OR_ORG/$RE#REPO/settings/pages

**Build and deployment** - **Source** is set to ``GitHub Actions``


Update 
https://github.com/#USER_OR_ORG/#REPO/settings/environments
``github-pages`` environment to have the branches you want to deploy from.

If this is not set, the workflow will fail with a permission error.

I add ``develop`` and ``master`` branches.

If you wish to use ``main`` then also alter docs.yml if statement
```yml
(github.ref == 'refs/heads/develop' 
        || github.ref == 'refs/heads/master' 
        || (github.event_name == 'workflow_dispatch' && github.event.inputs.push_pages == 'true') 
)
```

This if statement also allows you to trigger the workflow manually from the Actions tab.

**Note:** It is still environment locked to specific branches/tags you configured
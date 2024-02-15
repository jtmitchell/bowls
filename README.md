# bowls

A Django website to set up a lawn bowls tournament.

### Installation

Run the following commands...
   ```
   just venv
   just install
   ./manage.py createsuperuser
   ```

## Updating dependencies

We are using [pip-tools](https://pip-tools.readthedocs.io/en/latest/) to manage the dependencies.

Within a project, dependencies are specified in ``pyproject.toml``. The development packages are in the ***project.optional-dependancies*** section.

The idea is:
1. Use ``just pip-compile`` to sort out the combined production and development dependencies, as *requirements.txt*.
   1. this will use the flag ``--extra dev`` to include the development dependencies
2. It will then run a second time for just production dependencies and constrain them to the versions already found to produce *requirements.production.txt*
   1. the file *prod-requirements.in* specifies the constraint

### Updating a particular package

To upgrade one or more packages, use ``just pip-upgrade``,
i.e. dependabot recommends flask (2.3.2), so try
```
just pip-upgrade flask
```
or, to be explicit about the version
```
just pip-upgrade flask==2.3.2
```


[Refer to pip-tools documentation](https://github.com/jazzband/pip-tools#updating-requirements)

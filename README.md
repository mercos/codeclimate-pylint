[![Maintainability](https://api.codeclimate.com/v1/badges/af6595b5ba0a85c3c0a1/maintainability)](https://codeclimate.com/github/meuspedidos/codeclimate-pylint/maintainability)

# Code Climate Pylint Engine

`codeclimate-pylint` is a Code Climate engine that wraps the [Pylint](https://github.com/PyCQA/pylint) source code analyzer. You can run it on your command line using the Code Climate CLI, or on our hosted analysis platform.

### Installation

1. If you haven't already, [install the Code Climate CLI](https://github.com/codeclimate/codeclimate).
2. Enable the engine in your .codeclimate.yml file:
```
engines:
  pylint:
    enabled: true
```
3. You're ready to analyze! Browse into your project's folder and run `codeclimate analyze`.

### Configuration

You can configure which files to be analyzed in your `.codeclimate.yml` file.

Other configurations can be made through a `.pylintrc` file. More information can be found on [Pylint's documentation](https://pylint.readthedocs.io/en/latest/)

PYTHONPATH can be modified by setting the PYTHONPATH configuration variable:

```yaml
engines:
  pylint:
    enabled: true
    PYTHONPATH:
      - src
```

This adds the `src` directory to PYTHONPATH before running `pylint`. Relative paths are properly resolved to the current directory.

Plugin activation can also be made in `.codeclimate.yml`:

```
engines:
  pylint:
    enabled: true
    plugins:
      - django
```

Currently the following plugins are supported:

- [pylint-django](https://github.com/PyCQA/pylint-django)
- [pylint-celery](https://github.com/PyCQA/pylint-celery)
- [pylint-quotes](https://github.com/edaniszewski/pylint-quotes)

### Using pylint-django

According to the [latest pylint-django docs](https://github.com/PyCQA/pylint-django#usage) it's required to set Django settings module according to the project. If you have your settings module at root level you should do nothing, but if that's not the case then you need to declare your settings module in `.codeclimate.yml` as shown below.

```
engines:
  pylint:
    enabled: true
    plugins:
      - django
    django_settings_module: mymodule.settings
```

We welcome PRs adding support for other plugins.

### Need help?

For help with Pylint, [check out their documentation](https://pylint.readthedocs.io/en/latest/).

If you're running into a Code Climate issue, first check out this project's GitHub Issues, as your question may have already been covered. If not, [go ahead and open a support ticket with us](https://codeclimate.com/help).

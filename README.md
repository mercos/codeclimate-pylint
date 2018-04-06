# Code Climate Pylint Engine

`codeclimate-pylint` is a Code Climate engine that wraps the [Pylint](https://github.com/PyCQA/pylint) source code analyzer. You can run it on your command line using the Code Climate CLI, or on our hosted analysis platform.

You can configure which files to be analyzed in your `.codeclimate.yml` file. Other configurations can be made through a `.pylintrc` file. More information can be found on [Pylint's documentation](https://pylint.readthedocs.io/en/latest/)

### Installation

1. If you haven't already, [install the Code Climate CLI](https://github.com/codeclimate/codeclimate).
2. Run `codeclimate engines:enable pylint`. This command both installs the engine and enables it in your `.codeclimate.yml` file.
3. You're ready to analyze! Browse into your project's folder and run `codeclimate analyze`.

### Need help?

For help with Pylint, [check out their documentation](https://pylint.readthedocs.io/en/latest/).

If you're running into a Code Climate issue, first check out this project's GitHub Issues, as your question may have already been covered. If not, [go ahead and open a support ticket with us](https://codeclimate.com/help).

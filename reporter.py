import json

from pylint.interfaces import IReporter
from pylint.reporters import BaseReporter


class CodeClimateReporter(BaseReporter):
    __implements__ = IReporter
    name = 'codeclimate'
    extension = 'json'
    category_map = {
        'convention': ['Style'],
        'refactor': ['Complexity'],
        'warning': ['Bug Risk'],
        'error': ['Bug Risk'],
        'fatal': ['Bug Risk'],
    }
    severity_map = {
        'convention': 'info',
        'refactor': 'info',
        'warning': 'normal',
        'error': 'critical',
        'fatal': 'critical',
    }

    def handle_message(self, pylint_issue):
        codeclimate_dict = dict()
        codeclimate_dict['type'] = 'issue'
        codeclimate_dict['check_name'] = pylint_issue.symbol
        codeclimate_dict['categories'] = self.category_map[pylint_issue.category]

        message = self._parse_message(pylint_issue.msg)

        message_lines = message.splitlines()
        codeclimate_dict['description'] = message_lines[0]

        body = self._parse_message(self.linter.msgs_store.get_message_definition(pylint_issue.symbol).descr)
        for line in message_lines[1:]:
            body += "\n" + line
        codeclimate_dict['content'] = {'body': body}

        location = dict()
        location['path'] = pylint_issue.path
        location['positions'] = {
            'begin': {
                'line': pylint_issue.line,
                'column': pylint_issue.column,
            },
            'end': {
                'line': pylint_issue.line,
                'column': pylint_issue.column,
            },
        }
        codeclimate_dict['location'] = location

        codeclimate_dict['severity'] = self.severity_map[pylint_issue.category]

        codeclimate_string = json.dumps(codeclimate_dict, indent=4)
        self.writeln(codeclimate_string + "\0")

    def _parse_message(self, message):
        while '  ' in message:
            message = message.replace('  ', ' ')
        message = message.replace('"', '`')
        message = message.replace('\\', '')
        return message

    def _display(self, layout):
        pass

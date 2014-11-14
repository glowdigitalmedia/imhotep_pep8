import re

from imhotep.tools import Tool


class Pep8Linter(Tool):

    def __init__(self, *args, **kwargs):
        super(Pep8Linter, self).__init__(*args, **kwargs)
        self.linter = 'pep8'
        self.config = 'tox.ini'
        self.extension = 'py'
        self.regex = re.compile(
            r'(?P<filename>.*):(?P<line_num>\d+):\d+: (?P<message>.*)'
        )

    def format_linter_output(self, repo_dir, linter_output, linter_errors):
        """ Returns a dict of linter errors """
        for line in linter_output:
            match = self.regex.search(line)
            if match is not None:
                filename = match.group('filename')[len(repo_dir) + 1:]
                linter_errors[filename][match.group('line_num')].append(
                    match.group('message')
                )
        return linter_errors

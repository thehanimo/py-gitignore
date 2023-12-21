import re
import os


class Glob:
    def __init__(self, pattern, base_path, is_negated=False):
        self.is_negated = is_negated
        self.base_path = base_path
        self.regex = self._create_regex_from_gitignore_pattern(pattern)

    def _create_regex_from_gitignore_pattern(self, pattern):
        if pattern.startswith("!"):
            pattern = pattern[1:]

        directory_specific = pattern.endswith("/")

        pattern = re.escape(pattern)
        pattern = pattern.replace(r"\*\*", ".*")  # '**' -> '.*'
        pattern = pattern.replace(r"\*", "[^/]*")  # '*' -> '[^/]*'
        pattern = pattern.replace(r"\?", ".")  # '?' -> '.'

        if directory_specific:
            pattern += r"(.*)?"

        if not pattern.startswith(".*"):
            pattern = "^" + os.path.join(re.escape(self.base_path), pattern)

        return re.compile(pattern)

    def matches(self, path):
        normalized_path = os.path.normpath(path)
        return self.regex.match(normalized_path) is not None

import os
import re
import fnmatch

class Glob:
    """
    The Glob class represents a single glob pattern in a .gitignore file.
    It is responsible for converting the glob pattern into a regular expression
    and matching file paths against this regular expression.
    """

    def __init__(self, pattern, base_path, is_negated=False):
        self.is_negated = is_negated
        self.base_path = base_path
        self.regex = self._create_regex_from_gitignore_pattern(pattern)

    def _create_regex_from_gitignore_pattern(self, pattern):
        # Handle negated patterns
        if pattern.startswith('!'):
            pattern = pattern[1:]

        # Handle directory specific patterns
        directory_specific = pattern.endswith('/')
        if directory_specific:
            pattern = pattern[:-1]

        # Escape special regex characters
        pattern = re.escape(pattern)

        # Replace gitignore wildcards with regex equivalents
        pattern = pattern.replace(r'\*\*', '.*')  # '**' -> '.*'
        pattern = pattern.replace(r'\*', '[^/]*')  # '*' -> '[^/]*'
        pattern = pattern.replace(r'\?', '.')      # '?' -> '.'

        # Adjust directory specific patterns
        if directory_specific:
            pattern += r'(/.*)?'

        # Convert pattern to match from the base directory
        if not pattern.startswith('.*'):
            pattern = '^' + os.path.join(re.escape(self.base_path), pattern)

        return re.compile(pattern)

    def matches(self, path):
        normalized_path = os.path.normpath(path)
        return self.regex.match(normalized_path) is not None
    
class Gitignore:
    """
    The Gitignore class represents a .gitignore file.
    It is responsible for reading the .gitignore file and creating Glob objects for each non-comment line.
    """

    def __init__(self, file_path):
        self.path = file_path
        self.globs = []
        self._load_globs()

    def _load_globs(self):
        if os.path.exists(self.path) and os.access(self.path, os.R_OK):
            with open(self.path, 'r') as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        is_negated = line.startswith('!')
                        if is_negated:
                            line = line[1:]
                        self.globs.append(Glob(line, os.path.dirname(self.path), is_negated))
        else:
            raise FileNotFoundError(f"The file {self.path} does not exist or is not readable.")

class GitignoreBuilder:
    """
    The GitignoreBuilder class is responsible for creating a GitignoreMatcher object.
    It allows adding multiple .gitignore files which will all be used when matching file paths.
    """

    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.gitignores = []

    def add(self, path_to_gitignore):
        self.gitignores.append(Gitignore(path_to_gitignore))

    def build(self):
        return GitignoreMatcher(self.gitignores)


class GitignoreMatcher:
    """
    The GitignoreMatcher class is responsible for matching file paths against all added .gitignore files.
    It uses the Glob objects created by the Gitignore objects to match file paths.
    """

    def __init__(self, gitignores):
        self.gitignores = gitignores

    def match(self, path_to_file):
        normalized_path = os.path.normpath(path_to_file)
        for gitignore in self.gitignores:
            for glob in gitignore.globs:
                print(f"Testing glob: {glob.regex.pattern}, path: {normalized_path}")
                if glob.matches(normalized_path):
                    return not glob.is_negated
        return False

    def match_all(self, multiple_paths):
        return [self.match(path) for path in multiple_paths]


# Example usage
if __name__ == "__main__":
    root_directory = os.getcwd()
    path_to_gitignore_file = os.path.join(root_directory, ".gitTest")
    builder = GitignoreBuilder(root_directory)
    builder.add(path_to_gitignore_file)
    # Add more .gitignore files if necessary

    matcher = builder.build()

    # Test with a single file
    path_to_file = os.path.join(root_directory, "README.MD")
    print(matcher.match(path_to_file))

    path_to_file = os.path.join(root_directory, "Gitignore_Matcher/Gitignore.py")
    print(matcher.match(path_to_file))
    print(path_to_file)

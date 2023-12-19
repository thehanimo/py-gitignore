import os

class GitignoreMatcher:
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
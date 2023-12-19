from .gitignore import Gitignore
from .gitignoreMatcher import GitignoreMatcher

class GitignoreBuilder:
    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.gitignores = []

    def add(self, path_to_gitignore):
        self.gitignores.append(Gitignore(path_to_gitignore))

    def build(self):
        return GitignoreMatcher(self.gitignores)
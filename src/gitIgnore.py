import os
from .glob import Glob


class Gitignore:
    def __init__(self, file_path):
        self.path = file_path
        self.globs = []
        self._load_globs()

    def _load_globs(self):
        if os.path.exists(self.path) and os.access(self.path, os.R_OK):
            with open(self.path, "r") as file:
                for line in file:
                    line = line.strip()
                    if line and not line.startswith("#"):
                        is_negated = line.startswith("!")
                        if is_negated:
                            line = line[1:]
                        self.globs.append(
                            Glob(line, os.path.dirname(self.path), is_negated)
                        )
        else:
            raise FileNotFoundError(
                f"The file {self.path} does not exist or is not readable."
            )
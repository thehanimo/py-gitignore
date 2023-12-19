import os
import re

from .glob import Glob
from .gitignoreMatcher import GitignoreMatcher
from .gitignoreBuilder import GitignoreBuilder
from .gitignore import Gitignore


if __name__ == "__main__":
    root_directory = os.getcwd()
    path_to_gitignore_file = os.path.join(root_directory, ".gitTest")
    builder = GitignoreBuilder(root_directory)
    builder.add(path_to_gitignore_file)

    matcher = builder.build()

    path_to_file = os.path.join(root_directory, "README.MD")
    print(matcher.match(path_to_file))

    path_to_file = os.path.join(root_directory, "Gitignore_Matcher/Gitignore.py")
    print(matcher.match(path_to_file))
    print(path_to_file)

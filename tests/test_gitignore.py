import unittest
import os
from src.gitIgnore import GitignoreMatcher, GitignoreBuilder  # Replace with your actual module name

class TestGitignoreMatcher(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Assuming the .gitignore file is in the root directory of your project
        root_directory = os.path.dirname(os.path.abspath(__file__))  # Adjust this as needed
        gitignore_file_path = os.path.join(root_directory, '.gitignoreTest')  # Path to your .gitignore file

        # Initialize the GitignoreMatcher with the .gitignore file
        cls.matcher = cls.create_gitignore_matcher(gitignore_file_path, os.getcwd())

    @classmethod
    def create_gitignore_matcher(cls, file_path, root_dir):
        builder = GitignoreBuilder(os.getcwd())
        builder.add(file_path)
        return builder.build()

    def assertGitignoreMatch(self, path, expected):
        full_path = os.path.join(os.getcwd(), path)  # Adjust 'ROOT' if needed
        result = self.matcher.match(full_path)
        print(f"Testing path: {full_path}, Expected: {expected}, Actual: {result}")
        self.assertEqual(result, expected)

    def test_files_in_root(self):
        # Example test for files in root with debugging
        self.assertGitignoreMatch("README.MD", True)
        self.assertGitignoreMatch("file_root_01", False)
    
    def test_files_in_subdirectories(self):
        self.assertGitignoreMatch("src/gitIgnore.py", False)
        self.assertGitignoreMatch("tests/.gitignoreTest", True)

    def test_directories(self):
        self.assertGitignoreMatch("src", False)
        self.assertGitignoreMatch("tests", False)

    def test_negated_patterns(self):
        self.assertGitignoreMatch("src/.venv", True)
        self.assertGitignoreMatch("src/venv", True)

if __name__ == "__main__":
    unittest.main()


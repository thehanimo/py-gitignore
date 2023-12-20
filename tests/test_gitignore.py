import unittest
import os
from src import GitignoreBuilder

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
        full_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)  # Adjust 'ROOT' if needed
        result = self.matcher.match(full_path)
        print(f"Testing path: {full_path}, Expected: {expected}, Actual: {result}")
        self.assertEqual(result, expected)
        

    def test_files_in_root(self):
        self.assertGitignoreMatch("README.MD", True)
        self.assertGitignoreMatch("file_root_00", True)
        self.assertGitignoreMatch("file_root_01", False)
        self.assertGitignoreMatch("file_root_02", False)
        self.assertGitignoreMatch("file_root_02/file_leaf", True)
        self.assertGitignoreMatch("file_root_03", False)
        self.assertGitignoreMatch("file_root_03/file_leaf", True)
        self.assertGitignoreMatch("file_root_03/nested_dir/file_leaf", True)

        self.assertGitignoreMatch("/file_root_10", True)
        self.assertGitignoreMatch("/file_root_11", False)
        self.assertGitignoreMatch("/file_root_12", False)
        self.assertGitignoreMatch("/file_root_12/file_leaf", True)
        self.assertGitignoreMatch("/file_root_13", False)
        self.assertGitignoreMatch("/file_root_13/file_leaf", True)
        self.assertGitignoreMatch("/file_root_13/nested_dir/file_leaf", True)

        self.assertGitignoreMatch("/file_root_20", False)
        self.assertGitignoreMatch("/file_root_21", False)
        self.assertGitignoreMatch("/file_root_22", False)
        self.assertGitignoreMatch("/file_root_22/file_leaf", False)
        self.assertGitignoreMatch("/file_root_23", False)
        self.assertGitignoreMatch("/file_root_23/file_leaf", False)
        self.assertGitignoreMatch("/file_root_23/nested_dir/file_leaf", False)

        self.assertGitignoreMatch("/file_root_30", True)
        self.assertGitignoreMatch("/file_root_31", False)
        self.assertGitignoreMatch("/file_root_32", False)
        self.assertGitignoreMatch("/file_root_32/file_leaf", True)
        self.assertGitignoreMatch("/file_root_33", False)
        self.assertGitignoreMatch("/file_root_33/file_leaf", True)
        self.assertGitignoreMatch("/file_root_33/nested_dir/file_leaf", True)

        self.assertGitignoreMatch("subdir/file_subdir_00", True)
        self.assertGitignoreMatch("subdir/file_subdir_01", False)
        self.assertGitignoreMatch("subdir/file_subdir_02", False)
        self.assertGitignoreMatch("subdir/file_subdir_02/file_leaf", True)
        self.assertGitignoreMatch("subdir/file_subdir_03", False)
        self.assertGitignoreMatch("subdir/file_subdir_03/file_leaf", True)
        self.assertGitignoreMatch("subdir/file_subdir_03/nested_dir/file_leaf", True)
    
    def test_different_file_types(self):
        # Test for a Python file
        self.assertGitignoreMatch("example.py", False)
        
        # Test for a text file
        self.assertGitignoreMatch("example.txt", False)
        
        # Test for a configuration file
        self.assertGitignoreMatch("config.ini", False)
        
    def test_edge_cases(self):
        # Test for an empty file (if applicable)
        self.assertGitignoreMatch("empty_file.txt", False)
        
        # Test for a non-existent file
        self.assertGitignoreMatch("nonexistent_file.txt", False)

        

if __name__ == "__main__":
    unittest.main()


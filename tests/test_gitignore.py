import unittest
import os
from src import GitignoreBuilder

class TestGitignore(unittest.TestCase):
    def setUp(self):
        # Create a temporary test directory structure for testing
        self.root = os.path.abspath(os.path.join(os.path.dirname(__file__), "test_dir"))
        os.makedirs(self.root, exist_ok=True)

        # Create a dummy .gitignore file for testing purposes
        gitignore_path = os.path.join(self.root, ".gitignore")
        with open(gitignore_path, "w") as f:
            f.write("file1.txt\nfile2.txt\nfolder/\n")

        # Create some test files and directories
        test_files = ["file1.txt", "file2.txt"]
        for file in test_files:
            open(os.path.join(self.root, file), "w").close()

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
        

if __name__ == "__main__":
    unittest.main()

import unittest
import os
from Gitignore_Matcher.Gitignore import read_gitignore

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

        os.makedirs(os.path.join(self.root, "folder"))

    def test_files_in_root(self):
        # Example test for files in root with debugging
        self.assertGitignoreMatch("README.MD", True)
        self.assertGitignoreMatch("file_root_01", False)

if __name__ == "__main__":
    unittest.main()

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

    def test_read_gitignore(self):
        # Test the read_gitignore function
        gitignore_paths, all_paths, matches = read_gitignore(self.root)

        # Expected values based on the test directory structure
        expected_gitignore_paths = ["file1.txt", "file2.txt", "folder/"]
        expected_all_paths = [
            os.path.join(self.root, "file1.txt"),
            os.path.join(self.root, "file2.txt"),
            os.path.join(self.root, "folder"),
        ]
        expected_matches = [
            os.path.join(self.root, "file1.txt"),
            os.path.join(self.root, "file2.txt"),
            os.path.join(self.root, "folder"),
        ]

        self.assertEqual(gitignore_paths, expected_gitignore_paths)
        self.assertEqual(all_paths, expected_all_paths)
        self.assertEqual(matches, expected_matches)

    def tearDown(self):
        # Remove the temporary test directory and files
        import shutil

        shutil.rmtree(self.root, ignore_errors=True)

if __name__ == "__main__":
    unittest.main()
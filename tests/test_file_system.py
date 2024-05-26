import unittest
from src.file_system import FileSystem

class TestFileSystem(unittest.TestCase):
    def setUp(self):
        self.fs = FileSystem()

    def test_mkdir_and_ls(self):
        self.fs.mkdir("/data")
        self.assertEqual(list(self.fs.root.children.keys()), ["data"])

    def test_cd(self):
        self.fs.mkdir("/data")
        self.fs.cd("/data")
        self.assertEqual(self.fs.current.name, "data")

    def test_touch_and_cat(self):
        self.fs.touch("/file.txt")
        self.fs.echo("/file.txt", "Hello")
        self.assertEqual(self.fs.cat("/file.txt"), "Hello")

    def test_rm(self):
        self.fs.touch("/file.txt")
        self.fs.rm("/file.txt")
        with self.assertRaises(FileNotFoundError):
            self.fs.cat("/file.txt")

    def test_mv(self):
        self.fs.touch("/file.txt")
        self.fs.mkdir("/data")
        self.fs.mv("/file.txt", "/data/file.txt")
        self.assertEqual(list(self.fs._get_node("/data").children.keys()), ["file.txt"])

    def test_cp(self):
        self.fs.touch("/file.txt")
        self.fs.echo("/file.txt", "Hello")
        self.fs.mkdir("/data")
        self.fs.cp("/file.txt", "/data/file.txt")
        self.assertEqual(self.fs.cat("/data/file.txt"), "Hello")

if __name__ == "__main__":
    unittest.main()

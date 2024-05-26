from src.node import Node

class FileSystem:
    def __init__(self):
        self.root = Node("/", "directory")
        self.current = self.root

    def _get_node(self, path):
        if path == "/":
            return self.root
        if path.startswith("/"):
            path = path[1:]
            node = self.root
        else:
            node = self.current

        parts = path.split("/")
        for part in parts:
            if part == "..":
                node = self.root if node == self.root else node.parent
            elif part and node.type == "directory" and part in node.children:
                node = node.children[part]
            else:
                raise FileNotFoundError(f"Path '{path}' not found")
        return node

    def mkdir(self, path):
        parent, name = self._get_parent_and_name(path)
        if name in parent.children:
            raise FileExistsError(f"Directory '{name}' already exists")
        parent.children[name] = Node(name, "directory", parent)
    
    def cd(self, path):
        self.current = self._get_node(path)
    
    def ls(self, path="."):
        node = self._get_node(path)
        if node.type == "file":
            print(node.name)
        else:
            for child in node.children.values():
                print(child.name)
    
    def touch(self, path):
        parent, name = self._get_parent_and_name(path)
        if name in parent.children:
            raise FileExistsError(f"File '{name}' already exists")
        parent.children[name] = Node(name, "file", parent)

    def cat(self, path):
        node = self._get_node(path)
        if node.type != "file":
            raise IsADirectoryError(f"'{path}' is a directory")
        return node.content

    def echo(self, path, text):
        parent, name = self._get_parent_and_name(path)
        if name not in parent.children or parent.children[name].type != "file":
            raise FileNotFoundError(f"File '{path}' not found")
        node = parent.children[name]
        node.content = text

    def rm(self, path):
        parent, name = self._get_parent_and_name(path)
        if name not in parent.children:
            raise FileNotFoundError(f"'{path}' not found")
        del parent.children[name]

    def mv(self, src_path, dest_path):
        src_node = self._get_node(src_path)
        dest_parent, dest_name = self._get_parent_and_name(dest_path)
        if dest_name in dest_parent.children:
            raise FileExistsError(f"'{dest_name}' already exists at destination")
        del src_node.parent.children[src_node.name]
        dest_parent.children[dest_name] = src_node
        src_node.parent = dest_parent
        src_node.name = dest_name

    def cp(self, src_path, dest_path):
        src_node = self._get_node(src_path)
        dest_parent, dest_name = self._get_parent_and_name(dest_path)
        if dest_name in dest_parent.children:
            raise FileExistsError(f"'{dest_name}' already exists at destination")
        new_node = self._copy_node(src_node, dest_parent)
        dest_parent.children[dest_name] = new_node

    def _get_parent_and_name(self, path):
        if path.startswith("/"):
            path = path[1:]
            node = self.root
        else:
            node = self.current

        parts = path.split("/")
        name = parts.pop()
        for part in parts:
            if part not in node.children or node.children[part].type != "directory":
                raise FileNotFoundError(f"Path '{path}' not found")
            node = node.children[part]
        return node, name

    def _copy_node(self, node, parent):
        new_node = Node(node.name, node.type, parent)
        if node.type == "file":
            new_node.content = node.content
        else:
            for child in node.children.values():
                new_node.children[child.name] = self._copy_node(child, new_node)
        return new_node

class Node:
    def __init__(self, name, node_type, parent=None):
        self.name = name
        self.type = node_type  # "file" or "directory"
        self.content = ""  # Only used if node_type is "file"
        self.children = {}  # Only used if node_type is "directory"
        self.parent = parent
    
    def __repr__(self):
        return f"Node(name={self.name}, type={self.type})"

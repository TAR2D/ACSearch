class TrieNode:

    def __init__(self, c=None, weight=0):
        self.c = c
        self.weight = weight
        self.children = {}
        self.isWord = False

    def has_children(self, c):
        return self.children is not None and self.children.get(c) is not None

    def get_children(self, c):
        return self.children.get(c)

    def add_children(self, node):
        self.children.update({node.c: node})

    def can_delete(self):
        return self.children == {}

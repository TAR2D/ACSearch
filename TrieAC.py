from sidhuSearchEngine.TrieNode import TrieNode

suggestions = []


def delete(word, node, index):
    # if word doesnt exist or incomplete
    if node.has_children(word[index]) is False:
        return False

    if index == (len(word) - 1):

        current = node.get_children(word[index])
        current.isWord = False
        current.weight = 0

        if current.can_delete() is True:
            node.children.pop(word[index])
            return True
    else:
        # checking if word is not prefix of other word
        canDelete = delete(word, node.get_children(word[index]), ++index)

        if canDelete:
            current = node.get_children(word[--index])
            # checking if word is dont have children or contain another word
            if len(current.children) > 1 and current.isWord:
                return False
        # remove children
        node.children.pop(word[index])
        return True

    return False


def trie_traversal(current, word, level):
    if current.isWord:
        suggestions.append(word[:level])

    data = current.children.keys()
    for c in data:
        if current.has_children(c):
            word.insert(level, c)
            trie_traversal(current.get_children(c), word, level + 1)


def trie_traversal_limit(current, word, level, limit):
    if limit > 0:
        if current.isWord:
            suggestions.append(word[:level])

        data = current.children.keys()
        for c in data:
            if current.has_children(c):
                word.insert(level, c)
                trie_traversal_limit(current.get_children(c), word, level + 1, limit - 1)


def auto_complete(current, query, feature):
    temp = current
    for c in query:
        if temp.get_children(c) is None:
            print("{0} Not Found".format(query))
            return
        else:
            temp = temp.get_children(c)

    if temp.isWord:
        print("{0} is word".format(query))

    word = []
    length = len(query)
    if feature == 1 or feature == 2:
        trie_traversal(temp, word, length)
    elif feature == 3:
        trie_traversal_limit(temp, word, length, 3)


class TrieAC:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for c in word:
            if current.has_children(c):
                current = current.get_children(c)
            else:
                newNode = TrieNode(c, 0)
                current.add_children(newNode)
                current = newNode

        current.isWord = True

    def find(self, word):
        current = self.root
        for c in word:
            if current.has_children(c):
                current = current.get_children(c)
            else:
                return None
        return current

    def insert_weight(self, word):
        node = self.find(word)
        if node is not None:
            node.weight += 1

    def delete(self, word):
        return delete(word, self.root, 0)

    def print_trie(self):
        word = []
        trie_traversal(self.root, word, 0)
        for word in suggestions:
            print(''.join(word))
        if len(suggestions) == 0:
            print("No Suggestion")

    def auto_complete(self, query, feature):
        auto_complete(self.root, query, feature)

    @staticmethod
    def get_suggestion():
        return suggestions

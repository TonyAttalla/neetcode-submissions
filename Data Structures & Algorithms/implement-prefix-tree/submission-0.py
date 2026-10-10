
class PrefixTreeNode:

    def __init__(self):
        self.children = [None] * 26
        self.is_terminal = False
class PrefixTree:

    def __init__(self):
        self.root = PrefixTreeNode()
        

    def insert(self, word: str) -> None:
        curr_node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr_node.children[index] is None:
                curr_node.children[index] = PrefixTreeNode()
            curr_node = curr_node.children[index]
        curr_node.is_terminal = True
        return


    def search(self, word: str) -> bool:
        curr_node = self.root
        for c in word:
            index = ord(c) - ord('a')
            if curr_node.children[index] is None:
                return False
            curr_node = curr_node.children[index]
        return curr_node.is_terminal

        

    def startsWith(self, prefix: str) -> bool:
        curr_node = self.root
        for c in prefix:
            index = ord(c) - ord('a')
            if curr_node.children[index] is None:
                return False
            curr_node = curr_node.children[index]
        return True

        
        
import sys
from character_counter import CharacterCounter
from typing import List


class Node:

    def __init__(self, count: int, data: str = None):
        self.count: int = count
        self.data: str = data
        self.right: Node = None
        self.left: Node = None

    def __repr__(self):
        return f'[{self.data}:{self.count}]\n\t({self.left})\n\t({self.right})'

    def __eq__(self, other):
        return self.count == other.count and self.data == other.data


class HuffmanTree:

    def __init__(self, file_name: str):
        self.file_name: str = file_name
        self.counter: CharacterCounter = CharacterCounter()

        with open(file_name) as fp:
            result: str = fp.readline()
            while result != '':
                self.counter.add_text(result)
                result = fp.readline()

        self.nodes: List[Node] = []
        for letter, count in self.counter.get_characters().items():
            self.nodes.append(Node(count, letter))

        # Sort From Lowest Count to highest count.
        self.nodes.sort(key=lambda x: x.count)

    def _process_nodes(self):
        """
        Takes a single step in the encoding process, combining the two smallest items.
        """
        left: Node = self.nodes[0]
        right: Node = self.nodes[1]

        self.nodes.remove(left)
        self.nodes.remove(right)

        new_node: Node = Node(left.count + right.count)
        new_node.left = left
        new_node.right = right
        self.nodes.append(new_node)
        self.nodes.sort(key=lambda x: x.count)

    def construct_tree(self) -> Node:
        """
        Constructs the Huffman tree.

        Return:
            The node representing the root of the huffman tree.
        """
        while len(self.nodes) > 1:
            self._process_nodes()
        self.root: Node = self.nodes[0]
        return self.nodes[0]

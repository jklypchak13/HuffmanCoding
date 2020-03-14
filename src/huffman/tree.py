import sys
from huffman.character_counter import CharacterCounter
from huffman.node import Node
from typing import List, Dict, Tuple
from bitstring import BitArray


class HuffmanTree:

    def __init__(self, file_name: str = None, bit_array: BitArray = None):
        if file_name is not None:
            self.file_name: str = file_name
            self.counter: CharacterCounter = CharacterCounter()
            self.binary_map = None
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
        elif bit_array is not None:
            self.padding = bit_array[0:8].uint
            bit_array = bit_array[8:]
            self.root = Node()
            bit_array = self.root.from_bits(bit_array)
            self.data = bit_array

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
        self.root: Node = self.nodes[0] if self.nodes else None
        if self.root:
            self.binary_map = HuffmanTree._walk_tree(self.root)
        return self.root

    @staticmethod
    def _walk_tree(node, current: BitArray = BitArray()) -> Dict[str, BitArray]:
        """
        Walk the Huffman Tree, constructing a dictiary of their associated bit arrays
        """
        if node.data is not None:
            return {node.data: current}

        else:
            left_array: BitArray = current.copy()
            left_array.append('0b0')
            right_array: BitArray = current.copy()
            right_array.append('0b1')
            result: Dict[str, BitArray] = {}
            result.update(HuffmanTree._walk_tree(node.left, left_array))
            result.update(HuffmanTree._walk_tree(node.right, right_array))
            return result

    def get_character(self, char: str) -> BitArray:
        """
        Returns the character's corresonding BitArray

        Parameters:
            char: the character to find the BitArray of

        Return:
            char's BitArray, representing the instructions to reach it in the tree.
        """
        return self.binary_map[char]

    def to_bits(self) -> BitArray:
        """
        Writes the representation of this Tree to a BitArray

        Return:
            The bit array representing this tree.
        """
        return self.root.to_bits() if self.root else None

    def get_data(self) -> BitArray:
        """
        Returns the remaining data after reading from a bitarray
        """
        return self.data[:-self.padding]

    def process_stream(self, stream) -> Tuple[str, BitArray]:
        """
        Processes the given stream for one character.

        Parameters:
            stream: the bit array to process

        Return:
            A tuple, containing the resulting character and the left over data in the stream.
        """
        current: Node = self.root
        i: int = 0
        while current.data is None:
            if(stream[i] == 0):
                current = current.left
            else:
                current = current.right
            i += 1
        return current.data, stream[i:]

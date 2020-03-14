from bitstring import BitArray


class Node:

    def __init__(self, count: int = 0, data: str = None, left=None, right=None):
        self.count: int = count
        self.data: str = data
        self.right: Node = right
        self.left: Node = left

    def __repr__(self):
        return f'[{self.data}:{self.count}]\n\t({self.left})\n\t({self.right})'

    def __eq__(self, other):
        current_equal: bool = self.count == other.count and self.data == other.data
        children_equal: bool = self.left == other.left and self.right == other.right

        return current_equal and children_equal

    def to_bits(self) -> BitArray:
        """
        Returns the Binary Representation of this Node

        Return:
            the binary representation of this node.
        """
        if self.data is None:
            return BitArray('0b1') + self.left.to_bits() + self.right.to_bits()
        else:
            return BitArray('0b0') + BitArray(bytes(self.data, encoding='utf8'))

    def from_bits(self, bits: BitArray) -> BitArray:
        """
        Overrides the current node, with the well-formed bit array

        Parameters:
            bits: the well formed bitarray representing a node in the binary tree.

        Return:
            any left over bits in the bit array after parsing bits.
        """
        if bits[0] == 0:
            self.data: str = bits[1:9].tobytes().decode(encoding="utf-8")
            return bits[9:]
        else:
            self.data: str = None
            self.left = Node()
            self.right = Node()
            remaining: BitArray = self.left.from_bits(bits[1:])
            remaining = self.right.from_bits(remaining)
            return remaining

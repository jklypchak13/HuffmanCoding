import sys
import os
from typing import List, Dict
sys.path.append(os.path.abspath('src'))
from huffman.tree import HuffmanTree, Node
from bitstring import BitArray


def test_init_simple():
    """
    Test Initialization of the HuffManTree
    """
    data: HuffmanTree = HuffmanTree('test/data/simple.txt')

    expected: Dict[str, int] = {
        'H': 1,
        'e': 2,
        'l': 3,
        'o': 2,
        ' ': 3,
        'w': 1,
        'r': 1,
        'd': 1,
        '\n': 1,
        't': 3,
        'h': 1,
        'i': 2,
        's': 2,
        'x': 1,
    }
    assert data.counter.get_characters() == expected
    assert data.nodes[0].data == 'H'
    assert data.nodes[0].count == 1
    assert data.nodes[1].data == 'w'
    assert data.nodes[1].count == 1


def test_init_empty():
    """
    Test Initialization of Huffman Tree with an empty File
    """
    data: HuffmanTree = HuffmanTree('test/data/empty.txt')

    assert data.counter.get_characters() == {}
    assert data.nodes == []


def test_init_bit_array():
    """
    Test Construction of a Huffman Tree from a bit array
    """
    given: BitArray = BitArray(filename="test/data/biased.bin")
    data: HuffmanTree = HuffmanTree(bit_array=given)
    expected = Node(
        left=Node(left=Node(data='b'), right=Node(data='c')), right=Node(data='a'))
    assert data.root == expected
    assert data.get_data() == BitArray('0b1110001')
    assert data.padding == 4


def test_single_step():
    """
    Test a single step, combining multiple nodes.
    """
    data: HuffmanTree = HuffmanTree('test/data/simple.txt')

    original_length: int = len(data.nodes)
    data._process_nodes()

    assert not data.nodes[9].data
    assert data.nodes[9].count == 2
    assert data.nodes[9].left == Node(1, 'H')
    assert data.nodes[9].right == Node(1, 'w')
    assert len(data.nodes) == original_length - 1


def test_construct_tree_root():
    """
    Test the root of constructing the Huffman Trees
    """
    data: HuffmanTree = HuffmanTree('test/data/simple.txt')
    root: Node = data.construct_tree()

    assert root.count == 24
    assert root.data is None


def test_construct_tree_leaf_simple():
    """
    Test the leftmost leaf of the Huffman Tree
    """
    data: HuffmanTree = HuffmanTree('test/data/simple.txt')
    root: Node = data.construct_tree()

    assert root.left.left.left.left == Node(1, 'r')


def test_construct_tree_leaf_complex():
    """
    Test another leaf in the Huffman Tree
    """
    data: HuffmanTree = HuffmanTree('test/data/simple.txt')
    root: Node = data.construct_tree()

    assert root.right.right.left.right == Node(2, 'i')


def test_construct_tree_biased_popular():
    """
    Test the Huffman Tree on a file with many of one letter.
    """
    data: HuffmanTree = HuffmanTree('test/data/biased.txt')
    root: Node = data.construct_tree()

    assert root.right == Node(3, 'a')


def test_construct_tree_biased_unpopular():
    """
    Test the Huffman Tree on a file with many of one letter.
    """
    data: HuffmanTree = HuffmanTree('test/data/biased.txt')
    root: Node = data.construct_tree()

    assert root.left.left == Node(1, 'b')
    assert root.left.right == Node(1, 'c')


def test_walk_tree_popular():
    """
    Test constructing the bitarray dictionary on the biased text file.
    """
    expected: Dict[str, BitArray] = {
        'a': BitArray('0b1'),
        'b': BitArray('0b00'),
        'c': BitArray('0b01')
    }
    data: HuffmanTree = HuffmanTree('test/data/biased.txt')
    root: Node = data.construct_tree()
    result: Dict[str, BitArray] = HuffmanTree._walk_tree(root)
    assert result == expected


def test_walk_tree_simple():
    """
    Test constructing the bitarray dictionary on simple test file
    """
    expected: Dict[str, BitArray] = {
        'r': BitArray('0b0000'),
        'd': BitArray('0b0001'),
        '\n': BitArray('0b0010'),
        'h': BitArray('0b0011'),
        'l': BitArray('0b010'),
        ' ': BitArray('0b011'),
        't': BitArray('0b100'),
        'x': BitArray('0b1010'),
        'e': BitArray('0b1011'),
        'o': BitArray('0b1100'),
        'i': BitArray('0b1101'),
        's': BitArray('0b1110'),
        'H': BitArray('0b11110'),
        'w': BitArray('0b11111')}

    data: HuffmanTree = HuffmanTree('test/data/simple.txt')
    root: Node = data.construct_tree()
    result: Dict[str, BitArray] = HuffmanTree._walk_tree(root)

    assert result == expected


def test_get_character_simple():
    """
    Test getting the given BitArray for simple characters.
    """
    expected: Dict[str, BitArray] = {
        'r': BitArray('0b0000'),
        'd': BitArray('0b0001'),
        '\n': BitArray('0b0010'),
        'h': BitArray('0b0011'),
        'l': BitArray('0b010'),
        ' ': BitArray('0b011'),
        't': BitArray('0b100'),
        'x': BitArray('0b1010'),
        'e': BitArray('0b1011'),
        'o': BitArray('0b1100'),
        'i': BitArray('0b1101'),
        's': BitArray('0b1110'),
        'H': BitArray('0b11110'),
        'w': BitArray('0b11111')}

    data: HuffmanTree = HuffmanTree('test/data/simple.txt')
    data.construct_tree()

    assert data.get_character('e') == BitArray('0b1011')
    assert data.get_character('x') == BitArray('0b1010')
    assert data.get_character('l') == BitArray('0b010')


def test_process_stream_biased():
    """
    Processing a stream to get a character
    """
    given: BitArray = BitArray(filename="test/data/biased.bin")
    data: HuffmanTree = HuffmanTree(bit_array=given)
    expected: str = 'a'
    stream: BitArray = data.get_data()
    result, leftover = data.process_stream(stream)
    assert result == expected
    assert leftover == BitArray('0b110001')

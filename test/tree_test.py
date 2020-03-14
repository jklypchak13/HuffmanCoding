import sys
import os
from typing import List, Dict
sys.path.append(os.path.abspath('src'))
from huffman import HuffmanTree, Node


def test_init_simple():
    """
    Test Initialization of the HuffManTree
    """
    data: HuffmanTree = HuffmanTree('data/simple.txt')

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
    data: HuffmanTree = HuffmanTree('data/empty.txt')

    assert data.counter.get_characters() == {}
    assert data.nodes == []


def test_single_step():
    """
    Test a single step, combining multiple nodes.
    """
    data: HuffmanTree = HuffmanTree('data/simple.txt')

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
    data: HuffmanTree = HuffmanTree('data/simple.txt')
    root: Node = data.construct_tree()

    assert root.count == 24
    assert root.data is None


def test_construct_tree_leaf_simple():
    """
    Test the leftmost leaf of the Huffman Tree
    """
    data: HuffmanTree = HuffmanTree('data/simple.txt')
    root: Node = data.construct_tree()

    assert root.left.left.left.left == Node(1, 'r')


def test_construct_tree_leaf_complex():
    """
    Test another leaf in the Huffman Tree
    """
    data: HuffmanTree = HuffmanTree('data/simple.txt')
    root: Node = data.construct_tree()

    assert root.right.right.left.right == Node(2, 'i')

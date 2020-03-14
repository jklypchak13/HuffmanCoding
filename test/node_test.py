import sys
import os
from typing import List, Dict
sys.path.append(os.path.abspath('src'))
from huffman.tree import Node
from bitstring import BitArray


def test_to_bits_leaf():
    """
    Tests converting a leaf node into a bitarray
    """
    test: Node = Node(5, 'x')
    expected: BitArray = BitArray('0b001111000')
    assert test.to_bits() == expected


def test_to_bits_parent():
    """
    Test converting a parent node into a bit array
    """
    test: Node = Node(5, left=Node(2, 'x'), right=Node(3, 'b'))
    expected: BitArray = BitArray('0b1001111000001100010')
    assert test.to_bits() == expected


def test_equality_leaf_equal():
    """
    Test node equality on equal leaves.
    """
    test: Node = Node(5, 'x')
    expected: Node = Node(5, 'x')
    assert test == expected


def test_equality_leaf_not_equal_count():
    """
    Test node equality on leaves with unequal counts
    """
    test: Node = Node(5, 'x')
    expected: Node = Node(2, 'x')
    assert test != expected


def test_equality_leaf_not_equal_data():
    """
    Test node equality on leaves with unequal data
    """
    test: Node = Node(5, 'x')
    expected: Node = Node(5, 'b')
    assert test != expected


def test_equality_parent_equal():
    """
    Test node equality on two equal parents.
    """
    test: Node = Node(5, left=Node(2, 'x'), right=Node(3, 'b'))
    expected: Node = Node(5, left=Node(2, 'x'), right=Node(3, 'b'))
    assert test == expected


def test_equality_parent_not_equal_count():
    """
    Test node equality with two parents with nonequivalent counts.
    """
    test: Node = Node(5, left=Node(2, 'x'), right=Node(3, 'b'))
    expected: Node = Node(3, left=Node(2, 'x'), right=Node(3, 'b'))
    assert test != expected


def test_equality_parent_not_equal_child():
    """
    Test node equality with two parents with nonequivalent children
    """
    test: Node = Node(5, left=Node(2, 'x'), right=Node(3, 'b'))
    expected: Node = Node(5, left=Node(2, 'a'), right=Node(3, 'b'))
    assert test != expected


def test_from_bits_leaf():
    """
    Test constructing a node from bits
    """
    given = BitArray('0b001111000100')
    expected = Node(data='x')

    result = Node()
    remaining = result.from_bits(given)

    assert result == expected
    assert remaining == BitArray('0b100')


def test_from_bits_parent():
    """
    Test constructing a node from bits
    """
    given = BitArray('0b1001111000001100010')
    expected = Node(left=Node(data='x'), right=Node(data='b'))

    result = Node()
    remaining = result.from_bits(given)

    assert result == expected
    assert remaining == BitArray()

import sys
import os
from typing import List, Dict
sys.path.append(os.path.abspath('src'))
from huffman.file import HuffmanIO
from bitstring import BitArray


def test_file_compression_biased():
    """
    Test compression of a short text file with  multiple of a given character.
    """
    file_writer: HuffmanIO = HuffmanIO()
    file_writer.compress_file("test/data/biased.txt", "test/data/result.bin")

    result: BitArray = BitArray(filename='test/data/result.bin')
    expected: BitArray = BitArray(filename='test/data/biased.bin')

    assert result == expected


def test_file_compression_simple():
    """
    Test Text compression on a simple text file.
    """
    file_writer: HuffmanIO = HuffmanIO()
    file_writer.compress_file("test/data/simple.txt", "test/data/result2.bin")

    result: BitArray = BitArray(filename='test/data/result2.bin')
    expected: BitArray = BitArray(filename='test/data/simple.bin')

    assert result == expected


def test_file_compression_empty():
    """
    Test text compression on an  empty text file.
    """
    file_writer: HuffmanIO = HuffmanIO()
    file_writer.compress_file("test/data/empty.txt", "test/data/result3.bin")

    with open("test/data/result3.bin", 'rb') as fp:
        result: bytes = fp.read()
    expected: bytes = b''

    assert result == expected


def test_file_decompression_simple():
    """
    Test text decompression on a simple text file.
    """
    file_writer: HuffmanIO = HuffmanIO()
    file_writer.decompress_file(
        "test/data/simple.bin", "test/data/result2.txt")

    with open("test/data/result2.txt") as fp:
        result: str = fp.read()

    with open("test/data/simple.txt") as fp:
        expected: str = fp.read()
    assert result == expected


def test_file_decompression_biased():
    """
    Test Text decompression on a text file with multiple of a character.
    """
    file_writer: HuffmanIO = HuffmanIO()
    file_writer.decompress_file(
        "test/data/biased.bin", "test/data/result.txt")

    with open("test/data/result.txt") as fp:
        result: str = fp.read()

    with open("test/data/biased.txt") as fp:
        expected: str = fp.read()
    assert result == expected


def test_file_decompression_empty():
    """
    Test text decompression on an empty text file.
    """
    file_writer: HuffmanIO = HuffmanIO()
    file_writer.decompress_file("test/data/empty.bin", "test/data/result3.txt")

    with open("test/data/result3.bin", 'rb') as fp:
        result: bytes = fp.read()
    expected: bytes = b''

    assert result == expected

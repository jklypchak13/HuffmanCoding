from huffman.file import HuffmanIO

stuff = HuffmanIO()
stuff.compress_file("test/data/simple.txt", "test/data/test.bin")
stuff.decompress_file("test/data/test.bin", "test/data/result.txt")

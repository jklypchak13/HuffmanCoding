from huffman.tree import HuffmanTree, Node
from bitstring import BitArray


class HuffmanIO:

    def compress_file(self, input_file_name, output_file_name):
        tree: HuffmanTree = HuffmanTree(input_file_name)
        root: Node = tree.construct_tree()
        if root is not None:
            padding: int = 0
            with open(input_file_name) as file_in:
                with open(output_file_name, 'wb') as file_out:

                    # Write Place Holder for Padding
                    file_out.write(BitArray('0b0000').tobytes())

                    current: str = file_in.readline()
                    bits: BitArray = BitArray()
                    bits += tree.to_bits()
                    while current != '':
                        for char in current:
                            bits += tree.get_character(char)
                            if(len(bits) % 8 == 0):
                                file_out.write(bits.tobytes())
                                bits = BitArray()
                        current = file_in.readline()
                    file_out.write(bits.tobytes())
                    padding = 8 - (len(bits) % 8)

                # Write the Padding Number to the start of the file.
                with open(output_file_name, 'rb+') as fp:
                    fp.seek(0, 0)
                    fp.write(padding.to_bytes(1, byteorder="little"))
        else:
            with open(output_file_name, 'w'):
                pass

    def decompress_file(self, input_file_name, output_file_name):
        with open(input_file_name, 'rb') as file_in:
            binary: bytes = file_in.read()
        if(binary != b''):
            data: BitArray = BitArray(filename=input_file_name)
            tree: HuffmanTree = HuffmanTree(bit_array=data)
            data: BitArray = tree.get_data()

            with open(output_file_name, 'w') as fp:
                while data:
                    character, data = tree.process_stream(data)
                    fp.write(character)

        else:
            with open(output_file_name, 'w'):
                pass

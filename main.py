from HuffmanTree import build_huffman_tree, generate_codes
from PriorityQueue import build_min_heap

def compress_file(input_file, output_file):
    with open(input_file, 'r') as file:
        text = file.read()
    
    freq_map = {}
    for char in text:
        freq_map[char] = freq_map.get(char, 0) + 1
    
    heap = build_min_heap(freq_map)
    huffman_tree = build_huffman_tree(heap)
    
    codes = {}
    generate_codes(huffman_tree, "", codes)
    
    encoded_text = "".join([codes[char] for char in text])
    
    with open(output_file, 'w') as file:
        file.write(encoded_text)
    
    print("File compressed successfully!")



def decompress_file(input_file, output_file, huffman_tree):
    with open(input_file, 'r') as file:
        encoded_text = file.read()
    
    current_node = huffman_tree
    decoded_text = ""
    
    for bit in encoded_text:
        if bit == '0':
            current_node = current_node.left
        else:
            current_node = current_node.right
        
        if current_node.char is not None:
            decoded_text += current_node.char
            current_node = huffman_tree
    
    with open(output_file, 'w') as file:
        file.write(decoded_text)
    
    print("File decompressed successfully!")


if __name__ == "__main__":
    input_file = "test_files/test_in.txt"
    compressed_file = "test_files/test_out.txt"
    compress_file(input_file, compressed_file)
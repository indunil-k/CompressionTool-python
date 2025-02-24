import heapq
from PriorityQueue import HuffmanNode

def build_huffman_tree(heap):
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    return heapq.heappop(heap)



def generate_codes(node, current_code, codes):
    if node is None:
        return
    if node.char is not None:
        codes[node.char] = current_code
        return
    generate_codes(node.left, current_code + "0", codes)
    generate_codes(node.right, current_code + "1", codes)
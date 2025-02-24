import heapq

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_min_heap(freq_map):
    heap = []
    for char, freq in freq_map.items():
        heapq.heappush(heap, HuffmanNode(char, freq))
    return heap
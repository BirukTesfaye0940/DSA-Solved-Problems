import heapq  # Python's built-in priority queue (min-heap)

# Step 0: Define a Node class to represent each character and its frequency
class Node:
    def __init__(self, freq, char=None, left=None, right=None):
        self.freq = freq  # Frequency of the character(s)
        self.char = char  # Character stored (None for internal nodes)
        self.left = left  # Left child (used for tree structure)
        self.right = right  # Right child (used for tree structure)
    
    # This makes Node comparable based on freq, required for the heap
    def __lt__(self, other):
        return self.freq < other.freq


# Main function to build Huffman codes
def huffman_coding(chars, freqs):
    heap = []  # Step 1: Create a min-heap to store nodes

    # Step 1: Build the heap with initial character nodes
    for c, f in zip(chars, freqs):
        # Create a Node for each character and push to heap
        heapq.heappush(heap, Node(f, c))
    
    # Step 2: Build the Huffman Tree
    # Keep merging the two smallest nodes until one node remains
    while len(heap) > 1:
        left = heapq.heappop(heap)  # Pop node with smallest frequency
        right = heapq.heappop(heap)  # Pop node with second smallest frequency

        # Merge them into a new internal node
        merged = Node(left.freq + right.freq, None, left, right)
        # Push the merged node back to the heap
        heapq.heappush(heap, merged)
    
    # The remaining node is the root of the Huffman Tree
    root = heap[0]
    
    # Step 3: Generate Huffman codes by traversing the tree
    codes = {}  # Dictionary to store character -> code mapping

    def generate_codes(node, current_code):
        if node is None:
            return  # Base case: empty node
        
        # If it's a leaf node (actual character), store its code
        if node.char is not None:
            codes[node.char] = current_code
            return
        
        # Traverse left child, append "0" to the code
        generate_codes(node.left, current_code + "0")
        # Traverse right child, append "1" to the code
        generate_codes(node.right, current_code + "1")
    
    generate_codes(root, "")  # Start traversal from root with empty code
    
    return codes


# Example usage
chars = ['a','b','c','d','e','f']
freqs = [45,13,12,16,9,5]

print(huffman_coding(chars, freqs))
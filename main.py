class Node:
    def __init__(self, char=None, freq=0):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# -------------------------------------------Classes must be declared above this line-----------------------------------------------------------


# Huffman
def create_tree(chars, freqs):
    nodes = [Node(c, f) for c, f in zip(chars, freqs)]

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)

        left = nodes.pop(0)
        right = nodes.pop(0)

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right

        nodes.append(merged)

    return nodes[0]

def generate_codes(node, prefix="", codes=None):
    if codes is None:
        codes = {}

    if node.char is not None:
        codes[node.char] = prefix
        return codes

    generate_codes(node.left, prefix + "0", codes)
    generate_codes(node.right, prefix + "1", codes)

    return codes
# End of Huffman

# -------------------------------------------Helper functions above this line-------------------------------------------------------------------

def coin_change():
    print_title("Coin Change")

    """
    Coin Change code




    """

def huffman():
    print_title("Huffman")

    print_title("Enter values in Space Separated format: ")
    print("Sample: ")
    print("Enter Characters: A B C D")
    print("Enter Frequencies: 10 2 3 5")
    print("-------------------------------")

    chars = input("Enter characters: ").split()
    freqs = list(map(int, input("Enter frequencies: ").split()))

    if len(chars) != len(freqs):
        print("Number of Characters and Frequency doesn't match")

    root = create_tree(chars, freqs)
    codes = generate_codes(root)

    print("Huffman Codes:")
    for ch in chars:
        print(f"{ch}: {codes[ch]}")

def fractional_knapsack():
    print_title("Fractional Knapsack")

    
    """
    fractional knapsack code



    
    """

def job_scheduling():
    print_title("Job Scheduling")

    
    """
    job_scheduling code



    
    """

def print_title(title: str):
    width = 50
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()

def main():

    algorithms = [
        "Coin Change",
        "Huffman Coding",
        "Fractional Knapsack",
        "Job Scheduling with Deadlines",
        "Exit"
    ]

    while True:
        print_title("Greedy Algorithms")

        for i in range(0, len(algorithms)):
            print(f"{i + 1}. {algorithms[i]}")
        print()

        isValid = False
        while (not isValid):
            try:
                option = int(input("Select an option: "))
                isValid = True
            except ValueError:
                print("Insert an integer")

        match option:
            case 1:
                coin_change()
            case 2:
                huffman()
            case 3:
                fractional_knapsack()
            case 4:
                job_scheduling()
            case 5:
                break
            case _:
                print("Choose value between 1-5")

        

        

if __name__ == "__main__":
    main()
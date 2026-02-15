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
    """create a list of nodes for each character and its frequency"""

    while len(nodes) > 1:
        nodes.sort(key=lambda x: x.freq)
        """sort nodes by frequency ascending"""

        left = nodes.pop(0)
        right = nodes.pop(0)
        """take two nodes with smallest frequency"""

        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        """merge them into a new node and assign children"""

        nodes.append(merged)
        """add the merged node back to the list"""

    return nodes[0]
    """return root of the tree"""

def generate_codes(node, prefix="", codes=None):
    if codes is None:
        codes = {}

    if node.char is not None:
        codes[node.char] = prefix
        return codes
        """assign code to leaf node character"""

    generate_codes(node.left, prefix + "0", codes)
    generate_codes(node.right, prefix + "1", codes)
    """traverse left with 0 and right with 1 recursively"""

    return codes
# End of Huffman

# -------------------------------------------Helper functions above this line-------------------------------------------------------------------

def coin_change(): 
    """using dynamic programming -> Vince Evangelista"""
    orig_amt  = int(input("Enter the original amount: "))
    denominations = sorted([int(x) for x in input("Enter coin denominations (split them with spaces): ").strip().split()], reverse=True)
    """get coin denominations and sort descending for clarity"""
    i = 0
    used_coins = {}

    dp = [float("inf")] * (orig_amt + 1)
    dp[0] = 0
    """dp array to track min coins needed for each amount"""

    choice = [-1] * (orig_amt + 1)
    """choice array to reconstruct which coin was used"""

    for amt in range(1, orig_amt + 1):
        for coin in denominations:
            if coin <= amt and dp[amt - coin] + 1 < dp[amt]:
                dp[amt] = dp[amt - coin] + 1
                choice[amt] = coin
                """update dp and choice if using this coin gives fewer coins"""

    if dp[orig_amt] == float("inf"):
        print("No solution possible.")
        return

    amt = orig_amt
    while amt > 0:
        coin = choice[amt]
        if coin not in used_coins:
            used_coins[coin] = 1
        else:
            used_coins[coin] += 1
        amt -= coin
        """reconstruct which coins were used to make up original amount"""

    print()
    print(f"Total Coins Used: {sum([x for x in used_coins.values()])}")
    print()
    print("Breakdown:")
    print(f"{'COIN':<10} {'COUNT':>5}")
    print("-" * 17)

    for coin, count in used_coins.items():
        print(f"{coin:<10} {count:>5}")

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
    """create huffman tree and generate codes"""

    print("Huffman Codes:")
    for ch in chars:
        print(f"{ch}: {codes[ch]}")

def fractional_knapsack():

    n = int(input("Enter number of items: "))
    weights = list(map(float, input("Enter the weights (space-separated): ").split()))
    values = list(map(float, input("Enter the values (space-separated): ").split()))
    W = float(input("Enter knapsack capacity: "))
    
    if len(weights) != n or len(values) != n:
        print("Error: Number of weights and values must match the number of items.")
        return  

    ratios = [v / w for v, w in zip(values, weights)]
    """calculate value to weight ratio for each item"""

    fractions = [0] * n
    max_value = 0
    remaining_capacity = W
    """initialize fraction taken and max value"""

    while remaining_capacity > 0:
        max_ratio = -1
        max_index = -1
        for i in range(n):
            if fractions[i] == 0 and ratios[i] > max_ratio:
                max_ratio = ratios[i]
                max_index = i
        if max_index == -1:
            break  
        """select next item with highest ratio that is not yet taken"""

        if weights[max_index] <= remaining_capacity:
            fractions[max_index] = 1
            max_value += values[max_index]
            remaining_capacity -= weights[max_index]
        else:
            fraction = remaining_capacity / weights[max_index]
            fractions[max_index] = fraction
            max_value += values[max_index] * fraction
            remaining_capacity = 0
        """take full item if possible, otherwise take fraction to fill remaining capacity"""

    items = []
    for i in range(n):
        profit = values[i] * fractions[i]
        items.append((ratios[i], i+1, ratios[i], fractions[i], profit))  
    items.sort(reverse=True)  
    """prepare table of items sorted by ratio for display"""

    print("\nItem | Ratio   | Fraction Taken | Profit")
    for item in items:
        _, item_num, ratio, fraction, profit = item
        print(f"{item_num:>4} | {ratio:>7.2f} | {fraction:>14.2f} | {profit:>6.2f}")
    print("Fractions:", [round(f, 2) for f in fractions])
    print("Max value:", round(max_value, 2))




def job_scheduling():

    n = int(input("Enter the number of jobs: "))
    deadline = list(map(int, input(f"Enter the deadlines for {n} jobs (space-separated): ").split()))
    profit = list(map(int, input(f"Enter the profits for {n} jobs (space-separated): ").split()))

    jobs = [(f"J{i+1}", deadline[i], profit[i], i) for i in range(n)]
    """combine job info into a list of tuples (name, deadline, profit, index)"""

    print("\nORIGINAL TABLE")
    print("Job\tDeadline\tProfit")
    for j in jobs:
        print(f"{j[0]}\t{j[1]}\t\t{j[2]}")

    jobs_sorted = sorted(jobs, key=lambda x: x[2], reverse=True)
    """sort jobs by profit descending for greedy selection"""

    print("\nSORTED BY PROFIT (DESC)")
    print("Job\tProfit\tDeadline")
    for j in jobs_sorted:
        print(f"{j[0]}\t{j[2]}\t{j[1]}")

    slot = [None] * n
    """initialize slot timeline for scheduled jobs"""
    total_profit = 0
    job_count = 0

    for job in jobs_sorted:
        name, d, p, idx = job
        for s in range(min(n, d) - 1, -1, -1):
            if slot[s] is None:
                slot[s] = job
                total_profit += p
                job_count += 1
                break
        """place job in latest available slot before its deadline"""

    print("\nFINAL SLOTS (Timeline)")
    print("Time :", end=" ")
    for i in range(n):
        print(f"{i}", end="   ")
    print()

    print("Jobs :", end=" ")
    for s in slot:
        if s:
            print(f"{s[0]}", end=" ")
        else:
            print("-", end=" ")
    print()

    selected = [s[0] for s in slot if s]
    """list of selected jobs based on final slots"""

    print("\nSelected Jobs (Left to Right Timeline):")
    print(selected)

    print("\nJobs Done:", job_count)
    print("Total Profit:", total_profit)


def print_title(title: str):
    width = 50
    print("=" * width)
    print(title.center(width))
    print("=" * width)
    print()
    """print a formatted title block with given width"""


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
        """prompt user to select an algorithm and validate input"""

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
        """call the corresponding algorithm based on user selection or exit"""


if __name__ == "__main__":
    main()
    """entry point for program execution"""

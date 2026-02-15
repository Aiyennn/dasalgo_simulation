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

def coin_change(): # using dynamic programming -> Vince Evangelista
    orig_amt  = int(input("Enter the original amount: "))
    denominations = sorted([int(x) for x in input("Enter coin denominations (split them with spaces): ").strip().split()], reverse=True)
    i = 0
    used_coins = {}

    dp = [float("inf")] * (orig_amt + 1)
    dp[0] = 0

    choice = [-1] * (orig_amt + 1)

    for amt in range(1, orig_amt + 1):
        for coin in denominations:
            if coin <= amt and dp[amt - coin] + 1 < dp[amt]:
                dp[amt] = dp[amt - coin] + 1
                choice[amt] = coin

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

    print("Huffman Codes:")
    for ch in chars:
        print(f"{ch}: {codes[ch]}")

def fractional_knapsack():
    print_title("Fractional Knapsack")

    """
    fractional knapsack code
    """

def job_scheduling():

    n = int(input("Enter the number of jobs: "))


    deadline = list(map(int, input(f"Enter the deadlines for {n} jobs (space-separated): ").split()))

    profit = list(map(int, input(f"Enter the profits for {n} jobs (space-separated): ").split()))


    jobs = [(f"J{i+1}", deadline[i], profit[i], i) for i in range(n)]

    print("\nORIGINAL TABLE")
    print("Job\tDeadline\tProfit")
    for j in jobs:
        print(f"{j[0]}\t{j[1]}\t\t{j[2]}")


    jobs_sorted = sorted(jobs, key=lambda x: x[2], reverse=True)

    print("\nSORTED BY PROFIT (DESC)")
    print("Job\tProfit\tDeadline")
    for j in jobs_sorted:
        print(f"{j[0]}\t{j[2]}\t{j[1]}")

    # Slot tracker
    slot = [None] * n
    total_profit = 0
    job_count = 0

    # Scheduling
    for job in jobs_sorted:
        name, d, p, idx = job
        for s in range(min(n, d) - 1, -1, -1):
            if slot[s] is None:
                slot[s] = job
                total_profit += p
                job_count += 1
                break

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

    print("\nSelected Jobs (Left to Right Timeline):")
    selected = [s[0] for s in slot if s]
    print(selected)

    print("\nJobs Done:", job_count)
    print("Total Profit:", total_profit)

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

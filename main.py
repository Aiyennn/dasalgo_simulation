def coin_change():
    print_title("Coin Change")

    """
    Coin Change code




    """

def huffman():
    print_title("Huffman")

    
    """
    Huffman code



    
    """

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
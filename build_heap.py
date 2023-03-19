# python3
swaps = []

def heapify_down(arr, n, i):
    global swaps
    min_idx = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] < arr[min_idx]:
        min_idx = l
    if r < n and arr[r] < arr[min_idx]:
        min_idx = r
    if i != min_idx:
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        swaps.append((i, min_idx))
        heapify_down(arr, n, min_idx)


def build_heap(arr):
    n = len(arr)
    # Start from the last non-leaf node and perform heapify_down on each node
    for i in range(n // 2, -1, -1):
        heapify_down(arr, n, i)
    return swaps


def main():
    input_type = input("I or F: ")

    if input_type == "I":
        # Read input from keyboard
        n = int(input().strip())
        arr = list(map(int, input().split()))
    else:
        # Read input from file
        while True:
            filename = input("Enter filename: ").strip()
            try:
                with open(filename, "r") as f:
                    n = int(f.readline().strip())
                    arr = list(map(int, f.readline().split()))
                    break
            except FileNotFoundError:
                print("File not found. Please try again.")

    swaps = build_heap(arr)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

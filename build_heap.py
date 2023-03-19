# python3
def heapify_down(arr, n, i, swaps):
    """
    Perform a single swap operation and ensure that the min-heap property is maintained.
    """
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
        heapify_down(arr, n, min_idx, swaps)


def build_heap(arr):
    n = len(arr)
    swaps = []
    # Start from the last non-leaf node and perform heapify_down on each node
    for i in range(n // 2, -1, -1):
        heapify_down(arr, n, i, swaps)
    return swaps
def main():
    
    n = int(input().strip())
    arr = list(map(int, input().split()))
    swaps = build_heap(arr)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

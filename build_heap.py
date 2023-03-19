import os
#KristersRicardsAunins221RDC033
def build_heap(data):
    heap_size = len(data)
    swaps = []
    for i in range(heap_size):
        parent = (i - 1) // 2
        j = i
        while j > 0 and data[j] > data[parent]:
            swaps.append((parent, j))
            data[parent], data[j] = data[j], data[parent]
            j = parent
            parent = (j - 1) // 2
    return swaps

def sift_down(data, i, swaps):
    heap_size = len(data)
    while True:
        min_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2
        if left_child < heap_size and data[left_child] < data[min_index]:
            min_index = left_child
        if right_child < heap_size and data[right_child] < data[min_index]:
            min_index = right_child
        if min_index == i:
            break
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        i = min_index

def main():
    ievade = input("K, F")
    if "I" in ievade:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif "F" in ievade:
        fails = input("K")
        atrasanas = './tests/'
        faila_vieta = os.path.join(atrasanas, fails)
        with open(faila_vieta, mode="r") as file:
            n = int(file.readline())
            data = list(map(int, file.readline().split()))
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
        
if __name__ == "__main__":
    main()

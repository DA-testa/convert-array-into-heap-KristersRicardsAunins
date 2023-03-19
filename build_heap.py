#KristersRicardsAunins
import pathlib

def main():
    input_type = input()
    parser = {
        'I': parse_input,
        'F': parse_file
    }
    n, data = parser[input_type]()
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

def build_heap(data):
    swaps = []
    heap_size = len(data)
    for i in range(heap_size // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    heap_size = len(data)
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2 
    if left_child < heap_size and data[left_child] < data[min_index]:
        min_index = left_child
    if right_child < heap_size and data[right_child] < data[min_index]:
        min_index = right_child
    if min_index != i:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(data, min_index, swaps)

def parse_input():
    n = int(input())
    data = list(map(int, input().split()))
    return n, data

def parse_file():
    filename = input().strip()
    file_path = pathlib.Path('tests') / filename
    with file_path.open(mode="r") as file:
        n = int(file.readline().strip())
        data = list(map(int, file.readline().split()))
    return n, data

if __name__ == "__main__":
    main()

# python3
def parent(i):

    return (i-1)//2

def left_child(i):

    return 2*i + 1

def right_child(i):

    return 2*i + 2

def sift_down(data, swaps, i):

# Find the maximum element among i and its children
    max_index = i
    l = left_child(i)
    if l < len(data) and data[l] < data[max_index]:
        max_index = l
        r = right_child(i)
    if r < len(data) and data[r] < data[max_index]:
        max_index = r
# If i is not the maximum, swap it with the maximum and continue sifting down
    if i != max_index:
        swaps.append((i, max_index))
        data[i], data[max_index] = data[max_index], data[i]
    sift_down(data, swaps, max_index)

def build_heap(data):

    swaps = []
# Start from the last node and work upwards to the root node
    for i in range(len(data)//2, -1, -1):
        sift_down(data, swaps, i)
    return swap


def main():
    
    input_type = input()
    if input_type == "I":
        n = int(input())
        data = list(map(int, input().split()))

    elif input_type == "F":
        with open("input_file.txt", "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    else:
        print("Invalid")
        return

    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

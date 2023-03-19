# python3
def parent(i):
"""
This function returns the index of the parent of node i
"""
return (i-1)//2

def left_child(i):
"""
This function returns the index of the left child of node i
"""
return 2*i + 1

def right_child(i):
"""
This function returns the index of the right child of node i
"""
return 2*i + 2

def sift_down(data, swaps, i):
"""
This function sifts down the element at index i to maintain the heap property
"""
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
"""
This function converts the input array into a heap using O(n) swaps
"""
swaps = []
# Start from the last node and work upwards to the root node
for i in range(len(data)//2, -1, -1):
sift_down(data, swaps, i)
return swap


def main():
    
    input_type = input("Enter input type (K for keyboard input, F for file input): ")
    if input_type == "K":
        n = int(input())
        data = list(map(int, input().split()))

    elif input_type == "F":
        with open("input_file.txt", "r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))

    else:
        print("Invalid input type. Enter K for keyboard input or F for file input.")
        return

    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

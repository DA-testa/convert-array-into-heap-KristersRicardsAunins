#KristersRicardsAunins
import os

def build_heap(data):
    swaps = []
    lielums = len(data)
    for i in range(lielums // 2, -1, -1):
        sift_down(data, i, swaps)
    return swaps

def sift_down(data, i, swaps):
    lielums = len(data)
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2 
    if left_child < lielums and data[left_child] < data[min_index]:
        min_index = left_child
    if right_child < lielums and data[right_child] < data[min_index]:
        min_index = right_child
    if min_index != i:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        sift_down(data, min_index, swaps)

def main():       
    ievade = input()
    if "I" in ievade:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif "F" in ievade:
        fails = input()
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

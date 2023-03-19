import os
#KristersRicardsAunins221RDC033
def uztaisam(data):
    jamaina = []
    lielums = len(data)
    for i in range(lielums // 2, -1, -1):
        sift_down(data, i, jamaina)
    return jamaina

def samainam(data, i, jamaina):
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
        jamaina.append((i, min_index))
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
    jamaina = uztaisam(data)
    print(len(jamaina))
    for i, j in jamaina:
        print(i, j)
        
if __name__ == "__main__":
    main()
#KRISTERSRICARDSAUNINS

import os
#KristersRA
def taisam(data):
    mainam = []
    lielums = len(data)
    for i in range(lielums // 2, -1, -1):
        maz(data, i, mainam)
    return maz

def maz(data, i, mainam):
    lielums = len(data)
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < lielums and data[left_child] < data[min_index]:
        min_index = left_child
    if right_child < lielums and data[right_child] < data[min_index]:
        min_index = right_child
    if min_index != i:
        mainam.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        maz(data, min_index, mainam)
        
def main():
    ievade = input("K  F")
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
    mainam = taisam(data)
    print(len(mainam))
    for i, j in mainam:
        print(i, j)

if __name__ == "__main__":
    main()
 #KristersAunins

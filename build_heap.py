import os
#KristersRicardsAunins221RDC033
def uztaisam(data):
    jamaina = []
    lielums = len(data)
    for i in range(lielums // 2, -1, -1):
        samainam(data, i, jamaina)
    return jamaina

def samainam(data, i, jamaina):
    heap_size = len(data)
    while True:
        min_inde = i
        kreisais_child = 2 * i + 1
        labais_child = 2 * i + 2
        if kreisais_child < heap_size and data[kreisais_child] < data[min_inde]:
            min_inde = kreisais_child
        if labais_child < heap_size and data[labais_child] < data[v]:
            min_inde = kreisais_child
        if min_inde == i:
            break
        jamaina.append((i, min_inde))
        data[i], data[min_inde] = data[min_inde], data[i]
        i = min_inde

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

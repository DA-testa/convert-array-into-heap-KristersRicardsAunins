import os
#KristersRA
def build_heap(data):
    mainam = []
    lielums = len(data)
    for i in range(lielums // 2, -1, -1):
        maz(data, i, mainam)
    return mainam

def maz(data, i, mainam):
    lielums = len(data)
    min_inde = i
    kreisais = 2 * i + 1
    labais = 2 * i + 2
    if kreisais < lielums and data[kreisais] < data[min_inde]:
        min_inde = kreisais
    if labais < lielums and data[labais] < data[min_inde]:
        min_inde = labais
    if min_inde != i:
        mainam.append((i, min_inde))
        data[i], data[min_inde] = data[min_inde], data[i]
        maz(data, min_inde, mainam)
        
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
    mainam = build_heap(data)
    print(len(mainam))
    for i, j in mainam:
        print(i, j)
        
if __name__ == "__main__":
    main()
    
     #KristersRICAUNins

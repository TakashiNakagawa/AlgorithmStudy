n = int(input())
cards = list(input().split())
cards_original = list(cards)

def get_value(card):
    return card[1]

def BubbleSort(C):
    for i in range(0, len(C)):
        for j in range(len(C)-1, i, -1):
            if get_value(C[j]) < get_value(C[j-1]):
                C[j], C[j-1] = C[j-1], C[j]

def SelectionSort(C):
    for i in range(0, len(C)):
        mini = i
        for j in range(i, len(C)):
            if get_value(C[j]) < get_value(C[mini]):
                mini = j
        if i != mini:
            C[i], C[mini] = C[mini], C[i]

def check_stable(C_original, C):
    def create_dict(ary):
        d = {}
        for i in range(0, len(ary)):
            key = ary[i][1]
            val = ary[i][0]
            if key in d:
                d[key].append(val)
            else:
                d[key] = list(val)
        return d

    d_original = create_dict(C_original)
    d = create_dict(C)
    def check(d_original, d):
        for key, value in d_original.items():
            if value != d[key]:
                print("Not stable")
                return
        print("Stable")
    check(d_original, d)

BubbleSort(cards)
print(" ".join(map(str, cards)))
check_stable(cards_original, cards)

cards = list(cards_original)
SelectionSort(cards)
print(" ".join(map(str, cards)))
check_stable(cards_original, cards)


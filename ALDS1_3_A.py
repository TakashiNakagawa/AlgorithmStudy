line = input().split()

def compute(a, b, op):
    if op == "+":
        return int(a) + int(b)
    elif op == "-":
        return int(a) - int(b)
    else :
        return int(a)*int(b)

ary = []
while not ary or not len(ary) == 1:
    i = 0
    while i < len(line):
        if i + 2 < len(line):
            x1 = line[i]
            x2 = line[i+1]
            x3 = line[i+2]
            if x1.lstrip("-").isdigit() and x2.lstrip("-").isdigit() and not x3.lstrip("-").isdigit():
                ary.append(str(compute(x1, x2, x3)))
                i += 3
                continue
        ary.append(line[i])
        i += 1
    if len(ary) == 1:
        break
    line = ary[:]
    ary = []
print(ary[0])



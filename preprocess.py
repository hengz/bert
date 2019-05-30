import json

A = []
B = []
C = []

with open("data/input.txt", "r", encoding="utf8") as f:
    for line in f:
        x = json.loads(line)
        A.append(x["A"])
        B.append(x["B"])
        C.append(x["C"])

with open("data/input_A.txt", "w", encoding="utf8") as f_a:
    for line in A:
        print(line.replace("\n", " "), file=f_a)

with open("data/input_B.txt", "w", encoding="utf8") as f_b:
    for line in B:
        print(line.replace("\n", " "), file=f_b)

with open("data/input_C.txt", "w", encoding="utf8") as f_c:
    for line in C:
        print(line.replace("\n", " "), file=f_c)

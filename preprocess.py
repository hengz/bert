import json

A = []
B = []
C = []
count = 400

with open("data/input.txt", "r", encoding="utf8") as f:
    for line in f:
        x = json.loads(line)
        A.append(x["A"])
        B.append(x["B"])
        C.append(x["C"])

with open("data/input_A.txt", "w", encoding="utf8") as f_a, open("data/test_A.txt", "w", encoding="utf8") as t_a:
    for (i, line) in enumerate(A):
        if i < count:
            print(line.replace("\n", " "), file=f_a)
        else:
            print(line.replace("\n", " "), file=t_a)

with open("data/input_B.txt", "w", encoding="utf8") as f_b, open("data/test_B.txt", "w", encoding="utf8") as t_b:
    for (i, line) in enumerate(B):
        if i < count:
            print(line.replace("\n", " "), file=f_b)
        else:
            print(line.replace("\n", " "), file=t_b)

with open("data/input_C.txt", "w", encoding="utf8") as f_c, open("data/test_C.txt", "w", encoding="utf8") as t_c:
    for (i, line) in enumerate(C):
        if i < count:
            print(line.replace("\n", " "), file=f_c)
        else:
            print(line.replace("\n", " "), file=t_c)

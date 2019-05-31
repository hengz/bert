lines_A = ["a_1", "a_2", "a_3"]
lines_B = ["b_1", "b_2", "b_3"]

for (i, line_A), line_B in zip(enumerate(lines_A), lines_B):
    print(i, line_A, line_B)
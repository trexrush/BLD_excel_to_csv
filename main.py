# Eduardo Mazuera 2022

import csv
"""
Converts a CSV file of letter pairs based on a CSV file, ready to import into anki.
This script was intended for personal use, and thus demands a specific format.
If your CSV export is different, change 'name' to the file name you are using as input. (but the ranges may differ)
"""
name = 'BLD Algs _ Memo - Letter Pairs.csv'

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']
pairs = []
with open('pairs.csv', 'w', newline='', encoding="utf8") as csv_file:
    out = csv.writer(csv_file)
    with open(name, 'r', encoding="utf8") as csv_input:
        w = csv.reader(csv_input)
        row_n = 0
        for row in w:
            if 0 < row_n < 25:
                for i, col in enumerate(row):
                    if i == row_n:
                        continue
                    if 0 < i < 25:
                        out.writerow([letters[i - 1] + letters[row_n - 1]] + [col])
                        print([letters[i - 1] + letters[row_n - 1]], col)
            row_n += 1

"""
Generates an empty list of letter pairs ready to import into anki.
"""
# with open('pairs.csv', 'w', newline='') as csv_file:
#     w = csv.writer(csv_file)
#     for i in ascii_uppercase[:-2]:
#         for j in ascii_uppercase[:-2]:
#             pair = i + j
#             if i == j:
#                 continue
#             print(pair, ">> _")
#             w.writerow([i + j])

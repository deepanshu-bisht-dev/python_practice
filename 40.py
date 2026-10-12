# Matrix Operations
m = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

n = len(m)
transpose = [[m[j][i] for j in range(n)] for i in range(n)]
main_diag = sum(m[i][i] for i in range(n))
sec_diag = sum(m[i][n - 1 - i] for i in range(n))

print("Transpose:")
for row in transpose:
    print(row)
print("Main diagonal sum:", main_diag)
print("Secondary diagonal sum:", sec_diag)
n, m = map(int, input().split())
board = [input() for _ in range(n)]

def count_changes(x, y):
    pattern1 = 0
    pattern2 = 0
    for i in range(8):
        for j in range(8):
            current = board[x + i][y + j]
            if (i + j) % 2 == 0:
                if current != 'W':
                    pattern1 += 1
                if current != 'B':
                    pattern2 += 1
            else:
                if current != 'B':
                    pattern1 += 1
                if current != 'W':
                    pattern2 += 1
    return min(pattern1, pattern2)

min_count = 64
for i in range(n - 7):
    for j in range(m - 7):
        min_count = min(min_count, count_changes(i, j))

print(min_count)

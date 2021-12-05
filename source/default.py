import time

def default(a, b):
    start_time = time.time()
    m, n = len(a), len(b)
    count = 0
    for k in range(n - m + 1):
        i, j = 0, k
        while i < m:
            if a[i] != b[j]: break
            i, j = i + 1, j + 1
        if i == m: count += 1
    end_time = time.time()
    print(f'Default: Found {count} times in {end_time - start_time} seconds.')
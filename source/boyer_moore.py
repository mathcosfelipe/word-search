import time

def boyer_moore(a, b):
    start_time = time.time()
    m, n = len(a), len(b)
    count = 0
    last = [-1] * 256
    for k in range(m): last[ord(a[k])] = k
    while k < n:
        j, i = k, m - 1
        while i >= 0:
            if a[i] != b[j]: break
            j, i = j - 1, i - 1
        if i < 0: count += 1
        if k + 1 >= n: break
        k = k + m - last[ord(b[k+1])]
    end_time = time.time()
    print(f'Boyer Moore: Found {count} times in {end_time - start_time} seconds.')
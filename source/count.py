import time

def count(a, b):
    start_time = time.time()
    count = b.count(a)
    end_time = time.time()
    print(f'Count: Found {count} times in {end_time - start_time} seconds.')
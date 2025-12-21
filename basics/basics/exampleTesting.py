import time

# List O(n)
ls = list(range(10000))
start = time.time()
10000 in ls  # Scans 10K elements → slow
print("List:", time.time() - start)

# Set O(1)
s = set(range(10000))
start = time.time()
10000 in s  # Hash → direct access → fast
print("Set:", time.time() - start)

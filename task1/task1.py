#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys

def circular_array_path(n, m):
    circular_array = list(range(1, n + 1))
    path = []

    current_index = 0
    while len(circular_array) > 0:
        next_index = (current_index + m - 1) % len(circular_array)
        path.append(circular_array.pop(next_index))
        current_index = next_index

    return path

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <n> <m>")
        sys.exit(1)

    n = int(sys.argv[1])
    m = int(sys.argv[2])

    if n <= 0 or m <= 0:
        print("Both n and m should be positive integers.")
        sys.exit(1)

    result = circular_array_path(n, m)
    print(" ".join(map(str, result)))


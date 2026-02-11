def findUnion(a, b):
    return list(set(a) | set(b))


# Example
a = [1, 2, 3, 2, 1]
b = [3, 2, 2, 3, 3, 2]
print(sorted(findUnion(a, b)))   # Output: [1, 2, 3]

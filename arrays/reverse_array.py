import array as pa
a = pa.array('i', [2, 3, 4, 5])
size = len(a)
b = pa.array('i')

for i in range(0, size):
    b.insert(i, a[size-i-1])


print(b)

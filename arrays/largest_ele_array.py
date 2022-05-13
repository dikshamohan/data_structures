import array as pa
a = pa.array('i', [2, 8, 4, 9, 5, 1])
size = len(a)

largest = 0
for i in range(0, size):
    if a[i]>largest:
        largest=a[i]
        
print(largest)
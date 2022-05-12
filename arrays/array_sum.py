import array as pa
a = pa.array('i', [2, 3, 4, 5])

sum = 0
for i in range(0, len(a)):
  sum = sum + a[i]

print("sum of array is:" + str(sum))


import numpy as np

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

#print(arr1.shape,arr2.shape)

a = np.array(arr1).reshape(1,4)
b = np.array(arr2).reshape(1,4)

print(a.shape,b.shape)

con = np.add(a,b)/2
print(con.shape,con)




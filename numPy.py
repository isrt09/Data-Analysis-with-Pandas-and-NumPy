import numpy as np

# Array Create
list = [2,5,7,8]
np.array(list)
np.array([list,list])
np.array([[1,2,3],[5,6,7]])
np.array([[3,4,5],[1,2,4],[5,4,3]])
np.eye(4)
np.zeros(4)
np.ones(4)
np.identity(4)
np.zeros(shape=(3,4))
np.ones(shape=(3,4))
np.arange(10)
np.arange(2,40,2)
np.arange(100,0,-2)
np.linspace(0,20,2)
np.random.rand(2,3)
np.random.rand(2,3,4)
np.random.randn(2,3)
np.random.randint(1,10)
np.random.randint(1,10,4)
mat = np.random.randn(2,3)
mat.size
mat.shape

# Array Index & Selection

arr = np.arange(50,80)
arr.size
arr.shape
arr
arr[:]
arr[3:8]
arr[5:]
arr[:5]
arr[:,1]
arr[:,1:2]
arr[:,1:3]
arr = np.random.rand(3,4)
arr[0,1]
arr[1,]
arr[,3]
arr[1:]
arr[:,3]
arr[1:3]
arr[1:3,1:3]
arr[1:2,:]

# Built In Functions
a = np.random.rand(3,4)
b = np.random.rand(3,4)
np.hstack((a,b))
np.vstack((a,b))
np.vstack((b,a))
a = 10 * a
np.floor(a)
np.ceil(a)

new_mat = np.floor(a)
np.sum(new_mat)
np.sum(new_mat,axis=0)
np.sum(new_mat,axis=1)

np.mean(new_mat)
np.mean(new_mat, axis=0)
np.mean(new_mat, axis=1)

np.min(new_mat)
np.min(new_mat, axis=0)
np.min(new_mat, axis=1)

np.max(new_mat)
np.max(new_mat, axis=0)
np.max(new_mat, axis=1)

np.cumsum(new_mat)
np.cumproduct(new_mat)
np.unique(new_mat)

arr = np.arange(1,10)

for value in arr:
	print(value)

for index,value in enumerate(arr):
	print(index,value)

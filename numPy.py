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

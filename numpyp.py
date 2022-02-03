import numpy as np

a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
print(a.ndim) 
print(a.size)
print(a[0], a[1], a[2]) 
a[0] = 5
print(a)

c = np.array([[1, 2, 3], [4, 5, 6]]) 
print(c.shape)                       
print(c.size)                        
print(c[0, 0], c[0, 1], c[1, 0])   

#NumPy arrays are designed for numerical (vector/matrix) operations, while lists are for more general purposes
l = [1, 2, 3] 
i = np.array([l, [3, 4, 5], l])
print(i)

# Define a malformed matrix. Note the third row contains 3 elements, while other rows contain 2 elements
a= np.array([[1,2],[3,4]])
print(a*2)

b = np.array([[1, 2], [3, 4], [5, 6, 7]])
print(b*2)

  # Define an array of all zeros
a=np.zeros((3,3))
print(a)

a=np.ones((1,3))
print(a)

a=np.full((2,2),10)
print(a)
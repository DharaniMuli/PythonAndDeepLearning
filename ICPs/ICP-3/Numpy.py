import numpy as np

# Create a random vector of size 15
# randomArray1 = np.random.random(15)

# Generate an array with random 15 integer numbers
# randomArray2= np.random.random_integers(15)


# Create a random vector of size 15 with range 1-20
# randonArray3 = np.linspace(1,20,15,endpoint=True,retstep=False)
# print("Original value",randonArray3)
# randonArray3[randonArray3.argmax()]=0
# print("Maximum value replaced by 0:",randonArray3)

# numpy.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None, axis=0)


# randomvale= np.random.random_integers(1, 20,15)   -- this is deprecated

randomvale= np.random.randint(1, 20,15)
print(randomvale)
randomvale[randomvale.argmax()]=0
print(randomvale)

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





#Generating 15 Random numbers bwtween 1to20
randomvale= np.random.randint(1, 20,15)

# Converting one dimentional to multi dimentional
reshaapping=randomvale.reshape(3,5)
print(reshaapping)

# Finding the max value and replacing with zero
numzero=np.where(reshaapping==np.amax(reshaapping,axis=1,keepdims=True),0,reshaapping)

print(numzero)




import numpy as np

"""
Histogram: Represents the frequency of data distribution

ex: {11,20,5,1,7,15,25,35} , we divide this in to bins of 1-10 , 10-20, ...

then we count how many values fall under each bin 
"""

a = np.random.randint(0, 50, 20)
print(f"Random vector\n{a}\n")

print(
    f"Histogram of above\n{np.histogram(a, bins=[0,10,20,30,40,50])}"
)  # 0-10, 10-20,...

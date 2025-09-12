import numpy as np

"""
Histogram: Represents the frequency of data distribution

ex: {11,20,5,1,7,15,25,35} , we divide this in to bins of 1-10 , 10-20, ...

then we count how many values fall under each bin 
"""

a = np.random.randint(0, 50, 20)
print(f"Random vector\n{a}\n")

print(
    f"Histogram of above\n{np.histogram(a, bins=[0,10,20,30,40,50])}\n"
)  # 0-10, 10-20,...


"""
Corelation: Basically tells how corelated two quantites are. Lets say no. of years of experience is corelated to how much one's salary could be.

Lies between -1 to 1. If its 0 then there is no Corelation.
"""

salary = np.array([25000, 40000, 20000, 35000, 60000])
experience = np.array([1, 3, 2, 4, 2])

print(f"salary\n{salary}\n")
print(f"experience\n{experience}\n")
print(f"{np.corrcoef(salary,experience)}")

import numpy as np 

def forward_difference(f, x, h):
    
    return (f(x + h) - f(x)) / h 

def backward_difference(f, x, h):
    
    return (f(x) - f(x - h)) / h


f1 = lambda x: x**3 + 2*x**2 - 5*x + 7 
f2 = lambda x: np.exp(x)  

x1, h1 = 2, 0.1  
x2, h2 = 1, 0.01  

forward_result = forward_difference(f1, x1, h1)
backward_result = backward_difference(f2, x2, h2)


print(f"Forward Difference at x={x1} with h={h1}: {forward_result}")
print(f"Backward Difference at x={x2} with h={h2}: {backward_result}")

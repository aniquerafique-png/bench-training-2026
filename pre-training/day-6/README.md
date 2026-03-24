# Day 6: Neural Networks - Forward Propagation

## What does each weight represent?
Weights control how much each input affects the output.  
Large weights = strong influence, small weights = weak influence.  
Negative weights push the result in the opposite direction.

## What does the bias do?
Bias is an extra value added to the weighted sum.  
It helps shift the output and gives the neuron more flexibility, even when inputs are zero.

## ReLU vs Sigmoid

**ReLU:**
- Outputs 0 for negative values, otherwise keeps the value  
- Fast and good for hidden layers  

**Sigmoid:**
- Outputs values between 0 and 1  
- Useful for probability-like outputs  

**Difference:**  
ReLU is better for learning patterns, sigmoid is better for final outputs.

## Forward Propagation
Forward propagation is how data moves through the network.

- Input → first layer  
- First layer → next layer  
- Continue until final output  

The network produces a result based on current weights and biases.

## What’s Missing for Learning?
Right now, the network doesn’t learn because weights are fixed.

To learn, it needs:
- Loss function (measure error)  
- Backpropagation (find mistakes)  
- Weight updates (improve results)  

**Process:**
1. Predict  
2. Compare with actual  
3. Calculate error  
4. Update weights  
5. Repeat
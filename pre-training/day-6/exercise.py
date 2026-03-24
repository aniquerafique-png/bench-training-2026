import math

def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

class Neuron:
    def __init__(self, weights, bias, activation="relu"):
        self.weights = weights
        self.bias = bias
        self.activation = activation

    def forward(self, inputs):
        total = 0
        for w, x in zip(self.weights, inputs):
            total += w * x
        total += self.bias

        if self.activation == "sigmoid":
            return sigmoid(total)
        else:
            return relu(total)

class DenseLayer:
    def __init__(self, n_inputs, n_neurons, weights, biases, activation="relu"):
        self.neurons = []

        for i in range(n_neurons):
            neuron = Neuron(weights[i], biases[i], activation)
            self.neurons.append(neuron)

    def forward(self, inputs):
        outputs = []
        for neuron in self.neurons:
            outputs.append(neuron.forward(inputs))
        return outputs

weights1 = [
    [0.2, -0.5, 0.1],
    [0.7, 0.3, -0.3],
    [0.4, 0.1, 0.6],
    [-0.2, 0.8, 0.5]
]
biases1 = [0.1, -0.2, 0.05, 0.3]

layer1 = DenseLayer(3, 4, weights1, biases1, activation="relu")

weights2 = [
    [0.3, -0.1, 0.2, 0.5],
    [-0.4, 0.6, -0.2, 0.1]
]
biases2 = [0.2, -0.1]

layer2 = DenseLayer(4, 2, weights2, biases2, activation="sigmoid")

input_data = [0.5, -0.3, 0.8]

output1 = layer1.forward(input_data)
output2 = layer2.forward(output1)

print("Layer 1 Output:", output1)
print("Final Output:", output2)
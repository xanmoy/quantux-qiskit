#     A simple implementation of the quantum search algorithm using Qiskit. The code is divided into four main steps: 
    
#     Initialize all qubits in superposition 
#     Apply the Oracle 
#     Apply the Diffusion Operator 
#     Measure the qubits 
    
#     The code uses the  Aer  simulator to run the quantum circuit and display the result. 
#     The result is displayed as a histogram showing the probabilities of measuring each possible state.

#     The quantum search algorithm is a quantum algorithm that can be used to search an unsorted database faster than classical algorithms.
#     It is based on Grover's algorithm, which can be used to search a list of N items in O(√N) time complexity.
#     The algorithm works by amplifying the amplitude of the target state (the solution) and reducing the amplitude of the other states through a series of operations.
#     The Oracle operation marks the target state, and the Diffusion Operator amplifies the target state and reduces the other states.
#     By repeating these operations multiple times, the algorithm converges to the target state, allowing for efficient search.
#     The quantum search algorithm has applications in various fields, such as optimization, cryptography, and machine learning.
#     Qiskit is an open-source quantum computing framework that provides tools and libraries for developing quantum algorithms and applications.
#     The code demonstrates a simple implementation of the quantum search algorithm using Qiskit, showing the steps involved in the algorithm and how to run a quantum circuit to perform the search.
#     The code uses the Aer simulator to simulate the quantum circuit and display the result as a histogram showing the probabilities of measuring each possible state.
#     The quantum search algorithm is a fundamental quantum algorithm that showcases the power of quantum computing in solving specific problems more efficiently than classical algorithms.

from qiskit import QuantumCircuit, Aer, transpile, assemble, execute
from qiskit.visualization import plot_histogram
import numpy as np

# Number of qubits (for 4 items, we need 2 qubits)
n = 2  

# Create a quantum circuit
qc = QuantumCircuit(n)

# Step 1: Initialize all qubits in superposition
qc.h(range(n))

# Step 2: Oracle (assume we mark |11⟩ as the solution)
qc.cz(0, 1)  # Phase flip |11⟩

# Step 3: Diffusion Operator
qc.h(range(n))
qc.x(range(n))
qc.cz(0, 1)  # Flip the sign of |00⟩
qc.x(range(n))
qc.h(range(n))

# Step 4: Measurement
qc.measure_all()

# Run the quantum circuit
simulator = Aer.get_backend('aer_simulator')
tqc = transpile(qc, simulator)
qobj = assemble(tqc)
result = simulator.run(qobj).result()
counts = result.get_counts()

# Display the result
print(counts)
plot_histogram(counts)
    
    
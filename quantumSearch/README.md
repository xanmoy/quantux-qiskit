# Quantum Search Algorithm (Grover's Algorithm) Implementation

## Overview

This project demonstrates an implementation of Grover's Quantum Search Algorithm using Qiskit, showcasing the power of quantum computing in solving search problems more efficiently than classical algorithms.

## 🔬 Algorithm Concept

Grover's algorithm provides a quadratic speedup for searching an unsorted database, reducing the time complexity from O(N) in classical search to O(√N) in quantum search.

### Key Features
- Searches an unsorted database with O(√N) time complexity
- Demonstrates quantum amplitude amplification
- Provides a probabilistic search mechanism

## 🚀 Technical Details

### Algorithm Steps
1. **Superposition Initialization**: Create an equal superposition of all possible states
2. **Oracle Marking**: Identify the target state
3. **Diffusion Operator**: Amplify the amplitude of the target state
4. **Measurement**: Retrieve the most likely solution

## 📦 Prerequisites

- Python 3.8+
- Qiskit
- NumPy
- Matplotlib

## 🛠 Installation

```bash
python3 -m venv quantum_env
source quantum_env/bin/activate
pip install qiskit[visualization] numpy matplotlib
```

## 💻 Usage

```python
# Run the quantum search algorithm
python main.py
```

## 🧮 Mathematical Insight

The algorithm works by:
- Initializing qubits in superposition
- Marking the target state via phase inversion
- Amplifying the target state's probability
- Repeating amplification steps optimally

## 🔍 Limitations

- Works best for small to medium-sized search spaces
- Requires precise quantum circuit construction
- Probabilistic nature means not 100% guaranteed to find the solution

## 📚 References
- Grover's original paper (1996)
- Nielsen & Chuang's Quantum Computation and Quantum Information
- Qiskit Documentation

## 🌐 Potential Applications
- Database searching
- Optimization problems
- Cryptanalysis
- Machine learning

## 🧪 Experimental Notes
- The implementation uses a 2-qubit system
- Target state is hardcoded as |11⟩
- Simulation performed using Qiskit Aer

## 🔬 Future Improvements
- Generalize oracle for different target states
- Implement for larger qubit systems
- Add more robust error handling

## 📝 License
MIT License

## 👥 Contributors
- Tanmoy Ganguly
- Open to community contributions!
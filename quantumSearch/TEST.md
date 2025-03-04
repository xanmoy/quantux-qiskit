# Quantum Search with Qiskit

This project demonstrates Grover's algorithm for quantum search using Qiskit. Grover's algorithm provides a quadratic speedup over classical search algorithms for unstructured databases.

## Prerequisites
Ensure you have Python 3 installed. It is recommended to use a virtual environment.

### Install Python Virtual Environment (If Not Installed)
For Debian/Ubuntu:
```bash
sudo apt install python3.12-venv
```

## Setup
### 1. Clone the Repository
```bash
git clone https://github.com/xanmoy/quantux-cs-0079.git
cd quantux-cs-0079
cd quantumSearch
```

### 2. Create and Activate Virtual Environment
```bash
python3 -m venv qiskit_env
source qiskit_env/bin/activate  # Linux/macOS
```
For Windows (Command Prompt):
```cmd
qiskit_env\Scripts\activate
```
For Windows (PowerShell):
```powershell
.\qiskit_env\Scripts\Activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

## Running the Quantum Search Algorithm
Execute the Python script to run the Grover search algorithm simulation:
```bash
python quantum_search.py
```

## Expected Output
The script will simulate the quantum search and display a histogram showing the most probable quantum state corresponding to the correct answer.

## Dependencies
- Python 3
- Qiskit
- NumPy
- Matplotlib (for visualization)

## License
This project is licensed under the MIT License.

## Author
**Tanmoy Ganguly**


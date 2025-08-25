import numpy as np
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_bloch_multivector, visualize_transition
import matplotlib.pyplot as plt

# Target state: cos(θ/2)|0⟩ + sin(θ/2)|1⟩ with α = √3/2, β = 1/2
theta =73.73 #2 * np.arccos(np.sqrt(3)/2) #modify alpha value based on your desired superposition


# Build the circuit using Ry to create the state instead of initialize
qc = QuantumCircuit(1)
qc.ry(theta, 0)  # Creates the desired superposition
qc.x(0)          # Apply Pauli-X gate  (we can replace x with y or z to see the working of pauli Y and Z gates)

# Simulate and visualize
backend = Aer.get_backend("statevector_simulator")
compiled = transpile(qc, backend)
result = backend.run(compiled).result()
state = result.get_statevector()

# Plot Bloch sphere
plot_bloch_multivector(state)
plt.show()

# Visualize the state transition (this will now work!)
visualize_transition(qc)

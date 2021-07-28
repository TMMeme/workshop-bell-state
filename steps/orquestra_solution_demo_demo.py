from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from zquantum.core import circuits
from zquantum.core.utils import create_object
from zquantum.core.bitstring_distribution
import yaml

def main(backend_specs):
    n=3
    q=QuantumRegister(n)
    c=ClassicalRegister(n)
    circuit=QuantumCircuit(q, c)

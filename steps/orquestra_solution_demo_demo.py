from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from zquantum.core import circuits
from zquantum.core.utils import create_object
from zquantum.core.bitstring_distribution
import yaml

def main(backend_specs):
    n=3
    q=QuantumRegister(n)
    c=ClassicalRegister(n)
    qc=QuantumCircuit(q, c)

    qc.h(q[0])
    qc.cnot(q[0], q[1])
    qc.cnot(q[0], q[2])
    
    zap_circuit=create_object.import_from_qiskit(qc)
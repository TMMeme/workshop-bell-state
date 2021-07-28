from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from zquantum.core import circuits
from zquantum.core.utils import create_object
from zquantum.core.bitstring_distribution import save_bitstring_distribution
import yaml

def main(backend_specs):
    n=3
    q=QuantumRegister(n)
    c=ClassicalRegister(n)
    qc=QuantumCircuit(q, c)

    qc.h(q[0])
    qc.cnot(q[0], q[1])
    qc.cnot(q[0], q[2])
    
    zap_circuit=circuits.import_from_qiskit(qc)

    if isinstance(backend_specs, str):
        backend_specs_dict=yaml.load(backend_specs, Loader=yaml.SafeLoader)
    else:
        backend_specs_dict=backend_specs
    backend=create_object(backend_specs_dict)

    distribution=backend.get_bitstring_distribution(zap_circuit)

    save_bitstring_distribution(distribution, "output-distribution.json")
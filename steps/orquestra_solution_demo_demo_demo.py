from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from yaml.loader import SafeLoader
from zquantum.core import circuits
from zquantum.core.utils import create_object
from zquantum.core.bitstring_distribution import save_bitstring_distribution
import yaml

def main(backend_specs):
    q = QuantumRegister(4)
    c = ClassicalRegister(4)
    qc = QuantumCircuit(q, c)
 
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])

    qc.x(q[3])
    qc.h(q[3])
    qc.cnot(q[0], q[3])
    qc.cnot(q[1], q[3])
    qc.cnot(q[2], q[3])
    
    
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])

    zap_circuit=circuits.import_from_qiskit(qc)

    if isinstance(backend_specs, str):
        backend_specs_dict=yaml.load(backend_specs, Loader=yaml.SafeLoader)
    else:
        backend_specs_dict=backend_specs
    backend=create_object(backend_specs_dict)


    distribution=backend.get_bitstring_distribution(zap_circuit)
    save_bitstring_distribution(distribution, "output-distribution.json")
    
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, circuit
from yaml.loader import SafeLoader
from zquantum.core import circuits
from zquantum.core.utils import create_object
from zquantum.core.bitstring_distribution import save_bitstring_distribution
import yaml

def main(backend_specs):
    q=QuantumRegister(3)
    c=ClassicalRegister(3)
    circuit=QuantumCircuit(q, c)

    circuit.h(q[0])
    circuit.cnot(q[0], q[1])
    circuit.cnot(q[0], q[2])

    zap_circuit=circuits.import_from_qiskit(circuit)

    if isinstance(backend_specs, str):
        backend_specs_dict=yaml.load(backend_specs, Loader=yaml.SafeLoader)
    else:
        backend_specs_dict=backend_specs
    backend=create_object(backend_specs_dict)


    distribution=get_bitstring_distribution(backend)
    save_bitstring_distribution(distribution, "output-distribution.json")
    
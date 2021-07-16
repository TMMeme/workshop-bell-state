from qiskit import ClassicalRegister, QuantumRegister, QuantumCircuit
from zquantum.core import circuits
from zquantum.core.utils import create_object

from zquantum.core.bitstring_distribution import save_bitstring_distribution

import yaml

def main(backend_specs):
    circuit=QuantumCircuit(2,2)
    circuit.h(0)
    circuit.cx(0,1)

    zap_circuit=circuits.import_from_qiskit(circuit)

    if isinstance(backend_specs, str):
        backend_specs_dict=yaml.load(backend_specs, Loader=yaml.SafeLoader)
    else:
        backend_specs_dict=backend_specs
    backend=create_object(backend_specs_dict)

    distribution=backend.get_bitstring_distribution(zap_circuit)

    save_bitstring_distribution(distribution, "output-distribution.json")




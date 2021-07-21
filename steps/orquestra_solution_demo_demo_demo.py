from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit
from yaml.loader import SafeLoader
from zquantum.core import circuits
from zquantum.core.utils import create_object
from zquantum.core.bitstring_distribution import save_bitstring_distribution
import yaml

def main(backend_specs):
    #ドイチジョサアルゴリズムを設計
    n=4
    q = QuantumRegister(n)
    c = ClassicalRegister(n)
    qc = QuantumCircuit(q, c)
    
    for i in range(n-1):
        qc.h(q[i])

    qc.x(q[n-1])
    qc.h(q[n-1])

    for j in range(n-1):
        qc.cnot(q[j], q[n-1])

    for k in range(n-1):
        qc.h(q[k])
    #グローバーアルゴリズム設計

    #q=QuantumRegister(2)
    #c=ClassicalRegister(2)
    #qc=QuantumCircuit(q,c)
    #qc.h(q[0])
    #qc.h(q[1])
    #qc.cz(q[0], q[1])
    #qc.h(q[0])
    #qc.h(q[1])
    #qc.x(q[0])
    #qc.x(q[1])
    #qc.cz(q[0], q[1])
    #qc.x(q[0])
    #qc.x(q[1])
    #for i in range(2):
    #    qc.h(i)
    #qc.h(q[0])
    #qc.h(q[1])の代わりにFor_in_range関数使っても大丈夫

    zap_circuit=circuits.import_from_qiskit(qc)

    if isinstance(backend_specs, str):
        backend_specs_dict=yaml.load(backend_specs, Loader=yaml.SafeLoader)
    else:
        backend_specs_dict=backend_specs
    backend=create_object(backend_specs_dict)


    distribution=backend.get_bitstring_distribution(zap_circuit)
    save_bitstring_distribution(distribution, "output-distribution.json")
    
from qiskit import execute, Aer, ClassicalRegister, QuantumRegister, QuantumCircuit
import json

def main():
    #Define registers and circuit
    
    q=QuantumRegister(4)
    c=ClassicalRegister(4)
    qc=QuantumCircuit(q,c)

    #Creating the superposition
    qc.h(0)
    qc.h(1)
    qc.h(2)
    
    #Creating |-> state at ancilla
    qc.x(3)
    qc.h(3)

    #Creating Oracle
    qc.cx(0,3)
    qc.cx(1,3)
    qc.cx(2,3)
    
    #アダマールを入力量子ビットにかける
    qc.h(0)
    qc.h(1)
    qc.h(2)

    #measure
    qc.measure(q,c)

    #execute
    backend=Aer.get_backend("qasm_simulator")
    shots=10000
    job=execute(qc, backend=backend, shots=shots)

    result=job.result()
    counts=result.get_counts(qc)


    with open("results.json", "w") as outfile:
        json.dump(counts, outfile)  



    
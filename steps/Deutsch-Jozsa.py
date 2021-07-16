from qiskit import execute, Aer, ClassicalRegister, QuantumRegister, QuantumCircuit
import json

def main():
    #Define registers and circuit
    
    q=QuantumRegister(4)
    c=ClassicalRegister(4)
    qc=QuantumCircuit(q,c)
    #Creating the superposition
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])
    #Creating |-> state at ancilla
    qc.x(q[3])
    qc.h(q[3])
    #Creating Oracle
    qc.cx(q[0],q[3])
    qc.cx(q[1],q[3])
    qc.cx(q[2],q[3])
    #アダマールを入力量子ビットにかける
    qc.h(q[0])
    qc.h(q[1])
    qc.h(q[2])
    #measure
    qc.measure(q,c)
    result = execute(qc, Aer.get_backend("qasm_simulator"), shots=10000).result()
    counts = result.get_counts(qc)

    with open("results.json", "w") as outfile:
        json.dump(counts, outfile)  
    #execute
    #backend=Aer.get_backend("qasm_simulator")
    #shots=10000
    #job=execute(qc, backend=backend, shots=shots)
    #result=job.result()
    #counts=result.get_counts(qc)


    



    
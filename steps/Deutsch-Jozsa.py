from qiskit import execute, Aer, ClassicalRegister, QuantumRegister, QuantumCircuit
import json

def main():
    #Define registers and circuit
    n=3
    q=QuantumRegister(n+1)
    c=ClassicalRegister(n+1)
    qc=QuantumCircuit(q,c)

    #Creating the superposition
    for i in range(n):
        qc.h(i)
    
    #Creating |-> state at ancilla
    qc.x(n)
    qc.h(n)

    #Creating Oracle
    for i in range(n):
        qc.cx(i,n)
    
    #アダマールを入力量子ビットにかける
    for i in range(n):
        qc.h(i)

    #measure
    for i in range(n):
        qc.measure(i)

    #execute
    backend=Aer.get_backend('qasm_simulator')
    shots=10000
    job=execute(qc, backend=backend, shots=shots)

    result=job.result()
    counts=result.get_counts(qc)


    with open("results.json", "w") as outfile:
        json.dump(counts, outfile)  



    
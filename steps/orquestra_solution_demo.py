from qiskit import ClassicalRegister, QuantumCircuit, QuantumRegister
from zquantum.core import circuits
from zquantum.core.utils import create_object

from zquantum.core.bitstring_distribution import save_bitstring_distribution

import yaml

def main(backend_specs):
    q=QuantumRegister(2)
    c=ClassicalRegister(2)
    circuit=QuantumCircuit(q,c)
    # Define registers and circuit
    #mainはワークフローで指定するbackend_specsの関数

    # Quantum circuit starts here
    circuit.h(q[0])
    circuit.cnot(q[0],q[1])
    #ZapataOrquestraの回路の形式に変換するため，測定（measure）は取り除かないといけない
    # End quantum circuit

    #ここからOrquestraの力を使って，別のバックエンドを指定する
    #Zapata式の量子回路指定は以下のよう
    zap_circuit = circuits.import_from_qiskit(circuit)
    #from zquantum.core import circuitsでインポートした関数にqiskitで書いたcircuitをぶち込む

    #yamlファイルのstepsで指定したbackendをここで構築する
    #Pythonのisinstance()を使用すると、オブジェクトの型判定を行うことができます。
    #isinstance()とは指定したオブジェクトとクラスの結果を返す関数であり、指定したオブジェクトが指定したクラスなのかどうかをTrueかFalseで判定を行います。
    #その為、計算処理などを行う前の型チェックとしてisinstance()を使うととても便利です。

    #ここいまいちよくわかんない　
    if isinstance(backend_specs, str):
        backend_specs_dict = yaml.load(backend_specs, Loader=yaml.SafeLoader)
    else:
        backend_specs_dict = backend_specs
    backend = create_object(backend_specs_dict)
    #from zquantum.core.utils import create_objectでインポートしたcreate_object(specs: Dict, **kwargs)関数はdict型のbackend_specsをぶち込むことで，backendオブジェクトを作るのに便利
    #yamlファイルで指定したbackend_specsには、backendオブジェクトの作成に必要なモジュール名（例：qequlacs.simulator）と関数名（QulacsSimulator）に関する情報を含んでいます．

    #このbackendから計算結果であるビット列の分布を得る
    distribution = backend.get_bitstring_distribution(zap_circuit)
    
    #Qiskitでいうところのresult=execute(qc, backend).result()に非常に近い

    #get_bitstring_distribution(circuit)は引数に実行される量子回路をとり，ビット列の分布を計算できる．

    #最後に出力を保存する
    save_bitstring_distribution(distribution, "output-distribution.json")
    #Orquestraに特有な操作で，この関数によりファイルにビット列分布を保存する

    #save_bitstring_distribution(distribution: BitstringDistribution, filename: AnyPath)関数は第一引数に，計算したビット列分布を，第二引数にファイル名をとる．
    

# Como utilizar o ICP-Python

Para executar o programa é necessária a instalação de versão Python 3.6 ou maior.
Segue o link para download das diferentes versões do Python https://www.python.org/downloads

Além disso, você precisará ter instalado o pip3 (a partir da versão 3.4 do python ele já vem por padrão nas instalações
de python para Windows) para instalação dos requisitos necessários para executar o programa.

Com python e pip instalados, execute em um terminal ou no prompt de comando do Windows`, na pasta
raíz do projeto (icp-python/):
```
pip install -r requirements.txt
```

Feito isso a dependência PyQt5 já estará instalada.

Existem 2 modos de execução do programa, o primeiro é diretamente da linha de comando,
para isso vá até a pasta simulation e no terminal execute
```
python Simulator.py
```
Para executar no modo interface, vá até a pasta interface e execute o comando
```
python SimulatorInterface.py
```

# Parametrização da simulação

Se quiser mudar os parâmetros da simulação, basta entrar no arquivo config da pasta que possui
o modo de execução desejado e adicionar, remover ou editar os dispositivos já descritos no arquivo.
A estrutura do arquivo é parecida com esta:
```
{
    "devices": {
        "0": {
            "name": "ARDUINO-01",
            "host": "localhost",
            "port": 10000,
            "failure_risk": 0.5
        },
        "1": {
            "name": "ARDUINO-02",
            "host": "localhost",
            "port": 10002,
            "failure_risk": 0.1
        }
    }
}
```

Importante ressaltar que o programa assume que a porta indicada será a utilizada para comunicação TCP
o número da porta + 1 será utilizado para comunicação UDP, logo, a partir da porta 10000, para inserir novos
dispositivos sempre coloque uma porta par como port, já que a porta impar seguinte será usada para UDP.

Além disso, o programa assume que sempre existiram dispositivos a serem configurados e **não trata um arquivo
de configuração vazia**. O host também deverá ser definido como **localhost** para a realização de simulações
locais do protocolo. O atributo **failure_risk** define a probabilidade do dispositivo ter uma falha e ficar 10
segundos sem responder a nenhuma requisição.

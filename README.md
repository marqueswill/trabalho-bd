# trabalho-bd
O trabalho foi desenvolvido utilizando python

## Dependências
```
  pip install pandas
```
```
  pip install reportlab
```
```
pip install psycopg2
```
## Setup
1. Clone o repositório na sua máquina utilizando git:
```
git clone https://github.com/marqueswill/trabalho-bd
```   
2. Crie um arquivo chamado `dbConfig.json` na raiz no projeto e configure ele conforme o arquivo `dbConfig.json.example`
3. Crie uma database chamada *estoque* utilizando o PGAdmin ou o terminal. Caso queira rodar os testes criados, crie também uma database chamada *teste*

## Rodando
Na raiz do projeto, execute o seguinte comando no terminal:
```
python3 -m Programa.main
```
Para rodar os testes, execute:
```
python3 -m Programa.teste
```
Vale ressaltar que os testes resetam a database *teste* sempre que são instanciados

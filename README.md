# Pytest Conversão de Temperatura
Um projeto de estudos, utilizando pytest para realizar a cobertura de testes de uma função que converte temperaturas.

## Cenários de Teste Inclusos
Happy Path: Testa cenários de sucesso com entradas válidas.<br>
Error Handling: Testa se a função levanta as exceções corretas para entradas inválidas.

## Tecnologias Utilizadas
[Python 3.13.2](https://www.python.org/)<br>
[Pytest](https://docs.pytest.org/en/stable/)<br>

## Requisitos
Ter o Python instalado no computador.

## Instalação
1. Clone o repositório do projeto
```
git clone https://github.com/JoaoFernandoZ/pytest-converter-temperatura.git
cd pytest-converter-temperatura
```
2. Instale as dependências do Python
```
pip install -r \requirements.txt
```

## Execução dos Testes
1. Visualização dos resultados pela [CLI](https://aws.amazon.com/pt/what-is/cli/)
```
python -m pytest
```
2. Visualização dos resultados utilizando o pytest-html
```
python -m pytest --html=doc_testes.html
```
3. Visualização dos resultados utilizando o pytest--cov
```
python -m pytest --cov=. --cov-report=html
```

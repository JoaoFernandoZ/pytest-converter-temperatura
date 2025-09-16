import pytest
from conversores_temp import converter_temperatura


# --- [ Testes de Caminho Feliz (Happy Path) ] --- #

@pytest.mark.happy_path
@pytest.mark.parametrize(
    "de_temperatura, para_temperatura, valor, resultado_esperado",
    [
        # Caso 1: Kelvin para Celsius
        ("KELVIN", "CELSIUS", 50,       -223.15),
        # Caso 2: Kelvin para Fahrenheit
        ("KELVIN", "FAHRENHEIT", 50,    -369.67),

        # Caso 3: Celsius para Kelvin
        ("CELSIUS", "KELVIN", 50,       323.15),
        # Caso 4: Celsius para Fahrenheit
        ("CELSIUS", "FAHRENHEIT", 50,   122),

        # Caso 5: Fahrenheit para Celsius
        ("FAHRENHEIT", "CELSIUS", 50,   10),
        # Caso 6: Fahrenheit para Kelvin
        ("FAHRENHEIT", "KELVIN", 50,    283.15),
    ],
    ids = ["kelvin_celsius", "kelvin_fahrenheit", "celsius_kelvin", "celsius_fahrenheit", "fahrenheit_celsius", "fahrenheit_kelvin"]
)
def test_converter_temperatura_validos(de_temperatura, para_temperatura, valor, resultado_esperado):
    resultado = converter_temperatura(de_temperatura, para_temperatura, valor)

    assert resultado == pytest.approx(resultado_esperado)


# --- [ Testes de Tratamento de Erros (Error Handling) ] --- #

@pytest.mark.error_handling
@pytest.mark.parametrize(
        "de_temperatura, para_temperatura, valor, erro_esperado",
    [
        # Caso 1: Unidade inválida no primeiro paramêtro
        ("ALEX", "CELSIUS", 50,         "Escala de temperatura inválida"),
        # Caso 2: Unidade inválida no segundo paramêtro
        ("KELVIN", "IVO", 50,           "Escala de temperatura inválida"),

        # Caso 3: Temperatura Kelvin negativa
        ("KELVIN", "FAHRENHEIT", -1,    "Temperatura em KELVIN não pode ser negativa"),
    ],
    ids = ["unidade1_invalida", "unidade2_invalida", "kelvin_negativo"]
)
def test_converter_temperatura_valores_invalidos(de_temperatura, para_temperatura, valor, erro_esperado):
    with pytest.raises(ValueError, match=erro_esperado):
        converter_temperatura(de_temperatura, para_temperatura, valor)


@pytest.mark.error_handling
@pytest.mark.parametrize(
        "de_temperatura, para_temperatura, valor, erro_esperado",
    [
        # Caso 1: Unidade do tipo 'lista' no primeiro paramêtro
        (["KELVIN"], "CELSIUS", 50,         "As unidades devem ser textos em string"),
        # Caso 2: Unidade do tipo 'int' no segundo paramêtro
        ("FAHRENHEIT", 1298, 50,            "As unidades devem ser textos em string"),  

        # Caso 3: Temperatura do tipo 'string'
        ("FAHRENHEIT", "KELVIN", "50",      "O valor passado deve ser numérico"),
    ],
    ids = ["unidade1_lista", "unidade2_int", "temperatura_string"]
)
def test_converter_temperatura_tipos_invalidos(de_temperatura, para_temperatura, valor, erro_esperado):
    with pytest.raises(TypeError, match=erro_esperado):
        converter_temperatura(de_temperatura, para_temperatura, valor)
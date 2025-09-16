def converter_temperatura(de_temperatura: str, para_temperatura: str, valor: int|float):
    unidades = ("KELVIN","CELSIUS","FAHRENHEIT")

    if not all(isinstance(unidade, str) for unidade in (de_temperatura, para_temperatura)):
        raise TypeError("As unidades devem ser textos em string")
    elif not (de_temperatura.upper() in unidades and para_temperatura.upper() in unidades):
        raise ValueError("Escala de temperatura inválida")
    elif not isinstance(valor, (int, float)):
        raise TypeError("O valor passado deve ser numérico")
    elif de_temperatura.upper() == "KELVIN" and valor < 0:
        raise ValueError("Temperatura em KELVIN não pode ser negativa")
    
    de_temperatura = de_temperatura.upper()
    para_temperatura = para_temperatura.upper()

    if de_temperatura == "CELSIUS":
        match para_temperatura:
            case "KELVIN":
                return valor + 273.15
            case "FAHRENHEIT":
                return (valor * 1.8) + 32
    elif de_temperatura == "FAHRENHEIT":
        match para_temperatura:
            case "CELSIUS":
                return (valor - 32) / 1.8
            case "KELVIN":
                return ((valor - 32) * (5/9)) + 273.15
    elif de_temperatura == "KELVIN":
        match para_temperatura:
            case "CELSIUS":
                return valor - 273.15
            case "FAHRENHEIT":
                return (valor - 273.15) * 1.8 + 32
            
    return valor
def origin_destiny_equals(origin, destiny, errors_list):
    """
    função que verifica se o campo de origem e destino possuem os valores iguais

    Args:
        origin (string): Um local de origem
        destiny (string): Um local de destino
        errors_list (dict): dicionário de erros
    """
    if origin == destiny:
        errors_list['destiny'] = 'Origem e Destino não podem ser iguais.'

def has_number(value, name, errors_list):
    """
    função que verifica se o campo possui algum carácter numérico

    Args:
        value (string): Um local de origem ou destino
        name (string): nome do campo que está sendo preenchido
        errors_list (dict): dicionário de erros
    """
    if any(char.isdigit() for char in value):
        errors_list[name] = 'Não inclua números neste campo.'
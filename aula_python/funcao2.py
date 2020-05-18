# sum -> soma
# len -> tamanho
"""
def soma(numero_1, numero_2):
    return numero_1 + numero_2

def media(lista_de_numeros):
    return sum(lista_de_numeros) / len(lista_de_numeros)
"""

def imprime_relatorio(nome, cpf, telefone):
    return f"""
    Relatório parcial

    {nome}, portador do cpf {cpf}, que usa o número {telefone}

    Esta oficialmente de férias

    Ass. Direção
    """
    print(imprime_relatorio('Paulo Roberto', 23458901, 1199999))

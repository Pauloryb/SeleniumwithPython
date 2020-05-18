

def imprime_relatorio(pessoa):
    return f"""
    Relatório parcial

    {pessoa['nome']},
    portador do cpf {pessoa['cpf']},
    que usa o número {pessoa['telefone']}

    Esta oficialmente de férias

    Ass. Direção
    """
    print(imprime_relatorio('Paulo Roberto', 23458901, 1199999))

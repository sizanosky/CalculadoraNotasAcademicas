from main import alunos

# 1 Função = obter média das notas.
def obter_media(notas):
    """
    - Função para obter a média aritmética das notas de um aluno(lista).
    :param notas: Lista com todas as notas (provas, trabalhos, laboratório).
    :return: Média de todas as notas informadas.
    """
    total_soma = float(sum(notas))  # total_soma = float(total_soma)
    return total_soma / len(notas)


# 2 Função = média com base nos pesos.
def calcula_media_total(aluno):
    """
    - Função para calcular a média final por tipo / peso.
    :param aluno: Dicionário com os dados do aluno.
    :return: Média final com base nos pesos.
    """
    trabalhos = obter_media(aluno['trabalhos'])
    provas = obter_media(aluno['provas'])
    laboratorio = obter_media(aluno['laboratorio'])

    # 25% trabalhos
    # 55% provas
    # 20% laboratório

    return (trabalhos * 0.25) + (provas * 0.55) + (laboratorio * 0.20)


# 3 Função = atribuir a letra das notas.
def atribuir_letra_nota(nota_final_aluno):
    """
    - Função para atribuir um letra(conceito) de acordo com a nota final.  
    :param nota_final_aluno: Nota final do aluno.
    :return: Letra (conceito)
    """
    if nota_final_aluno >= 90:
        return "A"

    elif nota_final_aluno >= 80:
        return "B"

    elif nota_final_aluno >= 70:
        return "C"

    elif nota_final_aluno >= 60:
        return "D"

    else:
        return "F"


# 4 Função = obter média da classe.
def media_classe():
    """
    - Função para calcular a média final da classe/turma.
    :return: Média final classe/turma.
    """
    resultado_lista = []

    for aluno, detalhes in alunos.items():
        media_aluno = calcula_media_total(alunos[aluno])
        resultado_lista.append(media_aluno)

    return obter_media(resultado_lista)

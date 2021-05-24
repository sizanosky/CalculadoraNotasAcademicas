"""
* Módulo 20 - Calculadora de notas acadêmicas
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 23/05/2021
* Programa em Python 3 para calcular notas acadêmicas.
"""

from helpers import *

print("Hello World!")

if __name__ == "__main__":
    print("\n+=+=+=+ Calculadora de notas acadêmicas +=+=+=+\n")
    print(f"{50 * '*'}")

    # for looping no dicionário alunos para calcular as suas respectivas notas.
    for aluno, detalhes in dados.alunos.items():

        media_final_aluno = round(calcula_media_total(dados.alunos[aluno]), 2)

        # Imprime os dados do aluno.
        print(f"Aluno: {(dados.alunos[aluno]['nome'].title())}")
        print(f"Média final: {media_final_aluno}")
        print(f'Conceito nota: "{atribuir_letra_nota(media_final_aluno)}"')
        print(f"{50 * '*'}")

    # Calcula a média geral da classe/turma.
    media_classe = media_classe()

    # Imprime a média geral da classe/turma.
    print(f"\n{50 * '#'}")
    print(f"Media geral classe/turma: {round(media_classe, 2)}")
    print(f"Conceito geral classe/turma: {atribuir_letra_nota(media_classe)}")
    print(f"{50 * '#'}")

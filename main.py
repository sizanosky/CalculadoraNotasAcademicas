"""
* Módulo 20 - Calculadora de notas acadêmicas
* Criado por Marcos Fabricio Sizanosky
* Professor: Jefferson Santos
* Data criação: 23/05/2021
* Programa em Python 3 para calcular notas acadêmicas.
"""
print("Hello World!")

# "Banco de dados"
alunos = {
    "marcosfs": {
        "nome": "Marcos Fabricio Sizanosky",
        "trabalhos": [90, 95, 80, 100],
        "provas": [90, 80],
        "laboratorio": [70, 85.2]
    },
    "jeffersons": {
        "nome": "Jefferson Santos",
        "trabalhos": [70, 95, 60, 100],
        "provas": [90, 60],
        "laboratorio": [70, 55.2]
    },
    "mariacbs": {
        "nome": "maria clara bruske sizanosky",
        "trabalhos": [77, 82, 23, 39],
        "provas": [80, 60],
        "laboratorio": [70, 44.53]
    },
    "lucasbs": {
        "nome": "lucas bruske sizanosky",
        "trabalhos": [67, 55, 77, 21],
        "provas": [80, 60],
        "laboratorio": [69, 44.56]
    },
    "priscilabs": {
        "nome": "priscila bruske da silva",
        "trabalhos": [95, 89, 90, 86],
        "provas": [65, 56],
        "laboratorio": [50, 44.6]
    },
}

if __name__ == "__main__":
    print("\n+=+=+=+ Calculadora de notas acadêmicas +=+=+=+")

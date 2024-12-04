from entrada import *

def cadastrar_aluno(id):
    print("\n--- Cadastro de Aluno ---")
    nome = input("Nome do aluno: ").strip()
    idade = ler_inteiro("Idade do aluno: ", pos=True)
    peso = ler_real("Peso (kg): ", pos=True)
    altura = ler_real("Altura (m): ", pos=True)
    imc = round(peso / (altura ** 2), 2)
    return {
        "id": id,
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "imc": imc
    }

def imprimir_alunos(alunos):
    print("\n--- Lista de Alunos ---")
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    
    for aluno in alunos:
        print(f"ID: {aluno['id']} | Nome: {aluno['nome']} | Idade: {aluno['idade']} | "
              f"Peso: {aluno['peso']}kg | Altura: {aluno['altura']}m | IMC: {aluno['imc']}")

def buscar_aluno_por_id(alunos, id_busca):
    return next((aluno for aluno in alunos if aluno["id"] == id_busca), None)

def imprimir_dados_aluno(aluno):
    print("\n--- Dados do Aluno ---")
    print(f"ID: {aluno['id']}")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']} anos")
    print(f"Peso: {aluno['peso']} kg")
    print(f"Altura: {aluno['altura']} m")
    print(f"IMC: {aluno['imc']}")

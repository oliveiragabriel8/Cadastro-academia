import json
from aluno import *
from entrada import *
from navegabilidade import *

# Variáveis de controle dos dados na memória
id = 1
""" 
Número do ID de autoincremento.
"""

alunos = []
""" 
Lista de dicionários que armazena as abstrações de alunos.
"""

def salvar_dados(alunos, arquivo="alunos.json"):
   
    with open(arquivo, "w") as f:
        json.dump(alunos, f, indent=4)
    print("Dados salvos com sucesso!")

def carregar_dados(arquivo="alunos.json"):
  
    global id
    try:
        with open(arquivo, "r") as f:
            dados = json.load(f)
            if dados:
                id = max(aluno["id"] for aluno in dados) + 1 
            return dados
    except FileNotFoundError:
        return []  

alunos = carregar_dados()

def main():
  
    global id
    while True:
        imprimir_cabecalho()
        exibir_menu()
        opc = ler_inteiro("Opção: ")

        # Navegabilidade
        if opc == 1:
            # Função lê os dados de um aluno e retorna um dicionário.
            # Dicionário é adicionado à lista de alunos.
            aluno = cadastrar_aluno(id)
            alunos.append(aluno)
            id += 1
        elif opc == 2:
            #função imprime todos os alunos em tela
            imprimir_alunos(alunos)
        elif opc == 3:
            # Busca um aluno por ID e apresenta seus dados se existir
            id_busca = ler_inteiro("Digite o ID do aluno: ", pos=True)
            aluno = buscar_aluno_por_id(alunos, id_busca)
            if aluno:
                imprimir_dados_aluno(aluno)
            else:
                print("Aluno não encontrado.")
        elif opc == 4:
            # Exibe uma lista com todos os alunos filtrados por IMC
            imc_min = ler_real("IMC mínimo: ", pos=True)
            imc_max = ler_real("IMC máximo: ", pos=True)
            filtrados = filtrar_alunos_por_imc(alunos, imc_min, imc_max)
            imprimir_alunos(filtrados)
        elif opc == 5:
            # Salva os dados e pergunta se deseja sair do programa.
            salvar_dados(alunos)
            print("Saindo...")
            break
        else:
          
            print("Opção inválida!")

     
        limpar_tela()

if __name__ == "__main__":
    main()

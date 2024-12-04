import os

def imprimir_cabecalho():
    """
    Imprime o cabeçalho do programa.
    """
    cabecalho = """
****************************************************************
*                                                              *
*                         SysFitness                           *
*                                                              *
*                                       powered by: SI - FB 23 *
****************************************************************
"""
    print(cabecalho)

def exibir_menu():
    """
    Exibe o menu principal do programa.
    """
    menu = """
 1 - Cadastrar aluno
 2 - Imprimir cadastros
 3 - Buscar aluno por ID
 4 - Filtrar alunos por IMC
 5 - Salvar e sair
 -------------------------------
"""
    print(menu)

def limpar_tela():
    """
    Limpa a tela do terminal, independentemente do sistema operacional.
    """
    input("----------\nPressione 'ENTER' para continuar...")
    comando = "cls" if os.name == "nt" else "clear"
    os.system(comando)

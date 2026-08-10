import json
import time
def carregar_tarefas():
    try:
        with open("teste.json", "r") as arquivo:
            tarefas = json.load(arquivo)
        return(tarefas)
    except:
        return[]
    
def salvar_tarefas(listas_para_salvar):
    with open("teste.json", "w") as arquivo:
        json.dump(listas_para_salvar, arquivo, indent=4)
        print("Dados salvos com sucesso!")

minhas_tarefas = carregar_tarefas() 

while True:
    print("\n=== GERENCIADOR DE TAREFAS ===")
    print("1. Listar Tarefas")
    print("2. Adicionar Tarefa")
    print("3. Concluir Tarefa")
    print("4. Sair")
    
    opcao = input("Escolha uma opção: ")
    if opcao == "1":
        for i, tarefas in enumerate(minhas_tarefas):
            print(f"{i} - tarefas {tarefas['tarefa']} | Conclúida: {tarefas['concluida']}")
            pass    
    elif opcao == "2":
        nova_tarefa = input("Digite o nome da nova tarefa: ")
        minhas_tarefas.append({"tarefa": nova_tarefa, "concluida": False})
        salvar_tarefas(minhas_tarefas)
        pass
    elif opcao == "3":
        for i, tarefas in enumerate(minhas_tarefas):
            print(f"{i} - tarefas {tarefas['tarefa']} | Conclúida: {tarefas['concluida']}")
            escolha = int(input("Qual tarefa você deseja concluir?"))

    elif opcao == "4":
        print("Saindo do programa em 3 segundos....")
        time.sleep(3)
        break 
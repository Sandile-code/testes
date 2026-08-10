import json
class Aluno:
    def __init__(self, nome, idade, nota, matricula):
        self.nome = nome
        self.idade = idade
        self.nota = nota
        self. matricula = matricula

    def mostrar(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Nota: {self.nota}")
        print(f"Matrícula: {self.matricula}")
        print(f"Status: {self.status()}")

    def status(self):
        if self.nota >= 7:
            return "Aprovado"
        
        return "Reprovado"

    def alterar_nota (self, nova_nota):
        if nova_nota >= 0 and nova_nota <= 10:
            self.nota = nova_nota
            return True
        return False

    def to_dict(self):
        return{
            "nome":self.nome,
            "idade": self.idade,
            "nota": self.nota,
            "matricula": self.matricula
        }

    @classmethod
    def from_dict(cls, dados):
        return cls(
            dados['nome'],
            dados['idade'],
            dados['nota'],
            dados['matricula']
        )


    
class Escola:
    def __init__(self):
        self.alunos = []

    def localizar_aluno(self, nome):
        for aluno in self.alunos:
            if aluno.nome.lower() == nome.lower():
               return aluno
        return None

    def cadastrar_aluno(self):
        while True:
            nome = input("Nome: ").strip()
            if nome != "":
                break
            else:
                print("Nome inválido.")

        if self.localizar_aluno_nome(nome) is not None:
            print("Já existe um aluno com esse nome.")
            return
       
        idade = self.ler_inteiro("Idade: ")
        nota = self.ler_nota("Nota: ")

        matricula = self.ler_inteiro("Matrícula: ")

        if self.localizar_aluno_rga(matricula) is not None:
            print("Já existe um aluno com esse registro.")
            return
        

        aluno = Aluno(nome, idade, nota, matricula)

        self.alunos.append(aluno)
        self.salvar_dados()

    def listar_aluno(self):
        if not self.alunos:
            print("Não existem alunos cadastrados ainda.")
            return
        else:
            for aluno in self.alunos:
                print(aluno.nome)
                print("-"*20)

    def localizar_aluno_nome(self,nome):
        for aluno in self.alunos:
            if nome.lower() == aluno.nome.lower():
                return aluno
        return None

    def localizar_aluno_rga(self,rga):
        for aluno in self.alunos:
            if rga.lower() == aluno.matricula.lower():
                return aluno
        return None
    



    def buscar_aluno(self):
        if not self.alunos:
            print("Não existem alunos cadastrados.")
            return
        else:
            nome = input("Digite o nome do aluno: ")

            aluno = self.localizar_aluno(nome)
            if aluno is None:
                print("Aluno não encontrado")
                return
            else:
                aluno.mostrar()
                return

    def ler_nota(self, mensagem):
        while True:
            try:
                nota = float(input(mensagem))

                if 0 < nota <= 10:
                    return nota
                else:
                    print("Nota inválida.")
            except ValueError:
                print("Valor informado inválido")

    def ler_inteiro(self, mensagem):
        while True:
            try:
                return int(input(mensagem))

            except ValueError:
                print("Nota inválida")
    
        
    def remover_aluno(self):
        if not self.alunos:
            print("Não existem alunos cadastrados.")
            return
        else:
            nome = input("Digite o nome do aluno: ")
            aluno = self.localizar_aluno(nome)

            if aluno is None:
                print("Aluno não encontrado.")
                return
            else:
                opcao = input("Aluno encontrado será removido, confirma? (s/n):\n")
                if opcao.lower() == "s":
                    self.alunos.remove(aluno)
                    print("Aluno removido com sucesso.")
                    self.salvar_dados()
                else:
                    print("Cancelamento da remoção.")
                    return
            print("Aluno não encontrado.")

    def alterar_nota(self):
        if not self.alunos:
            print("Não existem alunos cadastrados.")
            return
        else:
            nome = input("Digite o nome do aluno: ")
            aluno = self.localizar_aluno(nome)

            if aluno is None:
                print("Aluno não encontrado.")
                return
            else:
                nota = self.ler_nota("Nota> ")

                if aluno.alterar_nota(nota):
                    self.salvar_dados()
                    print("Nota alterada.")
                else:
                    print("Nota inválida")
              
    def calcular_media(self):
        if not self.alunos:
            print("Não existem alunos cadastrados ainda.")
            return
        else:
            media = sum(aluno.nota for aluno in self.alunos)/ len(self.alunos)
            print(f"Média geral: {media:.2f}")

    def salvar_dados(self):
        dados = []
        for aluno in self.alunos:
            dados.append(aluno.to_dict())

        with open("alunos.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, indent=4, ensure_ascii=False)

    def carregar_dados(self):
        try:

            with open("alunos.json", "r", encoding="utf-8") as arquivo:
                dados = json.load(arquivo)
                self.alunos = []
            for aluno in dados:
                self.alunos.append(Aluno.from_dict(aluno))
        except (FileNotFoundError, json.JSONDecodeError):
            self.alunos=[]
escola = Escola()
escola.carregar_dados()

menu = (" - Sistema Escolar 4.0 -"
"1 - Cadastrar aluno\n"
"2 - Listar Aluno\n"
"3 - Alterar Nota\n"
"4 - Remover aluno\n"
"5 - Média Geral\n"
"6 - Buscar aluno\n"
"7 - Sair\n")




while True:
    print(menu)
    opcao = int(input("Digite a opção do que deseja fazer: "))

    if opcao == 1:
        escola.cadastrar_aluno()
    elif opcao == 2:
        escola.listar_aluno()
    elif opcao == 3:
        escola.alterar_nota()
    elif opcao == 4:
        escola.remover_aluno()
    elif opcao == 5:
        escola.calcular_media()
    elif opcao == 6:
        escola.buscar_aluno()
    elif opcao == 7:
        break
                
        

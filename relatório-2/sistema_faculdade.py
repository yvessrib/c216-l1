alunos = []
matriculas = {}

def gerar_matricula(curso: str):
  num = matriculas.get(curso, 0) + 1
  matriculas[curso] = num
  return f"{curso}{num}"

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    email = input("Digite o e-mail do aluno: ")
    curso = input("Digite o curso do aluno: ")

    matricula = gerar_matricula(curso)

    alunos.append({
        "nome": nome,
        "email": email,
        "curso": curso,
        "matricula": matricula
    })

    print(f"Aluno {nome} cadastrado com sucesso!")

def listar_alunos():
    if not alunos:
        print("Nenhum aluno cadastrado.")
    else:
        for aluno in alunos:
            print(f"Nome: {aluno['nome']}, E-mail: {aluno['email']}, Curso: {aluno['curso']}, Matrícula: {aluno['matricula']}")

def atualizar_aluno():
    nome = input("Digite o nome do aluno a ser atualizado: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            aluno["email"] = input("Digite o novo e-mail: ")
            aluno["curso"] = input("Digite o novo curso: ")
            aluno["matricula"] = gerar_matricula(aluno["curso"])
            print("Aluno atualizado com sucesso!")
            return
    print("Aluno não encontrado.")

def remover_aluno():
    nome = input("Digite o nome do aluno a ser removido: ")
    for aluno in alunos:
        if aluno["nome"] == nome:
            alunos.remove(aluno)
            print("Aluno removido com sucesso!")
            return
    print("Aluno não encontrado.")

def main():
    while True:
        print("\nMenu de Opções:")
        print("1. Cadastrar Aluno")
        print("2. Listar Alunos")
        print("3. Atualizar Aluno")
        print("4. Remover Aluno")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_aluno()
        elif opcao == '2':
            listar_alunos()
        elif opcao == '3':
            atualizar_aluno()
        elif opcao == '4':
            remover_aluno()
        elif opcao == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
import bcrypt
import json
import os
ARQUIVO_USUARIOS = 'usuarios.json'

# Carregar usuários do arquivo
def carregar_usuarios():
    if not os.path.exists(ARQUIVO_USUARIOS):
        return {}
    with open(ARQUIVO_USUARIOS, 'r') as f:
        return json.load(f)

# Salvar usuários no arquivo
def salvar_usuarios(usuarios):
    with open(ARQUIVO_USUARIOS, 'w') as f:
        json.dump(usuarios, f, indent=4)

# Criar hash da senha
def gerar_hash_senha(senha):
    return bcrypt.hashpw(senha.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Verificar senha
def verificar_senha(senha, hash_salvo):
    return bcrypt.checkpw(senha.encode('utf-8'), hash_salvo.encode('utf-8'))

# Cadastrar novo usuário
def cadastrar():
    usuarios = carregar_usuarios()
    usuario = input("Novo usuário: ")
    if usuario in usuarios:
        print("Usuário já existe.")
        return
    senha = input("Senha: ")
    hash_senha = gerar_hash_senha(senha)
    usuarios[usuario] = hash_senha
    salvar_usuarios(usuarios)
    print("Usuário cadastrado com sucesso.")

# Fazer login
def login():
    usuarios = carregar_usuarios()
    usuario = input("Usuário: ")
    senha = input("Senha: ")
    if usuario in usuarios and verificar_senha(senha, usuarios[usuario]):
        print("Login bem-sucedido!")
    else:
        print("Usuário ou senha incorretos.")

# Menu
def menu():
    while True:
        print("\n1 - Cadastrar\n2 - Login\n3 - Sair")
        op = input("Escolha: ")
        if op == "1":
            cadastrar()
        elif op == "2":
            login()
        elif op == "3":
            break
        else:
            print("Opção inválida.")

menu()

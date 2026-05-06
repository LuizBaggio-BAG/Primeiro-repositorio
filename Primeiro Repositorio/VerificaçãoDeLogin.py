usuario_correto ="admin"

login = str(input("Digite o nome de usuario: ")).lower().strip()

if login == usuario_correto:
    print("Acesso concedido!")
else:
    print("Usuário desconhecido")
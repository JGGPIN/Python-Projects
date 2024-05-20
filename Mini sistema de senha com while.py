senha = 2002
su = int(input("Coloque a senha"))

while (su != senha):
    print("Senha inválida")
    su = int(input("Digite a senha novamente"))

print("Senha correta!")

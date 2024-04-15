nome = input("Qual seu nome?")
idade = int(input("Qual sua idade?"))

if nome == "Allan":
    print("Olá, Allan!")
elif idade < 18:
    print("Você não é o Allan! E é menor de idade")
elif idade > 100:
    print("Diferente de você, o Allan não é imortal!")
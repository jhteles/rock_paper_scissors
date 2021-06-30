while True:

    print("Pedra, papel ou tesoura?")
    acao = input()

    from random import randint
    num = (randint(1,3))

    if num == 1:
        acaoPc = "pedra"
    elif num == 2:
        acaoPc = "papel"
    elif num == 3:
        acaoPc = "tesoura"

    if acao == acaoPc:
        print("Empate!")
        
    if acao == "pedra" and acaoPc == "tesoura":
        print("Você venceu!")
    if acao == "pedra" and acaoPc == "papel":
        print("Você perdeu.")

    if acao == "papel" and acaoPc == "pedra":
        print("Você venceu!")
    if acao == "papel" and acaoPc == "tesoura":
        print("Você perdeu.")
    
    if acao == "tesoura" and acaoPc == "papel":
        print("Você venceu!")
    if acao == "tesoura" and acaoPc == "pedra":
        print("Você perdeu.")
        
    jogar_novamente = input("Jogar novamente? (s/n)")
    if jogar_novamente.lower() == "n":
        break
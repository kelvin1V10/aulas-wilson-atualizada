# import random 

# baralho = [1,2,3,4,5,6,7,8,9,10,10,10]

# def dar_cartas():
#     listaElementos = [[baralho]]
#     print(random.choice([listaElementos]))
#     print(listaElementos)

# print("\nBEM-VINDO AO 21") 

# p1 = str(input("""\nDIGITE
#                 \n[1] PARA JOGAR
#        \n[2] PARA SAIR
#        \n"""))

# p2 = 0
# if p1 == "1":
#     print("INICIANDO\n")
# while p1 != "2":
#     print("Sua carta é", random.choice(baralho))
#     while p2 != "nao":
#         p2 = str(input("Você quer mais cartas?\n"))
#         print("Sua carta é", random.choice(baralho))
#     else:
#         break
# else:
#     pass



import random

baralho = [1,2,3,4,5,6,7,8,9,10,10,10]
tracinhofofo = ('-=') * 20

print(f"{tracinhofofo}\n             BEM-VINDO AO JOGO!!!\n{tracinhofofo}")

p1 = int(input("\nDIGITE: \n[1] PARA JOGAR\n   [2] PAR SAIR\n>>> "))

p2 = total = x = 0

if p1 == "1":
    print("\nINICIANDO...")
elif p1 == "2":
    print("\nSAINDO... \n ATE MAIS :)")

    while p2 != "N":
        x = random.choice(baralho)

        total += x 

        print("\n Sua carta é", x)
        p2 = str(input("Voê quer mais carta?\n>>> ")).upper()

        if total > 21:
            print(f'\nVoê PERDEU')

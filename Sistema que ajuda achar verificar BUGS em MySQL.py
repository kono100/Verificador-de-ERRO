def gera():
    return (1)

def game():
    resposta = 'fim' or gera()


    texto=0
    while texto is not resposta:


        texto = str(input("\nQual seu texto: "))
        if texto == resposta:
               
            print("\n")
        else:



            virgula = texto.count(',')
            print('quantidade de Virgula: ',virgula)


            aspas = texto.count("'")
            print('quantidade de   aspas: ',aspas)

            '''aspas2 = texto.count('"')
            print('quantidade de aspas duplas: ',aspas2)'''


while True:
    game()
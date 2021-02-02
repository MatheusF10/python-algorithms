def partida():



    n = int(input("Quantas peças ?"))
    m = int(input('Limite de peças por jogada ? '))

    if m > n:
        print("Você não pode tirar mais peças do que a quatidade total de peças.")
        return partida()

    PCjoga = False 

    if n % (m + 1) == 0:
        print("Você começa !")
        usuario_escolhe_jogada(n, m)
        
    else:
        print("Eu começo !")
        PCjoga = True

        while n > 0:
            if PCjoga:
                ComputadorRemove = computador_escolhe_jogada(n, m)
                n = n - ComputadorRemove
                if ComputadorRemove == 1:
                    print("O computador tirou 1 peça")
                else:
                    print("O computador tirou", ComputadorRemove, "peças")
                    

                PCjoga = False

        
            else:
                jogada = usuario_escolhe_jogada(n , m)
                n = n - jogada
                if jogada == 1:
                    print("Você tirou uma peça")
                else:
                    print("Você tirou", jogada, "peças")

                PCjoga = True
                
            if n == 1:
                print("Agora resta somente uma peça no tabuleiro")

            else:
               if n != 0 :
                   print()
                   print("Agora restam,", n, "peças no tabuleiro.")
                   print()

               if n == 0 or n < m or n == 1: 
                        print("Fim do jogo ! O computador ganhou !")
                        
                       


            

           
            
            
            

def usuario_escolhe_jogada(n, m):

    print()

    print("Sua vez")

    print()

    jogadaValida = False

    while not jogadaValida:
         jogada = int(input("Quantas peças você vai retirar ?"))

   

         if jogada < m or jogada < 1 or jogada > n or jogada > m:
            print()
    
            print("digite uma jogada valida")

            print()
        
            return usuario_escolhe_jogada(n, m)

         else:
              jogadaValida = True

    
   




def computador_escolhe_jogada(n, m):
    ComputadorRemove = 1

    while ComputadorRemove != m:
        if (n - ComputadorRemove) % (m+1) == 0:
            return ComputadorRemove

        else:
            ComputadorRemove += 1

    return ComputadorRemove 

        

def campeonato ():
    
    Rodada = 1
    i = 1
    
    while Rodada <= 3:

        


        print("Rodada", Rodada)
        
        PCganha = partidacamp()
        Rodada = Rodada + i
        
 

    if Rodada <= 3:
        Rodada = Rodada
        print("O computador ganhou")
        print("Rodada" , Rodada)
        print("Placar: Você 0", "x", Rodada, "computador")
        partida()

    else:

        print()
    
        print("Placar: Você 0 x 3 computador")

        print()

        

        

        
        menu()
   

def partidacamp():

    n = int(input("Quantas peças ?"))
    m = int(input('Limite de peças por jogada ? '))

    if m > n:
        print("Você não pode tirar mais peças do que a quatidade total de peças.")
        return partidacamp()

    PCjoga = False 

    if n % (m + 1) == 0:
        print("Você começa !")
        usuario_escolhe_jogada(n, m)
        
    else:
        print("Eu começo !")
        PCjoga = True

        while n > 0:
            if PCjoga:
                ComputadorRemove = computador_escolhe_jogada(n, m)
                n = n - ComputadorRemove
                if ComputadorRemove == 1:
                    print("O computador tirou 1 peça")
                else:
                    print("O computador tirou", ComputadorRemove, "peças")
                    

                PCjoga = False

        
            else:
                jogada = usuario_escolhe_jogada(n , m)
                n = n - jogada
                if jogada == 1:
                    print("Você tirou uma peça")
                else:
                    print("Você tirou", jogada, "peças")

                PCjoga = True
                
            if n == 1:
                print("Agora resta somente uma peça no tabuleiro")

            else:
               if n != 0 :
                   print()
                   print("Agora restam,", n, "peças no tabuleiro.")
                   print()

               if n == 0 or n < m or n == 1: 
                        print("Fim do jogo ! O computador ganhou !")

                        
   

def menu ():

    print()

    print('Bem-vindo ao jogo do NIM! Escolha:')

    print()

    print('1 - para jogar uma partida isolada')

    tipoDePartida = int(input('2 - para jogar um campeonato '))

    if tipoDePartida == 2:
        print()
        print('Voce escolheu um campeonato!')
        print()
        campeonato()
    else:
        if tipoDePartida == 1:
            print()
            partida()


   






     

            


    

    

    

    
        

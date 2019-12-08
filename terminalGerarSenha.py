import os
import socket

server = '127.0.0.1'
port = 3033
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest = (server, port)

class Senha:

    n = 0
    p = 0

senha = Senha()

print(senha.n)
    
while True:
    
    print ("==========================")
    print ("====TERMINAL DE SENHAS====")
    print ("==========================")
    print ("==== Escolha o tipo ======")
    print ("1 - normal")
    print ("2 - prioridade")
    print ("==========================")

    try:
        senhas = 0
        senhas = int(input())
    except:
        print("")

    try:    
        if senhas == 1:
            senha.n += 1
            obj = 'n'
            udp.sendto(obj.encode(), dest)
            print ("Sua senha: n" + str(senha.n))
        elif senhas == 2:
            senha.p += 1
            obj = 'p'
            udp.sendto(obj.encode(), dest)
            print ("Sua senha: p" + str(senha.p))
        
        else:
            print ("Opcao invalida")

        print ("==========================")
        print ("Aguardando nova operacao .")
        print ("Pressione enter ...")
    except:
        print("")
   
        
    try:
        input()
    except:
        os.system('cls' if os.name == 'nt' else 'clear')

    os.system('cls' if os.name == 'nt' else 'clear')
udp.close()


import socket
import sys
import threading

entrada = 0
enviar = 'nada'
trigger = False


#variaveis para NORMAL
tuplaNormal = ()
countNormal = 0

#variaveis para PRIORIDADE
tuplaPrioridade = ()
countPrioridade = 0



def not_empty(any_structure):
    if any_structure:
        return True
    else:
        return False


        

#Servidor UDP
#Endereco IP do Servidor
HOST = ''
# Porta que o Servidor vai escutar
PORT= 3033
PORT2 = 3034
HOST2= '127.0.0.1'
dest = (HOST2, PORT2)
udp = socket.socket(socket.AF_INET,
socket.SOCK_DGRAM)
orig = (HOST, PORT)
udp.bind(orig)
obj = 'x'

snormal = 0
sprioridade = 0
while True:
    trigger = False
    msg = udp.recvfrom(1024)
    senharecebida = msg[0]

    if(senharecebida[0] == 110):
        snormal += 1
        tuplaNormal += (snormal,) 
        print(tuplaNormal)
    elif(senharecebida[0] == 112):
        sprioridade += 1
        tuplaPrioridade += (sprioridade,)
        print(tuplaPrioridade)


    elif(senharecebida[0] == 120):
        entrada += 1
        print(entrada)
        print(not_empty(tuplaNormal))

        try:
            if((entrada == 3) and (not_empty(tuplaPrioridade))):
                countPrioridade += 1
                obj = str((tuplaPrioridade[countPrioridade - 1])) + ' prioridade'
                entrada = 0
                udp.sendto(obj.encode(), dest) 

            elif((entrada < 3) and (not_empty(tuplaNormal))):
                countNormal += 1
                obj = str((tuplaNormal[countNormal - 1])) + ' normal'
                udp.sendto(obj.encode(), dest) 

            elif ((not_empty(tuplaPrioridade)) and (not_empty(tuplaNormal) == False)):
                countPrioridade += 1
                obj = str((tuplaPrioridade[countPrioridade - 1])) + ' prioridade'
                entrada = 0
                udp.sendto(obj.encode(), dest)

            elif ((not_empty(tuplaNormal)) and (not_empty(tuplaPrioridade) == False)):
                countNormal += 1
                obj = str((tuplaNormal[countNormal - 1])) + ' normal'
                udp.sendto(obj.encode(), dest) 

        except:
            obj = 'Aguardando ...'
            udp.sendto(obj.encode(), dest)
            tuplaPrioridade = ()
            countPrioridade = 0
            tuplaNormal = ()
            countNormal = 0
            entrada = 0
        
   
    

udp.close()
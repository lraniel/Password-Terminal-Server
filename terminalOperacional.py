import os
import socket

server = '127.0.0.1'
port = 3033
udp = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
dest = (server, port)
obj ='x'
    
while True:
    
    print ("==========================")
    print ("==== Chamar cliente  =====")
    print ("==========================")
    print ("===== Pressione ENTER ====")
    print ("==========================")
    print ("==========================")

        
    try:
        input()
        print ("== Pressione ENTER novamente para confirmar ==")
        input()
        udp.sendto(obj.encode(), dest)
        
    except:
        os.system('cls' if os.name == 'nt' else 'clear')

    os.system('cls' if os.name == 'nt' else 'clear')
udp.close()


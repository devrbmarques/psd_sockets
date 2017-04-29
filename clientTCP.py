
#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Adriano Freitas <https://adrianofreitas.me>
# Robson Marques <http://rbmarques.com.br>
#

import socket, struct
import sys, getopt, os

def banner():
    os.system('clear')
    print '#!/usr/bin/python2'
    print '# Adriano Freitas <https://adrianofreitas.me>'
    print '# Robson Marques  <http://rbmarques.com.br>'
    print '# Client Side'



def main(argv):
    # exibe autores
    banner()

    HOST = '127.0.0.1'
    PORT = 2048
    #cria socket tcp
    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #info do servidor
    dest = (HOST, PORT)
    #cria conexao
    tcp.connect(dest)

    try:
        opts, args = getopt.getopt(sys.argv[1:], "hc:v", ["help", "connect"])
    except getopt.GetoptError:
        # erro padrao, caso a opcao seja invalida
        print '\npython clientTCP.py --help\tPara exibir ajuda.'
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-v':
            verbose = True
            sys.exit()
        elif opt in ("-h", "--help"):
            banner()
            tcp.send ("help")
            sys.exit()
        elif opt in ("-c", "--connect"):
            print '\nhelp\tPara exibir ajuda.'
            print '\nDIGITE UM COMANDO: '
            cmd = raw_input()
            while cmd <> 'exit':#enquanto a msg for diferente de CTRL+x
                if cmd == 'help':
                    banner()
                    tcp.send(cmd)
                    reply = tcp.recv(1024)
                    print reply

                elif cmd == 'list':
                    banner()
                    tcp.send(cmd)
                    reply = tcp.recv(1024)
                    print reply

                elif cmd.find('status') >= 0:
                    banner()
                    tcp.send(cmd)
                    reply = tcp.recv(1024)
                    print reply

                elif cmd.find('deallocate') >= 0:
                    banner()
                    tcp.send(cmd)
                    reply = tcp.recv(1024)
                    print reply

                elif cmd.find('allocate') >= 0:
                    banner()
                    tcp.send(cmd)
                    reply = tcp.recv(1024)
                    print reply
                else:
                    print 'Comando invalido!'

                print '\nDIGITE UM COMANDO: '
                cmd = raw_input()
            sys.exit()
    tcp.close

# chama a funcao principal
if __name__ == "__main__":
    main(sys.argv[1:])

#!/usr/bin/python
# -*- coding: UTF-8 -*-
#
# Adriano Freitas <https://adrianofreitas.me>
# Robson Marques <http://rbmarques.com.br>
#

import socket
import sys, os

def banner():
    os.system('clear')
    print '#!/usr/bin/python2'
    print '# Adriano Freitas <https://adrianofreitas.me>'
    print '# Robson Marques  <http://rbmarques.com.br>'
    print '# Server Side'
    print '\n'

def ajuda():
    ajuda = "\nCOD\t\tFUNCAO\nlist   \t\tListar Salas\nstatus   \tExibir Status Salas\nallocate <N>\tReservar Sala\ndeallocate <N>\tLiberar Sala\nhelp   \t\tExibir Ajuda"
    ajuda += "\nExemplo:\n\tallocate 1\n\tdeallocate 1"
    return ajuda
def criarSala():
    matriz = []
    for i in range(5):
        linha = []
        for j in range(2):
            linha.append('Livre')
        matriz.append(linha)

    for x in range(5):
        matriz[x][0] = x+1
    return matriz

def exibirSala(matriz):
    #print 'SALA\tSTATUS'
    m = '\nSALA\tSTATUS'
    for i in range(len(matriz)):
        m += "\n0"+str(matriz[i][0])+"\t"+str(matriz[i][1])
    return str(m)

def reservarSala(matriz, sala):
    for i in range(len(matriz)):
        if matriz[i][0] == sala:
            if matriz[i][1] == 'Ocupada':
                return "Erro: Sala Ocupada"
            else:
                matriz[i][1] = 'Ocupada'
                return "Sucesso: Sala reservada"

def liberarSala(matriz, sala):
    for i in range(len(matriz)):
        if matriz[i][0] == sala:
            if matriz[i][1] == 'Livre':
                return "Erro: Sala ja esta livre"
            else:
                matriz[i][1] = 'Livre'
                return "Sucesso: Sala liberada"


def main():
    # exibe autores
    banner()

    matriz = criarSala()

    HOST = ''
    PORT = 2048

    tcp = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    tcp.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    orig = (HOST, PORT)
    tcp.bind(orig)
    tcp.listen(10)
    while True:
        con, cliente = tcp.accept()
        print 'Cliente conectado', cliente
        while True:
            msg = con.recv(1024)
            if not msg: break

            if msg == 'help':
                con.sendall(ajuda())#envia resposta para o cliente
            elif msg == 'list':
                con.sendall(exibirSala(matriz))
            elif msg.find('deallocate') >= 0:
                sala = msg[-1]
                con.sendall(liberarSala(matriz,int(sala)))
            elif msg.find('allocate') >=0:
                sala = msg[-1]
                con.sendall(reservarSala(matriz,int(sala)))

            elif msg == 'exit':
                print 'Finalizando conexao..', cliente
                con.close()


            print cliente, 'comando: ' , msg
            print 'Finalizando conexao..', cliente
        con.close()





# chama a funcao principal
main()

# coding: utf-8

# Консольный клиент игры "Виселица"

import socket
import sys
import time

HOST, PORT = "localhost", 9999

# Create a socket (SOCK_STREAM means a TCP socket)
print('Клиент игры "Виселица"')
print('Подключение к {}:{}...'.format(HOST, PORT))

try:        
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((HOST, PORT))
except:
    print('Ошибка подключения к серверу!')
    sys.exit(13)
    
try:
    sock.sendall(bytes("START\n", "utf-8"))
    received = str(sock.recv(1024), "utf-8")        
except:
    print('Ошибка отправки данных начала игры')
    sock.close()
    
data = received.split(';')    
if data[0] == 'GUESS':
    print('Угадайте число: {} < x  < {}'.format(data[1], data[2]))    

    
    while True:
        x = input('Ваш ответ (q - для выхода): ')
        if x == 'q':
            sock.sendall(bytes("GOODBYE", "utf-8"))
            break
            
        try:
            sock.sendall(bytes('TRY;{}'.format(x), "utf-8"))
            received = str(sock.recv(1024), "utf-8")        
        except:
            print('Ошибка отправки ответа серверу')
            break
        data = received.split(';')            
        if data[0] == 'TRUE':
            print('Вы угадали!')
            break
        elif data[0] == 'FALSE':
            if len(data) > 2:
                if data[2] == '<':
                    print('Вы не угадали. Число меньше. У Вас осталось попыток: {}'.format(data[1]))
                else:    
                    print('Вы не угадали. Число больше. У Вас осталось попыток: {}'.format(data[1]))
        elif data[0] == 'FAIL':
            print('Вы не угадали число и проиграли! :(')
            break
            
        
    sock.close()   
else:
    print('Неизвестный ответ сервера')
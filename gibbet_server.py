# coding: utf-8

# Сервер игры "Виселица"

import socketserver

'''
    Протокол обмена: текстовый
    Клиент                                      Сервер
    HELLO;md5(time.time()) - приветствие    - WELCOME;id = md5(user_md5 + salt) 
    CHECK;id;number           - проверка числа - TRUE
                                                 FALSE
    EASY;id                   -   уровень      - LEVEL?
    NORMAL;id
    HARD;id
    START;id                  - начало         - GUESS;a;b
                              - сервер возвращает диапазон
    GOODBYE;id                - отключение     - GOODBYE
'''


import random

class MyTCPHandler(socketserver.BaseRequestHandler):
    """
    The RequestHandler class for our server.

    It is instantiated once per connection to the server, and must
    override the handle() method to implement communication to the
    client.
    """

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).decode().strip()
        
        
        print("Клиент {} сообщает: {}".format(self.client_address[0], self.data))
        
        x = random.randint(1,100)
        if self.data == 'START':
            self.request.sendall(bytes('GUESS;1;100','utf-8'))
            try_count = 10
            while True:
                self.data = self.request.recv(1024).decode().strip()
                resp = self.data.split(';')
                print(resp)
                if resp[0] == 'TRY':
                    if int(resp[1]) == x:
                        self.request.sendall(bytes('TRUE','utf-8'))
                        print('Клиент {} выиграл'.format(self.client_address[0]))        
                        break
                    else:
                        try_count -= 1
                        if try_count == 0:                        
                            self.request.sendall(bytes('FAIL','utf-8'))
                            print('Клиент {} проиграл'.format(self.client_address[0]))
                            self.request.sendall(bytes('GOODBYE','utf-8'))
                            break
                        else:    
                            if x < int(resp[1]):
                                self.request.sendall(bytes('FALSE;{};<'.format(try_count),'utf-8'))
                            else:    
                                self.request.sendall(bytes('FALSE;{};>'.format(try_count),'utf-8'))
                elif resp[0] == 'GOODBYE':
                    self.request.sendall(bytes('GOODBYE','utf-8'))
                    print('Клиент {} отключился'.format(self.client_address[0]))
                    break
                else:
                    print('Неизвестный запрос от клиента')
                    break
                
            

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

    # Create the server, binding to localhost on port 9999
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    print('Сервер игры "Виселица" запущен')
    # Activate the server; this will keep running until you
    # interrupt the program with Ctrl-C
    server.serve_forever()
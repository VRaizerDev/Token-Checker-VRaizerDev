import requests
import time
import os
import random
import string
import colorama

from colorama import Fore, Back, Style

def checker():
    chars = string.ascii_letters + string.digits + 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.-'
    rnd = random.SystemRandom()

    os.system('title Token Checker')
    print(Fore.RED+'''
             _____  _____  _   _  ___    _   _     ___    _   _  ___    ___    _   _  ___    ___   
            (_   _)(  _  )( ) ( )(  _`\ ( ) ( )   (  _`\ ( ) ( )(  _`\ (  _`\ ( ) ( )(  _`\ |  _`\ 
              | |  | ( ) || |/'/'| (_(_)| `\| |   | ( (_)| |_| || (_(_)| ( (_)| |/'/'| (_(_)| (_) )
              | |  | | | || , <  |  _)_ | , ` |   | |  _ |  _  ||  _)_ | |  _ | , <  |  _)_ | ,  / 
              | |  | (_) || |\`\ | (_( )| |`\ |   | (_( )| | | || (_( )| (_( )| |\`\ | (_( )| |\ \ 
              (_)  (_____)(_) (_)(____/'(_) (_)   (____/'(_) (_)(____/'(____/'(_) (_)(____/'(_) (_)

                                    ----------------------------
                                    (1) Checker Um Token
                                    (2) Checker Mais De Um Token
                                    (3) Gerador De Token
                                    (4) Sair
                                    ----------------------------
                                            By wffDuck
    ''')
    sel = int(input('Opcão:'))
    if sel == 1:
        os.system('cls')
        print('Insira o token que deseja checkar >>')
        token = input('Token:')
        os.system('cls')
        headers = {'Content-Type': 'application/json', 'authorization': token}
        url = "https://discordapp.com/api/v6/users/@me/library"
        r = requests.get(url, headers=headers)
        if r.status_code == 200:
            print(Fore.GREEN+"{} Esse token é valido!!".format(token))
            time.sleep(10000)
        else:
            print(Fore.RED+"Ops... Esse token é invalido!")
            time.sleep(10000)
    if sel == 2:
        with open("tokens.txt") as f:
            for line in f:
                token = line.strip("\n")
                headers = {'Content-Type': 'application/json', 'authorization': token}
                url = "https://discordapp.com/api/v6/users/@me/library"
                r = requests.get(url, headers=headers)
                content = 'Token Checker'
                if r.status_code == 200:
                    print(Fore.GREEN+"{} Esse token é valido!!".format(line.strip("\n")))
                else:
                    print(Fore.RED+"Ops... Esse token é invalido")
    if sel == 3:
        os.system('cls')
        valor = int(input('Quantos tokens deseja gerar?'))
        for v in range(valor):
            token2 = print(Fore.WHITE+''.join(rnd.choice(chars) for i in range(70)))
    time.sleep(1000)
    if sel == 4:
        os.system('cls')
        os.system('exit')
checker()

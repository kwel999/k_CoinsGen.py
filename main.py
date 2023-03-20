community_link = "http://aminoapps.com/c/Heaven_999"

import concurrent.futures
from os import system, sys
from time import sleep
import threading
from colorama import Fore

print("\t\033[1;31m Super Fast         Termux Edition\n\n")
animation = '''


                Subscribes to :  https://youtube.com/c/KWELATEYOURPIZZA
                Githube : https://github.com/kwel999
                discord : https://discord.gg/wGRQYd3nVd

        ────╔╗        
        ╔═╦═╬╬═╦╗        
        ║═╣╬║║║║║        
        ╚═╩═╩╩╩═╝        
            
            
        ╔══╗        
        ║╔═╬═╦═╦╗        
        ║╚╗║╩╣║║║        
        ╚══╩═╩╩═╝  2.0          
                    
        
        
     '''
for x in animation:
	print(Fore.CYAN + x, end ='')
	sys.stdout.flush()
	sleep(0.008)

import os, json, time
import concurrent.futures
from os import system, sys
from time import sleep
import threading
from colorama import Fore
from k_amino import(
Client,
SubClient
)

try:
    import k_amino, pyfiglet
except:
    os.system('pip install k_amino==1.0.8')
    os.system('pip install pyfiglet')
    os.system("pip install easy_events")
    os.system("pip install flask")
    import k_amino, pyfiglet
else:
    os.system('clear')
    A = '\x1b[1;91m'
    Z1 = '\x1b[2;31m'
    E = '\x1b[1;92m'
    H = '\x1b[1;93m'
    L = '\x1b[1;95m'
    B = '\x1b[2;36m'
    Y = '\x1b[1;34m'
    M = '\x1b[1;94m'




    from flask import Flask
    from threading import Thread
    import random
    app = Flask('')

    @app.route('/')
    def home():
        return 'Bot on'


    def run():
        app.run(host='0.0.0.0', port=(random.randint(2000, 9000)))


    def keep_alive():
        t = Thread(target=run)
        t.start()


    keep_alive()
    client = Client()
    from_info = client.get_from_link(community_link)
    from_id = from_info.comId
    file = open('accounts.json')
    date = json.load(file)

    def threadit(email: str, password: str, device: str):
        try:
            client.login(email, password)
            print(H + '\nlogged in to -',email)
            #time.sleep(1)
            client.join_community(comId=from_id)
            #time.sleep(4)  #use time if you need <=
            print(H + '\n Joined Community -', email)
            from_client = SubClient(comId=from_id)
            for i in range(24):
                from_client.send_active_time()
                print(A + f"{i + 1} Coin Generating - OK")
                time.sleep(9)
            else:
                print(H + '\nCoins Genarated !! from - ',email)

        except Exception as e:
            try:
                print(e)
            finally:
                e = None
                del e


    def main():
        for acc in date:
            email = acc['email']
            password = acc['password']
            device = acc['deviceId']
            threadit(email=email, password=password, device=device)


    if __name__ == '__main__':
                main()

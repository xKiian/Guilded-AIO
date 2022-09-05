import time, threading, os
from lib.console import Console
from modules import creator, joiner, onliner, statuser, pfp, spammer

def spam(id, message, cookies):
    while True:
        for cookie in cookies:
            spammer.Spam(None, cookie, id, message).start()
            time.sleep(0.2)
def status(cookie):
    statuser.Statuser(None, cookie).start()
def acccreator():
    creator.AccCreator(None).start()
def join(cookie):
    joiner.Joiner(None, cookie).start()
def online(cookie):
    onliner.Onliner(None, cookie).start()
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    Console.logo()
    x = input(">>>")
    if x == "1":
        for i in range(7):
            threading.Thread(target=acccreator).start()
        time.sleep(1)
        Console.printl("[+] Created 7 accounts")# after seven accounts you get ratelimted for about 70 seconds :c
        time.sleep(1)
        main()
    
    elif x == "2":
        with open('./output/cookies.txt', 'r') as f:
            cookies = f.read().splitlines()
        for cookie in cookies:
            threading.Thread(target=join, args=(cookie,)).start()
            time.sleep(0.2)
        time.sleep(3)
        if threading.active_count == 0:
            Console.printl("[+] Joined all servers")
        time.sleep(1)
        main()
    
    elif x == "3":
        with open('./output/cookies.txt', 'r') as f:
            cookies = f.read().splitlines()
            for cookie in cookies:
                threading.Thread(target=online, args=(cookie,)).start()
                time.sleep(0.3)
        time.sleep(1)
        if threading.active_count == 0:
            Console.printl("[+] All accounts are now online")
        time.sleep(1)
        main()
    
    elif x == "4":
        with open('./output/cookies.txt', 'r') as f:
            cookies = f.read().splitlines()
            for cookie in cookies:
                threading.Thread(target=status, args=(cookie,)).start()
                time.sleep(0.25)
        time.sleep(3)
        if threading.active_count == 0:
            Console.printl("[+] Set status of all accounts")
        time.sleep(1)
        main()
    
    elif x == "5":
        with open('./output/cookies.txt', 'r') as f:
            cookies = f.read().splitlines()
            for cookie in cookies:
                pfp.Pfp(None, cookie).start()
            time.sleep(0.06)
        time.sleep(2)
        if threading.active_count == 0:
            Console.printl("[+] Set pfp of all accounts")
        time.sleep(1)
        main()
    
    elif x == "6":
        id = input("channelid: ")
        message = input("message: ")
        with open('./output/cookies.txt', 'r') as f:
            cookies = f.read().splitlines()
            for i in range(2):
                    threading.Thread(target=spam, args=(id, message, cookies)).start()
                    time.sleep(1.5)
    else:
        main()

if __name__ == "__main__":
    main()
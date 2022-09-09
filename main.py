import time, threading, os, random, json
from lib.console import Console
from modules import creator, joiner, onliner, statuser, pfp, spammer, checker
config = json.load(open('./input/config.json', 'r+'))
def check(cookie, proxy):
    checker.Checker(proxy, cookie).start()
def spam(id, message, cookies, proxy):
    while True:
        for cookie in cookies:
            spammer.Spam(proxy, cookie, id, message).start()
def status(cookie, proxy):
    statuser.Statuser(proxy, cookie).start()

def acccreator(proxy):
    creator.AccCreator(None).start()

def join(cookie, proxy):
    joiner.Joiner(proxy, cookie).start()

def online(cookie, proxy):
    onliner.Onliner(proxy, cookie).start()

def main():
    if config["proxy"]:
        proxy = open('./input/proxies.txt', 'r').read().splitlines()
    os.system('cls' if os.name == 'nt' else 'clear')
    Console.logo()
    x = input(">>>")
    if x == "1":
        if config["proxy"]:
            x = input("How many accounts do you want to create? ")
            for i in range(int(x)):
                threading.Thread(target=acccreator, args=(random.choice(proxy),)).start()
        else:
            for i in range(7):
                threading.Thread(target=acccreator, args=(None,)).start()
        time.sleep(1)
        main()
    
    elif x == "2":
        with open('./output/cookies.txt', 'r') as f:
            cookies = f.read().splitlines()
        if config["proxy"]:
            for cookie in cookies:
                threading.Thread(target=join, args=(cookie, random.choice(proxy))).start()
        else:
            for cookie in cookies:
                threading.Thread(target=join, args=(cookie, None)).start()
                time.sleep(0.2)
        time.sleep(3)
        if threading.active_count == 0:
            Console.printl("[+] Joined all servers")
        time.sleep(1)
        main()
    
    elif x == "3":
        with open('./output/cookies.txt', 'r') as f:
            cookies = f.read().splitlines()
        if config["proxy"]:
            for cookie in cookies:
                threading.Thread(target=online, args=(cookie,random.choice(proxy))).start()
        else:
            for cookie in cookies:
                threading.Thread(target=online, args=(cookie,None)).start()
                time.sleep(0.3)
        time.sleep(1)
        if threading.active_count == 0:
            Console.printl("[+] All accounts are now online")
        time.sleep(1)
        main()
    
    elif x == "4":
        with open('./output/cookies.txt', 'r') as f:
            cookies = f.read().splitlines()
        if config["proxy"]:
            for cookie in cookies:
                threading.Thread(target=status, args=(cookie,random.choice(proxy))).start()
        else:
            for cookie in cookies:
                threading.Thread(target=status, args=(cookie,None)).start()
                time.sleep(0.3)
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
        if config["proxy"]:
            for i in range(2):
                    threading.Thread(target=spam, args=(id, message, cookies,random.choice(proxy))).start()
        else:
            for i in range(2):
                    threading.Thread(target=spam, args=(id, message, cookies,None)).start()
    
    elif x == "7":
        open("./output/valid.txt", "w").close()# clear the file
        with open('./output/cookies.txt', 'r') as f:
            cookies = f.read().splitlines()
        if config["proxy"]:
            for cookie in cookies:
                threading.Thread(target=check, args=(cookie,random.choice(proxy))).start()
        else:
            for cookie in cookies:
                threading.Thread(target=check, args=(cookie,None)).start()
                time.sleep(0.05)
        time.sleep(1)
        if threading.active_count == 0:
            Console.printl("[+] Checked all accounts")
        time.sleep(1)
        main()
    else:
        main()

if __name__ == "__main__":
    main()
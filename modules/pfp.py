# sry for the filename xd
import os, binascii, httpx, random, string, time, threading, json, colorama, sys
from lib.console import Console
from lib.utils import Util
config = json.load(open('./input/config.json', 'r+'))
class Pfp(threading.Thread):
    def __init__(self, proxy, cookie):
        self.cookie = cookie
        self.api: Util = Util(proxy)
        self.proxy = proxy
        self.baseurl: str = 'https://www.guilded.gg/api'
    def start(self):
        try:
            pfp = random.choice(open('./input/user/pfp.txt', 'r+').read().splitlines())
            self.api.token_login(self.cookie)
            s = self.api.set_pfp(pfp)
            if str(pfp) in s.text:
                Console.printl(f'[+] set pfp of {self.cookie[:30]}')
            elif s.status_code == 429:
                Console.debug(f'[*] {self.cookie[:30]} got a ratelimit')
                time.sleep(5)
                self.start()
            else:
                Console.printl(f'[-] failed to set pfp of {self.cookie[:30]}')

        except Exception as e:
            Console.debug(f'[*]: {e}')
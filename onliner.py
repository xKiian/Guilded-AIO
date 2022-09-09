import os, binascii, httpx, random, string, time, threading, json, colorama, sys
from lib.console import Console
from lib.utils import Util
config = json.load(open('./input/config.json', 'r+'))
class Onliner(threading.Thread):
    def __init__(self, proxy, cookie):
        self.cookie = cookie
        self.api: Util = Util(proxy)
        self.proxy = proxy
        self.baseurl: str = 'https://www.guilded.gg/api'
    def start(self):
        try:
            self.api.token_login(self.cookie)
            self.api.ping()
            s = self.api.set_activity(3)
            if s.status_code == 429:
                Console.debug(f'[*] {self.cookie[:30]} got a ratelimit')
                time.sleep(5)
                self.start()
            else:
                Console.printl(f'[+] {self.cookie[:30]} is now online')
        except Exception as e:
            Console.debug(f'[*]: {e}')
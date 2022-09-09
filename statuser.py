# sry for the filename xd
import random, threading, json, time
from lib.console import Console
from lib.utils import Util
config = json.load(open('./input/config.json', 'r+'))
class Statuser(threading.Thread):
    def __init__(self, proxy, cookie):
        self.cookie = cookie
        self.api: Util = Util(proxy)
        self.proxy = proxy
        self.baseurl: str = 'https://www.guilded.gg/api'
    def start(self):
        try:
            status = random.choice(open('./input/user/status.txt', 'r+').read().splitlines())
            self.api.token_login(self.cookie)
            s = self.api.set_status(status)
            self.api.ping()
            if s.status_code == 200:
                Console.printl(f'[+] set status of {self.cookie[:30]} to {status}')
            elif s.status_code == 429:
                Console.debug(f'[*] {self.cookie[:30]} got a ratelimit')
                time.sleep(5)
                self.start()
        except Exception as e:
            Console.debug(f'[*]: {e}')
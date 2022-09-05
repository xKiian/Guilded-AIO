import time, threading, json
from lib.console import Console
from lib.utils import Util
config = json.load(open('./input/config.json', 'r+'))
class Checker(threading.Thread):
    def __init__(self, proxy, cookie):
        self.cookie = cookie
        self.api: Util = Util(proxy)
        self.proxy = proxy
        self.baseurl: str = 'https://www.guilded.gg/api'
    def start(self):
        try:
            self.api.token_login(self.cookie)
            s = self.api.check()

            if "profilePictureLg" in s.text and s.status_code == 200:
                Console.printl(f'[+] {self.cookie[:30]} is valid')
                with open('./output/valid.txt', 'a+') as f:
                    f.write(f'{self.cookie}\n')
            elif "TooManyRequestsError" in s.text or s.status_code == 429:
                Console.debug(f'[*] {self.cookie[:30]} ratelimited')
                time.sleep(4)
                self.start()
            else:
                Console.printl(f'[-] {self.cookie[:30]} is invalid')
        except Exception as e:
            Console.debug(f'[*]: {e}')
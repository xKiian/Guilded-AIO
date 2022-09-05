import os, binascii, httpx, random, string, time, threading, json, colorama, sys
from lib.console import Console
from lib.utils import Util
config = json.load(open('./input/config.json', 'r+'))
class Joiner(threading.Thread):
    def __init__(self, proxy, cookie):
        self.cookie = cookie
        self.api: Util = Util(proxy)
        self.proxy = proxy
        self.baseurl: str = 'https://www.guilded.gg/api'
    def start(self):
        try:
            self.api.token_login(self.cookie)
            r = self.api.join_server(config["invite_code"])
            self.api.ping()
            if "usedBy" in r.text:
                Console.printl(f"[+] Joined server with {self.cookie[:30]}")
            elif "cannot join a team, already a member" in r.text:
                Console.printl(f"[*] Already joined server with {self.cookie[:30]}")
            elif r.status_code == 429:
                Console.debug(f"[*] {self.cookie[:30]} got a ratelimit")
                time.sleep(5)
                self.start()
        except Exception as e:
            Console.debug(f'[*]: {e}')
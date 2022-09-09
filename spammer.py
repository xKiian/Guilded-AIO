from email import message
import os, binascii, httpx, random, string, time, threading, json, colorama, sys
from lib.console import Console
from lib.utils import Util
config = json.load(open('./input/config.json', 'r+'))
class Spam(threading.Thread):
    def __init__(self, proxy, cookie, id, message):
        self.message = message
        self.id = id
        self.cookie = cookie
        self.api: Util = Util(proxy)
        self.proxy = proxy
        self.baseurl: str = 'https://www.guilded.gg/api'
    def start(self):
        #try:
            self.api.token_login(self.cookie)
            self.api.ping()
            s = self.api.send_message(self.id, self.message)
            if "TooManyRequestsError" in s.text:
                Console.debug(f'[*] {self.cookie[:30]} is Ratelimited')
            elif self.message in s.text:
                Console.printl(f'[+] {self.cookie[:30]} sent {self.message}')
        #except Exception as e:
        #    Console.debug(f'[*]: {e}')
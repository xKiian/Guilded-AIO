from colorama import Fore, init; init()
import threading, json, os
config = json.load(open('./input/config.json', 'r+'))
lock = threading.Lock()
class Console:
    def __init__(self) -> None:
        pass

    def debug(content: str):
            if config['debug']:
                lock.acquire()
                print(f'[DEBUG] {content}{Fore.RESET}'.replace('[+]', f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}]').replace('[*]', f'[{Fore.LIGHTYELLOW_EX}*{Fore.RESET}]').replace('[>]', f'[{Fore.CYAN}>{Fore.RESET}]').replace('[-]', f'[{Fore.RED}-{Fore.RESET}]'))
                lock.release()
    def printl(content: str):
            lock.acquire()
            print(f'{content}{Fore.RESET}'.replace('[+]', f'[{Fore.LIGHTGREEN_EX}+{Fore.RESET}]').replace('[*]', f'[{Fore.LIGHTYELLOW_EX}*{Fore.RESET}]').replace('[>]', f'[{Fore.CYAN}>{Fore.RESET}]').replace('[-]', f'[{Fore.RED}-{Fore.RESET}]'))
            lock.release()
    def logo():
        os.system(f"title Guilded AIO ^| v1.2.0 ^| by xKian ^| Tokens loaded: {len(open('./output/cookies.txt', 'r+').read().splitlines())}")
        print(Fore.BLUE + f"""


                        ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗      █████╗ ██╗ ██████╗ 
                       ██╔════╝ ██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗    ██╔══██╗██║██╔═══██╗
                       ██║  ███╗██║   ██║██║██║     ██║  ██║█████╗  ██║  ██║    ███████║██║██║   ██║
                       ██║   ██║██║   ██║██║██║     ██║  ██║██╔══╝  ██║  ██║    ██╔══██║██║██║   ██║
                       ╚██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██████╔╝    ██║  ██║██║╚██████╔╝
                        ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═════╝     ╚═╝  ╚═╝╚═╝ ╚═════╝ 

                                                    {Fore.RESET}by \x78\x4B\x69\x61\x6E\x23\x31\x30\x30\x30

                                    {Fore.BLUE}[{Fore.RESET}1{Fore.BLUE}]{Fore.RESET} Account Creator       {Fore.BLUE}[{Fore.RESET}5{Fore.BLUE}]{Fore.RESET} Set Profile Picture
                                    {Fore.BLUE}[{Fore.RESET}2{Fore.BLUE}]{Fore.RESET} Server Joiner         {Fore.BLUE}[{Fore.RESET}6{Fore.BLUE}]{Fore.RESET} Spammer
                                    {Fore.BLUE}[{Fore.RESET}3{Fore.BLUE}]{Fore.RESET} Onliner               {Fore.BLUE}[{Fore.RESET}7{Fore.BLUE}]{Fore.RESET} Token Checker      
                                    {Fore.BLUE}[{Fore.RESET}4{Fore.BLUE}]{Fore.RESET} Set Status            {Fore.BLUE}[{Fore.RESET}8{Fore.BLUE}]{Fore.RESET} Coming soon...                                        

""")
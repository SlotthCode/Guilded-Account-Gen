import ctypes
import threading
import httpx, random, itertools, os
from colorama import Fore

x = input("INVITE ---> ")
MAX_THREADS = int(input("threads = "))
username = input("USERNAME = ")
os.system("cls")

class Gen:
    def __init__(self):
        self.password = "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8))
        with open("data/proxies.txt", encoding="utf-8") as f:
            self.proxies = itertools.cycle([i.strip() for i in f if i])
        self.created = 0

    def gen(self):
        ctypes.windll.kernel32.SetConsoleTitleW(f"Guilded Account Gen: Accounts Created: {self.created}")
        self.username = username + " | "+ "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=4))
        self.domains = ["@gmail.com", "@yahoo.com", "@outlook.com", "@hotmail.com", "@protonmail.com"]
        self.email =  f"Slotths" + "_" + "".join(random.choices("abcdefghijklmnopqrstuvwxyz", k=8)) + random.choice(self.domains)
        self.proxy = {
            "http://": "http://" + next(self.proxies),
            "https://": "http://" + next(self.proxies),
        }
        self.client = httpx.Client(proxies=self.proxy)

        self.headers = {
            'accept': 'application/json, text/javascript, */*; q=0.01',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'fr-FR,fr;q=0.9',
            'content-type': 'application/json',
            'guilded-device-type': 'desktop',
            'origin': 'https://www.guilded.gg',
            'referer': 'https://www.guilded.gg/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'dnt': '1',
            "Sec-Ch-Ua": '" Not;A Brand";v="99", "Google Chrome";v="97", "Chromium";v="97"',
            "Sec-Ch-Ua-Mobile": '?0',
            "Sec-Ch-Ua-Platform": "macOS",
            }

        self.payload  =  {
            "extraInfo": {
                "platform": "desktop",
                "referrerId": ""
            },
            "name": self.username,
            "email": self.email,
            "password": self.password,
            "fullName": self.username
            }
            
        try:
            self.response = self.client.post("https://www.guilded.gg/api/users?type=email", headers=self.headers, json=self.payload)
            if "email" in self.response.json()["user"]:
                print(f"({Fore.GREEN}!{Fore.RESET}) Made a Account! ({self.username})")
                hmacCookie = self.response.cookies['hmac_signed_session']
                self.client.cookies.set('hmac_signed_session', hmacCookie)
                self.client.put(f"https://www.guilded.gg/api/invites/{x}", headers=self.headers)
                self.created += 1
                with open("data/cookies.txt", "a") as f:
                    f.write(f"{hmacCookie}\n")
                    f.close()
            else:
                pass
        except Exception:
            pass

    def run(self):
        while True:
            if threading.active_count() <= MAX_THREADS:
                  threading.Thread(target=self.gen).start()

Gen().run()
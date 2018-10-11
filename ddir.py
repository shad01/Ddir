import requests
import sys

def banner():
    print("""
               /$$$$$$$  /$$$$$$$  /$$$$$$ /$$$$$$$
              | $$__  $$| $$__  $$|_  $$_/| $$__  $$
              | $$  \ $$| $$  \ $$  | $$  | $$  \ $$
              | $$  | $$| $$  | $$  | $$  | $$$$$$$/
              | $$  | $$| $$  | $$  | $$  | $$__  $$
              | $$  | $$| $$  | $$  | $$  | $$  \ $$
              | $$$$$$$/| $$$$$$$/ /$$$$$$| $$  | $$
              |_______/ |_______/ |______/|__/  |__/  """)
    print()

def diretorio():
    if len(sys.argv) < 3:
        print()
        print("[+]  python ddir.py https://www.site.com/ wordlist.txt [+]")
        print()

    else:
        with open(sys.argv[2], encoding="utf-8") as f:
            paginas = f.readlines()

        for pagina in paginas:
            try:
                pagina = pagina.replace("\n", "")
                url = sys.argv[1] + pagina
                site = requests.get(url)
            
                if site.status_code == 200:
                    print(f"\033[1;32mPAGINA ENCONTRADA: {url}\033[m")

                else:
                    print(f"PAGINA NÃO ENCONTRADA: {url}")

            except KeyboardInterrupt:
                sys.exit()

banner()
diretorio()

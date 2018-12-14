import requests
import sys

if len(sys.argv) < 3:
    print()
    print('[+]  python ddir.py https://www.site.com/  wordlist.txt [+]')
    print()
    sys.exit()

print('''
        /$$$$$$$  /$$$$$$$  /$$$$$$ /$$$$$$$
        | $$__  $$| $$__  $$|_  $$_/| $$__  $$
        | $$  \ $$| $$  \ $$  | $$  | $$  \ $$
        | $$  | $$| $$  | $$  | $$  | $$$$$$$/
        | $$  | $$| $$  | $$  | $$  | $$__  $$
        | $$  | $$| $$  | $$  | $$  | $$  \ $$
        | $$$$$$$/| $$$$$$$/ /$$$$$$| $$  | $$
        |_______/ |_______/ |______/|__/  |__/  ''')
print()
   

def diretorio(site, arquivo):
        with open(arquivo, encoding='utf-8') as f:
            paginas = f.readlines()

        for pagina in paginas:
            try:
                dire = pagina.replace('\n', '')
                url = site + dire
                r_site = requests.get(url)

                if r_site.status_code == 200:
                    print(f'[+] PAGINA ENCONTRADA: {url} [+]')

                elif r_site.status_code != 200:
                    print(f'PAGINA NÃO ENCONTRADA: {url}')

            except KeyboardInterrupt:
                print('SAINDO DO DDIR')


www = sys.argv[1]
wordlist = sys.argv[2]
diretorio(site=www, arquivo=wordlist)

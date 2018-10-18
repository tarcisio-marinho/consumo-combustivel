#!/usr/bin/env python3
import requests, json, os

def get_api_key():
    path = "key.txt"
    try:
        with open(path) as f:
            key = f.read()
    except FileNotFoundError:
        print("create key.txt on your directory with the key")
        exit(-1)
    return key

def busca_dicionario(partida, destino, key):
    link = "https://maps.googleapis.com/maps/api/directions/json?origin={0}&destination={1}&key={2}&language=pt".format(partida, destino, key)
    req = requests.get(link)
    dicionario = json.loads(req.text)
    return dicionario

def requests_api(dicionario):
    if(dicionario["status"] == "NOT_FOUND"):
        return -1
    distancia = (dicionario["routes"][0]["legs"][0]["distance"]["text"])
    distancia = float(distancia.replace("km", "").replace(" ", "").replace(",", "."))
    return distancia


def calculo_api(preco_combustivel, km_litro_cidade, distancia):
    litros_combustivel = distancia / km_litro_cidade
    valor_combustivel = litros_combustivel * preco_combustivel
    print ("total de litros gastos no trajeto: %.2f" % litros_combustivel)
    print("total do valor de combustivel: %.2f" % valor_combustivel)

def get_percurso(dicionario):
    percurso = (dicionario["routes"][0]["legs"][0]["steps"])
    print("Melhor trajeto:\n")
    for i in percurso: 
        print(i["html_instructions"].replace("<b>","").replace("</b>", "").replace('<div style="font-size:0.9em">', "").replace("</div>",""))
        

if __name__== "__main__":

    preco_combustivel = float(input("digite o preço do combustivel: "))
    km_litro_cidade = float(input("digite a quantidade de km/ litro que seu carro faz:"))
    key = get_api_key()
    partida = input("informe o ponto de partida: ")
    destino = input("informe o ponto o destino: ")
    os.system("clear")
    dicionario = busca_dicionario(partida,destino,key)
    distancia = requests_api(dicionario)
    print("distancia do trajeto em KM:", distancia)
    calculo_api(preco_combustivel, km_litro_cidade, distancia)
    get_percurso(dicionario)


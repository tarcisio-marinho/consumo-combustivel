import requests, json, time

def get_api_key():
    path = "key.txt"
    with open(path) as f:
        key = f.read()
        
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
    for i in percurso: 
        print(i["html_instructions"].replace("<b>","").replace("</b>", "").replace('<div style="font-size:0.9em">', "").replace("</div>",""))
        

if __name__== "__main__":
    preco_combustivel = 3.99
    km_litro_cidade = 12
    key = get_api_key()
    partida = "rua josé mario de oliveira, candeias, jaboatão dos guararapes"
    destino = "walmart, candeias jaboatão dos guararapes"
    dicionario = busca_dicionario(partida,destino,key)
    distancia = requests_api(dicionario)
    print("distancia do trajeto:", distancia)
    calculo_api(preco_combustivel, km_litro_cidade, distancia)
    get_percurso(dicionario)


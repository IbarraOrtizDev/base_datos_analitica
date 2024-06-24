from pymongo import MongoClient

def save_in_db(lista):
    #Conectar a la base de datos
    cliente = MongoClient('localhost', 27017)
    db = cliente['store_company']
    coleccion = db['ventas']
    #Insertar lista de diccionarios
    coleccion.insert_many(lista)

def customer(information_client):
    headers = ["CustomerID", "Name", "Email", "Phone"]
    diccionario = {}
    for i in headers:
        diccionario[i] = information_client[headers.index(i)].value
    return diccionario

def formatNumber(number):
    return float(number.replace(",", "."))
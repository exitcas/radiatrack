import json
import time
import requests
import os
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

PAGINA_URL = "https://meteo.fcaglp.unlp.edu.ar/davis/torre/torre.htm"
IMAGEN_CARPETA = "imagenes/"
IMAGEN_URL = "https://meteo.fcaglp.unlp.edu.ar/davis/torre/SolarRad.gif"
DB_ARCHIVO = "radiacion.json"
FRECUENCIA = 3600 # 3600 segs = 1 hr


def obtener_arbol_web (pagina_url):
    pagina = requests.get(pagina_url)
    soup = BeautifulSoup(pagina.text, "html.parser")
    arbol = ET.fromstring(str(soup))
    return arbol


def obtener_radiacion(pagina_url):
    arbol = obtener_arbol_web(pagina_url)

    extracto_radiacion = arbol.findall("./body/div[2]/table/tbody/tr[2]/td[1]/div/table/tbody/tr/td")[1].text
    radiacion = float(extracto_radiacion.split("\xa0")[0]) / 100

    return radiacion


def obtener_db(db_archivo):
    if os.path.isfile(db_archivo):
        f = open(db_archivo, "r")
        db = json.loads(f.read())
        f.close()
    else:
        db = {}

    return db


def guardar_db(db, db_archivo):
    f = open(db_archivo, "w")
    f.write(json.dumps(db))
    f.close()


def guardar_radiacion_db(hora_consulta, radiacion, db_archivo):
    db = obtener_db(db_archivo)
    db[hora_consulta] = radiacion
    guardar_db(db, db_archivo)


def crear_carpeta_no_existe(carpeta):
    if os.path.isdir(carpeta) == False:
        os.mkdir(carpeta)


def guardar_imagen(hora_consulta, imagen_carpeta, imagen_url):
    crear_carpeta_no_existe(imagen_carpeta)

    imagen = requests.get(imagen_url)
    f = open(imagen_carpeta + hora_consulta + ".gif", "wb")
    f.write(requests.get(imagen_url).content)
    f.close()


while True:
    hora_consulta = time.strftime("%Y-%m-%d_%H-%M-%S", time.localtime())
    radiacion = obtener_radiacion(PAGINA_URL)
    guardar_radiacion_db(hora_consulta, radiacion, DB_ARCHIVO)
    #guardar_imagen(hora_consulta, IMAGEN_CARPETA, IMAGEN_URL)
    print(f"[{hora_consulta}]: {radiacion} W/cm^2")
    time.sleep(FRECUENCIA)

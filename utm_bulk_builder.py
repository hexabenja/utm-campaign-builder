#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Librerias para descomponer juntar y reconocer URLs
from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl

   
#Define generate_utm_url como los valores de base_url y utm_params
def generate_utm_url(base_url, utm_params):
    parsed_url = urlparse(base_url) #Desarma URL base (subdominio, dominio, slash"
    query_params = dict(parse_qsl(parsed_url.query)) #Desarma las queries de la URL (Representadas por ? en BBDD SQL)

    # NUEVO: Filtrar solo parámetros UTM que no estén vacíos
    filtered_utm_params = {k: v for k, v in utm_params.items() if v.strip()}
    #K es la Key, V es el valor y v.strip verifica si es que hay espacios y si hay contenido al final en V

    query_params.update(filtered_utm_params) #Se reemplaza por valor NUEVO de utm_params a los nuevos filtrados por la función de arriba
    updated_query = urlencode(query_params) #Juntar los queries (UTM)
    updated_url = urlunparse(parsed_url._replace(query=updated_query)) #URL armada devuelta y reemplazada por updated_query
    return updated_url

def main(): #Definir programa main
    urls = [] #Función urls
    while True: #Mientras sea cierto "urls"
        url = input("Ingresa la URL del sitio (o 'ya' para terminar de ingresar): ") # El valor URL será el input ingresado
        if url.lower() == "ya": #En caso de que el input de url.lower sea "ya" 
            break #Se detiene la función url del input 
        urls.append(url)

    utm_params = {
        "utm_source": input("Ingresa fuente (source): "),
        "utm_medium": input("Ingresa medio (medium): "),
        "utm_campaign": input("Ingresa Nombre del campaña (campaign name): "),
        "utm_content": input("Ingresa contenido (content): "),
        "utm_term": input("Ingresa termino (term): "),
    }

    # Generar y printear URLs con UTM
    print("\nURLS con UTM generadas:")
    for url in urls:
        utm_url = generate_utm_url(url, utm_params)
        print(utm_url)

if __name__ == "__main__":
    main()

print("Se ha completado el enlace exitosamente")
input("Apreta ENTER para cerrar esta ventana")



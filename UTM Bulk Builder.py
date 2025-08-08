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
        url = input("Enter website URL (or 'done' to finish): ") # El valor URL será el input ingresado
        if url.lower() == "done": #En caso de que el input de url.lower sea "done" 
            break #Se detiene la función url del input 
        urls.append(url)

    utm_params = {
        "utm_source": input("Enter source: "),
        "utm_medium": input("Enter medium: "),
        "utm_campaign": input("Enter campaign name: "),
        "utm_content": input("Enter content: "),
        "utm_term": input("Enter term: "),
    }

    # Generar y printear URLs con UTM
    print("\nGenerated UTM-enabled URLs:")
    for url in urls:
        utm_url = generate_utm_url(url, utm_params)
        print(utm_url)

if __name__ == "__main__":
    main()


# In[4]:


from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl

def generate_utm_url(base_url, utm_params):
    parsed_url = urlparse(base_url)
    query_params = dict(parse_qsl(parsed_url.query))

    # NUEVO: Filtrar solo parámetros UTM que no estén vacíos
    filtered_utm_params = {k: v for k, v in utm_params.items() if v.strip()}

    query_params.update(filtered_utm_param) #Se reemplaza por valor NUEVO
    updated_query = urlencode(query_params)
    updated_url = urlunparse(parsed_url._replace(query=updated_query))
    return updated_url

def main():
    urls_text = input("Paste website URLs (paste URLs here, then 'done' when finished):\n")
    
    if urls_text.lower() == "done":
        print("No URLs provided.")
        return

    urls = [url.strip() for url in urls_text.strip().split("\n")]

    utm_params = {
        "utm_source": input("Enter source: "),
        "utm_medium": input("Enter medium: "),
        "utm_campaign": input("Enter campaign name: "),
        "utm_content": input("Enter content: "),
        "utm_term": input("Enter term: "),
    }

    # Generate and print UTM-enabled URLs with sequential numbers
    print("\nGenerated UTM-enabled URLs:")
    for i, url in enumerate(urls, start=1):
        utm_url = generate_utm_url(url, utm_params)
        print(f"{i}. {url} => {utm_url}")

if __name__ == "__main__":
    main()


# In[ ]:





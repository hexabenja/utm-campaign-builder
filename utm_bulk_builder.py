#!/usr/bin/env python
# coding: utf-8

# In[1]:

#Libraries to parse and separate URLs
from urllib.parse import urlencode, urlparse, urlunparse, parse_qsl

   
#Defines generate_utm_url as the values of base_url and utm_params
def generate_utm_url(base_url, utm_params):
    parsed_url = urlparse(base_url) #Parses base URL (subdomain, domain and slash)
    query_params = dict(parse_qsl(parsed_url.query)) #Parses the URL queries (Represented as "?")

    # NUEVO: Filters only UTM parameters which are not empty
    filtered_utm_params = {k: v for k, v in utm_params.items() if v.strip()}
    #K is Key, V is Value and v.strip verifies if there are spaces and if there are spaces at the end in V

    query_params.update(filtered_utm_params) #Is replaced by NEW value of utm_params to the new filtered by over function
    updated_query = urlencode(query_params) #Encode the queries (UTM queries)
    updated_url = urlunparse(parsed_url._replace(query=updated_query)) #Construct a new URL string modyfying the query parameters as updated_url
    return updated_url

def main(): #Defines main program
    urls = [] #urls function
    while True: #
        url = input("Enter website URL (or 'done' to finish): ") # The value URL it will be the value inserted
        if url.lower() == "done": #In the case of url.lower it is "done" 
            break #It stops url function of input 
        urls.append(url)

    utm_params = {
        "utm_source": input("Enter source:  "),
        "utm_medium": input("Enter medium: "),
        "utm_campaign": input("Enter campaign name: "),
        "utm_content": input("Enter content: "),
        "utm_term": input("Enter term: "),
    }

    # Generate and print URLs with UTM
    print("\nGenerated UTM-enabled URLs:")
    for url in urls:
        utm_url = generate_utm_url(url, utm_params)
        print(utm_url)

if __name__ == "__main__":
    main()

print("The URL(s) have been successfully completed")
input("Press ENTER to close this window")



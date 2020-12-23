
#https://realpython.com/beautiful-soup-web-scraper-python/
import requests
from bs4 import BeautifulSoup
import sqlLite as sql



def immobiliare(search=False):
    URL = 'https://www.immobiliare.it/vendita-case/rubano/con-piano-terra/?criterio=rilevanza&prezzoMinimo=50000&prezzoMassimo=140000'
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', class_='listing-item_body--content')
 
    listM = []
    listaReturneForSendingMessage = []
    for li in results:
        url_elem = li.find('a')
        if url_elem:
           singleUrl = url_elem.get('href')
           listM.append(str(singleUrl)) 
    # tento di inserire links dalla lista 
    if  not search :      
        listaReturneForSendingMessage = sql.insertIfNotExists("links_table_immobiliare", listM)
        return listaReturneForSendingMessage  
    else:
         returnedList = sql.view("links_table_immobiliare")
         return  returnedList
  



def subito(search=False):
    URL = 'https://www.subito.it/annunci-veneto/vendita/appartamenti/padova/selvazzano-dentro/?ps=20000&pe=130000&szs=100&o='
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('div', class_='jsx-3120895872')
    
    listM = []
    listaReturneForSendingMessage = []
    for li in results:
        url_elem = li.find('a')
        if url_elem:
           singleUrl = url_elem.get('href')
           listM.append(str(singleUrl)) 
    # tento di inserire links dalla lista 
    
    if  not search :   
        listaReturneForSendingMessage = sql.insertIfNotExists("links_table_subito", listM)  
        return listaReturneForSendingMessage  
    else:
         returnedList = sql.view("links_table_subito")
         return  returnedList






def casa(search=False):
    URL = 'https://www.casa.it/vendita/residenziale/selvazzano-dentro?level=piano+terra&mqMin=90&priceMin=50000&priceMax=140000&page='
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    results = soup.find_all('article', class_='srp-card')
    listM = []
    listaReturneForSendingMessage = []

    for li in results:
        url_elem = li.find('a')
        if url_elem:
           singleUrl = url_elem.get('href') 
           listM.append("www.casa.it" +str(singleUrl)) 

        # tento di inserire links dalla lista 
    if  not search :      
        listaReturneForSendingMessage = sql.insertIfNotExists("links_table_casa", listM)
        return listaReturneForSendingMessage  
    else:
         returnedList = sql.view("links_table_casa")
         return  returnedList



# My home agenzia
def myhome(search=False):
    listM = []
    listaReturneForSendingMessage = []

    for i in range(1,4): 
        page = str(i)
        URL = 'http://www.myhomegroup.it/it/cerca?sch_contratto=9&sch_comune%5B%5D=4894&sch_comune%5B%5D=6005&sch_comune%5B%5D=6775&sch_zona%5B%5D=38213&sch_zona%5B%5D=38217&sch_zona%5B%5D=38218&sch_zona%5B%5D=38223&sch_zona%5B%5D=38225&sch_zona%5B%5D=38246&sch_zona%5B%5D=38247&sch_zona%5B%5D=38316&sch_zona%5B%5D=38281&sch_zona%5B%5D=40542&sch_zona%5B%5D=38365&sch_zona%5B%5D=38364&sch_zona%5B%5D=38437&sch_zona%5B%5D=38439&sch_zona%5B%5D=38443&sch_zona%5B%5D=38441&sch_camere=&price_max=140000&mq_min=90&agency_code=&sch_agenzia=&page=' + page
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find_all('div', class_='row')

        for li in results:
            url_elem = li.find('a')
            if url_elem:
                singleUrl = url_elem.get('href') 
                listM.append("http://www.myhomegroup.it" + str(singleUrl)) 

  # tento di inserire links dalla lista 
    if  not search :      
        listaReturneForSendingMessage = sql.insertIfNotExists("links_table_myhome", listM)
        return listaReturneForSendingMessage  
    else:
         returnedList = sql.view("links_table_myhome")
         return  returnedList


# Tecnocasa agenzia
def tecnocasa(search=False):
    listM = []
    listaReturneForSendingMessage = []

    URLS = ["https://www.tecnocasa.it/annunci/immobili/veneto/padova/selvazzano-dentro.html/pag-", "https://www.tecnocasa.it/annunci/immobili/veneto/padova/rubano.html/pag-"]

    for j in URLS:
        for i in range(1,5): 
            page = str(i)
            URL = j + page
            page = requests.get(URL)
            soup = BeautifulSoup(page.content, 'html.parser')

            results = soup.find_all('a', class_='immobileLink')

            for li in results:  
                price = li.find("div", class_="immobiliListaAnnuncioPrezzo").contents[0]
                price =  price.strip()[2:]
                price = price.split(".")[0]
                if price != "" and int(price) >= 40 and int(price) <= 140:
                   singleUrl = li.get('href') 
                   listM.append( str(singleUrl)) 





  # tento di inserire links dalla lista 
    if  not search :      
        listaReturneForSendingMessage = sql.insertIfNotExists("links_table_tecnocasa", listM)
        return listaReturneForSendingMessage  
    else:
      #   print(listM)
         returnedList = sql.view("links_table_tecnocasa")
         return  returnedList



#Inserisce un utente nuovo
def insertUser(user_id, first_name, last_name):
    sql.insertUsers(user_id, first_name, last_name)

def viewUsers():
    return sql.viewUsers()
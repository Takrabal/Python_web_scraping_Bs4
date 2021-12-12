import requests
from bs4 import BeautifulSoup

url='https://www.scopelist.com/'

html_cont=requests.get(url).text
soup = BeautifulSoup(html_cont, 'html.parser')


url_list=[]
content=soup.find_all('h2', {'class':'heading'})
for product in content:
    link='https://www.scopelist.com/'+ product.find('a')['href']
    #print(link)
    url_list.append(link)

#print(url_list)

for links in url_list:
    htm1_cont1=requests.get(links).text
    soup = BeautifulSoup(htm1_cont1, 'html.parser')

    data = soup.findAll('div', {'class':'no-slide'})

    product_list=[]
    for prod_data in data:
        link='https://www.scopelist.com/'+ prod_data.find('a')['href']
        #print(link)
        product_list.append(link)

    for all_data in product_list:
        htm1_cont2=requests.get(all_data).text
        soup = BeautifulSoup(htm1_cont2, 'html.parser')
        product_names  = soup.find('span', {'id':'ctl00_MainContentHolder_lblName'}).text
        spec = soup.find('table', {'class': 'table table-striped'}).text
        prices = soup.find('strong', {'class' : 'latest-price'}).text
        image=soup.find('div', {'class' : 'content'})
        images_link= image.find('img')['data-src']
        
        print("product name")
        print(product_names)

        print("product price")
        print(prices)

        print("Specification of product")
        print(spec)

        print("product's image link")
        print(images_link)
        






    
    


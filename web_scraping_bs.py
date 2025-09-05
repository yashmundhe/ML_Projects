import threading
import requests
from bs4 import BeautifulSoup

url= [
    'https://www.geeksforgeeks.org/artificial-intelligence/introduction-to-langchain/'
]

def fetch_content(url):
    response=requests.get(url)
    soup=BeautifulSoup(response.content,'html.parser')
    print(f'Fetched {(len(soup.text))} charaters from url')

thread=threading.Thread(target=fetch_content,args=(url))
thread.start()

thread.join()

print("All web pages fetched")
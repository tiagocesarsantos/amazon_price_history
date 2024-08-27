import requests
from time import sleep

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36',
    'viewport-width': '777'
}

session = requests.Session()

response = session.get('https://www.amazon.com/', headers=headers)

#attempt = 0
#while response.status_code != 200:
#    attempt+=1
#    print("Trying to access... attempt = ", attempt)
#    sleep(2)
#    response = session.get('https://www.amazon.com/', headers=headers)


# TODO next requests search
#response = session.get('https://example.com/page2')
# exec(open("./fetch_amazon_data.py").read())

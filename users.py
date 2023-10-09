import requests

url = 'https://randomuser.me/a´pi/'
esponse = requests.get(url)

if response.status_code == 200:
    print(response.json())

else: 
    print('Algo ha salido mal')
    print('Codigo del error')
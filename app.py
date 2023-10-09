import requests
#documentacion list all assets
apikey= ''
servidor = 'https//rest.coinapi.io'
endpoint = '/v1/assets?filter_asset_id=EUR;USD;ETH'

url = servidor + endpoint
# diccionario
headers = {
    'X-CoinAPI-Key': apikey
} 

response =requests.get(url, headers=headers)

if response.status_code == 200: #codigo de estado, puede diferencias codigo de
    json_response = response.json())

    for coin in json_response:
        id = coin.get('asset_id') 
        #if (id in ('BTC', 'USD', 'EUR'))

        print(id, '-'coin.get('asset_id'),coin.get('name'), coin.get('type_is_crypto'))
else:
    print('Algo no ha saido bien. Error ', response.satatus_code, response reason)
# response.json()  #va a convertir respusta en json

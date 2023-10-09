import requests
#configuracion
apikey= ''
servidor = 'https//rest.coinapi.io'
endpoint = '/v1/exchangerate'

headers = {
    'X-CoinAPI-Key': apikey
} 
"""
pedir moneda de orgen: BTC
Pedir moneda estino: EUR
IR a la API Y preguntar el valor de cambio
{'asset_base_i: 'BTC, 'asset_id_quote'}
Si hay error, mostrar mensaje
recoger el dato
Mostrar un mensaje: un btc vale lo mismo que 30000 eur
pregunta: quieres consultar de nuevo? (s/n)
"""







#comprobar estao

while seguir == 's':
    origen = input('¿Que moneda quieres cambiar?')
    destino = input('Que monea desear obtener')

    url = servidor + endpoint + '/' + origen + '/' + destino
    #url = f'{servidor}{endpoint}/{origen}/{destino}'

    #peticion
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        #respuesta OK
        #recoger datos de verda
        exchange = response.json()
        rate = exchange['rate']
        print(f'Un {origen} vale lo mismo que {rate} {destino}')
    else:
        print('Error', response.status_code, ':', response.reason)

    
    seguir = ''
    while seguir.lower() not in ('s', 'n'):
    seguir = input('Quieres consultr de nuevo? (s/n)')
    
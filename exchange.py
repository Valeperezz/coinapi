import requests
#configuracion
apikey= '54CC9DB5-A9E5-4DEF-AFCA-BFAEE77C7995'
servidor = 'https//rest.coinapi.io'
endpoint = '/v1/exchangerate'

headers = {
    'X-CoinAPI-Key': apikey
} 
"""
1. Pedir moneda de origen: BTC
2. Pedir moneda destino: EUR
3. IR a la API y preguntar el valor de cambio

    {
    "time": "2017-08-09T14:31:18.3150000Z",
    "asset_id_base": "BTC",
    "asset_id_quote": "USD",
    "rate": 3260.3514321215056208129867667
    }
3.1 si hay error, mostrar mensaje

4. Recoger el dato
5. Mostrar un mensaje: 'Un BTC vale lo mismo que 30000 EUR'
6. Pregunta: ¿Quieres consultar de nuevo? (s/n)
"""




#comprobar estao
seguir = 's'
while seguir == 's':
    #vista
    origen = input('¿Que moneda quieres cambiar?')
    destino = input('Que moneda desear obtener')
    #/vista

    #modelo
    url = servidor + endpoint + '/' + origen + '/' + destino
    #url = f'{servidor}{endpoint}/{origen}/{destino}'

    #peticion
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        #respuesta OK
        #recoger datos de verda
        exchange = response.json()
        rate = exchange['rate']
        # /modelo

        #vista
        print(f'Un {origen} vale lo mismo que {rate} {destino}')
    else:
        #vista
        print('Error', response.status_code, ':', response.reason)
    

    #controlador es uin esta controlando si seguimos o no
    seguir = ''
    while seguir.lower() not in ('s', 'n'):
        seguir = input('Quieres consultar de nuevo? (s/n)')
    
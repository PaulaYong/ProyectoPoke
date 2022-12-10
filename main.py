BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

#Variables fijas de estilo
BRIGHT = '\033[1m'
DIM = '\033[2m'
NORMAL = '\033[22m'
RESET_ALL = '\033[0m'

import requests

def get_pokemons(url='https://pokeapi.co/api/v2/pokemon-form/', offset=0):
    args = {'offset' : offset} if offset else {}

    response = requests.get(url, params = args)

    if response.status_code == 200:

        payload = response.json()
        results = payload.get('results',[])

        if results:
            for pokemon in results:
                name = pokemon['name']
                print(name)
        
        next = input(BRIGHT+CYAN+'\n¿DESEA CONTINUAR LISTA? Y/N'+RESET_ALL).lower()
        if next == 'y':
            get_pokemons(offset=offset+20)

if __name__ == '__main__':
    url = 'https://pokeapi.co/api/v2/pokemon-form/'
    get_pokemons()


def pegar_tipo(poke):
    print(BRIGHT+GREEN+'TIPO', pokemon+RESET_ALL)
    for i in poke['types']:
        print(i['type']['name'])

def pegar_habilidades(poke):
    print(BRIGHT+BLUE+'HABILIDADES DE', pokemon+RESET_ALL)
    for i in poke['abilities']:
        print(i['ability']['name'])


def main ():
    global pokemon
    pokemon = str(input(BRIGHT+'\nIngrese Pokemon : '+RESET_ALL))
    api = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    res = requests.get(api)
    poke=res.json()
    pegar_tipo(poke)
    pegar_habilidades(poke)

if __name__ == '__main__':
    main()
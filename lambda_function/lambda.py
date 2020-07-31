import requests
import json
import os

URL = "https://www.datos.gov.co/resource/32sa-8pi3.json"

def get_information(url):
    response = requests.get(url)
    #print(response.content)
    content = json.loads(response.content)
    #print(content)
    dolar_value = float(content[0]['valor'])
    print(dolar_value)
    return dolar_value

def run():
    dolar_value= get_information(URL)

    pesos_to_dolars = lambda pesos, dolar_value: pesos/ dolar_value
    dolar_to_pesos = lambda dolars, dolar_value: dolars * dolar_value

    menu = """
    Binvenido al conversor de monedas dinámico

    [1] Dolares a pesos
    [2] Pesos a dolares

    Escribe tu opción: 

    """
    os.system('clear')
    choice = input(menu)

    if choice == '1':
        os.system('clear')
        dolars = float(input('¿Cuantos dolares tienes?: '))
        pesos = dolar_to_pesos(dolars, dolar_value)
        print(f'Tienes {pesos} pesos')
    elif choice == '2':
        os.system('clear')
        pesos = float(input('¿Cuantos pesos tienes?: '))
        dolars = pesos_to_dolars(pesos, dolar_value)
        print(f'Tienes {dolars} dolares')

    else:
        os.system('clear')
        print('Elige una opcion correcta')


if __name__ == "__main__":
    run()

import PySimpleGUI as sg
import requests
import json

def main():
    sg.theme('DarkAmber')

    layout = [  [sg.Text('Digite o CEP:'), sg.InputText()],
                [sg.Button('Buscar'), sg.Button('Finalizar')],
                [sg.Output(size=(80,20))]  ]

    window = sg.Window('Buscador de CEP', layout)

    while(True):
        event, values = window.read()
        if(event == sg.WIN_CLOSED or event == 'Finalizar'): 
            print('Finalizando programa.')
            break
        cep = values[0]
        if(tamanhoCep(cep) == False or caracteresCep(cep) == False): 
            print("CEP inválido!\n")
        else:
            print('Buscando... {}\n============================='.format(cep))
            recebeCep(cep)
        
    window.close()


def tamanhoCep(cep):
    if(len(cep) != 8): return False

def caracteresCep(cep):
    for caractere in cep:
        if(ord(caractere)>57 or ord(caractere)<48): return False
    
def recebeCep(cep):
    r = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))
    objeto = json.loads(r.text)
    for k, v in objeto.items():
        if(k == 'erro'): print("\nCEP inexistente!")
        else:
            if(k != '' and v != ''):
                print("{} - {} ".format(k.upper(), v.upper()))
    print("")

main()

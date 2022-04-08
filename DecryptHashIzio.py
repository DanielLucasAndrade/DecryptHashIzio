import json
from base64 import b64decode, b64encode
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
import yaml
import pyperclip as pc
import keyboard

with open('DecryptKey.yaml') as f:
    key = yaml.load(f, Loader=yaml.FullLoader)

key = key['key']

initialization_vector = key = key.encode()


while True:     

    hash = input('Cole a Hash aqui: ')
    hash = hash.replace('"','')
    print("")
    try:
        decipher = AES.new(key, AES.MODE_CBC, initialization_vector)
        plaintext = unpad(decipher.decrypt(b64decode(hash)), AES.block_size).decode("utf-8")
        print('Hash Decryptografada: {}'.format(plaintext))
        finalResult = json.loads(plaintext)
    except:
        print('Hash inválida ou Chave utilizada não é condizente com a Hash')
        input()
        exit()


    if finalResult['m'] == 1:
        metodo = 'GET'
    elif finalResult['m'] == 2:
        metodo = 'POST'
    elif finalResult['m'] == 3:
        metodo = 'PUT'
    elif finalResult['m'] == 4:
        metodo = 'PATCH'
    elif finalResult['m'] == 5:
        metodo = 'DELETE'
    else:
        metodo = ''

    try:
        print('\nToken: {}'.format(finalResult['t']))
    except:
        print('\nToken: {}'.format(finalResult['j']))
    print('Método: {}'.format(metodo))
    print('URL Api: {}'.format(finalResult['u']))
    try:
        print('Objeto da Requisição: {}'.format(finalResult['b']))
    except:
        pass
    print('Data da Requisição: {}'.format(finalResult['d']))
    print('\nToken copiado para o clipboard.')

    pc.copy(finalResult['t'])
    print('')
        

# criar .exe (pyinstaller --onefile example.py)

import pyautogui as py
import time
import random
import uuid
import mysql.connector
import hashlib
import os
from dotenv import load_dotenv, dotenv_values
import itertools
from colorama import init, Fore, Back, Style
import threading
from cryptography.fernet import Fernet
import io

# # hash MD5 original
# original_hash = "e10adc3949ba59abbe56e057f20f883e"

# # lista de caracteres a serem usados na busca
# caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

# # tentar todas as combinações possíveis de strings
# for length in range(1, 6):  # procurar por strings de até 5 caracteres
#     for attempt in itertools.product(caracteres, repeat=length):
#         attempt_str = "".join(attempt)
#         hash_obj = hashlib.md5(attempt_str.encode())
#         if hash_obj.hexdigest() == original_hash:
#             print("A string original é:", attempt_str)
#             break

# # Crie uma chave de criptografia
# key = Fernet.generate_key()

# # Salve a chave em um arquivo
# with open('key.key', 'wb') as key_file:
#     key_file.write(key)

# # Carregue a chave a partir do arquivo
# with open('key.key', 'rb') as key_file:
#     key = key_file.read()

# Crie um objeto Fernet com a chave
# fernet = Fernet(key)

# Leia o conteúdo do arquivo .env
# with open('.env', 'rb') as env_file:
#     env_content = env_file.read()

# Criptografe o conteúdo do arquivo .env
# encrypted_content = fernet.encrypt(env_content)

# Salve o conteúdo criptografado em um novo arquivo
# with open('encrypted.env', 'wb') as encrypted_file:
#     encrypted_file.write(encrypted_content)

init(convert=True)

load_dotenv()

# Carrega a chave de criptografia do arquivo key.key
with open('./key.key', 'rb') as key_file:
    key = key_file.read()

# Cria um objeto Fernet com a chave
fernet = Fernet(key)

# Lê o conteúdo do arquivo .env criptografado
with open('./encrypted.env', 'rb') as encrypted_file:
    encrypted_content = encrypted_file.read()

# Descriptografa o conteúdo do arquivo .env
decrypted_content = fernet.decrypt(encrypted_content)

# Converte o conteúdo descriptografado em um objeto stream
stream = io.StringIO(decrypted_content.decode())

# Converte o objeto stream em um dicionário
env_vars = dotenv_values(stream=stream)

# Conecta ao banco de dados usando as variáveis de ambiente carregadas
mydb = mysql.connector.connect(
    host=env_vars["DB_HOST"],
    user=env_vars["DB_USER"],
    password=env_vars["DB_PASSWORD"],
    database=env_vars["DB_NAME"]
)

# busca o endereço mac do adaptador de rede
mac = uuid.getnode()
# print(mac)
# converte o endereço mac em um UUID
hardware_id = uuid.UUID(int=mac)
# print(hardware_id)

# obter a representação hexadecimal do UUID
uuid_hex = hardware_id.hex

texto_codificado = uuid_hex.encode("utf-8")

hash_object = hashlib.md5(texto_codificado)
md5_hash = hash_object.hexdigest()

# print(md5_hash)

# Chave de acesso do usuário
api_key = md5_hash

# Variáveis Principais
logged = False


while True:
    if mydb.is_connected:
        controller = mydb.cursor()
        updateMac = "UPDATE users SET uuid = %s"
        updateParameters = ([mac])
        controller.execute(updateMac, updateParameters)
        regVerify = "SELECT * FROM users WHERE api_key = %s AND uuid = %s"
        parameters = (api_key, mac)
        controller.execute(regVerify, parameters)
        uuidVerify = controller.fetchone()
        if uuidVerify:
            print(
                Fore.RED + 'Máquina Registrada. Faça o login...' + Style.RESET_ALL)
            print('')
            username = input('Informe seu Usuário:')
            password = input('Informe sua Senha:')
            if username != '' and password != '':
                mydb.connect()
                # Preparar a consulta SQL
                query = (
                    "SELECT * FROM users WHERE username = %s AND password = %s AND status = 'ativo'")

                # Executar a consulta SQL
                controller.execute(query, (username, password))
                result = controller.fetchone()
                if result:
                    print(Fore.GREEN +
                          "Usuário autenticado com sucesso!" + Style.RESET_ALL)
                    logged = True
                    print('')
                    print(Fore.GREEN +
                          'Inicializando o BOT. Aguarde...' + Style.RESET_ALL)
                    time.sleep(random.randint(5, 15))
                    print(
                        Fore.GREEN + 'BOT Iniciado. Aguardando início da TG.' + Style.RESET_ALL)

                    # Variáveis Principais
                    cValue = 0.9
                    final = False
                    inTG = False

                    while True:
                        # Se achar o icone da TG
                        for i in range(5, 0, -1):
                            iconTG_i = py.locateOnScreen(f'./prints/icontg_1.PNG', confidence=cValue)
                        if iconTG_i:
                            py.press('o')

                        time.sleep(2)    
                        
                        
                        # Se achar botão Channel Select
                        for i in range(5, 0, -1):
                            channelSelect_i = py.locateOnScreen(f'./prints/channelSelect_{i}.PNG', confidence=cValue)
                        if channelSelect_i:
                            x, y = py.center(channelSelect_i)
                            py.click(x, y)

                        time.sleep(2)   
                        
                        # Se achar canal mWar
                        for i in range(5, 0, -1):
                            mWar_i = py.locateOnScreen(f'./prints/mwar_{i}.PNG', grayscale=True, confidence=0.75)
                        if mWar_i:
                            x, y = py.center(mWar_i)
                            py.doubleClick(x, y)
                            time.sleep(1)

                            # Se achar canal mWar
                            for i in range(5, 0, -1):
                                btnYes_i = py.locateOnScreen(f'./prints/btnYes_{i}.PNG', confidence=cValue)
                            if btnYes_i:
                                x, y = py.center(btnYes_i)
                                py.doubleClick(x, y)
                                time.sleep(1)

                            inTG = True

                        time.sleep(2)

                        # Se achar icone de morte
                        for i in range(5, 0, -1):
                            iconDeath_i = py.locateOnScreen(f'./prints/iconDeath_{i}.PNG', confidence=cValue)
                        if iconDeath_i:
                            # Se achar o botão OK
                            for i in range(5, 0, -1):
                                btnOk_i = py.locateOnScreen(f'./prints/btnOk_{i}.PNG', confidence=cValue)
                            if btnOk_i:
                                x, y = py.center(btnOk_i)
                                py.click(x, y)

                        time.sleep(2)   

                        # Se achar o botão OK
                        for i in range(5, 0, -1):
                            btnOk_i = py.locateOnScreen(f'./prints/btnOk_{i}.PNG', confidence=cValue)
                        if btnOk_i:
                            x, y = py.center(btnOk_i)
                            py.click(x, y)

                        time.sleep(2)   

                        # Se acha o icone de teleport
                        for i in range(5, 0, -1):
                            wrap_i = py.locateOnScreen(f'./prints/wrap_{i}.PNG', confidence=cValue)
                        if wrap_i:
                            x, y = py.center(wrap_i)
                            py.click(x, y)
                            inTG = True

                        time.sleep(2)

                        # Se acha o botão Confirm
                        for i in range(5, 0, -1):
                            btnConfirm_i = py.locateOnScreen(f'./prints/btnConfirm_{i}.PNG', confidence=cValue)
                        if btnConfirm_i:
                            x, y = py.center(btnConfirm_i)
                            py.click(x, y)

                            # Se encontra o botão OK
                            for i in range(5, 0, -1):
                                btnOk_i = py.locateOnScreen(f'./prints/btnOk_{i}.PNG', confidence=cValue)
                            if btnOk_i:
                                x, y = py.center(btnOk_i)
                                py.click(x, y)

                                # Se achar canal channel 7
                                for i in range(5, 0, -1):
                                    channel7_i = py.locateOnScreen(f'./prints/channel7_{i}.PNG', confidence=cValue)
                                if channel7_i:
                                    x, y = py.center(channel7_i)
                                    py.doubleClick(x, y)
                                    time.sleep(1)
                        
                        time.sleep(2)

                        # Se encontra o botão OK
                        for i in range(5, 0, -1):
                            btnOk_i = py.locateOnScreen(f'./prints/btnOk_{i}.PNG', confidence=cValue)
                        if btnOk_i:
                            x, y = py.center(btnOk_i)
                            py.click(x, y)

                        time.sleep(2)
                else:
                    print(
                        Fore.RED + "Credenciais inválidas ou Cadastro Inativo. Tente novamente! \n Caso o problema persista, entre me contato com o suporte!" + Style.RESET_ALL)
            else:
                print(
                    Fore.RED + 'Algo está incorreto. Tente novamente!' + Style.RESET_ALL)
        else:
            print(Fore.RED + 'Não reconhecemos está máquina!' + Style.RESET_ALL)
            a = input('Já comprou o BOT? (y=sim/n=não)')
            if a == 'Y' or a == 'y':
                userNew = input('Informe um usuário:')
                passNew = input('Informe uma senha:')

                # def createTable():
                #     controller = mydb.cursor()
                #     controller.execute(
#                             "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), api_key VARCHAR(255), uuid VARCHAR(255), payment_status VARCHAR(255), tempo VARCHAR(255), period VARCHAR(255), status VARCHAR(255))")

                # cadastra usuario na tabela do banco
                sql = "INSERT INTO users (username, password, api_key, uuid, payment_status, tempo, period, status) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                val = (userNew, passNew, api_key, mac, "aberto", "0", "mensal", "inativo")
                controller.execute(sql, val)
                mydb.commit()

                print(Fore.GREEN + 'Usuário Criado com Sucesso! Validando informações. Aguarde...'  + Style.RESET_ALL)
            else:
                print(Fore.RED + 'Então vai comprar... kkkk'  + Style.RESET_ALL)
                time.sleep(5)

            # a = input('Você já comprou o BOT? (y = sim / n = não)')
            # if a == 'y' or a == 'Y':
            #     b = input('Já recebeu a sua Key? (y = sim / n = não)')
            #     if b == 'y' or b == 'Y':
            #         print(
            #             'Tente acessar novamente... Caso o erro persista, entre em contato com o suporte através do Telegram (https://t.me/cabot).')
            #     elif b == 'n' or b == 'N':
            #         print(
            #             'Caso não tenha recebido por e-mail, entre em contato com o suporte através do Telegram (https://t.me/cabot).')
            # elif a == 'n' or a == 'N':
            #     print(
            #         'Efetue a compra do BOT pelo Telegram (https://t.me/cabot). Entre em contato para saber mais! <3')
            # else:
            #     print(
            #         Fore.YELLOW + 'Por favor, responda apenas com Y ou N.' + Style.RESET_ALL)
    elif mydb.is_connected != True:
        print(Fore.RED + 'Deconectado. Tente novamente!' + Style.RESET_ALL)
    else:
        print(Fore.RED + 'Verifique sua conexão e tente novamente!' + Style.RESET_ALL)

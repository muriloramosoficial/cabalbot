# Colocar o código dentro de um 'While True' para ficar em loop*
# Colocar cada if, dentro de um While para que fique aguardando alguma ação ocorrer*

# Se o icone do TG aparecer, aperta 'O' para abrir o Menu, da 1 clique em 'Channel Select' e da 2 cliques no Canal Desejado e aperte 'Yes' na tela seguinte para confirmar a entrada.

# Enquanto o icone de morte não aparecer, ficar pressionando 'Z 1 2 3 4 5 6 7 8 9'. (Repetir processo até o fim da partida)

# Se aparecer o icone de morte, de 1 clique no botão Ok. Aguarde aparecer os icones de Teleporte e quando aparecer clique em um para dar respawn. (Repetir processo até o fim da partida)

# Quando acaba a partida, aguardar aparecer a tela de 'Report', dar 1 clique no botão 'Confirm', aguarde até que apareça o botão Ok e de 1 clique no botão Ok. (atualizar variável booleana final para True)

import pyautogui as py
import time
import random
import requests
import uuid
import mysql.connector
import hashlib

mydb = mysql.connector.connect(
    host="45.132.157.1",
    user="u350851676_cabot",
    password="0Pe>LO;@i&Hp",
    database="u350851676_cabot"
)

# busca o endereço mac do adaptador de rede
mac = uuid.getnode()
print(mac)
# converte o endereço mac em um UUID
hardware_id = uuid.UUID(int=mac)
print(hardware_id)

# obter a representação hexadecimal do UUID
uuid_hex = hardware_id.hex

texto_codificado = uuid_hex.encode("utf-8")

hash_object = hashlib.md5(texto_codificado)
md5_hash = hash_object.hexdigest()

print(md5_hash)

# Chave de acesso do usuário
api_key = md5_hash

# controller = mydb.cursor()
# controller.execute(
#     "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), email VARCHAR(255), password VARCHAR(255), username VARCHAR(255), api_key VARCHAR(255), uuid VARCHAR(255))")

# cadastra usuario na tabela do banco
# sql = "INSERT INTO users (name, email, password, api_key, uuid) VALUES (%s, %s, %s, %s, %s)"
# val = ("John Doe", "johndoe@example.com", "1234567", api_key, mac)
# controller.execute(sql, val)
# mydb.commit()

# Variáveis Principais
logged = False

if mydb.is_connected:
    controller = mydb.cursor()
    controller = mydb.cursor()
    regVerify = "SELECT * FROM users WHERE api_key = %s AND uuid = %s"
    parameters = (api_key, mac)
    controller.execute(regVerify, parameters)
    uuidVerify = controller.fetchone()
    if uuidVerify:
        print('Máquina já resgistrada. Faça login para prosseguir...')
        print('')
        username = input('Informe seu usuário:')
        password = input('Informe sua senha:')
        if username != '' and password != '':
            # Preparar a consulta SQL
            query = ("SELECT * FROM users WHERE email = %s AND password = %s")

            # Executar a consulta SQL
            controller.execute(query, (username, password))
            result = controller.fetchone()
            if result:
                print("Usuário autenticado com sucesso!")
                print('')

            else:
                print("Usuário ou senha inválidos. Tente novamente!")
        else:
            print('Algo está incorreto. Tente novamente!')
    else:
        a = input('Você já comprou o BOT? (y = sim / n = não)')
        if a == 'y' or a == 'Y':
            b = input('Já recebeu a sua Key? (y = sim / n = não)')
            if b == 'y' or b == 'Y':
                print('Tente acessar novamente... Caso o erro persista, entre em contato com o suporte através do Telegram (https://t.me/cabot).')
            elif b == 'n' or b == 'N':
                print(
                    'Caso não tenha recebido por e-mail, entre em contato com o suporte através do Telegram (https://t.me/cabot).')
        elif a == 'n' or a == 'N':
            print('Efetue a compra do BOT pelo Telegram (https://t.me/cabot). Entre em contato para saber mais! <3')
        else:
            print('Por favor, responda apenas com Y ou N.')
else:
    print('Verifique sua conexão e tente novamente!')


# # cadastra usuario na tabela do banco
# sql = "INSERT INTO users (name, email, password, api_key, uuid) VALUES (%s, %s, %s, %s, %s)"
# val = ("John Doe", "johndoe@example.com", "1234567", api_key, mac)
# mycursor.execute(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "user inserted.")

# # lê os usuarios no banco
# mycursor = mydb.cursor()
# mycursor.execute("SELECT * FROM users")
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

# # Variáveis Principais
# final = False
# inGameTGBool = False
# iconMortBool = False
# botActive = False

# def finish():
#     print('fim da TG')
#     finish = py.locateOnScreen('local da imagem')  # imagem do botao confirm
#     if finish:
#         x, y = py.center(finish)
#         py.click(x, y)

#         time.sleep(3)

#         btnOk = py.locateOnScreen('local da imagem')  # imagem do botão OK
#         if btnOk:
#             x, y = py.center(btnOk)
#             py.click(x, y)


# def pushSkills():
#     print('Soltando Skills')

#     if inGameTGBool == True:
#         py.press('z')
#         py.press('1')
#         py.press('2')
#         py.press('3')
#         py.press('4')
#         py.press('5')
#         py.press('6')
#         py.press('7')
#         py.press('8')
#         py.press('9')
#     else:
#         print('Fora da TG.')


# def iconTG_finder():
#     print('Identifica icone da TG.')

#     py.press('o')
#     time.sleep(3)

#     inGameTGBool = False
#     btnChannelSelectBool = False
#     btnChannelSelect = py.locateOnScreen('local da imagem')
#     x, y = py.center(btnChannelSelect)
#     print('Aguardando botão Channel Select aparecer...')
#     while btnChannelSelectBool == False:
#         if btnChannelSelect:
#             print('Botão Channel Select encontrado. Efetuando o click...')
#             py.click(x, y)
#             btnChannelSelectBool = True
#         else:
#             print('Botão Channel Select não encontrado!')

#     mwarSelectionBool = False
#     mwarSelection = py.locateOnScreen('local da imagem')
#     x, y = py.center(mwarSelection)
#     while mwarSelectionBool == False:
#         if mwarSelection:
#             print('M.WAR encontrado. Efetuando click...')
#             py.doubleClick(x, y)
#             mwarSelectionBool = True
#         else:
#             print('M.WAR não encontrado!')

#     btnYesBool = False
#     btnYes = py.locateOnScreen('local da imagem')
#     x, y = py.center(btnYes)
#     print('Aguardando botão Channel Select aparecer...')
#     while btnYesBool == False:
#         if btnYes:
#             print('Botão Yes encontrado. Efetuando o click...')
#             py.click(x, y)
#             btnYesBool = True
#         else:
#             print('Botão Yes não encontrado!')


# def death():
#     print('Icone de Morte encontrado!')
#     iconMort = py.locateOnScreen('local da imagem')
#     if iconMort:
#         inGameTGBool = False
#         iconMort = True
#         btnOk = py.locateOnScreen('local da imagem')
#         if btnOk:
#             x, y = py.center(btnOk)
#             py.click(x, y)

#             time.sleep(3)

#             teleport = py.locateOnScreen('local da imagem')
#             if teleport:
#                 x, y = py.center(teleport)
#                 py.click(x, y)
#                 iconMort = False
#         else:
#             print('Botão OK não encontrado!')
#     else:
#         inGameTGBool = True
#         print('Icon Mort não encontrado!')


# # Main While
# while True:
#     iconTGBool = False
#     iconTG = py.locateOnScreen('local da imagem')
#     while iconTGBool == False:
#         time.sleep(1)
#         iconTG = py.locateOnScreen('local da imagem')
#         if iconTG:
#             iconTG_finder()
#             iconTGBool = True

#     while inGameTGBool == True:
#         time.sleep(random.randint(1, 3))
#         pushSkills()

#     while iconMortBool == False:
#         time.sleep(random.randint(1, 3))
#         death()

#     while final == False:
#         time.sleep(random.randint(1, 3))
#         finish()

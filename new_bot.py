# Colocar o código dentro de um 'While True' para ficar em loop*
# Colocar cada if, dentro de um While para que fique aguardando alguma ação ocorrer*

# Se o icone do TG aparecer, aperta 'O' para abrir o Menu, da 1 clique em 'Channel Select' e da 2 cliques no Canal Desejado e aperte 'Yes' na tela seguinte para confirmar a entrada.

# Enquanto o icone de morte não aparecer, ficar pressionando 'Z 1 2 3 4 5 6 7 8 9'. (Repetir processo até o fim da partida)

# Se aparecer o icone de morte, de 1 clique no botão Ok. Aguarde aparecer os icones de Teleporte e quando aparecer clique em um para dar respawn. (Repetir processo até o fim da partida)

# Quando acaba a partida, aguardar aparecer a tela de 'Report', dar 1 clique no botão 'Confirm', aguarde até que apareça o botão Ok e de 1 clique no botão Ok. (atualizar variável booleana final para True)

# criar .exe (pyinstaller --onefile example.py)

import pyautogui as py
import time
import random
import uuid
import mysql.connector
import hashlib
import os
from dotenv import load_dotenv
import itertools
from colorama import init, Fore, Back, Style

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

init(convert=True)

load_dotenv()

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
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


# def createTable():
#     controller = mydb.cursor()
#     controller.execute(
#         "CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), telegram VARCHAR(255), whatsapp VARCHAR(255), email VARCHAR(255), username VARCHAR(255), password VARCHAR(255), api_key VARCHAR(255), uuid VARCHAR(255), payment_status VARCHAR(255), tempo VARCHAR(255), period VARCHAR(255))")


# def userCreate():
#     # cadastra usuario na tabela do banco
#     sql = "INSERT INTO users (name, telegram, whatsapp, email, username, password, api_key, uuid, payment_status, tempo, period) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     val = ("John Doe", "@johndoe", "+5545991392793", "johndoe@example.com",
#            "johndoe", "toor", api_key, mac, "pago", "1", "ano")
#     controller.execute(sql, val)
#     mydb.commit()


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
                Fore.RED + 'Máquina já resgistrada. Faça login para prosseguir...' + Style.RESET_ALL)
            print('')
            username = input('Informe seu Usuário:')
            password = input('Informe sua Senha:')
            if username != '' and password != '':
                # Preparar a consulta SQL
                query = (
                    "SELECT * FROM users WHERE username = %s AND password = %s")

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
                    final = False
                    inGameTGBool = False
                    iconMortBool = False
                    botActive = False
                    confidenceValue = 0.7

                    def finish():
                        # print('fim da TG')
                        # imagem do botao confirm
                        finish = py.locateOnScreen('./prints/confirm.PNG', confidence=confidenceValue)
                        finish_1 = py.locateOnScreen('./prints/confirm_1.PNG', confidence=confidenceValue)
                        finish_2 = py.locateOnScreen('./prints/confirm_2.PNG', confidence=confidenceValue)
                        finish_3 = py.locateOnScreen('./prints/confirm_3.PNG', confidence=confidenceValue)
                        finish_4 = py.locateOnScreen('./prints/confirm_4.PNG', confidence=confidenceValue)
                        finish_5 = py.locateOnScreen('./prints/confirm_5.PNG', confidence=confidenceValue)
                        if finish or finish_1 or finish_2 or finish_3 or finish_4 or finish_5:
                            x, y = py.center(
                                finish or finish_1 or finish_2 or finish_3 or finish_4 or finish_5)
                            py.click(x, y)

                            time.sleep(3)

                            btnOk = py.locateOnScreen('./prints/ok.PNG', confidence=confidenceValue)
                            btnOk_1 = py.locateOnScreen('./prints/ok_1.PNG', confidence=confidenceValue)
                            btnOk_2 = py.locateOnScreen('./prints/ok_2.PNG', confidence=confidenceValue)
                            btnOk_3 = py.locateOnScreen('./prints/ok_3.PNG', confidence=confidenceValue)
                            btnOk_4 = py.locateOnScreen('./prints/ok_4.PNG', confidence=confidenceValue)
                            btnOk_5 = py.locateOnScreen('./prints/ok_5.PNG', confidence=confidenceValue)
                            if btnOk or btnOk_1 or btnOk_2 or btnOk_3 or btnOk_4 or btnOk_5:
                                x, y = py.center(
                                    btnOk or btnOk_1 or btnOk_2 or btnOk_3 or btnOk_4 or btnOk_5)
                                py.click(x, y)
                                final = True
                                if final == True:
                                    print(
                                        Fore.GREEN + 'Chegamos ao final. Vamos voltar para um Canal padrão.' + Style.RESET_ALL)
                                else:
                                    print(
                                        Fore.RED + 'Final não está TRUE.' + Style.RESET_ALL)

                    def pushSkills():
                        print(Fore.GREEN + 'Soltando Skills' + Style.RESET_ALL)

                        if inGameTGBool == True:
                            py.press('z')
                            py.press('1')
                            py.press('2')
                            py.press('3')
                            py.press('4')
                            py.press('5')
                            py.press('6')
                            py.press('7')
                            py.press('8')
                            py.press('9')
                        else:
                            print(Fore.RED + 'Fora da TG.' + Style.RESET_ALL)

                    def iconTG_finder():
                        py.press('o')
                        time.sleep(3)

                        inGameTGBool = False
                        btnChannelSelectBool = False
                        btnChannelSelect = py.locateOnScreen(
                            './prints/channel_select.PNG', grayscale=True, confidence=confidenceValue)
                        btnChannelSelect_1 = py.locateOnScreen(
                            './prints/channel_select_1.PNG', grayscale=True, confidence=confidenceValue)
                        btnChannelSelect_2 = py.locateOnScreen(
                            './prints/channel_select_2.PNG', grayscale=True, confidence=confidenceValue)
                        btnChannelSelect_3 = py.locateOnScreen(
                            './prints/channel_select_3.PNG', grayscale=True, confidence=confidenceValue)
                        btnChannelSelect_4 = py.locateOnScreen(
                            './prints/channel_select_4.PNG', grayscale=True, confidence=confidenceValue)
                        btnChannelSelect_5 = py.locateOnScreen(
                            './prints/channel_select_5.PNG', grayscale=True, confidence=confidenceValue)
                        print(
                            Fore.YELLOW + 'Aguardando botão Channel Select aparecer...' + Style.RESET_ALL)
                        while btnChannelSelectBool == False:
                            if btnChannelSelect or btnChannelSelect_1 or btnChannelSelect_2 or btnChannelSelect_3 or btnChannelSelect_4 or btnChannelSelect_5:
                                print(
                                    Fore.GREEN + 'Botão Channel Select encontrado. Efetuando o click...' + Style.RESET_ALL)
                                x, y = py.center(
                                    btnChannelSelect or btnChannelSelect_1 or btnChannelSelect_2 or btnChannelSelect_3 or btnChannelSelect_4 or btnChannelSelect_5)
                                py.click(x, y)
                                btnChannelSelectBool = True
                                print(btnChannelSelectBool)
                            else:
                                print(
                                    Fore.RED + 'Botão Channel Select não encontrado!' + Style.RESET_ALL)
                                time.sleep(5)

                        mwarSelectionBool = False
                        mwarSelection = py.locateOnScreen('./prints/mwar.PNG', confidence=confidenceValue)
                        mwarSelection_1 = py.locateOnScreen(
                            './prints/mwar_1.PNG', confidence=confidenceValue)
                        mwarSelection_2 = py.locateOnScreen(
                            './prints/mwar_2.PNG', confidence=confidenceValue)
                        mwarSelection_3 = py.locateOnScreen(
                            './prints/mwar_3.PNG', confidence=confidenceValue)
                        mwarSelection_4 = py.locateOnScreen(
                            './prints/mwar_4.PNG', confidence=confidenceValue)
                        mwarSelection_5 = py.locateOnScreen(
                            './prints/mwar_5.PNG', confidence=confidenceValue)
                        while mwarSelectionBool == False:
                            if mwarSelection or mwarSelection_1 or mwarSelection_2 or mwarSelection_3 or mwarSelection_4 or mwarSelection_5:
                                print(Fore.GREEN +
                                      'M.WAR encontrado. Efetuando click...' + Style.RESET_ALL)
                                x, y = py.center(
                                    mwarSelection or mwarSelection_1 or mwarSelection_2 or mwarSelection_3 or mwarSelection_4 or mwarSelection_5)
                                py.doubleClick(x, y)
                                mwarSelectionBool = True
                            else:
                                print(
                                    Fore.RED + 'M.WAR não encontrado!' + Style.RESET_ALL)

                        btnYesBool = False
                        btnYes = py.locateOnScreen('./prints/yes.PNG', confidence=confidenceValue)
                        btnYes_1 = py.locateOnScreen('./prints/yes_1.PNG', confidence=confidenceValue)
                        btnYes_2 = py.locateOnScreen('./prints/yes_2.PNG', confidence=confidenceValue)
                        btnYes_3 = py.locateOnScreen('./prints/yes_3.PNG', confidence=confidenceValue)
                        btnYes_4 = py.locateOnScreen('./prints/yes_4.PNG', confidence=confidenceValue)
                        btnYes_5 = py.locateOnScreen('./prints/yes_5.PNG', confidence=confidenceValue)
                        print(Fore.YELLOW +
                              'Aguardando botão Channel Select aparecer...' + Style.RESET_ALL)
                        while btnYesBool == False:
                            if btnYes or btnYes_1 or btnYes_2 or btnYes_3 or btnYes_4 or btnYes_5:
                                print(
                                    Fore.GREEN + 'Botão Yes encontrado. Efetuando o click...' + Style.RESET_ALL)
                                x, y = py.center(
                                    btnYes or btnYes_1 or btnYes_2 or btnYes_3 or btnYes_4 or btnYes_5)
                                py.click(x, y)
                                btnYesBool = True
                            else:
                                print(
                                    Fore.RED + 'Botão Yes não encontrado!' + Style.RESET_ALL)

                    def death():
                        print(Fore.GREEN +
                              'Icone de Morte encontrado!' + Style.RESET_ALL)
                        iconMort = py.locateOnScreen('./prints/icon_mort.PNG', confidence=confidenceValue)
                        iconMort_1 = py.locateOnScreen(
                            './prints/icon_mort_1.PNG', confidence=confidenceValue)
                        iconMort_2 = py.locateOnScreen(
                            './prints/icon_mort_2.PNG', confidence=confidenceValue)
                        iconMort_3 = py.locateOnScreen(
                            './prints/icon_mort_3.PNG', confidence=confidenceValue)
                        iconMort_4 = py.locateOnScreen(
                            './prints/icon_mort_4.PNG', confidence=confidenceValue)
                        iconMort_5 = py.locateOnScreen(
                            './prints/icon_mort_5.PNG', confidence=confidenceValue)
                        if iconMort or iconMort_1 or iconMort_1 or iconMort_1 or iconMort_1 or iconMort_1:
                            inGameTGBool = False
                            iconMort = True
                            btnOk = py.locateOnScreen('./prints/ok.PNG')
                            btnOk_1 = py.locateOnScreen('./prints/ok_1.PNG', confidence=confidenceValue)
                            btnOk_2 = py.locateOnScreen('./prints/ok_2.PNG', confidence=confidenceValue)
                            btnOk_3 = py.locateOnScreen('./prints/ok_3.PNG', confidence=confidenceValue)
                            btnOk_4 = py.locateOnScreen('./prints/ok_4.PNG', confidence=confidenceValue)
                            btnOk_5 = py.locateOnScreen('./prints/ok_5.PNG', confidence=confidenceValue)
                            if btnOk or btnOk_1 or btnOk_2 or btnOk_3 or btnOk_4 or btnOk_5:
                                x, y = py.center(
                                    btnOk or btnOk_1 or btnOk_2 or btnOk_3 or btnOk_4 or btnOk_5)
                                py.click(x, y)

                                time.sleep(3)

                                teleport = py.locateOnScreen(
                                    './prints/wrap.PNG', confidence=confidenceValue)
                                teleport_1 = py.locateOnScreen(
                                    './prints/wrap_1.PNG', confidence=confidenceValue)
                                teleport_2 = py.locateOnScreen(
                                    './prints/wrap_2.PNG', confidence=confidenceValue)
                                teleport_3 = py.locateOnScreen(
                                    './prints/wrap_3.PNG', confidence=confidenceValue)
                                teleport_4 = py.locateOnScreen(
                                    './prints/wrap_4.PNG', confidence=confidenceValue)
                                teleport_5 = py.locateOnScreen(
                                    './prints/wrap_5.PNG', confidence=confidenceValue)
                                if teleport or teleport_1 or teleport_2 or teleport_3 or teleport_4 or teleport_5:
                                    x, y = py.center(
                                        teleport or teleport_1 or teleport_2 or teleport_3 or teleport_4 or teleport_5)
                                    py.click(x, y)
                                    iconMort = False
                            else:
                                print(
                                    Fore.RED + 'Botão OK não encontrado!' + Style.RESET_ALL)
                        else:
                            inGameTGBool = True
                            print(
                                Fore.RED + 'Icon Mort não encontrado!' + Style.RESET_ALL)

                    # Main While
                    while True:
                        iconTGBool = False
                        iconTG = py.locateOnScreen('./prints/tg.PNG', confidence=confidenceValue)
                        iconTG_1 = py.locateOnScreen('./prints/tg_1.PNG', confidence=confidenceValue)
                        iconTG_2 = py.locateOnScreen('./prints/tg_2.PNG', confidence=confidenceValue)
                        iconTG_3 = py.locateOnScreen('./prints/tg_3.PNG', confidence=confidenceValue)
                        iconTG_4 = py.locateOnScreen('./prints/tg_4.PNG', confidence=confidenceValue)
                        iconTG_5 = py.locateOnScreen('./prints/tg_5.PNG', confidence=confidenceValue)
                        iconTG_6 = py.locateOnScreen('./prints/tg_6.PNG', confidence=confidenceValue)
                        iconTG_7 = py.locateOnScreen('./prints/tg_7.PNG', confidence=confidenceValue)
                        iconTG_8 = py.locateOnScreen('./prints/tg_8.PNG', confidence=confidenceValue)
                        iconTG_9 = py.locateOnScreen('./prints/tg_9.PNG', confidence=confidenceValue)
                        iconTG_10 = py.locateOnScreen('./prints/tg_10.PNG', confidence=confidenceValue)
                        while iconTGBool == False:
                            time.sleep(1)
                            iconTG = py.locateOnScreen('./prints/tg.PNG', confidence=confidenceValue)
                            iconTG_1 = py.locateOnScreen('./prints/tg_1.PNG', confidence=confidenceValue)
                            iconTG_2 = py.locateOnScreen('./prints/tg_2.PNG', confidence=confidenceValue)
                            iconTG_3 = py.locateOnScreen('./prints/tg_3.PNG', confidence=confidenceValue)
                            iconTG_4 = py.locateOnScreen('./prints/tg_4.PNG', confidence=confidenceValue)
                            iconTG_5 = py.locateOnScreen('./prints/tg_5.PNG', confidence=confidenceValue)
                            iconTG_6 = py.locateOnScreen('./prints/tg_6.PNG', confidence=confidenceValue)
                            iconTG_7 = py.locateOnScreen('./prints/tg_7.PNG', confidence=confidenceValue)
                            iconTG_8 = py.locateOnScreen('./prints/tg_8.PNG', confidence=confidenceValue)
                            iconTG_9 = py.locateOnScreen('./prints/tg_9.PNG', confidence=confidenceValue)
                            iconTG_10 = py.locateOnScreen('./prints/tg_10.PNG', confidence=confidenceValue)
                            if iconTG or iconTG_1 or iconTG_2 or iconTG_3 or iconTG_4 or iconTG_5 or iconTG_6 or iconTG_7 or iconTG_8 or iconTG_9 or iconTG_10:
                                iconTG_finder()
                                iconTGBool = True

                        time.sleep(5)        

                        while inGameTGBool == True:
                            time.sleep(random.randint(1, 3))
                            pushSkills()

                        time.sleep(5)

                        while iconMortBool == False:
                            time.sleep(random.randint(1, 3))
                            death()

                        time.sleep(5)

                        while final == False:
                            time.sleep(random.randint(1, 3))
                            finish()
                else:
                    print(
                        Fore.RED + "Usuário ou senha inválidos. Tente novamente!" + Style.RESET_ALL)
            else:
                print(
                    Fore.RED + 'Algo está incorreto. Tente novamente!' + Style.RESET_ALL)
        else:
            a = input('Não reconhecemos está máquina! \n Já comprou o BOT? (y=sim/n=não)')
            if a == 'Y' or a == 'y':
                userNew = input('Informe um usuário:')
                passNew = input('Informe uma senha:')
                emailNew = input('Informe um email:')

                # cadastra usuario na tabela do banco
                sql = "INSERT INTO users (name, telegram, whatsapp, email, username, password, api_key, uuid, payment_status, tempo, period) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = ("John Doe", "@johndoe", "+5545991392793", emailNew,
                    userNew, passNew, api_key, mac, "pago", "1", "ano")
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

import pyautogui as py
import time
import uuid
import hashlib
import mysql.connector
from dotenv import load_dotenv
import os
from cryptography.fernet import Fernet

# Crie uma chave de criptografia
key = Fernet.generate_key()

# Salve a chave em um arquivo
with open('key.key', 'wb') as key_file:
    key_file.write(key)

# Carregue a chave a partir do arquivo
with open('key.key', 'rb') as key_file:
    key = key_file.read()

# Crie um objeto Fernet com a chave
fernet = Fernet(key)

# Leia o conteúdo do arquivo .env
with open('.env', 'rb') as env_file:
    env_content = env_file.read()

# Criptografe o conteúdo do arquivo .env
encrypted_content = fernet.encrypt(env_content)

# Salve o conteúdo criptografado em um novo arquivo
with open('encrypted.env', 'wb') as encrypted_file:
    encrypted_file.write(encrypted_content)

# load_dotenv()

# mydb = mysql.connector.connect(
#     host=os.getenv("DB_HOST"),
#     user=os.getenv("DB_USER"),
#     password=os.getenv("DB_PASSWORD"),
#     database=os.getenv("DB_NAME")
# )

# controller = mydb.cursor()
# controller.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), password VARCHAR(255), api_key VARCHAR(255), uuid VARCHAR(255), payment_status VARCHAR(255), tempo VARCHAR(255), period VARCHAR(255), status VARCHAR(255))")




# # busca o endereço mac do adaptador de rede
# mac = uuid.getnode()
# print(mac)
# # converte o endereço mac em um UUID
# hardware_id = uuid.UUID(int=mac)
# print(hardware_id)

# # obter a representação hexadecimal do UUID
# uuid_hex = hardware_id.hex

# texto_codificado = uuid_hex.encode("utf-8")

# hash_object = hashlib.md5(texto_codificado)
# md5_hash = hash_object.hexdigest()

# print(md5_hash)

# # Chave de acesso do usuário
# api_key = md5_hash


        # # Se achar o icone da TG
        # for i in range(5, 0, -1):
        #     iconTG_i = py.locateOnScreen(f'./prints/icontg_{i}.PNG', grayscale=True, confidence=cValue)
        #     print(i)
        #     time.sleep(2)
        # if iconTG_i:
        #     print(iconTG_i)
        # else:
        #     print(iconTG_i)

        # # Se achar o botão Channel Select
        # for i in range(1, 5):
        #     channelSelect_i = py.locateOnScreen(f'./prints/channelSelect_{i}.PNG', grayscale=True, confidence=cValue)

        # if channelSelect_i:
        #     print(i)
        # else:
        #     print(i)
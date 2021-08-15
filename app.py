# 1. Importar bibliotecas necessárias
import pywhatkit
import keyboard
import time
from datetime import datetime
# 2. Definir para quais contatos iremos enviar as msgs
contatos = ['+558752215605']
# 3. Definir intervalo de envio
while len(contatos) >= 1:
    # enviar mensagens
    pywhatkit.sendwhatmsg(contatos[0], 'Oi! isso é so um teste', datetime.now(
    ).hour, datetime.now().minute + 1)
    time.sleep(60)
    keyboard.press_and_release('ctrl + w')
# 4. Testar!
# Importante
'''
* Conecte seu celular com web.whatsapp.com 1°(Escaneie o código de barras)
* Mantenha ele ligado e com a internet(se não estiver ligado, o whatsapp web pode demorar tempo demais para carregar e o programa, pode não funcionar)
'''


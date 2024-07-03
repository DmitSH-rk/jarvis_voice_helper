import config
import stt
import tts
from fuzzywuzzy import fuzz
from execute_commands import execute_cmd
import time
import pyautogui as pg
import keyboard as kb
import pywhatkit
import datetime
#from selenium import webdriver
#from selenium.webdriver.common.keys import Keys
import requests
print("Джарвис начал работать")
# now = datetime.datetime.now()

# pywhatkit.sendwhatmsg("+77072761863", "hi", int(now.hour), now.minute+1, 0)
listening = False

waiting_for_app_name = False
waiting_for_contact = False  # Добавленные переменные
waiting_for_message = False
contact_to_send = ""
message_to_send =""
def sender(contact_name: str, message:str):
    now = datetime.datetime.now()
    pywhatkit.sendwhatmsg(contact_name, message, int(now.hour), now.minute + 1, 0)
    time.sleep(67)
    pg.press('enter')
#     api_url = "https://whatsapp.com"
#     api_key = "your_api_key_here"

#     headers = {"Authorization": f"Bearer {api_key}"}
#     data = {"contact": contact_name, "message": message}

#     response = requests.post(api_url, headers=headers, data=data)
#     if response.status_code == 200:
#         print("Message sent successfully")
#     else:
#         print("Failed to send message")

# # Пример использования функции для отправки сообщения
# contact_name = "Имя контакта"
# message = "Ваше сообщение"
def open(app: str):
    pg.leftClick(90, 1050)  # 'win' key to open the start menu/search bar
    kb.write(app)
    time.sleep(2.5)
    pg.press('enter')

def va_respond(voice: str):
    global now
    global listening
    global waiting_for_app_name
    global waiting_for_contact
    global waiting_for_message
    global contact_to_send
    global message_to_send 
    print("Вы", '"' + voice + '"')
    
    if not listening:
        if voice in config.db_name():
            tts.va_speak("Слушаю хозяин")
            listening = True
            return
        else:
            listening = False
            return
        
    elif waiting_for_contact:
        contact_to_send = "+77072761863"
        tts.va_speak("Что вы хотите отправить?")
        waiting_for_contact = False
        waiting_for_message = True


    elif waiting_for_message:
        print(contact_to_send)
        message_to_send = voice
        sender(contact_to_send, message_to_send)
        tts.va_speak("Сообщение отправлено")
        listening = False

    elif waiting_for_app_name:
        tts.va_speak(f"Открываю {voice}")
        open(voice)
        waiting_for_app_name = False
        listening = False
        
    else:
        
        cmd = recognize_cmd(voice)
        
        if cmd['cmd'] in config.db_commands().keys():
            if cmd['cmd'] == 'ctime':
                # execute_cmd(cmd['cmd'], tts, stt)
                # listening = False
                tts.va_speak("Кому вы хотите отправить сообщение?")
                time.sleep(3)
                waiting_for_contact = True

            elif cmd['cmd'] == 'open':
                tts.va_speak("Какое приложение вы хотите открыть?")
                waiting_for_app_name = True
                   
            else:

                tts.va_speak("Исполняю хозяин")
                execute_cmd(cmd['cmd'], tts, stt)
                listening = False

def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.db_commands().items():
        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt
                
    return rc

stt.va_listen(va_respond)




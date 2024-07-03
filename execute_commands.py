
from num2t4ru import num2text
import datetime
import webbrowser
import random
import pyautogui as pg

def open(app: str):
    pg.hotkey(80, 1060)
    pg.typewrite(app)
    pg.press('enter')


def execute_cmd(cmd: str, tts, stt):
    global listening
    if cmd == 'thanks':
        text = "Я ваш слуга и раб мой хозяин"
        tts.va_speak(text)
        pass
    # elif cmd == 'ctime':
    #     now = datetime.datetime.now()
    #     text = "Сейчас " + num2text(now.hour) + ' ' + num2text(now.minute)
    #     tts.va_speak(text)
    elif cmd == 'joke':
        jokes = [
            'Идет как-то Айбек по дорожке, пипиську травка щекочет, внезапно гравий пошел, Айбек без пипськи пришел',
            'Толик пошел домой, но вдруг вспомнил, что он вообще то раб Айбека'
        ]
        tts.va_speak(random.choice(jokes))
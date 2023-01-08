from pytube import *
from random import randint
from plyer import notification
import os

# ═╔║╣╠╗╚╝
def modes():
    print("╔═══════════════════════════════╗")
    print("║ 1. video downloader           ║")
    print("║ 2. audio downloader           ║")
    print("╚═══════════════════════════════╝")
    mode = str(input("change mode:"))
    ID = randint(1, 1000)


    def show_downloaded(title):
        notification.notify(
            title="youtube video downloaded",
            message=f"{yt.author}",
            app_icon="icon/icon.ico",
            timeout=5
        )


    if mode == "2":
        link = input('Введите ссылку на видео: ')
        yt = YouTube(link)
        print('Заглавие: ', yt.title) 
        print(f"Автор: {yt.author}\nСкачивание...")
        # youlink.streams.filter(abr='160kbps', progressive=False).first().download('Audio', filename=f'Audio_{ID}.mp3') # .download('Audio', filename=f'Audio_{ID}.mp3')
        yt.streams.filter(abr='160kbps', progressive=False).first().download('Audio', filename=f'Audio_{ID}.mp3')
        show_downloaded(f"{yt.title}")
        print('Успешно скачать с: ', link)
                 
    elif mode == "1":
        link = input('введите ссылку на видео: ')
        yt = YouTube(link)
        print('Заглавие: ', yt.title)
        print(f"Автор: {yt.author}\nСкачивание...")
        yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download('Video', filename=f'Video_{ID}.mp4')
        show_downloaded(f"{yt.title}")
        print('Успешно скачать с: ', link)

modes()


import os
import sys
import pyautogui
import time
from datetime import datetime
import pywhatkit as kit
from gtts import gTTS
from playsound import playsound
import random



def speak(string):
    tts=gTTS(string,lang="tr")
    rand=random.randint(1,10000)
    file="audio-"+str(rand)+".mp3"
    tts.save(file)
    playsound(file)
    os.remove(file)

speak("Mehmetin yerde oku yoktur :)))")

kontrol=1
while kontrol==1:
    mesaj=input("Mesajda yazmasını istediğin özel bir mesaj varsa gir knk yoksa boş bırakabilirsin: ")
    adet=input("Mesajı kaç kez göndereceksiniz Mehmet bey: ")

    speak("İmleci yerleştirin ve uçuş bitene kadar dokunmayın. İyi uçuşlar")
    print("10 saniye içinde imleci mesaj yazmak istediğiniz yere yerleştirin ve arkanıza yaslanın")
    time.sleep(10)
    for i in range(int(adet)):
        pyautogui.typewrite(f"{mesaj,i}")
        pyautogui.press("enter")

    speak("Uçuş tamamlandı.")
    print("Görev tamamdır...")
    print("Yeni görev için: 1\n"
          "Programı kapatmak için: 0")
    girdi=input("Cevabınızı bekliyoruz: ")
    if int(girdi)==0:
        speak("MRK havayollarını tercih ettiğiniz için teşekkür ederiz")
        sys.exit()

# PYHTON
from gtts import gTTS
import os


txt = ("Olá; Sou o computador conversando com vocês.")
tts = gTTS(text=txt, tld='com', lang='pt-BR', slow=False)
# abaixo é apenas um caminho para a gravação do arquivo
# faça o caminho mais apropriado para vc...
tts.save(r"C:\Users\AAA\Documents\GoogleTextToSpeech\test.mp3")

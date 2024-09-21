from gtts import gTTS
from playsound import playsound
import os

# Seslendirilecek metin
metin = "Merhaba, ben Yusuf. Tanıştığımıza memnun oldum."

# Türkçe dilinde metni sese dönüştür
tts = gTTS(text=metin, lang='tr')

# Ses dosyasını kaydet
tts.save("ses.mp3")

# Ses dosyasını oynat
playsound("ses.mp3")

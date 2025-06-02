from transcribe import transcribe_audio
from analyze import analiz_yap, raporu_kaydet

# Yollar
audio_path = "audios/ornek_musteri_gorusmesi.wav"
model_path = "model/vosk-model-small-tr-0.3"

# Transkripsiyon
print("\n🔄 Ses yazıya çevriliyor...")
metin = transcribe_audio(audio_path, model_path)

# Analiz ve kayıt
print("\n🔍 Metin analiz ediliyor...")
rapor = analiz_yap(metin)
raporu_kaydet(rapor)

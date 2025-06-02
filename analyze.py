import json
import os
from datetime import datetime

def analiz_yap(metin):
    metin = metin.lower()
    konu = "Genel"
    duygu = "Nötr"

    pozitif_kelimeler = ["teşekkür", "memnun", "iyi", "harika", "çok güzel", "beğendim"]
    negatif_kelimeler = ["şikayet", "kötü", "endişe", "iptal", "sorun", "yardımcı olur musunuz", "kaybettim"]

    pozitif_sayi = sum(1 for kelime in pozitif_kelimeler if kelime in metin)
    negatif_sayi = sum(1 for kelime in negatif_kelimeler if kelime in metin)

    duygu_skoru = 50 + (pozitif_sayi - negatif_sayi) * 10
    skor = max(0, min(100, duygu_skoru))

    if skor >= 70:
        duygu = "Pozitif"
    elif skor <= 40:
        duygu = "Negatif"
    else:
        duygu = "Nötr"

    if "kart" in metin and ("kaybettim" in metin or "iptal" in metin):
        konu = "Kart İşlemleri > Kayıp Kart"

    return {
        "metin": metin,
        "kategori": konu,
        "duygu": duygu,
        "memnuniyet_skoru": skor,
        "aksiyon": "Takip gerekmez" if skor >= 50 else "Takip çağrısı yapılmalı"
    }

def raporu_kaydet(rapor):
    os.makedirs("outputs/results", exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_path = os.path.join("outputs/results", f"analiz_{timestamp}.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(rapor, f, ensure_ascii=False, indent=4)
    print(f"\n✅ JSON analiz raporu kaydedildi: {output_path}")

# Post-Call AI Agent

Bu proje, çağrı merkezi sonrası ses kayıtlarını analiz ederek konuşmaları yazıya döker, duygu durumu ve konu analizi yapar ve takip çağrısının yapılıp yapılmayacağına karar verir. Daha sonra sonuçları JSON formatında raporlar.

## Klasör Yapısı
- `audios/` — Ses dosyaları (.wav)
- `model/` — Vosk ses tanıma modeli
- `outputs/` — Transkriptler ve analiz raporları

## Kurulum
```bash
pip install vosk

## 🔊 Türkçe Vosk Modeli
Bu projede kullanılan model [vosk-model-small-tr-0.3](https://alphacephei.com/vosk/models) bağlantısından indirilebilir.

İndirdikten sonra `vosk-model-small-tr-0.3` klasörünü proje dizinine (aynı hizada olacak şekilde) yerleştirin.
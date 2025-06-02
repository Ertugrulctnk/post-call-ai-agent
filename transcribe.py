from vosk import Model, KaldiRecognizer
import wave
import json
import os
from datetime import datetime

def transcribe_audio(audio_path, model_path, save_output=True):
    model = Model(model_path)
    wf = wave.open(audio_path, "rb")
    rec = KaldiRecognizer(model, wf.getframerate())

    full_text = ""
    while True:
        data = wf.readframes(4000)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            full_text += result.get('text', '') + " "

    final_result = json.loads(rec.FinalResult())
    full_text += final_result.get('text', '')

    if save_output:
        os.makedirs("outputs/transcriptions", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        out_path = f"outputs/transcriptions/transcript_{timestamp}.txt"
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(full_text.strip())
        print(f"\n✅ Transkript kaydedildi: {out_path}")

    return full_text.strip()

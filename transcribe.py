import whisper
import arabic_reshaper
from bidi.algorithm import get_display

def print_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    print(bidi_text)

print("...جاري تحميل نموذج Whisper في الذاكرة...")
model = whisper.load_model("medium")
print("...تم تحميل النموذج بنجاح.")

audio_file = "Audio-Tests/recording_2025-07-06_04-49-58.wav"
print_arabic(f"جاري تحليل الملف الصوتي: {audio_file}")
result = model.transcribe(audio_file)


print_arabic("--- النص الذي تم التعرف عليه ---")
print_arabic(result["text"])
import sounddevice as sd
import soundfile as sf
import time
import arabic_reshaper
from bidi.algorithm import get_display
import datetime # <-- 1. نستدعي مكتبة الوقت

# دالة لجعل النص العربي يظهر بشكل صحيح
def print_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    print(bidi_text)

# إعدادات التسجيل
samplerate = 16000
duration = 5

# --- 2. إنشاء اسم ملف فريد باستخدام الوقت الحالي ---
timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
filename = f"recording_{timestamp}.wav"
# ----------------------------------------------------

print_arabic("سيبدأ التسجيل بعد 3 ثوانٍ...")
time.sleep(3)

print_arabic("... الآن! ابدأ بالتحدث.")

# تسجيل الصوت من المايكروفون الافتراضي
recording = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
sd.wait()

print_arabic("... انتهى التسجيل.")

# حفظ التسجيل في ملف
sf.write(filename, recording, samplerate)

print_arabic(f"تم حفظ التسجيل بنجاح في الملف: {filename}")
print_arabic("يمكنك الآن فتح الملف والاستماع إليه للتأكد من أن صوتك تم تسجيله.")
import sounddevice as sd
import numpy as np
import whisper
import time
import arabic_reshaper
from bidi.algorithm import get_display

# --- دالة لجعل النص العربي يظهر بشكل سليم ---
def print_arabic(text):
    reshaped_text = arabic_reshaper.reshape(text)
    bidi_text = get_display(reshaped_text)
    print(bidi_text)

# --- بداية الكود الأساسي ---

print_arabic("...جاري تهيئة بيئة Whisper...")
model = whisper.load_model("medium")
print_arabic("...تم تحميل النموذج وجاهز للاستماع.")
print_arabic("====================================")

# --- الموجه الأولي الشامل لزيادة الدقة ---
professional_prompt = (
    "يجب على الطبيب المختص تشخيص وضبط جرعات الدواء بدقة، فالظروف الصحية للمريض تتطلب اهتماماً قوياً وجاداً. "
    "أخذ عينة ضرورية لفحص الجرثومة الغامضة التي سببت هذا الألم الطارئ، وقد أكد على أهمية التغذية السليمة والراحة، "
    "وزيارة الطوارئ فوراً عند الشعور بأي خطر أو ضيق في التنفس."
)
# ---------------------------------------------

# إعدادات التسجيل
samplerate = 16000
duration = 607

# حلقة لا نهائية لجعل البرنامج تفاعلياً
while True:
    print_arabic("\n--- قائمة الأوامر ---")
    print_arabic("اكتب (7) لبدء تسجيل جديد.")
    print_arabic("اكتب (8) لإنهاء البرنامج.")
    
    user_choice = input("الرجاء إدخال اختيارك: ")
    
    if user_choice == '7':
        print_arabic(f"سيبدأ التسجيل لمدة {duration} ثوانٍ...")
        
        recording_data = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1, dtype='float32')
        sd.wait()

        print_arabic("...انتهى التسجيل، جاري التحليل الآن...")
        
        start_time = time.time()
        
        # --- القيام بعملية التفريغ الصوتي مع استخدام الموجه الأولي ---
        result = model.transcribe(
            np.squeeze(recording_data), 
            language='ar', 
            fp16=False,
            initial_prompt=professional_prompt # <-- تم تفعيل الموجه هنا
        )
        
        end_time = time.time()
        processing_time = end_time - start_time

        print_arabic("--- النص الذي تم التعرف عليه ---")
        print_arabic(result["text"])
        print_arabic("------------------------------------")
        print_arabic(f"⏱️ زمن التحليل: {processing_time:.2f} ثانية")
        print("------------------------------------\n")

    elif user_choice == '8':
        break

    else:
        print_arabic("خيار غير صحيح. الرجاء إدخال 7 أو 8 فقط.")

print_arabic("...تم إنهاء البرنامج. شكراً لاستخدامك منصة نبض.")
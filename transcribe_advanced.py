import whisperx
import time
import gc # لإدارة الذاكرة

# --- بداية الكود الأساسي ---

# تحديد الجهاز الذي سيعمل عليه النموذج
# "cuda" يعني استخدام كرت الشاشة NVIDIA القوي
device = "cuda" 
# حجم النموذج الذي سنستخدمه
model_size = "medium"
# المسار إلى الملف الصوتي
# !!! انتبه: يجب تغيير هذا الاسم إلى اسم الملف الصوتي الحقيقي لديك !!!
audio_file = "Audio-Tests/test_recording.wav" 

print(f"Starting analysis for: {audio_file}")
print("------------------------------------")

# --- 1. تحميل نموذج Whisper الرئيسي ---
print(f"Loading model '{model_size}'...")
model = whisperx.load_model(model_size, device)
print("Model loaded successfully.")
print("------------------------------------")

# --- 2. القيام بعملية التفريغ الصوتي (الخطوة الأولى) ---
print("Step 1: Transcribing audio...")
# نحتاج لقراءة الملف الصوتي أولاً
audio = whisperx.load_audio(audio_file)
# نقوم بعملية التحويل
result = model.transcribe(audio)
print("Transcription complete.")
print("Detected language:", result["language"])
print("------------------------------------")


# --- 3. القيام بعملية المحاذاة للحصول على توقيت الكلمات (الخطوة الثانية) ---
print("Step 2: Aligning transcript to get word timestamps...")
# نقوم بتحميل نموذج المحاذاة
# سيتم تحميله من الإنترنت في أول مرة فقط
model_a, metadata = whisperx.load_align_model(language_code=result["language"], device=device)
# نقوم بعملية المزامنة
result = whisperx.align(result["segments"], model_a, metadata, audio, device, return_char_alignments=False)
print("Alignment complete.")
print("------------------------------------")


# --- 4. طباعة النتائج بشكل منظم ---
print("\n--- Transcription with Word Timestamps ---")
# result["word_segments"] يحتوي الآن على كل كلمة مع توقيتها
for segment in result["word_segments"]:
    start_time = segment["start"]
    end_time = segment["end"]
    word = segment["word"]
    
    # نطبع كل كلمة مع وقت بدايتها ونهايتها
    print(f"[{start_time:.2f}s -> {end_time:.2f}s] {word}")

# تنظيف الذاكرة بعد الانتهاء (ممارسة جيدة)
del model_a
del model
gc.collect()
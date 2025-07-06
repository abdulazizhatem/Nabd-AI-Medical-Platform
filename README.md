Nabd AI Medical Platform (منصة "نبض")
AI for Healthcare in Low-Resource Settings


This project is a submission for the Google - The Gemma 3n Impact Challenge.

🎯 The Problem
In the heart of Yemen's healthcare sector, clinicians face immense daily challenges. Overwhelming patient loads leave little time for accurate, detailed documentation. Traditional paper-based records are prone to damage and loss, leading to the erosion of critical patient history.

Furthermore, Yemen's rich dialectal diversity can create communication barriers between doctors and patients, while the absence of digital monitoring systems means that epidemic outbreaks are often detected too late. These challenges impact not only the efficiency of physicians but the quality of care for an entire population.

✨ Our Solution: The Nabd Platform
From these challenges, Nabd (Pulse) was born. It is not just a tool, but an intelligent and reliable partner for the physician, specifically designed for the Yemeni context. Nabd is an integrated AI platform that listens to doctor-patient conversations and instantly generates structured medical reports, while also analyzing aggregated data to provide valuable public health insights.

Nabd's core principle is being Offline-First. All processing happens locally on the doctor's device, ensuring 100% patient data privacy and guaranteeing functionality in any clinic, regardless of infrastructure quality.

🌟 Key Features
🌐 100% Offline Functionality: All audio and text processing is done on-device, ensuring unparalleled security, privacy, and reliability.

🇾🇪 Advanced Yemeni Dialect Support: Utilizes an innovative "Lexical Bridge" (a specialized Yemeni-to-Standard-Arabic dictionary) to interpret local dialects with high accuracy.

🩺 Structured Medical Reports: Automatically extracts vital information (chief complaint, history, assessment, plan) and generates a structured report ready for printing or archiving.

📈 Early Epidemic Warning System: By analyzing anonymized, aggregated data, the system can detect abnormal spikes in specific diagnoses and trigger an early warning.

🎤 Advanced Audio Analysis: Leverages WhisperX for precise, word-level timestamps, paving the way for future features like speaker diarization and sentiment analysis.

💰 Zero-Cost Implementation: Built entirely with open-source models and tools, making this advanced technology accessible to all.

🛠️ Technology Stack
Programming Language: Python

Core Models: Gemma 3n, WhisperX

Local Inference Engine: Ollama

Database: SQLite

Audio Handling: sounddevice

GUI (Future): Tkinter or PyQt

🏗️ System Architecture
The system relies on a "team of experts" architecture to ensure the highest quality at each stage:

Precise Transcription (WhisperX): Audio is captured and transcribed using WhisperX to get a highly accurate text with word-level timestamps.

Dialectical Understanding (The Lexical Bridge): The transcribed text is passed through our custom Yemeni-to-Standard-Arabic dictionary to interpret colloquial terms and prepare the text for the next stage.

Intelligent Analysis & Generation (Gemma 3n): The enriched text is sent to Gemma 3n via Ollama with a detailed prompt. The model then understands the medical context and generates the final structured report and a JSON summary for analysis.

🚀 Getting Started
(This section will be detailed further as the project progresses)

Clone the repository: git clone https://github.com/abdulazizhatem/Nabd-AI-Medical-Platform.git

Install requirements: pip install -r requirements.txt

Pull the models via Ollama.

Run the main application: python main.py

Abdulaziz Hatem | Biomedical Engineer & Applied AI Researcher.

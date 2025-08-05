import speech_recognition as sr
from flask import request, jsonify

def transcribe_audio(audio_file):
    recognizer = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = recognizer.record(source)
    try:
        # 中文优先，自动降级到离线引擎[7](@ref)
        return recognizer.recognize_google(audio, language='zh-CN')
    except sr.UnknownValueError:
        return recognizer.recognize_sphinx(audio)  # 离线回退
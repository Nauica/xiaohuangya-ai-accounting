# backend/api.py
from flask import Flask, jsonify, request
import spacy
from voice_processor import transcribe_audio

app = Flask(__name__)
nlp = spacy.load("zh_core_web_sm")

@app.route('/parse-text', methods=['POST'])
def parse_text():
    # 模拟文档中的文本解析功能（如"打车到公司23元"）
    return jsonify({"amount": 23, "category": "交通"})

if __name__ == "__main__":
    app.run(port=5000)

# 添加根路由处理函数
@app.route('/')
def home():
    return jsonify({"status": "running", "version": "1.0.0"})


@app.route('/parse', methods=['POST'])
def handle_speech():
    audio_file = request.files['audio']
    text = transcribe_audio(audio_file)
    # 使用 spaCy 的 nlp 对象解析消费指令
    doc = nlp(text)
    # 这里可以根据需要从 doc 中提取信息，暂时返回原始文本
    return jsonify({"transcribed_text": text})
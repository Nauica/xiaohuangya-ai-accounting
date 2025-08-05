# backend/api.py
from flask import Flask, jsonify
import spacy

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
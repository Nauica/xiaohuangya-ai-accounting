# 🦆 小黄鸭AI记账 - AI-Powered Expense Tracker

一款融合语音识别与自然语言处理的智能记账应用，让记账变得高效又有趣！  
**当前版本**：MVP开发阶段（Sprint 0完成）

---

## 🚀 项目亮点
- **语音智能记账**：说出"早餐花了15元"，自动解析金额/分类
- **文本灵活输入**：支持自然语言（"打车23元"）和结构化输入（"30元奶茶"）
- **趣味互动体验**：AI生成个性化反馈（如"早餐要吃好！"）
- **简洁数据看板**：消费趋势一目了然

---

## ⚙️ 环境搭建（Sprint 0已完成）
### 前置要求
- Node.js v18+
- Python 3.10+
- Git

### 安装步骤
1. 克隆仓库
git clone https://github.com/Nauica/xiaohuangya-ai-accounting.git
cd xiaohuangya-ai-accounting

2. 前端依赖安装
cd frontend
npm install

3. 后端虚拟环境配置
cd ../backend
python -m venv venv
source venv/bin/activate # Linux/macOS
venv\Scripts\activate # Windows
pip install -r requirements.txt

---

## 🖥️ 运行应用
### 启动后端服务
bash
cd backend
flask run --port=5000 # 启动API服务 (http://localhost:5000)

### 启动前端应用
bash
cd frontend
npm start # 访问 http://localhost:3000
---

## 📂 项目结构
xiaohuangya-ai-accounting/
├── frontend/ # React Native前端
│ ├── assets/ # 静态资源
│ ├── components/ # 公用组件
│ │ ├── VoiceButton.tsx # 语音按钮组件
│ │ └── ExpenseItem.tsx # 消费项组件
│ ├── screens/ # 页面组件
│ │ ├── HomeScreen.tsx # 首页
│ │ ├── RecordScreen.tsx # 记账页
│ │ └── BillsScreen.tsx # 账单页
│ └── App.tsx # 应用入口
│
├── backend/ # Python后端
│ ├── nlp_parser.py # 文本解析模块
│ ├── voice_processor.py # 语音处理模块
│ ├── api.py # RESTful API
│ └── database.py # SQLite操作
│
├── docs/ # 项目文档
│ └── DESIGN.md # 设计文档
│
├── .gitignore
├── LICENSE
└── README.md # 本文档

---

## 🔍 功能模块（MVP开发中）
### 核心模块
| 模块 | 状态 | 技术实现 | 测试命令 |
|------|------|----------|----------|
| **语音记账** | ✅ Sprint 0 验证完成 | React Native + Google Speech API | `npm test VoiceButton` |
| **文本解析** | 🚧 开发中 | Python + spaCy NLP | `pytest backend/nlp_parser_test.py` |
| **账单管理** | 📅 Sprint 2 | SQLite + React Native Paper | - |

### 交互流程示例
tsx

// 语音记账流程（frontend/screens/RecordScreen.tsx）

const handleVoiceInput = async () => {

const result = await recognizeSpeech(); // 调用语音API

setExpense({ amount: result.amount, category: result.category });

};

---

## 🐞 常见问题解决
### 1. 语音按钮不可见
bash

确保安装语音依赖
cd frontend

npm install expo-speech expo-av

检查浏览器控制台错误
F12 > Console > 排查未定义API

### 2. NLP解析失败
bash

下载中文语言模型
python -m spacy download zh_core_web_sm

测试解析功能
python backend/nlp_parser.py "打车到公司23元"

### 3. 依赖冲突
bash

重建node_modules
rm -rf frontend/node_modules

npm install

重置Python环境
deactivate

rm -rf backend/venv

python -m venv venv

---

## 📆 开发路线图
| 阶段 | 时间窗 | 里程碑 | 进度 |
|------|--------|--------|------|
| **Sprint 1** | 第2-3周 | 语音记账MVP | 🟢 进行中 |
| **Sprint 2** | 第4-5周 | 文本记账+账单管理 | 🟡 待开始 |
| **Sprint 3** | 第6周 | 增强功能与优化 | ⚪ 未开始 |

---

## 📬 反馈与支持
**技术问题**：  
提交Issue至 [GitHub Issues](https://github.com/Nauica/xiaohuangya-ai-accounting/issues)  
**产品建议**：  
联系 product@xiaohuangya.com  

---
© 2023 小黄鸭AI记账团队 | [MIT License](LICENSE)
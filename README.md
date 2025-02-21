# 供电服务智能问答系统

## 简介

供电服务智能问答系统是一个基于大语言模型的智能客服解决方案，通过处理客户音频通话记录，提供智能分析和专业解答。系统集成了供电营业规则知识库，可以自动提取关键信息并生成专业的解决方案。

🔗 **在线演示**: [https://master-qtqkunyeoqrl22xzuyxayp.streamlit.app/](https://master-qtqkunyeoqrl22xzuyxayp.streamlit.app/)



## 项目结构

```
project_root/
├── src/
│   ├── config/           # 配置相关
│   │   ├── settings.py   # 系统配置
│   │   └── models.json   # 模型配置
│   ├── core/            # 核心功能
│   │   ├── llm.py      # LLM服务
│   │   └── qa_chain.py # 知识库检索
│   ├── services/        # 服务层
│   │   ├── audio.py    # 音频处理
│   │   └── analysis.py # 对话分析
│   ├── utils/          # 工具函数
│   │   └── session.py  # 会话管理
│   └── ui/             # UI组件
│       └── components.py
├── data/               # 数据文件
│   └── 供电营业规则.pdf
├── app.py             # 主程序入口
└── requirements.txt   # 项目依赖
```

## 主要功能

- 🎙️ **语音识别**：支持 mp3、wav、m4a 格式的音频转文字
- 📝 **智能分析**：自动提取通话记录中的关键信息，包括：
  - 受理时间
  - 联系人
  - 联系地址
  - 受理内容
  - 后续跟进事项
- 🤖 **智能问答**：基于供电营业规则知识库提供专业解答
- 📊 **结构化输出**：清晰展示分析结果和解决方案

## 安装说明

### 环境要求

- Python 3.8+
- OpenAI API 访问权限
- 8GB+ 系统内存推荐

### 安装步骤

1. **安装依赖**
```bash
# Windows 用户使用
pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple

# Linux/Mac 用户使用
pip install -r requirements.txt
```

2. **准备知识库**
- 将供电营业规则PDF文件放入 `data` 目录

3. **启动应用**
```bash
streamlit run app.py
```

## 使用指南

1. **API配置**
   - 在侧边栏填写：
     - OpenAI API Key
     - API Base URL
   - 点击"保存配置"按钮

2. **音频处理**
   - 上传音频文件（支持 mp3、wav、m4a）
   - 点击"开始分析"按钮
   - 等待系统处理

3. **查看结果**
   - 通话记录文本
   - 结构化分析结果
   - 专业解决方案

## 技术架构

- **Web框架**：Streamlit
- **LLM框架**：LangChain
- **模型服务**：OpenAI API
- **向量数据库**：FAISS
- **语音识别**：Whisper

## 核心依赖

```
streamlit>=1.28.0
langchain>=0.1.0
langchain-openai>=0.0.2
openai>=1.3.0
faiss-cpu>=1.7.4
pypdf>=3.17.0
sounddevice>=0.4.6
soundfile>=0.12.1
```

## 注意事项

1. **API安全**
   - 请妥善保管 API 密钥
   - 避免将密钥提交到代码仓库

2. **音频要求**
   - 确保音频质量清晰
   - 支持格式：mp3、wav、m4a

3. **知识库维护**
   - 确保 PDF 文件格式正确
   - 定期更新供电营业规则文档

## 常见问题

1. **Windows 安装依赖失败**
   - 使用清华源安装：
     ```bash
     pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
     ```
   - 或使用命令：
     ```bash
     pip install --no-cache-dir -r requirements.txt
     ```

2. **Streamlit 命令未找到**
   - 确保 pip 安装成功
   - 尝试重新打开命令行
   - 或使用完整路径：
     ```bash
     python -m streamlit run app.py
     ```

## 更新日志

### v1.0.0
- 初始版本发布
- 实现基础功能：音频转写、智能分析、解决方案生成

## 配置说明

### API配置
- **API Key**: OpenAI API密钥，可从 [OpenAI API Keys](https://platform.openai.com/api-keys) 获取
- **API Base URL**: API接口地址，默认使用OpenAI官方接口
- 支持使用其他兼容的API服务商

### 模型参数
- **模型选择**: 支持 gpt-4o-mini、gpt-3.5-turbo、gpt-4
- **Temperature**: 控制输出随机性（0-1）
  - 0: 固定输出
  - 1: 最大随机性

### 知识库参数
- **分块大小**: 文档分块大小（100-2000）
- **重叠大小**: 文档分块重叠大小（0-500）

这些参数可以在系统界面的侧边栏中进行配置。

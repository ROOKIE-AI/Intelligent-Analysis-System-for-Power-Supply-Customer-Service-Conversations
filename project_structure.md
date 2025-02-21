project_root/
├── src/
│   ├── config/           # 配置相关
│   │   ├── settings.py   # 系统配置
│   │   └── models.json    # 模型配置
│   ├── core/            # 核心功能
│   │   ├── __init__.py
│   │   ├── llm.py      # LLM相关功能
│   │   └── qa_chain.py # 知识库相关功能
│   ├── services/        # 服务层
│   │   ├── __init__.py
│   │   ├── audio.py    # 音频处理服务
│   │   └── analysis.py # 对话分析服务
│   ├── utils/          # 工具函数
│   │   ├── __init__.py
│   │   └── session.py  # session状态管理
│   └── ui/             # UI相关
│       ├── __init__.py
│       └── components.py # UI组件
├── data/               # 数据文件
│   └── 供电营业规则.pdf
├── app.py             # 主程序入口
└── requirements.txt   # 项目依赖 
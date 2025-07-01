# 金融知识图谱项目

基于港股、A股、美股数据构建的知识图谱系统，支持REfO KBQA和图分析功能。

## 项目功能

- **数据采集**: 自动采集港股、A股、美股的基础信息和交易数据
- **知识图谱构建**: 构建包含公司、行业、财务指标等实体关系的知识图谱
- **KBQA系统**: 基于REfO的自然语言问答系统
- **图分析**: 提供图算法分析功能，如路径分析、社区发现等

## 项目结构

```
financial-knowledge-graph/
├── data/                   # 数据存储目录
├── src/                    # 源代码
│   ├── data_collection/    # 数据采集模块
│   ├── knowledge_graph/    # 知识图谱构建模块
│   ├── kbqa/              # KBQA系统
│   └── graph_analysis/     # 图分析模块
├── config/                 # 配置文件
├── requirements.txt        # 依赖包
└── main.py                # 主程序入口
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

1. 数据采集：
```bash
python main.py --mode collect
```

2. 构建知识图谱：
```bash
python main.py --mode build_kg
```

3. 启动KBQA系统：
```bash
python main.py --mode kbqa
```

4. 图分析：
```bash
python main.py --mode analysis
```

## 技术栈

- Python 3.8+
- Neo4j (图数据库)
- REfO (规则引擎)
- NetworkX (图分析)
- pandas (数据处理)
- requests (数据采集) 
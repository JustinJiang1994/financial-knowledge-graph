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
│   ├── financial_data.json         # 原始数据文件 (23.8MB)
│   └── financial_data_sample.json  # 样本数据文件 (100条记录)
├── src/                    # 源代码
│   ├── data_collection/    # 数据采集模块
│   │   └── sample_extract.py      # 样本抽取脚本
│   ├── knowledge_graph/    # 知识图谱构建模块
│   ├── kbqa/              # KBQA系统
│   └── graph_analysis/     # 图分析模块
├── config/                 # 配置文件
├── requirements.txt        # 依赖包
└── main.py                # 主程序入口
```

## 操作流程

本项目采用"数据清洗与标准化 → RDF三元组生成 → 属性图导入 → RDF与属性图同步 → 图分析与KBQA开发"的混合知识图谱构建流程。

### 1. 数据清洗与标准化
- 目的：处理原始数据中的缺失值、格式不统一、冗余等问题，生成结构化干净数据。
- 操作命令：
```bash
python src/data_collection/data_cleaning.py
```
- 输入：`data/financial_data_sample.json`
- 输出：`data/financial_data_cleaned.json`

### 2. RDF三元组生成与导出
- 目的：将清洗后的数据转为RDF三元组，便于语义建模和数据共享。
- 操作命令：
```bash
python src/data_collection/rdf_export.py
```
- 输入：`data/financial_data_cleaned.json`
- 输出：`data/financial_data_cleaned.ttl`（Turtle格式）

### 3. 属性图数据导入（Neo4j）
- 目的：将结构化数据导入Neo4j图数据库，支持高效的图查询和分析。
- 操作命令：
（待补充，后续会提供导入脚本和说明）

### 4. RDF与属性图同步
- 目的：实现RDF数据与Neo4j属性图的互操作，支持语义推理和图分析的结合。
- 操作命令：
（待补充，后续会提供同步脚本和说明）

### 5. 图分析与KBQA开发
- 目的：基于知识图谱实现图算法分析和基于REfO的问答系统。
- 操作命令：
（待补充，后续会提供分析和问答模块的说明）

---

每完成一步，都会同步更新本流程和相关脚本，并推送到GitHub。

## 实验步骤记录

### 1. 项目初始化 (2024-01-XX)

**步骤**:
1. 创建项目目录结构
2. 编写 `requirements.txt` 依赖文件
3. 初始化Git仓库

**遇到的问题**:
- 无

### 2. 数据获取 (2024-01-XX)

**步骤**:
1. 从OpenKG获取金融数据源: `http://data.openkg.cn/dataset/c0bd56fb-2374-42a6-8ee3-bbbd536f07e9/resource/655b5dea-a4d0-4649-b842-55f8da663b9a/download/data.json`
2. 下载原始数据文件 (23.8MB)
3. 创建样本抽取脚本 `src/data_collection/sample_extract.py`

**遇到的问题**:
- 原始数据文件过大，无法直接读取分析
- 解决方案: 编写脚本随机抽取100条样本进行分析

**数据文件路径问题**:
- 初始脚本中路径设置为 `../../data/financial_data.json`，导致文件未找到错误
- 解决方案: 修正为相对路径 `data/financial_data.json`

### 3. 数据结构分析 (2024-01-XX)

**分析结果**:
每条数据代表一家上市公司，包含以下主要字段：

**基本信息**:
- 公司名称、英文名称、股票代码
- 办公地址/公司总部、所属地域、所属行业
- 注册资金、员工人数
- 公司网址、电话、传真、邮编、邮箱
- 公司logo (img)

**经营信息**:
- 主营业务
- 控股股东、实际控制人、最终控制人
- 总经理、董事长、董事长秘书、法人代表
- 曾用名

**其他信息** (部分港股公司):
- 年终日、核数师、法律顾问、注册地址、证券事务代表

**实体类型设计**:
- Company (公司)
- Person (人物: 董事长、总经理、实际控制人等)
- Industry (行业)
- Region (地域)
- Shareholder (股东)

**关系类型设计**:
- Company BELONGS_TO Industry (公司属于行业)
- Company LOCATED_IN Region (公司位于地域)
- Company CONTROLLED_BY Person/Company (公司被控制)
- Company CHAIRMAN Person (公司董事长)
- Company CEO Person (公司总经理)
- Company LEGAL_REPRESENTATIVE Person (公司法人代表)
- Company REGISTERED_IN Region (公司注册地)

### 4. 版本控制 (2024-01-XX)

**步骤**:
1. 初始化Git仓库
2. 提交初始项目结构
3. 推送到GitHub远程仓库

**遇到的问题**:
- 无

## 安装依赖

```bash
pip install -r requirements.txt
```

## 使用方法

### 数据预处理
```bash
# 抽取样本数据
python src/data_collection/sample_extract.py
```

### 主要功能 (待实现)
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
- jieba (中文分词)
- matplotlib/seaborn/plotly (数据可视化)
- streamlit (Web界面)
- fastapi (API服务)

## 项目进展

- [x] 项目初始化
- [x] 数据获取和预处理
- [x] 数据结构分析
- [x] 版本控制设置
- [ ] 知识图谱建模
- [ ] Neo4j数据库设计
- [ ] 数据导入脚本
- [ ] REfO KBQA系统
- [ ] 图分析算法
- [ ] Web界面开发

## 下一步计划

1. **知识图谱建模**: 设计Neo4j图数据库schema
2. **数据导入**: 编写数据清洗和导入脚本
3. **KBQA系统**: 基于REfO实现问答规则
4. **图分析**: 实现路径分析、社区发现等算法
5. **Web界面**: 开发用户友好的交互界面

## 问题记录

### 已解决问题
1. **文件路径错误**: 修正了样本抽取脚本中的相对路径问题
2. **大文件处理**: 通过样本抽取解决了大文件无法直接分析的问题

### 待解决问题
1. 数据质量评估和清洗
2. 实体关系抽取的准确性
3. 中文文本处理的优化
4. 图数据库性能优化

## 贡献指南

欢迎提交Issue和Pull Request来改进项目。

## 许可证

MIT License 

## Jena Fuseki集成与SPARQL查询

### 1. Jena Fuseki安装
- 访问 https://jena.apache.org/download/index.cgi 下载最新Fuseki二进制包
- 解压后进入目录
- **注意：Fuseki 5.4.0 及以上需要Java 17**
- Mac用户可用Homebrew安装Java 17：
  ```bash
  brew install openjdk@17
  export JAVA_HOME="/usr/local/opt/openjdk@17"
  export PATH="$JAVA_HOME/bin:$PATH"
  ```
- 检查Java版本：
  ```bash
  java -version
  # 应显示 openjdk version "17..."
  ```

### 2. 启动Fuseki服务
```bash
cd ~/jena-fuseki
./fuseki-server
```
- 默认Web管理界面：http://localhost:3030

### 3. 导入RDF数据
- 浏览器访问 http://localhost:3030
- 新建数据集（如 financialkg），选择 Persistent (TDB2)
- 上传 data/financial_data_cleaned.ttl 文件

### 4. SPARQL查询示例
```sparql
SELECT ?company ?name WHERE {
  ?company <http://example.org/ontology/companyName> ?name .
} LIMIT 10
```

### 5. 遇到的问题与解决建议
- **报错：UnsupportedClassVersionError (class file version 61.0)**
  - 说明Java版本过低，需升级到Java 17
  - Mac可用brew安装openjdk@17，并设置JAVA_HOME
- 其他问题可参考官方文档或联系开发者 
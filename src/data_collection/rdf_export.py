import json
from rdflib import Graph, URIRef, Literal, Namespace, RDF

# 输入和输出文件路径
INPUT_FILE = 'data/financial_data_cleaned.json'  # 清洗后的公司数据
OUTPUT_FILE = 'data/financial_data_cleaned.ttl'  # 导出的RDF三元组（Turtle格式）

# 定义自定义本体的命名空间
EX = Namespace("http://example.org/ontology/")

# 字段与RDF属性的映射关系
FIELD_MAP = {
    '公司名称': EX.companyName,           # 公司中文名
    '英文名称': EX.englishName,           # 公司英文名
    '股票代码': EX.stockCode,             # 股票代码
    '主营业务': EX.mainBusiness,          # 主营业务
    '所属行业': EX.industry,              # 所属行业
    '所属地域': EX.region,                # 所属地域
    '办公地址': EX.officeAddress,         # 办公地址
    '注册资金': EX.registeredCapital,     # 注册资金
    '员工人数': EX.employeeCount,         # 员工人数
    '公司网址': EX.website,               # 公司网址
    '电话': EX.phone,                     # 电话
    '传真': EX.fax,                       # 传真
    '邮编': EX.zipcode,                   # 邮编
    '邮箱': EX.email,                     # 邮箱
    '控股股东': EX.majorShareholder,      # 控股股东
    '实际控制人': EX.actualController,     # 实际控制人
    '最终控制人': EX.finalController,      # 最终控制人
    '总经理': EX.ceo,                     # 总经理
    '董事长': EX.chairman,                # 董事长
    '董事长秘书': EX.chairmanSecretary,   # 董事长秘书
    '法人代表': EX.legalRepresentative,    # 法人代表
    'img': EX.logo                        # 公司logo
}


def export_rdf(input_file, output_file):
    """
    读取清洗后的公司数据，将每家公司转为RDF三元组，导出为Turtle格式文件。
    :param input_file: 输入的json数据文件
    :param output_file: 输出的ttl文件
    """
    g = Graph()
    g.bind("ex", EX)  # 绑定命名空间前缀
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        # 用公司代码生成公司唯一的URI节点，作为RDF三元组的主语
        # 例如：code=839421 -> http://example.org/ontology/company/839421
        code = item.get('股票代码', None)
        name = item.get('公司名称', None)
        if code and code != '未知':
            subj = URIRef(EX[f"company/{code}"])
        elif name:
            subj = URIRef(EX[f"company/{name}"])
        else:
            continue  # 没有唯一标识则跳过
        g.add((subj, RDF.type, EX.Company))  # 声明类型为Company
        # 遍历所有字段，生成属性三元组
        for k, v in item.items():
            if v and v != '未知' and k in FIELD_MAP:
                g.add((subj, FIELD_MAP[k], Literal(v)))
    # 序列化为Turtle格式文件
    g.serialize(output_file, format="turtle")

if __name__ == '__main__':
    export_rdf(INPUT_FILE, OUTPUT_FILE) 
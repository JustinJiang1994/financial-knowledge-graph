import json
import pandas as pd

INPUT_FILE = 'data/financial_data_sample.json'
OUTPUT_FILE = 'data/financial_data_cleaned.json'

# 需要保留的主要字段
FIELDS = [
    '公司名称', '英文名称', '股票代码', '主营业务', '所属行业', '所属地域', '办公地址',
    '注册资金', '员工人数', '公司网址', '电话', '传真', '邮编', '邮箱',
    '控股股东', '实际控制人', '最终控制人', '总经理', '董事长', '董事长秘书', '法人代表',
    'img'
]

def clean_data(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    df = pd.DataFrame(data)
    # 只保留主要字段
    df = df[[col for col in FIELDS if col in df.columns]]
    # 去重
    df = df.drop_duplicates(subset=['公司名称', '股票代码'])
    # 缺失值填充
    df = df.fillna('未知')
    # 格式统一：去除多余空格
    for col in df.columns:
        df[col] = df[col].astype(str).str.strip()
    # 保存为json
    df.to_json(output_file, orient='records', force_ascii=False, indent=2)

if __name__ == '__main__':
    clean_data(INPUT_FILE, OUTPUT_FILE) 
import json
import random

INPUT_FILE = 'data/financial_data.json'
OUTPUT_FILE = 'data/financial_data_sample.json'
SAMPLE_SIZE = 100

def extract_sample(input_file, output_file, sample_size):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    if isinstance(data, dict):
        # 如果是字典，尝试取出其中的一个主键对应的list
        for v in data.values():
            if isinstance(v, list):
                data = v
                break
    sample = random.sample(data, min(sample_size, len(data)))
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(sample, f, ensure_ascii=False, indent=2)

if __name__ == '__main__':
    extract_sample(INPUT_FILE, OUTPUT_FILE, SAMPLE_SIZE) 
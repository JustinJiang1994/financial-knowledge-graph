import json
from py2neo import Graph, Node, Relationship

# Neo4j连接信息（如有自定义请修改）
NEO4J_URL = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

INPUT_FILE = "data/financial_data_cleaned.json"

def import_to_neo4j(input_file):
    # 连接Neo4j数据库
    graph = Graph(NEO4J_URL, auth=(NEO4J_USER, NEO4J_PASSWORD))
    # 清空数据库（可选，开发阶段建议）
    graph.delete_all()
    
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for item in data:
        # 创建公司节点
        company = Node("Company",
            name=item.get("公司名称", "未知"),
            code=item.get("股票代码", "未知"),
            english_name=item.get("英文名称", "未知"),
            main_business=item.get("主营业务", "未知"),
            region=item.get("所属地域", "未知"),
            industry=item.get("所属行业", "未知"),
            address=item.get("办公地址", "未知"),
            capital=item.get("注册资金", "未知"),
            employees=item.get("员工人数", "未知"),
            website=item.get("公司网址", "未知"),
            phone=item.get("电话", "未知"),
            fax=item.get("传真", "未知"),
            zipcode=item.get("邮编", "未知"),
            email=item.get("邮箱", "未知"),
            logo=item.get("img", "")
        )
        graph.merge(company, "Company", "code")  # 按股票代码唯一

        # 创建行业节点及关系
        industry_name = item.get("所属行业", None)
        if industry_name and industry_name != "未知":
            industry = Node("Industry", name=industry_name)
            graph.merge(industry, "Industry", "name")
            graph.merge(Relationship(company, "BELONGS_TO", industry))

        # 创建地域节点及关系
        region_name = item.get("所属地域", None)
        if region_name and region_name != "未知":
            region = Node("Region", name=region_name)
            graph.merge(region, "Region", "name")
            graph.merge(Relationship(company, "LOCATED_IN", region))

        # 创建人物节点及关系（董事长、总经理、法人代表等）
        for role, rel in [("董事长", "CHAIRMAN"), ("总经理", "CEO"), ("法人代表", "LEGAL_REPRESENTATIVE")]:
            person_name = item.get(role, None)
            if person_name and person_name != "未知":
                person = Node("Person", name=person_name)
                graph.merge(person, "Person", "name")
                graph.merge(Relationship(company, rel, person))

        # 控股股东、实际控制人、最终控制人等可扩展
        # ...

if __name__ == "__main__":
    import_to_neo4j(INPUT_FILE) 
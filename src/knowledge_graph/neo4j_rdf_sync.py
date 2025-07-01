from py2neo import Graph
import os

# Neo4j连接信息
NEO4J_URL = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "password"

# RDF文件路径（请根据实际情况修改为绝对路径）
RDF_FILE = os.path.abspath("data/financial_data_cleaned.ttl")


def init_n10s(graph):
    """
    初始化n10s插件配置（只需执行一次）
    """
    graph.run("CALL n10s.graphconfig.init()").data()


def import_rdf(graph, rdf_file):
    """
    导入RDF文件到Neo4j属性图
    :param graph: py2neo Graph对象
    :param rdf_file: RDF文件的绝对路径
    """
    cypher = f'CALL n10s.rdf.import.fetch("file:///{rdf_file}", "Turtle")'
    result = graph.run(cypher).data()
    print("RDF导入结果：", result)


def export_rdf(graph):
    """
    从Neo4j导出RDF三元组（Turtle格式）
    :param graph: py2neo Graph对象
    """
    cypher = 'CALL n10s.rdf.export.stream(null, "Turtle")'
    result = graph.run(cypher).data()
    # 只取RDF内容部分
    rdf_data = "\n".join([row['RDF'] for row in result if 'RDF' in row])
    with open("data/neo4j_exported.ttl", "w", encoding="utf-8") as f:
        f.write(rdf_data)
    print("RDF已导出到 data/neo4j_exported.ttl")


def main():
    graph = Graph(NEO4J_URL, auth=(NEO4J_USER, NEO4J_PASSWORD))
    print("1. 初始化n10s插件配置...")
    init_n10s(graph)
    print("2. 导入RDF文件到Neo4j...")
    import_rdf(graph, RDF_FILE)
    print("3. 从Neo4j导出RDF三元组...")
    export_rdf(graph)
    print("全部操作完成！")

if __name__ == "__main__":
    main() 
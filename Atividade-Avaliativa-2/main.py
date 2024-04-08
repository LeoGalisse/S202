from neo4j import GraphDatabase

class Neo4jClient:
    def __init__(self, uri, user, password):
        self._driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self._driver.close()

    def query(self, query, params=None):
        with self._driver.session() as session:
            result = session.run(query, params)
            return result.data()

if __name__ == "__main__":
    uri = "bolt://3.239.68.125:7687"
    user = "neo4j"
    password = "foam-carelessness-default"
    
    client = Neo4jClient(uri, user, password)
    
    # Exemplo de consultas
    query1 = "MATCH (p:Pessoa {sexo: 'Masculino'}) RETURN p.nome"
    result1 = client.query(query1)
    print("\n1. Quem da família é do sexo Masculino?")
    for record in result1:
        print(record['p.nome'])

    print("\n2. Fulano de tal é pai de quem?")
    result = client.query("MATCH (p1:Pessoa)-[:PAI_DE]->(p2:Pessoa) RETURN p1.nome, p2.nome")
    for record in result:
        print(f"{record['p1.nome']} é pai de {record['p2.nome']}")

    query3 = "MATCH (p:Pessoa {profissao: 'Engenheiro'}) RETURN p.nome"
    result3 = client.query(query3)
    print("\n1. Quem na família é Engenheiro?")
    for record in result3:
        print(record['p.nome'])

    client.close()

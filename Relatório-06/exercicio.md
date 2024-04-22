### Questão 01:

1. **Todos os registros do banco de dados:**
```cypher
MATCH (n)
RETURN n;
```

2. **Jogos lançados após o ano de 2012:**
```cypher
MATCH (g:Game)
WHERE g.ano > 2012
RETURN g;
```

3. **Jogos do gênero de terror:**
```cypher
MATCH (g:Game)
WHERE g.genero = 'Terror'
RETURN g;
```

4. **Jogos com uma nota igual ou maior que 7:**
```cypher
MATCH (:Jurado)-[r:JOGOU]->(g:Game)
WHERE r.nota >= 7
RETURN g;
```

### Questão 02:

1. **Acrescentar quatro novos jogos ao banco de dados:**
```cypher
CREATE (g:Game{titulo:'The Witcher 3: Wild Hunt', genero:'RPG', ano:2015}),
       (g2:Game{titulo:'Red Dead Redemption 2', genero:'Ação-Aventura', ano:2018}),
       (g3:Game{titulo:'Among Us', genero:'Ação', ano:2018}),
       (g4:Game{titulo:'Hades', genero:'Roguelike', ano:2020});
```

2. **Adicionar três novos jurados ao banco de dados:**
```cypher
CREATE (j:Jurado{nome:'Ana'}),
       (j2:Jurado{nome:'Lucas'}),
       (j3:Jurado{nome:'Carolina'});
```

3. **Estabelecer as relações entre os jurados e os jogos que eles avaliaram, incluindo a nota e a quantidade de horas jogadas:**
```cypher
MATCH (j:Jurado{nome:'Ana'}),(g:Game{titulo:'The Witcher 3: Wild Hunt'})
CREATE (j)-[:JOGOU{nota:9, horas: 300}]->(g);

MATCH (j:Jurado{nome:'Lucas'}),(g:Game{titulo:'Red Dead Redemption 2'})
CREATE (j)-[:JOGOU{nota:8, horas: 150}]->(g);

MATCH (j:Jurado{nome:'Carolina'}),(g:Game{titulo:'Among Us'})
CREATE (j)-[:JOGOU{nota:7, horas: 50}]->(g);
```
from typing import Collection
import pymongo # pip install pymongo

class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connection_string = "mongodb+srv://root:QMdiJvbqrpx5pEQT@entraai.0w7drnc.mongodb.net/"
            self.cluster_connection = pymongo.MongoClient(
                connection_string,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.cluster_connection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def reset_database(self):
        try: 
            self.db.drop_collection(self.collection)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)
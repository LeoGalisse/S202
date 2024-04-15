from database.database import Database

class MotoristaDAO:
  def __init__(self, database: Database):
        _database = database
        self.db = _database
        self.collection = self.db.collection

  def criar_motorista(self, motorista_data):
        try:
            self.db.collection.insert_one(motorista_data)
            print("Motorista criado com sucesso!")
        except Exception as e:
            print(e)

  def ler_motorista(self, filtro):
      try:
          motorista = self.db.collection.find_one(filtro)
          
          return motorista
      except Exception as e:
          print(e)

  def atualizar_motorista(self, filtro, novos_dados):
      try:
          resultado = self.db.collection.update_one(filtro, {"$set": novos_dados})
          if resultado.modified_count > 0:
              print("Motorista atualizado com sucesso!")
          else:
              print("Nenhum motorista foi atualizado.")
      except Exception as e:
          print(e)

  def deletar_motorista(self, filtro):
      try:
          resultado = self.db.collection.delete_one(filtro)
          if resultado.deleted_count > 0:
              print("Motorista deletado com sucesso!")
          else:
              print("Nenhum motorista foi deletado.")
      except Exception as e:
          print(e)
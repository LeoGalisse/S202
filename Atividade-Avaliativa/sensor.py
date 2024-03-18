import threading
import random
import time
from datetime import datetime
from database.database import Database

class Sensor(threading.Thread):
    def __init__(self, name, database: Database):
        threading.Thread.__init__(self)
        self.name = name
        self.running = True
        self.alarmado = False
        _database = database
        self.db = _database

    def run(self):
        while self.running:
            temperatura = random.uniform(30, 40)
            if temperatura > 38:
                self.alarmado = True
                print(f"Atenção! Temperatura muito alta! Verificar Sensor {self.name}!")
                return
            else:
                self.alarmado = False
            print(f"Sensor {self.name}: {temperatura} C°")
            self.update_database(temperatura)
            time.sleep(5)  # Tempo de espera ajustável

    def update_database(self, temperatura):
        data = {
            "nomeSensor": self.name,
            "valorSensor": temperatura,
            "unidadeMedida": "C°",
            "sensorAlarmado": self.alarmado,
            "timestamp": datetime.now()
        }
        self.db.collection.insert_one(data)
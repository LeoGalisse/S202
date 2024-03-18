from database.database import Database
from sensor import Sensor
import time
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

def plot_last_hour_data(database: Database):
    end_time = datetime.now()
    start_time = end_time - timedelta(hours=1)
    query = {"timestamp": {"$gte": start_time, "$lte": end_time}}
    data = database.collection.find(query)
    
    timestamps = []
    valores = []

    for entry in data:
        timestamps.append(entry['timestamp'])
        valores.append(entry['valorSensor'])

    # Criar o gráfico
    plt.figure(figsize=(10, 6))
    plt.plot(timestamps, valores, marker='o', linestyle='-')
    plt.title('Valores dos Sensores na Última Hora')
    plt.xlabel('Tempo')
    plt.ylabel('Temperatura (C°)')
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.tight_layout()

    plt.show()

db = Database(database="bancoiot", collection="sensores")
db.reset_database()

sensores = [Sensor(f"Temp{i}", db) for i in range(1, 4)]

for sensor in sensores:
  sensor.start()

time.sleep(3600)

plot_last_hour_data(db)

for sensor in sensores:
  sensor.running = False
  sensor.join()